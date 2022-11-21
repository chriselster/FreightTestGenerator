class Fare:
    @staticmethod
    def header():
        return ["veichleType, fare"]

    def __init__(self, veichleType, fare):
        self.vehicleType = veichleType
        self.fare = fare

    def asList(self):
        return [self.vehicleType, self.fare]
