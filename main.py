from experiments.basin_study import run_basin_study
from visualization.plots import Plotting
from models.first_order_system import FirstOrderSystem
from controllers.p import PController
from controllers.pi import PIController
from controllers.pid import PIDController
from experiments.setpoint_tracking import run_setpoint_tracking
from parameters import PID_Kp, PID_Ki, BASIN_DIR, PHASE_DIR, SETPOINT_DIR, BASIN_DATA_DIR, SETPOINT_DATA_DIR, DISTURBANCE_DATA_DIR
from experiments.tuning_study import run_p_tuning_study, run_pi_tuning_study, run_pid_tuning_study, run_pid_instability_study, run_p_vs_pi_comparison
from experiments.disturbance_response import run_disturbance_response_study
from utils.data_export import save_trajectory_to_csv, save_multi_trajectory_to_csv

# Run basin study with and without control and plot results
times, temperatures, labels = run_basin_study()
Plotting.plot_trajectory(times, 
                         temperatures, 
                         labels, 
                         filename=f"{BASIN_DIR}/uncontrolled_basin_dynamics.png", 
                         title="Uncontrolled Temperature Trajectories"
                         )
save_multi_trajectory_to_csv(
    times,
    temperatures,
    labels,
    filename=f"{BASIN_DATA_DIR}/uncontrolled_basin_dynamics.csv"
    )

times, temperatures, labels = run_basin_study(controller=PController(Kp=1.0, setpoint=300))
Plotting.plot_trajectory(times, 
                         temperatures, 
                         labels, 
                         filename=f"{BASIN_DIR}/p_controlled_basin_dynamics.png", 
                         title="P-Controlled Temperature Trajectories (setpoint = 300K)"
                         )
save_multi_trajectory_to_csv(
    times,
    temperatures,
    labels,
    filename=f"{BASIN_DATA_DIR}/p_controlled_basin_dynamics.csv"
    )

times, temperatures, labels = run_basin_study(controller=PIController(Kp=1.0, Ki=1.0, setpoint=300))
Plotting.plot_trajectory(times, 
                         temperatures, 
                         labels, 
                         filename=f"{BASIN_DIR}/pi_controlled_basin_dynamics.png", 
                         title="PI-Controlled Temperature Trajectories (setpoint = 300K)"
                         )
save_multi_trajectory_to_csv(
    times,
    temperatures,
    labels,
    filename=f"{BASIN_DATA_DIR}/pi_controlled_basin_dynamics.csv"
    )

times, temperatures, labels = run_basin_study(controller=PIDController(Kp=PID_Kp, Ki=PID_Ki, Kd=0.1, setpoint=300))
Plotting.plot_trajectory(times, 
                         temperatures, 
                         labels, 
                         filename=f"{BASIN_DIR}/pid_controlled_basin_dynamics.png", 
                         title="PID-Controlled Temperature Trajectories (setpoint = 300K)"
                         )
save_multi_trajectory_to_csv(
    times,
    temperatures,
    labels,
    filename=f"{BASIN_DATA_DIR}/pid_controlled_basin_dynamics.csv"
    )

# Run setpoint tracking experiment with P controller, plot results, and export data
times, temperatures, labels = run_setpoint_tracking(controller_type=PController, Kp=1.0)
Plotting.plot_trajectory(times, [temperatures], labels, filename=f"{SETPOINT_DIR}/p_setpoint_tracking.png", title="P-Controlled Setpoint Tracking", setpoint=320)
save_trajectory_to_csv(times, temperatures, filename=f"{SETPOINT_DATA_DIR}/p_controlled.csv")
run_p_tuning_study()

# Run setpoint tracking experiment with PI controller, plot results, and export data
times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=1.0, Ki=2.0)
Plotting.plot_trajectory(times, [temperatures], labels, filename=f"{SETPOINT_DIR}/pi_setpoint_tracking.png", title="PI-Controlled Setpoint Tracking", setpoint=320)
save_trajectory_to_csv(times, temperatures, filename=f"{SETPOINT_DATA_DIR}/pi_best.csv")
run_pi_tuning_study()

# Run setpoint tracking experiment with PID controller, plot results, and export data
times, temperatures, labels = run_setpoint_tracking(controller_type=PIDController, Kp=PID_Kp, Ki=PID_Ki, Kd=0.1)
Plotting.plot_trajectory(times, [temperatures], labels, filename=f"{SETPOINT_DIR}/pid_setpoint_tracking.png", title="PID-Controlled Setpoint Tracking", setpoint=320)
save_trajectory_to_csv(times, temperatures, filename=f"{SETPOINT_DATA_DIR}/pid_best.csv")
run_pid_tuning_study()
run_pid_instability_study()

# Run disturbance response study, plot results, and export data
times, trajectories, labels = run_disturbance_response_study()
filenames = [
    "p_disturbance_response.csv",
    "pi_disturbance_response.csv",
    "pid_disturbance_response.csv"
]
for trajectory, filename in zip(trajectories, filenames):
    save_trajectory_to_csv(
        times,
        trajectory,
        filename=f"{DISTURBANCE_DATA_DIR}/{filename}"
    )

# PControl vs PIControl comparison plot
run_p_vs_pi_comparison()
# Plot phase portrait of the system
model = FirstOrderSystem()
Plotting.plot_phase_portrait(model=model, filename=f"{PHASE_DIR}/phase_portrait.png")

# Plot controlled phase portrait with P controller
Plotting.plot_controlled_phase_portrait(model=model, filename=f"{PHASE_DIR}/controlled_vs_uncontrolled_phase_portrait.png")