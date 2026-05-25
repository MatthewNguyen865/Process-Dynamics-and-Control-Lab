from experiments.basin_study import run_basin_study
from visualization.plots import Plotting
from models.first_order_system import FirstOrderSystem
times, temperatures, labels =run_basin_study()
Plotting.plot_trajectory(times, temperatures, labels)
model = FirstOrderSystem()
Plotting.plot_phase_portrait(model=model)