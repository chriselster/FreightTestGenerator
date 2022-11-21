class Fare:
    @staticmethod
    def header():
        return ["veichleType", "fare"]

    def __init__(self, veichleType, fare):
        self.vehicleType = veichleType
        self.fare = fare

    def asList(self):
        return [self.vehicleType, self.fare]


class FareFactory:
    @staticmethod
    def createFare(line):
        tokens = line.split(",")
        return Fare(int(tokens[0].strip()), float(tokens[1].strip()))
