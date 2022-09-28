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
        self.read_params()

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

    def read_params(self):
        with open("in/veichle_params.txt", "r") as f:
            params = f.read().splitlines()
            self.types = int(self.parse_value(params[0]))
            self.min_capacity = float(self.parse_value(params[1]))
            self.max_capacity = float(self.parse_value(params[2]))
            self.min_minimumCapacity = float(self.parse_value(params[3]))
            self.max_minimumCapacity = float(self.parse_value(params[4]))
            self.min_costPerAdditionalCustomer = float(
                self.parse_value(params[5]))
            self.max_costPerAdditionalCustomer = float(
                self.parse_value(params[6]))
            self.min_pricePerWeightperKm = float(self.parse_value(params[7]))
            self.max_pricePerWeightperKm = float(self.parse_value(params[8]))
            self.min_maxDistanceBetweenCustomers = float(
                self.parse_value(params[9]))
            self.max_maxDistanceBetweenCustomers = float(
                self.parse_value(params[10]))

    def parse_value(self, line):
        return line.split(":")[1].strip()
