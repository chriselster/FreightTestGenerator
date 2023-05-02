from random import choice
from entities.carrier import Carrier


class CarrierFactory:
    def __init__(self):
        self.baseCosts = []

    def generate(self, quantity):
        result = []
        for index in range(quantity):
            result.append(self.generateCarrier(index))
        return result

    def generateCarrier(self, index):
        carrier = Carrier.fromIndex(index)
        carrier.baseCost = choice(self.baseCosts)
        return carrier

    def setBaseCosts(self, baseCosts):
        self.baseCosts = baseCosts
