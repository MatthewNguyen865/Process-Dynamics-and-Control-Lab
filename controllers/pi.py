class PIController:
    def __init__(self, Kp, setpoint, Ki):
        self.Kp = Kp
        self.Ki = Ki
        self.setpoint = setpoint
        self.integral = 0.0
    
    def compute_control(self, current_temp, dt):
        error = self.setpoint - current_temp
        self.integral += error * dt
        
        control_signal = self.Kp * error + self.Ki * self.integral
        return control_signal