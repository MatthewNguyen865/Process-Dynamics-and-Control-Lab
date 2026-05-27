#Simulation Parameters
time_step = 0.01
num_steps = 100
default_k = 0.001

#Experiment Parameters
initial_temps = [240, 260, 290, 310, 340, 360]
Kp_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
Ki_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

#Plot/Output Parameters
PLOT_DIR = "example_plots"
BASIN_DIR = f"{PLOT_DIR}/basin_dynamics"
SETPOINT_DIR = f"{PLOT_DIR}/setpoint_tracking"
PHASE_DIR = f"{PLOT_DIR}/phase_portraits"