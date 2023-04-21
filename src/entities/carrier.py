

import random

from entities.ParamReader import ParamReader


class Carrier:
    quadrants = []

    @staticmethod
    def header():
        return ['id', 'minimumCapacity',
                'costPerAdditionalCustomer',
                'discoutPerCapacityIncrease',
                'maxDistanceBetweenCustomers',]

    def __init__(self, index,
                 quadrants,
                 minimumCapacity,
                 costPerAdditionalCustomer,
                 discoutPerCapacityIncrease,
                 maxDistanceBetweenCustomers):
        self.id = index
        # Cost per weight per km for each vehicle type
        self.quadrants = quadrants
        # Percentage of the vehicle capacity that must be filled
        self.minimumCapacity = minimumCapacity
        # Base value +- 10%
        self.costPerAdditionalCustomer = costPerAdditionalCustomer

        # Desconto por kg total do caminhão
        self.discoutPerCapacityIncrease = discoutPerCapacityIncrease

        # 5% / 2,5%
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers
        self.clients = []

    def asList(self):
        return [self.id,
                self.minimumCapacity,
                self.costPerAdditionalCustomer,
                self.discoutPerCapacityIncrease,
                self.maxDistanceBetweenCustomers]

    def generateClientList(self, clients):
        if self.quadrants.count(1) == 1:
            # x < 50 and y < 50
            self.clients += [
                client for client in clients if client.position.x < 50 and client.position.y < 50]
        if self.quadrants.count(2) == 1:
            # x > 50 and y < 50
            self.clients += [
                client for client in clients if client.position.x > 50 and client.position.y < 50]
        if self.quadrants.count(3) == 1:
            # x < 50 and y > 50
            self.clients += [
                client for client in clients if client.position.x < 50 and client.position.y > 50]
        if self.quadrants.count(4) == 1:
            # x > 50 and y > 50
            self.clients += [
                client for client in clients if client.position.x > 50 and client.position.y > 50]


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
                       self.quadrants[self.index-1],
                       random.choice(self.minimumCapacity),
                       self.costPerAdditionalCustomer,
                       self.discoutPerCapacityIncrease,
                       random.choice(self.maxDistanceBetweenCustomers),
                       )

    def read_params(self):
        with open("in/carriers_params.txt", "r", encoding=" utf-8") as f:
            params = f.read().splitlines()
            reader = ParamReader(params)
            reader.next()
            self.quadrants = reader.next()
            self.minimumCapacity = reader.next()
            self.costPerAdditionalCustomer = reader.next()[0]
            self.maxDistanceBetweenCustomers = reader.next()
            self.discoutPerCapacityIncrease = reader.next()[0]
