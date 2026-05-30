import numpy as np
import matplotlib.pyplot as plt
import os
from controllers.p import PController
from models.first_order_system import FirstOrderSystem
class Plotting:
    @staticmethod
    def set_plotting_style():
        plt.style.use('default')

        plt.rcParams['figure.figsize'] = (10, 6)
        plt.rcParams['axes.grid'] = True
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['font.size'] = 12
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['legend.frameon'] = True
    
    @staticmethod
    def plot_trajectory(times: list[float], 
                        temperatures: list[list[float]], 
                        labels: list[str], 
                        filename: str="temperature_trajectories.png", 
                        title: str="Temperature Trajectories", 
                        setpoint: float | None=None
                        ) -> None:
        Plotting.set_plotting_style()
        plt.figure()

        #Plot stable and unstable equilibria
        plt.axhline(250, linestyle='--', color='gray', alpha=0.5,label='Stable Equilibria')
        plt.axhline(350, linestyle='--', color='gray', alpha=0.5)
        plt.axhline(300, linestyle=':', color='black', alpha=0.5, label='Unstable Equilibrium')
       
        #Plot trajectories
        for trajectory, label in zip(temperatures, labels):
                plt.plot(times, trajectory, label=label, linewidth=2)
        
        if setpoint is not None:
            plt.axhline(setpoint, color='red', linestyle='--', label='Setpoint')
        
        plt.xlabel('Time')
        plt.ylabel('Temperature (T)')
        plt.title(title)
        plt.xlim(times[0], times[-1])
        plt.grid(True, linestyle='--', alpha=0.5)
        
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)

        plt.show()
        plt.close()
    

    @staticmethod
    def draw_phase_portrait(model):

        T_values = np.linspace(220, 380, 100)
        dTdt_values = [model.derivative(T) for T in T_values]

        #Plot dT/dt vs T and markers for equilibria
        plt.plot(T_values, dTdt_values, label='dT/dt')
        plt.scatter(model.low_stable_equilibrium, 0, marker='o', color='green', label='Stable Equilibria')
        plt.scatter(model.unstable_equilibrium, 0, marker='o', edgecolors='red', facecolors='none', label='Unstable Equilibrium')
        plt.scatter(model.high_stable_equilibrium, 0, marker='o', color='green')
        
        plt.axhline(0, color='black', linestyle='--')
        plt.xlabel('Temperature (T)')
        plt.ylabel('Temperature rate of change (dT/dt)')

        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

    
    @staticmethod
    def plot_phase_portrait(model: FirstOrderSystem, filename: str="phase_portraits/phase_portrait.png") -> None:
        Plotting.set_plotting_style()
        plt.figure()

        plt.title('Phase Portrait')
        plt.xlim(220, 380)
        
        Plotting.draw_phase_portrait(model=model)

        #add arrows to indicate direction of flow
        low_midpoint = (model.low_stable_equilibrium+220)/2
        plt.arrow(low_midpoint, 7, np.sign(model.derivative(low_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        low_unstable_midpoint = (model.low_stable_equilibrium+model.unstable_equilibrium)/2
        plt.arrow(low_unstable_midpoint, 7, np.sign(model.derivative(low_unstable_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        high_unstable_midpoint = (model.high_stable_equilibrium+model.unstable_equilibrium)/2
        plt.arrow(high_unstable_midpoint, 7, np.sign(model.derivative(high_unstable_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        high_midpoint = (model.high_stable_equilibrium+380)/2
        plt.arrow(high_midpoint, 7, np.sign(model.derivative(high_midpoint))*10, 0, head_width=5, head_length=3, color='black')

        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)
        
        plt.show()
        plt.close()
    

    @staticmethod
    def plot_controlled_phase_portrait(model: FirstOrderSystem, 
                                       filename: str="phase_portraits/controlled_phase_portrait.png", 
                                       Kp: float=1.0, 
                                       setpoint: float=300
                                       ):
        Plotting.set_plotting_style()
        plt.figure()
        
        plt.title('Controlled vs Uncontrolled Phase Portrait')
        plt.xlim(220, 380)
        T_values = np.linspace(220, 380, 100)
        controller = PController(Kp=Kp, setpoint=setpoint)
        dTdt_values = [model.derivative(T) + controller.compute_control(T) for T in T_values]
        plt.plot(T_values, dTdt_values, label='Controlled dT/dt', linewidth=2, linestyle='--')
        Plotting.draw_phase_portrait(model=model)

        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)

        plt.show()
        plt.close()