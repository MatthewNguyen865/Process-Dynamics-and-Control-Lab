class PController:
    def __init__(self, Kp, setpoint):
        self.Kp = Kp
        self.setpoint = setpoint
    
    
    def compute_control(self, current_temp):
        error = self.setpoint - current_temp
        control_signal = self.Kp * error
        return control_signal