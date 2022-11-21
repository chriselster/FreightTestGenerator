

import random

from entities.ParamReader import ParamReader


class Carrier:
    @staticmethod
    def header():
        return ['id', 'quadrantId', 'minimumCapacity', 'costPerAdditionalCustomer', 'discoutPerCapacityIncrease', 'maxDistanceBetweenCustomers']

    def __init__(self, index,    quadrants, minimumCapacity, costPerAdditionalCustomer, discoutPerCapacityIncrease, maxDistanceBetweenCustomers):
        self.id = index
        # Cost per weight per km for each veichle type
        self.quadrants = quadrants
        # Percentage of the veichle capacity that must be filled
        self.minimumCapacity = minimumCapacity
        # Base value +- 10%
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.discoutPerCapacityIncrease = discoutPerCapacityIncrease
        # 5% / 2,5%
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    def asList(self):
        return [self.id, self.quadrants, self.minimumCapacity, self.costPerAdditionalCustomer, self.discoutPerCapacityIncrease, self.maxDistanceBetweenCustomers]


class CarrierFactory:

    def __init__(self):
        self.index = 0
        self.quadrants = []
        self.minimumCapacity = []
        self.costPerAdditionalCustomer = 0
        self.discoutPerCapacityIncrease = 0.2
        self.maxDistanceBetweenCustomers = []
        self.read_params()

    def generate(self):
        self.index += 1
        return Carrier(self.index,
                       random.randint(1, len(self.quadrants)),
                       random.choice(self.minimumCapacity),
                       self.costPerAdditionalCustomer,
                       self.discoutPerCapacityIncrease,
                       random.choice(self.maxDistanceBetweenCustomers),
                       )

    def read_params(self):
        with open("in/carriers_params.txt", "r") as f:
            params = f.read().splitlines()
            reader = ParamReader(params)
            reader.next()
            self.quadrants = reader.next()
            self.minimumCapacity = reader.next()
            self.costPerAdditionalCustomer = reader.next()[0]
            self.maxDistanceBetweenCustomers = reader.next()
            self.discoutPerCapacityIncrease = reader.next()[0]
