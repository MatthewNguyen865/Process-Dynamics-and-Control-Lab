class FirstOrderSystem():
    def __init__(self):
        self.low_stable_equilibrium = 250
        self.unstable_equilibrium = 300
        self.high_stable_equilibrium = 350

    def derivative(self, T, k=0.001):
        dTdt = k * -(T - self.low_stable_equilibrium) * (T - self.unstable_equilibrium) * (T - self.high_stable_equilibrium)
        return dTdt