import numpy as np
import matplotlib.pyplot as plt
import os
from parameters import PLOT_DIR
class Plotting:
    def plot_trajectory(times, temperatures, labels, filename="temperature_trajectories.png", title="Temperature Trajectories", setpoint=None):
        
        if not os.path.exists(PLOT_DIR):
            os.makedirs(PLOT_DIR)
        
        plt.figure(figsize=(10, 6))
        
        #Plot stable and unstable equilibria
        plt.plot(times, np.ones_like(times) * 250, linestyle='--', color='gray', alpha=0.5,label='Stable Equilibria')
        plt.plot(times, np.ones_like(times) * 350, linestyle='--', color='gray', alpha=0.5)
        plt.plot(times, np.ones_like(times) * 300, linestyle=':', color='black', alpha=0.5, label='Unstable Equilibrium')
       
        #Plot trajectories
        for trajectory, label in zip(temperatures, labels):
                plt.plot(times, trajectory, label=label, linewidth=2)
        
        if setpoint is not None:
            plt.axhline(setpoint, color='red', linestyle='--', label='Setpoint')
        
        plt.xlabel('Time')
        plt.ylabel('Temperature (T)')
        plt.title(title)
        plt.grid()
        
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.savefig(f"{PLOT_DIR}/{filename}")

        plt.show()
    
    
    def plot_phase_portrait(model):
        if not os.path.exists(PLOT_DIR):
            os.makedirs(PLOT_DIR)
        
        T_values = np.linspace(220, 380, 100)
        dTdt_values = [model.derivative(T) for T in T_values]
        
        plt.figure(figsize=(10, 6))
        
        #Plot dT/dt vs T and markers for equilibria
        plt.plot(T_values, dTdt_values, label='dT/dt')
        plt.scatter(model.low_stable_equilibrium, 0, marker='o', color='green', label='Stable Equilibria')
        plt.scatter(model.unstable_equilibrium, 0, marker='o', edgecolors='red', facecolors='none', label='Unstable Equilibrium')
        plt.scatter(model.high_stable_equilibrium, 0, marker='o', color='green')
        
        #add arrows to indicate direction of flow
        low_midpoint = (model.low_stable_equilibrium+220)/2
        plt.arrow(low_midpoint, 7, np.sign(model.derivative(low_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        low_unstable_midpoint = (model.low_stable_equilibrium+model.unstable_equilibrium)/2
        plt.arrow(low_unstable_midpoint, 7, np.sign(model.derivative(low_unstable_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        high_unstable_midpoint = (model.high_stable_equilibrium+model.unstable_equilibrium)/2
        plt.arrow(high_unstable_midpoint, 7, np.sign(model.derivative(high_unstable_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        high_midpoint = (model.high_stable_equilibrium+380)/2
        plt.arrow(high_midpoint, 7, np.sign(model.derivative(high_midpoint))*10, 0, head_width=5, head_length=3, color='black')
        
        plt.axhline(0, color='black', linestyle='--')
        plt.xlabel('Temperature (T)')
        plt.ylabel('Temperature rate of change (dT/dt)')
        plt.title('Phase Portrait')
        plt.grid()
        
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{PLOT_DIR}/phase_portraits/phase_portrait.png")
        
        plt.show()