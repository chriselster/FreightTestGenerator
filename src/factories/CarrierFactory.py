from random import choice
from entities.carrier import Carrier


class CarrierFactory:
    def __init__(self):
        self.baseCosts = []
        self.quadrants = []
        self.minimalContractedLoadPercentages = []
        self.costsPerAdditionalCustomer = []
        self.maxDistanceBetweenCustomers = []
        self.discountsPerCapacityIncrease = []

    def generate(self, quantity):
        result = []
        for index in range(quantity):
            result.append(self.generateCarrier(index))
        return result

    def generateCarrier(self, index):
        carrier = Carrier.fromIndex(index)
        carrier.baseCost = choice(self.baseCosts)
        carrier.quadrants = self.quadrants[index % len(self.quadrants)]
        carrier.minimalContractedLoadPercentage = choice(
            self.minimalContractedLoadPercentages
        )
        carrier.costPerAdditionalCustomer = choice(self.costsPerAdditionalCustomer)
        carrier.maxDistanceBetweenCustomers = choice(self.maxDistanceBetweenCustomers)
        carrier.discountPerCapacityIncrease = choice(self.discountsPerCapacityIncrease)
        return carrier

    def setBaseCosts(self, baseCosts):
        self.baseCosts = baseCosts

    def setQuadrants(self, quadrants):
        self.quadrants = quadrants

    def setMinimalContractedLoadPercentages(self, minimalContractedLoadPercentages):
        self.minimalContractedLoadPercentages = minimalContractedLoadPercentages

    def setCostsPerAdditionalCustomer(self, costsPerAdditionalCustomer):
        self.costsPerAdditionalCustomer = costsPerAdditionalCustomer

    def setMaxDistanceBetweenCustomers(self, maxDistanceBetweenCustomers):
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    def setDiscountPerCapacityIncrease(self, discountPerCapacityIncrease):
        self.discountsPerCapacityIncrease = discountPerCapacityIncrease
