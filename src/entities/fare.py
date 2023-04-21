import random


class Fare:
    @staticmethod
    def header():
        return ["vehicleType", "fare", "carrierId"]

    def __init__(self, vehicleType, fare, carrierId):
        self.vehicleType = vehicleType
        self.fare = fare
        self.carrierId = carrierId

    def asList(self):
        # round to 2 decimals
        return [self.vehicleType, round(self.fare, 2), self.carrierId]


class FareFactory:
    maxFarePerVehicleType = {}

    def readParams(self):
        with open("in/fares.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                tokens = line.split(",")
                self.maxFarePerVehicleType[int(
                    tokens[0].strip())] = float(tokens[1].strip())

    def createFares(self, carrierId):
        return [
            Fare(
                vehicleType,
                random.uniform(0, self.maxFarePerVehicleType[vehicleType]),
                carrierId,
            )
            for vehicleType in self.maxFarePerVehicleType.keys()
        ]
