from models.first_order_system import FirstOrderSystem
from simulation.simulator import EulerSimulator
from visualization.plots import Plotting

temperatures_240, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=240, time_step=0.01, num_steps=100)
temperatures_260, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=260, time_step=0.01, num_steps=100)
temperatures_290, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=290, time_step=0.01, num_steps=100)
temperatures_310, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=310, time_step=0.01, num_steps=100)
temperatures_340, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=340, time_step=0.01, num_steps=100)
temperatures_360, times = EulerSimulator().simulate(FirstOrderSystem(), initial_temp=360, time_step=0.01, num_steps=100)
all_temps = [temperatures_240, temperatures_260, temperatures_290, temperatures_310, temperatures_340, temperatures_360]
labels = ['T0=240 K', 'T0=260 K', 'T0=290 K', 'T0=310 K', 'T0=340 K', 'T0=360 K']
Plotting.plot_trajectory(times, all_temps, labels)