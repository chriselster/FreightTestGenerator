

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
        self.quadrants = quadrants
        self.minimumCapacity = minimumCapacity
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.discoutPerCapacityIncrease = discoutPerCapacityIncrease
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers
        self.clients = []
        self.vehicle_capacities = []
        self.accepted_types = []
        self.fares = {}

    def asList(self):
        return [self.id,
                self.minimumCapacity,
                self.costPerAdditionalCustomer,
                self.discoutPerCapacityIncrease,
                self.maxDistanceBetweenCustomers]

    def generateClientList(self, clients):
        if self.quadrants.count(1) == 1:
            self.clients += [
                client for client in clients if client.position.x < 50 and client.position.y < 50]

        if self.quadrants.count(2) == 1:
            self.clients += [
                client for client in clients if client.position.x > 50 and client.position.y < 50]

        if self.quadrants.count(3) == 1:
            self.clients += [
                client for client in clients if client.position.x < 50 and client.position.y > 50]

        if self.quadrants.count(4) == 1:
            self.clients += [
                client for client in clients if client.position.x > 50 and client.position.y > 50]

    def add_vehicle_capacities(self, weights):
        self.vehicle_capacities = weights

    def add_accepted_types(self, types):
        self.accepted_types = types

    def add_fare(self, vehicle_type, fare):
        self.fares[vehicle_type] = fare

    def add_vehicle(self, vehicle):
        vehicle.type = random.choice(self.accepted_types)
        vehicle.capacity = random.choice(self.vehicle_capacities)
        vehicle.deadFreight = vehicle.capacity * self.minimumCapacity
        vehicle.costPerKmPerWeight = self.fares[vehicle.type]
        index = self.vehicle_capacities.index(vehicle.capacity)
        vehicle.costPerKmPerWeight -= 0.5 * index


class CarrierFactory:

    def __init__(self):
        self.index = 0
        self.possibleQuadrants = []
        self.possibleMinimumCapacities = []
        self.costPerAdditionalCustomer = 0
        self.discoutPerCapacityIncrease = 0.2
        self.maxDistanceBetweenCustomers = []
        self.read_params()

    def generate(self):
        self.index += 1
        return Carrier(self.index,
                       self.possibleQuadrants[self.index-1],
                       random.choice(self.possibleMinimumCapacities),
                       self.costPerAdditionalCustomer,
                       self.discoutPerCapacityIncrease,
                       random.choice(self.maxDistanceBetweenCustomers),
                       )

    def read_params(self):
        with open("in/carriers_params.txt", "r", encoding=" utf-8") as f:
            params = f.read().splitlines()
            reader = ParamReader(params)
            reader.next()
            self.possibleQuadrants = reader.next()
            self.possibleMinimumCapacities = reader.next()
            self.costPerAdditionalCustomer = reader.next()[0]
            self.maxDistanceBetweenCustomers = reader.next()
            self.discoutPerCapacityIncrease = reader.next()[0]
