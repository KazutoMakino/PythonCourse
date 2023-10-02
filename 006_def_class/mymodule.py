class MyCalculator:
    z = 100

    def __init__(self, x, y=10):
        self.x = x
        self.y = y

    def add_xyz(self):
        return self.x + self.y + self.z

    @classmethod
    def get_z_squared(cls):
        return cls.z**2

    @staticmethod
    def returns_value_sqrt(value):
        return value ** (1 / 2)
