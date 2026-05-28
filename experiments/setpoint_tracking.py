from models.first_order_system import FirstOrderSystem
from simulation.simulator import EulerSimulator
from parameters import time_step, num_steps

def run_setpoint_tracking(controller_type, initial_temp=260, setpoint=320, Kp=1.0, Ki=None, Kd=None, disturbance=None):
    
    system = FirstOrderSystem()
    simulator = EulerSimulator()
    labels = []
    
    controller = controller_type(Kp=Kp, setpoint=setpoint, Ki=Ki, Kd=Kd)
    
    trajectory, times = simulator.simulate(system, initial_temp=initial_temp, time_step=time_step, num_steps=num_steps, controller=controller, disturbance=disturbance)
    if Ki is None:
        labels.append(f'Kp={Kp}')
    elif Kd is None:
        labels.append(f'Kp={Kp}, Ki={Ki}')
    else:
        labels.append(f'Kp={Kp}, Ki={Ki}, Kd={Kd}')

    return times, trajectory, labels