class PIDController:
    def __init__(self, setpoint: float, Kp: float, Ki: float, Kd: float):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint

        self.integral = 0.0
        self.previous_error = 0.0

    def compute_control(self, measurement: float, dt: float) -> float:
        error = self.setpoint - measurement

        self.integral += error * dt

        derivative = (error - self.previous_error) / dt

        control_signal = (
            self.Kp * error
            + self.Ki * self.integral
            + self.Kd * derivative
        )

        self.previous_error = error

        return control_signal