

import random

from entities.ParamReader import ParamReader


class Carrier:
    @staticmethod
    def header():
        return ['id', 'quadrantId', 'minimumCapacity', 'costPerAdditionalCustomer', 'discoutPerCapacityIncrease', 'maxDistanceBetweenCustomers']

    def __init__(self, index,    quadrantId, minimumCapacity, costPerAdditionalCustomer, discoutPerCapacityIncrease, maxDistanceBetweenCustomers):
        self.id = index
        # Cost per weight per km for each vehicle type
        self.quadrantId = quadrantId
        # Percentage of the vehicle capacity that must be filled
        self.minimumCapacity = minimumCapacity
        # Base value +- 10%
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.discoutPerCapacityIncrease = discoutPerCapacityIncrease
        # 5% / 2,5%
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers
        self.clients = []

    def asList(self):
        return [self.id, self.quadrantId, self.minimumCapacity, self.costPerAdditionalCustomer, self.discoutPerCapacityIncrease, self.maxDistanceBetweenCustomers]

    def generateClientList(self, clients):
        if (self.quadrantId == 0):
            # x < 50 and y < 50
            self.clients = [
                client for client in clients if client.position.x < 50 and client.position.y < 50]
        elif (self.quadrantId == 1):
            # x > 50 and y < 50
            self.clients = [
                client for client in clients if client.position.x > 50 and client.position.y < 50]
        elif (self.quadrantId == 2):
            # x < 50 and y > 50
            self.clients = [
                client for client in clients if client.position.x < 50 and client.position.y > 50]
        elif (self.quadrantId == 3):
            # x > 50 and y > 50
            self.clients = [
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
