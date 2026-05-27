class PController:
    def __init__(self, Kp, setpoint, Ki=None):
        self.Kp = Kp
        self.setpoint = setpoint
    
    
    def compute_control(self, current_temp, dt=None):
        error = self.setpoint - current_temp
        control_signal = self.Kp * error
        return control_signal