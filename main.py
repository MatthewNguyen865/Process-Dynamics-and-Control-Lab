from experiments.basin_study import run_basin_study
from visualization.plots import Plotting
times, temperatures, labels =run_basin_study()
Plotting.plot_trajectory(times, temperatures, labels)