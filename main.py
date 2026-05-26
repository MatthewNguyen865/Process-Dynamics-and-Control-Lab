from experiments.basin_study import run_basin_study
from visualization.plots import Plotting
from models.first_order_system import FirstOrderSystem
from controllers.p import PController

times, temperatures, labels = run_basin_study()
Plotting.plot_trajectory(times, temperatures, labels, title="Uncontrolled Temperature Trajectories")
times, temperatures, labels = run_basin_study(controller=PController(Kp=0.05, setpoint=300))
Plotting.plot_trajectory(times, temperatures, labels, filename="controlled_temperature_trajectories.png", title="P-Controlled Temperature Trajectories")

model = FirstOrderSystem()
Plotting.plot_phase_portrait(model=model)