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

Results files are stored inside the `custom_plots/kpis` folder, and they are named following this logic: `NRUN_SELFRATE_exec_numMotes_NMOTES.dat.kpi` (e.g., `1_040_exec_numMotes_100.dat.kpi`).

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
