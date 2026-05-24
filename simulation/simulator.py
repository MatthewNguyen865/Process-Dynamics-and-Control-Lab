class EulerSimulator():
    def simulate(self, model, initial_temp, time_step, num_steps):
        temperatures = [initial_temp]
        times = [0]
        current_temp = initial_temp
        for i in range(num_steps):
            derivative = model.derivative(current_temp)
            current_temp = current_temp + derivative * time_step
            temperatures.append(current_temp)
            times.append(times[-1] + time_step)
        return temperatures, times