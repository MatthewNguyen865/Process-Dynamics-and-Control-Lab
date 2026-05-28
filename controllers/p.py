class PController:
    def __init__(self, Kp, setpoint, Ki=None, Kd=None):
        self.Kp = Kp
        self.setpoint = setpoint
    
    
    def compute_control(self, measurement, dt=None):
        error = self.setpoint - measurement
        control_signal = self.Kp * error
        return control_signal