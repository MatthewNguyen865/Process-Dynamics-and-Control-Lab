class PIController:
    def __init__(self, setpoint: float, Kp: float, Ki: float, Kd=None):
        self.Kp = Kp
        self.Ki = Ki
        self.setpoint = setpoint
        self.integral = 0.0
    
    def compute_control(self, measurement: float, dt: float) -> float:
        error = self.setpoint - measurement
        self.integral += error * dt
        
        control_signal = self.Kp * error + self.Ki * self.integral
        return control_signal