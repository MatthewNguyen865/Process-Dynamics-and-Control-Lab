#Simulation Parameters
time_step = 0.01
num_steps = 100
default_k = 0.001

#Experiment Parameters
initial_temps = [240, 260, 290, 310, 340, 360]
Kp_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
Ki_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
Kd_values = [0.01, 0.05, 0.1, 0.2, 0.5]
PID_Kp = 1.0
PID_Ki = 2.0

#Plot Parameters
RESULTS_DIR = "results"
PLOT_DIR = f"{RESULTS_DIR}/plots"

BASIN_DIR = f"{PLOT_DIR}/basin_dynamics"
SETPOINT_DIR = f"{PLOT_DIR}/setpoint_tracking"
PHASE_DIR = f"{PLOT_DIR}/phase_portraits"

# Data Parameters
DATA_DIR = f"{RESULTS_DIR}/data"

BASIN_DATA_DIR = f"{DATA_DIR}/basin_dynamics"
SETPOINT_DATA_DIR = f"{DATA_DIR}/setpoint_tracking"
DISTURBANCE_DATA_DIR = f"{DATA_DIR}/disturbance_response"