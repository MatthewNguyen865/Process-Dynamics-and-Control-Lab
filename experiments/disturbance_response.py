from experiments.setpoint_tracking import run_setpoint_tracking
from controllers.p import PController
from controllers.pi import PIController
from controllers.pid import PIDController
from visualization.plots import Plotting
from parameters import time_step, SETPOINT_DIR, PID_Kp, PID_Ki

def step_disturbance(time):
    disturbance_magnitude = 15 * time_step
    if time >= 0.5:
        return disturbance_magnitude
    return 0

def run_disturbance_response_study(setpoint=320):
    trajectory_list = []
    label_list = []

    times, temperatures, labels = run_setpoint_tracking(controller_type=PController, Kp=PID_Kp, disturbance=step_disturbance)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIController, Kp=PID_Kp, Ki=PID_Ki, disturbance=step_disturbance)
    trajectory_list.append(temperatures)
    label_list.extend(labels)
    times, temperatures, labels = run_setpoint_tracking(controller_type=PIDController, Kp=PID_Kp, Ki=PID_Ki, Kd=0.1, disturbance=step_disturbance)
    trajectory_list.append(temperatures)
    label_list.extend(labels)

    Plotting.plot_trajectory(
        times, 
        trajectory_list, 
        label_list, 
        filename=f"{SETPOINT_DIR}/disturbance_response_tuning.png", 
        title="Controller Disturbance Rejection Comparison", 
        setpoint=setpoint)
    
    return times, trajectory_list, label_list