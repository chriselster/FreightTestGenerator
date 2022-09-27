from random import randint, uniform


class Veichle:
    def __init__(self, index, type, capacity, minimumCapacity, costPerAdditionalCustomer,
                 pricePerWeightperKm, allowedItemTypes, maxDistanceBetweenCustomers):
        self.index = index
        self.type = type
        self.capacity = capacity
        self.minimumCapacity = minimumCapacity
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        self.pricePerWeightperKm = pricePerWeightperKm
        self.allowedItemTypes = allowedItemTypes
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    def __str__(self):
        return f"{str(self.index)},{str(self.type)},{str(self.capacity)},{str(self.minimumCapacity)}"


class VeichleFactory:
    def __init__(self):
        self.index = 0
        self.types = 10
        self.min_capacity = 50
        self.max_capacity = 500
        self.min_minimumCapacity = 1
        self.max_minimumCapacity = 50
        self.min_costPerAdditionalCustomer = 1
        self.max_costPerAdditionalCustomer = 10
        self.min_pricePerWeightperKm = 1
        self.max_pricePerWeightperKm = 10
        self.min_maxDistanceBetweenCustomers = 5
        self.max_maxDistanceBetweenCustomers = 100

    def create(self):
        veichle = Veichle(self.index, self.generate_type(), self.generate_capacity(), self.generate_minimumCapacity(),
                          self.generate_costPerAdditionalCustomer(), self.generate_pricePerWeightperKm(),
                          self.generate_allowedItemTypes(), self.generate_maxDistanceBetweenCustomers())
        self.index += 1
        return veichle

    def generate_allowedItemTypes(self):
        return self.generateRandomList(randint(1, 10))

    def generateRandomList(self, length):
        return [randint(1, 10) for _ in range(length)]

    def generate_type(self):
        return randint(1, self.types)

    def generate_capacity(self):
        return round(uniform(self.min_capacity, self.max_capacity), 2)

    def generate_minimumCapacity(self):
        return round(uniform(self.min_minimumCapacity, self.max_minimumCapacity), 2)

    def generate_costPerAdditionalCustomer(self):
        return round(uniform(self.min_costPerAdditionalCustomer, self.max_costPerAdditionalCustomer), 2)

    def generate_pricePerWeightperKm(self):
        return round(uniform(self.min_pricePerWeightperKm, self.max_pricePerWeightperKm), 2)

    def generate_maxDistanceBetweenCustomers(self):
        return round(uniform(self.min_maxDistanceBetweenCustomers, self.max_maxDistanceBetweenCustomers), 2)
