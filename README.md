## SA-6TiSCH: Selfishness-Aware 6TiSCH

SA-6TiSCH is a modified version of the 6TiSCH simulator. It enables the simulation of 6TiSCH networks with the presence of selfish nodes. It includes detection and reaction algorithms for selfish nodes. The detection algorithm is implemented in the file `sixp.py`, while the selfish behavior itself and the reaction algorithm are implemented inside the file `sf.py`.
 
Authors:

* Yassine Boufenneche (yboufenneche@usthb.dz)
* Rafik Zitouni (rafik.zitouni@ece.fr)

## SelfishnessDetector module

The `SelfishnessDetector` module represents the Fuzzy Selfishness Estimator (FSE). It relies on the fuzzy logic theory to compute a `Selfishness` value given a `Pr` value, a `RSR` value and a `Distance` value.

## Detection algorithm

The detection algorithm uses the selfishness module, and is implemented in the file `SimEngine/Mote/sixp.py`.

## Reaction algorithm

The reaction mechanism is implemented in the file `SimEngine/Mote/sf.py`

## Choosing selfish nodes

The strategy of choosing which nodes to be configured as selfish ones is implemented in the files `SimEngine/SimEngine.py` and `SimEngine/Mote/rpl.py`.

## Results

The `custom_plots` folder hosts the results files as well as Python files used to generate our plots and boxes.

Results files are stored inside the `custom_plots/kpis` folder, and they are named following this logic: `NRUN_SELFRATE_exec_numMotes_NMOTES.dat.kpi`

* `NRUN` = the number of the run for the same configuration.
* `SELFRATE` = the selfishness rate.
* `NMOTES` = the number of nodes used in the simulation.
* If the file name starts with `R`, this means that the reaction mechanism was activated. Otherwise, no reaction mechanism was used.

## Installation

