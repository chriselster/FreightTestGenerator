from random import randint, uniform


class Veichle:
    def __init__(self, id):
        self.id = id
        self.type = randint(1, 10)
        self.capacity = round(uniform(50, 500), 2)
        self.minimumCapacity = round(uniform(1, 50), 2)
        self.costPerAdditionalCustomer = round(uniform(1, 10), 2)
        self.pricePerWeightperKm = round(uniform(1, 10), 2)
        self.allowedItemTypes = self.generateRandomList(randint(1, 10))
        self.maxDistanceBetweenCustomers = round(uniform(5, 100), 2)

    def generateRandomList(self, length):
        return [randint(1, 10) for _ in range(length)]

    def __str__(self):
        return f"{str(self.id)},{str(self.type)},{str(self.capacity)},{str(self.minimumCapacity)}"
