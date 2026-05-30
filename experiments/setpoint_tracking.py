from models.first_order_system import FirstOrderSystem
from simulation.simulator import EulerSimulator
from parameters import time_step, num_steps
from controllers.p import PController
from controllers.pi import PIController
from controllers.pid import PIDController

def run_setpoint_tracking(controller_type, initial_temp=260, setpoint=320, Kp=1.0, Ki=None, Kd=None, disturbance=None):
    
    system = FirstOrderSystem()
    simulator = EulerSimulator()
    labels = []
    
    controller = controller_type(Kp=Kp, setpoint=setpoint, Ki=Ki, Kd=Kd)
    
    trajectory, times = simulator.simulate(system, initial_temp=initial_temp, time_step=time_step, num_steps=num_steps, controller=controller, disturbance=disturbance)
    if controller_type == PController:
        labels.append(f'Kp={Kp}')
    elif controller_type == PIController:
        labels.append(f'Kp={Kp}, Ki={Ki}')
    elif controller_type == PIDController:
        labels.append(f'Kp={Kp}, Ki={Ki}, Kd={Kd}')

    return times, trajectory, labels