from models.first_order_system import FirstOrderSystem
from simulation.simulator import EulerSimulator
from parameters import initial_temps, time_step, num_steps
def run_basin_study(controller=None):
    system = FirstOrderSystem()
    simulator = EulerSimulator()
    labels = []
    all_trajectories = []
    for T0 in initial_temps:
        labels.append(f'T0={T0} K')
        trajectory, times = simulator.simulate(system, initial_temp=T0, time_step=time_step, num_steps=num_steps, controller=controller)
        all_trajectories.append(trajectory)
    return times, all_trajectories, labels