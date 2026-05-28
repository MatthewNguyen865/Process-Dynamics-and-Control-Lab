class PIController:
    def __init__(self, Kp, setpoint, Ki, Kd=None):
        self.Kp = Kp
        self.Ki = Ki
        self.setpoint = setpoint
        self.integral = 0.0
    
    def compute_control(self, measurement, dt):
        error = self.setpoint - measurement
        self.integral += error * dt
        
        control_signal = self.Kp * error + self.Ki * self.integral
        return control_signal