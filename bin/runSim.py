#!/usr/bin/python
'''
\brief Entry point to start a simulation.

A number of command-line parameters are available to modify the simulation
settings. Use '--help' for a list of them.

\author Thomas Watteyne <watteyne@eecs.berkeley.edu>
\author Kazushi Muraoka <k-muraoka@eecs.berkeley.edu>
\author Nicola Accettura <nicola.accettura@eecs.berkeley.edu>
\author Xavier Vilajosana <xvilajosana@eecs.berkeley.edu>
'''

#============================ adjust path =====================================

import os
import sys
if __name__=='__main__':
    here = sys.path[0]
    sys.path.insert(0, os.path.join(here, '..'))

#============================ logging =========================================

import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('BatchSim')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

#============================ imports =========================================

import time
import itertools
import logging.config
import argparse
import threading

from SimEngine     import SimEngine,   \
                          SimSettings, \
                          SimStats
from SimGui        import SimGui

#============================ defines =========================================

#============================ body ============================================

def parseCliOptions():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument( '--squareSide',
        dest       = 'squareSide',
        nargs      = '+',
        type       = float,
        default    = 2.000,
        help       = 'Length of the side of the square area the motes are deployed in, in km.',
    )
    
    parser.add_argument( '--numMotes',
        dest       = 'numMotes',
        nargs      = '+',
        type       = int,
        default    = [20],
        help       = 'Number of simulated motes.',
    )
    
    parser.add_argument( '--numChans',
        dest       = 'numChans',
        nargs      = '+',
        type       = int,
        default    = 16,
        help       = 'Number of frequency channels (between 1 and 16).',
    )
    
    parser.add_argument( '--minRssi',
        dest       = 'minRssi',
        type       = int,
        default    = -97,
        help       = 'Mininum RSSI with positive PDR, in dBm.',
    )
    
    parser.add_argument( '--slotDuration',
        dest       = 'slotDuration',
        nargs      = '+',
        type       = float,
        default    = 0.010,
        help       = 'Duration of a TSCH timeslot, in seconds.',
    )
    
    parser.add_argument( '--slotframeLength',
        dest       = 'slotframeLength',
        nargs      = '+',
        type       = int,
        default    = 101,
        help       = 'Number of timeslots in a slotframe.',
    )
    
    parser.add_argument( '--pkPeriod',
        dest       = 'pkPeriod',
        nargs      = '+',
        type       = float,
        default    = [10.0],
        help       = 'Average period (is s) between two packets generated by a mote.',
    )
    
    parser.add_argument( '--pkPeriodVar',
        dest       = 'pkPeriodVar',
        nargs      = '+',
        type       = float,
        default    = 0.5,
        help       = 'Variability percentage of the period between two generated packets. Use 0 for CBR traffic.',
    )

    parser.add_argument( '--dioPeriod',
        dest       = 'dioPeriod',
        nargs      = '+',
        type       = float,
        default    = 1.0,
        help       = 'DIO period, in sec',
    )
    
    parser.add_argument( '--otfThreshold',
        dest       = 'otfThreshold',
        nargs      = '+',
        type       = int,
        default    = 0,
        help       = 'OTF threshold, in cells.',
    )

    parser.add_argument( '--otfHousekeepingPeriod',
        dest       = 'otfHousekeepingPeriod',
        nargs      = '+',
        type       = float,
        default    = 1.0,
        help       = 'OTF Housekeeping Period, in sec.',
    )

    parser.add_argument( '--topHousekeepingPeriod',
        dest       = 'topHousekeepingPeriod',
        nargs      = '+',
        type       = float,
        default    = 1.0,
        help       = '6top Housekeeping Period, in sec.',
    )

    parser.add_argument( '--topPdrThreshold',
        dest       = 'topPdrThreshold',
        nargs      = '+',
        type       = float,
        default    = 2.0,
        help       = '6top PDR threshold for cell relocation',
    )
    
    parser.add_argument( '--numCyclesPerRun',
        dest       = 'numCyclesPerRun',
        type       = int,
        default    = 20,
        help       = 'Duration of one simulation run, in slotframe cycle.',
    )
    
    parser.add_argument( '--numRuns',
        dest       = 'numRuns',
        type       = int,
        default    = 2,
        help       = 'Number of simulation runs per each configurations.',
    )
    
    parser.add_argument('--gui',
        dest       = 'gui',
        action     = 'store_true',
        default    = False,
        help       = 'Display the GUI during execution.',
    )

    parser.add_argument('--noInterference',
        dest       = 'noInterference',
        nargs      = '+',
        type       = int,
        default    = 0,
        help       = 'Turn off interference in the same cell transmission.',
    )

    parser.add_argument('--noTopHousekeeping',
        dest       = 'noTopHousekeeping',
        nargs      = '+',
        type       = int,
        default    = 0,
        help       = 'Turn off 6top housekeeping.',
    )

    parser.add_argument('--noRemoveWorstCell',
        dest       = 'noRemoveWorstCell',
        nargs      = '+',
        type       = int,
        default    = 0,
        help       = 'Turn on removing random cell function instead of removing the worst.',
    )
    
    parser.add_argument( '--processID',
        dest       = 'processID',
        type       = int,
        default    = None,
        help       = 'ID associated with a batch of numRuns simulations (used in multiprocess simulations).',
    )
    
    parser.add_argument('--simDataDir',
        dest       = 'simDataDir',
        type       = str,
        default    = 'simData',
        help       = 'SimData directory.',
    )
    
    parser.add_argument( '--numPacketsBurst',
        dest       = 'numPacketsBurst',
        nargs      = '+',
        type       = int,
        default    = None,
        help       = 'Number of packets to be enqueued as burst.',
    )
    
    parser.add_argument( '--burstTime',
        dest       = 'burstTime',
        nargs      = '+',
        type       = float,
        default    = 20.0,
        help       = 'Burst time (in sec).',
    )
    
    options        = parser.parse_args()
    
    return options.__dict__

