from experiments.basin_study import run_basin_study
from visualization.plots import Plotting
from models.first_order_system import FirstOrderSystem
from controllers.p import PController
from controllers.pi import PIController
from experiments.setpoint_tracking import run_setpoint_tracking
from parameters import Kp_values, Ki_values, BASIN_DIR, PHASE_DIR, SETPOINT_DIR

# Run basin study with and without control and plot results
times, temperatures, labels = run_basin_study()
Plotting.plot_trajectory(times, temperatures, labels, filename=f"{BASIN_DIR}/uncontrolled_basin_dynamics.png", title="Uncontrolled Temperature Trajectories")
times, temperatures, labels = run_basin_study(controller=PController(Kp=1.0, setpoint=300))
Plotting.plot_trajectory(times, temperatures, labels, filename=f"{BASIN_DIR}/p_controlled_basin_dynamics.png", title="P-Controlled Temperature Trajectories (setpoint = 300K)")
times, temperatures, labels = run_basin_study(controller=PIController(Kp=1.0, Ki=1.0, setpoint=300))
Plotting.plot_trajectory(times, temperatures, labels, filename=f"{BASIN_DIR}/pi_controlled_basin_dynamics.png", title="PI-Controlled Temperature Trajectories (setpoint = 300K)")

# Run setpoint tracking experiment with P controller and plot results
times, temperatures, labels = run_setpoint_tracking(controller_type=PController, Kp=1.0)
Plotting.plot_trajectory(times, [temperatures], labels, filename=f"{SETPOINT_DIR}/setpoint_tracking_baseline.png", title="P-Controlled Setpoint Tracking", setpoint=320)

trajectory_list = []
label_list = []
for Kp in Kp_values:
    times, temperatures, labels = run_setpoint_tracking(controller_type=PController, Kp=Kp)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
Plotting.plot_trajectory(times, trajectory_list, label_list, filename=f"{SETPOINT_DIR}/setpoint_tracking_Kp_sweep.png", title="P-Controlled Setpoint Tracking", setpoint=320)

# Run setpoint tracking experiment with PI controller and plot results
times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=1.0, Ki=2.0)
Plotting.plot_trajectory(times, [temperatures], labels, filename=f"{SETPOINT_DIR}/setpoint_tracking_pi_best.png", title="PI-Controlled Setpoint Tracking", setpoint=320)

trajectory_list = []
label_list = []
for Kp, Ki in zip(Kp_values, Ki_values):
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=Kp, Ki=Ki)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
Plotting.plot_trajectory(times, trajectory_list, label_list, filename=f"{SETPOINT_DIR}/setpoint_tracking_Kp_Ki_sweep.png", title="PI-Controlled Setpoint Tracking", setpoint=320)

# PControl vs PIControl comparison plot
times, p_temperatures, p_labels = run_setpoint_tracking(controller_type=PController, Kp=1.0)
trajectory_list = []
label_list = []
comparison_Ki_values = [1.0, 2.0, 20.0]
for Ki in comparison_Ki_values:
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=1.0, Ki=Ki)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
Plotting.plot_trajectory(times, [p_temperatures]+trajectory_list, [p_labels[0]]+label_list, filename=f"{SETPOINT_DIR}/p_vs_pi_comparison.png", title="P vs PI-Controlled Setpoint Tracking", setpoint=320)

# Plot phase portrait of the system
model = FirstOrderSystem()
Plotting.plot_phase_portrait(model=model, filename=f"{PHASE_DIR}/phase_portrait.png")

# Plot controlled phase portrait with P controller
Plotting.plot_controlled_phase_portrait(model=model, filename=f"{PHASE_DIR}/controlled_vs_uncontrolled_phase_portrait.png")