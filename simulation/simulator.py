from parameters import time_step, num_steps
class EulerSimulator():
    def simulate(self, model, initial_temp, time_step=time_step, num_steps=num_steps, controller=None):
        temperatures = [initial_temp]
        times = [0]
        current_temp = initial_temp
        for i in range(num_steps):
            if controller is not None:
                derivative = model.derivative(current_temp) + controller.compute_control(current_temp, time_step)
            else:
                derivative = model.derivative(current_temp)
            current_temp = current_temp + derivative * time_step
            temperatures.append(current_temp)
            times.append(times[-1] + time_step)
        return temperatures, times