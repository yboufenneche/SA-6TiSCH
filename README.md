## SA-6TiSCH: Selfishness-Aware 6TiSCH

Authors:

* Yassine Boufenneche (yboufenneche@usthb.dz)
* Rafik Zitouni (rafik.zitouni@ece.fr)
* Laurent George (laurent.george@esiee.fr)
* Nawel Gharbi (ngharbi@usthb.dz)

SA-6TiSCH is a modified version of the 6TiSCH simulator. It enables the simulation of 6TiSCH networks with the presence of selfish nodes. We define a selfish node as the one that does not amply cooperate with its neighbors during the negotiation process of the protocol, 6P which enables adding new cells between neighbors. In fact, a selfish node intentionnally disagree to install a number of cells with the neighbor, either to save its energy or to disrupt the network performance.

## Additional features of SA-6TiSCH compared to 6TiSCH

The purpose of SA-6TiSCH is to consider the selfishness while simulating 6TiSCH networks. For so doing, we extended the 6TiSCH simulator with the following features:

* Selfish Behavior: we define and implement the selfish behavior in 6TiSCH networks, by making nodes not fairly running 6top Protocol. This behavior is implemented the file `SimEngine/Mote/sf.py`.

* Detection Algorithm: is a distributed algorithm based on fuzzy logic theory that enables each node in the network to identify its non-cooperative neighbors. It is implemented in the file `SimEngine/Mote/sixp.py`, and relies on the values provided by `SelfishnessDetector`module.
    
    * Fuzzy Selfishness Estimator: it uses the fuzzy logic theory to compute a `Selfishness` value given an `Occupancy probability` value, a `Request Satisfaction Rate (RSR)` value and a `Distance` value. It is implemented in `fuzzySelfishnessEstimator.py`.
       
* Reaction Algorithm:  is a countermeasure solution that helps nodes anticipating their reaction in the presence of suspicious nodes. The reaction mechanism is implemented in the file `SimEngine/Mote/sf.py`.

## Choosing selfish nodes

The strategy of choosing which nodes to be configured as selfish ones is implemented in the files `SimEngine/SimEngine.py` and `SimEngine/Mote/rpl.py`. We start with the first nodes that have successfully joined the network.

## Results

The `custom_plots` folder hosts the results files as well as Python files used to generate our plots and boxes.

Results files are stored inside the `custom_plots/kpis` subfolder, and they are named following this logic: `NRUN_SELFRATE_exec_numMotes_NMOTES.dat.kpi` (e.g., `1_040_exec_numMotes_100.dat.kpi`).

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
   $ git clone https://github.com/yboufenneche/SA-6TiSCH.git
   ```
1. Install the Python dependencies:
   `cd simulator` and `pip install -r requirements.txt`
1. Execute `runSim.py` :
   ```
   $ cd bin
   $ python runSim.py
   ```
   * a new directory having the timestamp value as its name is created under
     `bin/simData/` (e.g., `bin/simData/20181203-161254-775`)
   * raw output data and raw charts are stored in the newly created directory

## Code Organization

* `SelfishnessDetector/`:
    * `fuzzySelfishnessEstimator.py`: Fuzzy Selfishness Estimator (FSE).
* `custom_plots/`: the results
    * `kpis/`: the result files
    * `custom_plots.py`: generate plolts and boxes.
    * `extract_data.py`: extract and combine data from different result files.
    * `utilities.py`: useful functions.
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
