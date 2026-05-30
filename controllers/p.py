class PController:
    def __init__(self, setpoint: float, Kp: float, Ki=None, Kd=None):
        self.Kp = Kp
        self.setpoint = setpoint
    
    
    def compute_control(self, measurement: float, dt=None) -> float:
        error = self.setpoint - measurement
        control_signal = self.Kp * error
        return control_signal