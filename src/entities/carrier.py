import random

from entities.client import Client


class Carrier:
    quadrants = []

    @staticmethod
    def fromIndex(index):
        return Carrier(index, [], 0, 0, 0, 0)

    def __init__(
        self,
        index,
        quadrants,
        minimalContractedLoadPercentage,
        costPerAdditionalCustomer,
        discoutPerCapacityIncrease,
        maxDistanceBetweenCustomers,
    ):
        self.index = index
        self.quadrants = quadrants
        self.minimalContractedLoadPercentage = minimalContractedLoadPercentage
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.discountPerCapacityIncrease = discoutPerCapacityIncrease
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers
        self.clients = []
        self.vehicle_capacities = []
        self.accepted_types = []
        self.fares = {}
        self.baseCost = 0

    def asList(self):
        return [
            self.index,
            self.minimalContractedLoadPercentage,
            self.costPerAdditionalCustomer,
            self.discountPerCapacityIncrease,
            self.maxDistanceBetweenCustomers,
        ]

    def generateClientList(self, clients):
        if self.quadrants.count(1) == 1:
            self.clients += [
                client for client in clients if client.x < 50 and client.y < 50
            ]

        if self.quadrants.count(2) == 1:
            self.clients += [
                client for client in clients if client.x > 50 and client.y < 50
            ]

        if self.quadrants.count(3) == 1:
            self.clients += [
                client for client in clients if client.x < 50 and client.y > 50
            ]

        if self.quadrants.count(4) == 1:
            self.clients += [
                client for client in clients if client.x > 50 and client.y > 50
            ]

    def add_vehicle_capacities(self, weights):
        self.vehicle_capacities = weights

    def add_accepted_types(self, types):
        self.accepted_types = types

    def add_fare(self, vehicle_type, fare):
        self.fares[vehicle_type] = fare

    def add_vehicle(self, vehicle):
        vehicle.type = random.choice(self.accepted_types)
        vehicle.capacity = random.choice(self.vehicle_capacities)
        vehicle.deadFreight = vehicle.capacity * self.minimalContractedLoadPercentage
        vehicle.costPerKmPerWeight = self.fares[vehicle.type]
        index = self.vehicle_capacities.index(vehicle.capacity)
        vehicle.costPerKmPerWeight -= 0.5 * index

    def canAttend(self, clientId: int):
        return clientId in map(lambda client: client.index, self.clients)
