from models.first_order_system import FirstOrderSystem
from simulation.simulator import EulerSimulator
from parameters import time_step, num_steps

def run_setpoint_tracking(controller_type, initial_temp=260, setpoint=320, Kp=0.05):
    
    system = FirstOrderSystem()
    simulator = EulerSimulator()
    labels = []
    
    controller = controller_type(Kp=Kp, setpoint=setpoint)
    
    trajectory, times = simulator.simulate(system, initial_temp=initial_temp, time_step=time_step, num_steps=num_steps, controller=controller)
    #labels.append(f'P Control: {initial_temp} K → {setpoint} K (Kp={Kp})')
    labels.append(f'Kp={Kp}')

    return times, trajectory, labels