* Install Python 2.7 (or Python 3)
* Clone or download this repository
* To plot the graphs, you need Matplotlib and scipy. On Windows, Anaconda (http://continuum.io/downloads) is a good one-stop-shop.

While 6TiSCH Simulator has been tested with Python 2.7, it should work with Python 3 as well.

## Getting Started

1. Download the code:
   ```
   $ git clone https://bitbucket.org/6tisch/simulator.git
   ```
1. Install the Python dependencies:
   `cd simulator` and `pip install -r requirements.txt`
1. Execute `runSim.py` or start the GUI:
    * runSim.py
       ```
       $ cd bin
       $ python runSim.py
       ```
        * a new directory having the timestamp value as its name is created under
          `bin/simData/` (e.g., `bin/simData/20181203-161254-775`)
        * raw output data and raw charts are stored in the newly created directory
    * GUI
       ```
       $ gui/backend/start
       Starting the backend server on 127.0.0.1:8080
       ```
        * access http://127.0.0.1:8080 with a web browser
        * raw output data are stored under `gui/simData`
        * charts are NOT generated when the simulator is run via GUI

1. Take a look at `bin/config.json` to see the configuration of the simulations you just ran.

The simulator can be run on a cluster system. Here is an example for a cluster built with OAR and Conda:

1. Edit `config.json`
    * Set `numCPUs` with `-1` (use all the available CPUs/cores) or a specific number of CPUs to be used
    * Set `log_directory_name` with `"hostname"`
1. Create a shell script, `runSim.sh`, having the following lines:

        #!/bin/sh
        #OAR -l /nodes=1
        source activate py27
        python runSim.py

1. Make the shell script file executable:
   ```
   $ chmod +x runSim.sh
   ```
1. Submit a task for your simulation (in this case, 10 separate simulation jobs are submitted):
   ```
   $ oarsub --array 10  -S "./runSim.sh"
   ```
1. After all the jobs finish, you'll have 10 log directories under `simData`, each directory name of which is the host name where a job is executed
1. Merge the resulting log files into a single log directory:
   ```
   $ python mergeLogs.py
   ```

If you want to avoid using a specific host, use `-p` option with `oarsub`:
```
$ oarsub -p "not host like 'node063'" --array 10 -S "./runSim.sh"
```
In this case, `node063` won't be selected for submitted jobs.

The following commands could be useful to manage your jobs:

* `$ oarstat`: show all the current jobs
* `$ oarstat -u`: show *your* jobs
* `$ oarstat -u -f`: show details of your jobs
* `$ oardel 87132`: delete a job whose job ID is 87132
* `$ oardel --array 87132`: delete all the jobs whose array ID is 87132

You can find your job IDs and array ID in `oarsub` outputs:

```
$ oarsub --array 4 -S "runSim.sh"
...
OAR_JOB_ID=87132
OAR_JOB_ID=87133
OAR_JOB_ID=87134
OAR_JOB_ID=87135
OAR_ARRAY_ID=87132
```

## Code Organization

* `SimEngine/`: the simulator
    * `Connectivity.py`: Simulates wireless connectivity.
    * `SimConfig.py`: The overall configuration of running a simulation campaign.
    * `SimEngine.py`: Event-driven simulation engine at the core of this simulator.
    * `SimLog.py`: Used to save the simulation logs.
    * `SimSettings.py`: The settings of a single simulation, part of a simulation campaign.
    * `Mote/`: Models a 6TiSCH mote running the different standards listed above.
* `bin/`: the scripts for you to run
* `gui/`: files for GUI (see "GUI" section for further information)
* `tests/`: the unit tests, run using `pytest`
* `traces/`: example `k7` connectivity traces

## Configuration

`runSim.py` reads `config.json` in the current working directory.
You can specify a specific `config.json` location with `--config` option.

```
python runSim.py --config=example.json
```

The `config` parameter can contain:

* the name of the configuration file in the current directory, e.g. `example.json`
* a path to a configuration file on the computer running the simulation, e.g. `c:\simulator\example.json`
* a URL of a configuration file somewhere on the Internet, e.g. `https://www.example.com/example.json`

### base format of the configuration file

```
{
    "version":               0,
    "execution": {
        "numCPUs":           1,
        "numRuns":           100
    },
    "settings": {
        "combination": {
            ...
        },
        "regular": {
            ...
        }
    },
    "logging":               "all",
    "log_directory_name":    "startTime",
    "post": [
        "python compute_kpis.py",
        "python plot.py"
    ]
}
```

* the configuration file is a valid JSON file
* `version` is the version of the configuration file format; only 0 for now.
* `execution` specifies the simulator's execution
    * `numCPUs` is the number of CPUs (CPU cores) to be used; `-1` means "all available cores"
    * `numRuns` is the number of runs per simulation parameter combination
* `settings` contains all the settings for running the simulation.
    * `combination` specifies variations of parameters
    * `regular` specifies the set of simulator parameters commonly used in a series of simulations
* `logging` specifies what kinds of logs are recorded; `"all"` or a list of log types
* `log_directory_name` specifies how sub-directories for log data are named: `"startTime"` or `"hostname"`
* `post` lists the post-processing commands to run after the end of the simulation.

See `bin/config.json` to find  what parameters should be set and how they are configured.

### more on connectivity models

#### using a *k7* connectivity model

`k7` is a popular format for connectivity traces.
You can run the simulator using connectivity traces in your K7 file instead of using the propagation model.

```
{
    ...
    "settings": {
        "conn_class": "K7"
        "conn_trace": "../traces/grenoble.k7.gz"
    },
    ...
}
```

* `conn_class` should be set with `"K7"`
* `conn_trace` should be set with your K7 file path

Requirements:

* the number of nodes in the simulation must match the number of nodes in the trace file.
* the trace duration should be longer that 1 hour has the first hour is used for initialization

### more on applications

`AppPeriodic` and `AppBurst` are available.

### configuration file format validation

The format of the configuration file you pass is validated before starting the simulation. If your configuration file doesn't comply with the format, an `ConfigfileFormatException` is raised, containing a description of the format violation. The simulation is then not started.

## GUI / 6TiSCH Simulator WebApp
The repository of 6TiSCH Simulator has only artifacts of 6TiSCH Simulator WebApp.

Full source code of the webapp is hosted at [https://github.com/yatch/6tisch-simulator-webapp/](https://github.com/yatch/6tisch-simulator-webapp/).
[WEBAPP_COMMIT_INFO.txt](./gui/WEBAPP_COMMIT_INFO.txt) has the commit (version) of the webapp code that generates the files under `gui`.

![Screenshot of GUI](figs/gui.png)

## About 6TiSCH

| what         | where                                                                                                                                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
| charter      | [http://tools.ietf.org/wg/6tisch/charters](http://tools.ietf.org/wg/6tisch/charters)                                                   |
| data tracker | [http://tools.ietf.org/wg/6tisch/](http://tools.ietf.org/wg/6tisch/)                                                                   |
| mailing list | [http://www.ietf.org/mail-archive/web/6tisch/current/maillist.html](http://www.ietf.org/mail-archive/web/6tisch/current/maillist.html) |
| source       | [https://bitbucket.org/6tisch/](https://bitbucket.org/6tisch/)                                                                         |
