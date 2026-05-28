from experiments.setpoint_tracking import run_setpoint_tracking
from controllers.p import PController
from controllers.pi import PIController
from controllers.pid import PIDController
from parameters import Kp_values, Ki_values, Kd_values, PID_Kp, PID_Ki, SETPOINT_DIR
from visualization.plots import Plotting

def run_p_tuning_study(setpoint=320):
    trajectory_list = []
    label_list = []

    for Kp in Kp_values:
        times, temps, labels = run_setpoint_tracking(
            controller_type=PController,
            Kp=Kp
        )

        trajectory_list.append(temps)
        label_list.extend(labels)

    Plotting.plot_trajectory(
        times,
        trajectory_list,
        label_list,
        filename=f"{SETPOINT_DIR}/p_tuning_study.png",
        title="P Controller Tuning Study",
        setpoint=setpoint
    )

def run_pi_tuning_study(setpoint=320):
    trajectory_list = []
    label_list = []

    for Kp, Ki in zip(Kp_values, Ki_values):
        times, temps, labels = run_setpoint_tracking(
            controller_type=PIController,
            Kp=Kp,
            Ki=Ki
        )

        trajectory_list.append(temps)
        label_list.extend(labels)

    Plotting.plot_trajectory(
        times,
        trajectory_list,
        label_list,
        filename=f"{SETPOINT_DIR}/pi_tuning_study.png",
        title="PI Controller Tuning Study",
        setpoint=setpoint
    )

def run_pid_tuning_study(setpoint=320):

    trajectory_list = []
    label_list = []

    for Kd in Kd_values:
        times, temps, labels = run_setpoint_tracking(
            controller_type=PIDController,
            Kp=PID_Kp,
            Ki=PID_Ki,
            Kd=Kd
        )

        trajectory_list.append(temps)
        label_list.extend(labels)

    Plotting.plot_trajectory(
        times,
        trajectory_list,
        label_list,
        filename=f"{SETPOINT_DIR}/pid_tuning_study.png",
        title="PID Controller Tuning Study",
        setpoint=setpoint
    )

def run_pid_instability_study(setpoint=320):
    trajectory_list = []
    label_list = []
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIDController, Kp=PID_Kp, Ki=PID_Ki, Kd=0.1)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIDController, Kp=PID_Kp, Ki=PID_Ki, Kd=1.0)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
    
    Plotting.plot_trajectory(
        times, 
        trajectory_list, 
        label_list, 
        filename=f"{SETPOINT_DIR}/setpoint_tracking_pid_high_Kd_instability.png", 
        title="PID High-Derivative Instability Study", 
        setpoint=setpoint)

def run_p_vs_pi_comparison(setpoint=320):
    times, p_temperatures, p_labels = run_setpoint_tracking(controller_type=PController, Kp=1.0)
    trajectory_list = []
    label_list = []
    comparison_Ki_values = [1.0, 2.0, 20.0]
    for Ki in comparison_Ki_values:
        times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=1.0, Ki=Ki)
        trajectory_list.append(temperatures)
        label_list.extend(labels)
    
    Plotting.plot_trajectory(
        times, 
        [p_temperatures]+trajectory_list, 
        [p_labels[0]]+label_list, 
        filename=f"{SETPOINT_DIR}/p_vs_pi_comparison.png", 
        title="P vs PI-Controlled Setpoint Tracking", 
        setpoint=setpoint)