def runSims(options):
    
    # compute all the simulation parameter combinations
    combinationKeys     = sorted([k for (k,v) in options.items() if type(v)==list])
    simParams           = []
    for p in itertools.product(*[options[k] for k in combinationKeys]):
        simParam = {}
        for (k,v) in zip(combinationKeys,p):
            simParam[k] = v
        for (k,v) in options.items():
            if k not in simParam:
                simParam[k] = v
        simParams      += [simParam]
    
    # run a simulation for each set of simParams
    for (simParamNum,simParam) in enumerate(simParams):
        
        # print
        if simParam['processID']==None:
            print('parameters {0}/{1}'.format(simParamNum+1,len(simParams)))
        else:
            print('parameters {0}/{1}, processID {2}'.format(simParamNum+1,len(simParams), simParam['processID']))
        
        # record run start time
        runStartTime = time.time()
        
        # run the simulation runs
        for runNum in xrange(simParam['numRuns']):
            
            # print
            if simParam['processID']==None:
                print('   run {0}/{1}'.format(runNum+1,simParam['numRuns']))
            
            # create singletons
            settings         = SimSettings.SimSettings(**simParam)
            settings.setStartTime(runStartTime)
            settings.setCombinationKeys(combinationKeys)
            simengine        = SimEngine.SimEngine(runNum)
            simstats         = SimStats.SimStats(runNum)
            
            # start simulation run
            simengine.start()
            
            # wait for simulation run to end
            simengine.join()
            
            # destroy singletons
            simstats.destroy()
            simengine.destroy()
            settings.destroy()
    
def main():
    # initialize logging
    logging.config.fileConfig('logging.conf')
    
    # parse CLI options
    options        = parseCliOptions()
    
    if options['gui']:
        # create the GUI
        gui        = SimGui.SimGui()
        
        # run simulations (in separate thread)
        simThread  = threading.Thread(target=runSims,args=(options,))
        simThread.start()
        
        # start GUI's mainloop (in main thread)
        gui.mainloop()
    else:
        # record simulation start time
        simStartTime   = time.time()
        
        # run the simulations
        runSims(options)
        
        # print
        print '\nSimulation ended after {0:.0f}s.'.format(time.time()-simStartTime)

#============================ main ============================================

if __name__=="__main__":
    main()
