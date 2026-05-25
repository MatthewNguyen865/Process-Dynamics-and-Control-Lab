import numpy as np
import matplotlib.pyplot as plt
import os
from parameters import PLOT_DIR
class Plotting:
    def plot_trajectory(times, temperatures, labels):
        
        if not os.path.exists(PLOT_DIR):
            os.makedirs(PLOT_DIR)
        
        plt.figure(figsize=(10, 6))
        
        #Plot stable and unstable equilibria
        plt.plot(times, np.ones_like(times) * 250, linestyle='--', color='gray', alpha=0.5,label='Stable Equilibria')
        plt.plot(times, np.ones_like(times) * 350, linestyle='--', color='gray', alpha=0.5)
        plt.plot(times, np.ones_like(times) * 300, linestyle=':', color='black', label='Unstable Equilibrium')
       
        #Plot trajectories
        for trajectory, label in zip(temperatures, labels):
                plt.plot(times, trajectory, label=label, linewidth=2)
        
        plt.xlabel('Time')
        plt.ylabel('Temperature (T)')
        plt.title('Temperature Trajectories')
        plt.grid()
        
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.savefig(f"{PLOT_DIR}/temperature_trajectories.png")

        plt.show()