

import random

from entities.fares import Fares


class Carrier:
    @staticmethod
    def header():
        return ['baseFarePerType', 'quadrants', 'minimumCapacity', 'costPerAdditionalCustomer', 'discoutPerCapacityIncrease', 'maxDistanceBetweenCustomers']

    def __init__(self,  veichles, baseFarePerType, quadrants, minimumCapacity, costPerAdditionalCustomer, discoutPerCapacityIncrease, maxDistanceBetweenCustomers):
        self.veichles = veichles
        # Cost per weight per km for each veichle type
        self.baseFarePerType = baseFarePerType
        self.quadrants = quadrants
        # Percentage of the veichle capacity that must be filled
        self.minimumCapacity = minimumCapacity
        # Base value +- 10%
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.discoutPerCapacityIncrease = discoutPerCapacityIncrease
        # 5% / 2,5%
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    def __str__(self):
        veichles = ''.join(f"{str(veichle)}\n" for veichle in self.veichles)
        info = f"{str(self.baseFarePerType)},{str(self.quadrants)},{str(self.minimumCapacity)},{str(self.costPerAdditionalCustomer)},{str(self.discoutPerCapacityIncrease)},{str(self.maxDistanceBetweenCustomers)},{len(self.veichles)}\n"

        return info + veichles

    def asList(self):
        return [self.baseFarePerType, self.quadrants, self.minimumCapacity, self.costPerAdditionalCustomer, self.discoutPerCapacityIncrease, self.maxDistanceBetweenCustomers]

    def veichlesIds(self):
        return "/".join([str(veichle.index) for veichle in self.veichles])

    def veichlesAsList(self):
        return [veichle.index for veichle in self.veichles]


class CarrierFactory:
    def __init__(self):
        self.index = 0
        self.quadrants = []
        self.minimumCapacity = 0
        self.costPerAdditionalCustomer = 20
        self.discoutPerCapacityIncrease = 0.2
        self.maxDistanceBetweenCustomers = 0
        self.read_params()

    def generate(self, veichles):
        self.index += 1
        return Carrier(veichles,
                       self.baseFarePerType,
                       random.randint(1, len(self.quadrants)),
                       self.minimumCapacity,
                       self.costPerAdditionalCustomer,
                       self.discoutPerCapacityIncrease,
                       self.maxDistanceBetweenCustomers,
                       )

    def read_params(self):
        with open("in/carriers_params.txt", "r") as f:
            params = f.read().splitlines()
            self.baseFarePerType = Fares(
                self.parse_value(params[1]).split(","))
            self.readQuadrants(params)
            self.readMinimumCapacity(params)

    def readQuadrants(self, params):
        quadrants = self.parse_value(params[2])
        quadrants = quadrants.split(",")
        self.quadrants = quadrants

    def readMinimumCapacity(self, params):
        minimumCapacity = self.parse_value(params[3])
        self.minimumCapacity = self.getRandomFromList(minimumCapacity)

    def readMaxDistanceBetweenCustomers(self, params):
        distanceList = self.parse_value(params[4])
        self.maxDistanceBetweenCustomers = self.getRandomFromList(distanceList)

    def getRandomFromList(self, value):
        return random.choice(value.split(","))

    def parse_value(self, line):
        return line.split(":")[1].strip()
