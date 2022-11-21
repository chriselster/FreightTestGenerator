
from random import randint, seed

from entities.carrier import CarrierFactory
from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.fare import FareFactory
from entities.item import ItemFactory
from entities.ParamReader import ParamReader
from entities.utils import Quadrants
from entities.veichle import VeichleFactory


class TestGenerator:
    itemFactory = ItemFactory()
    veichleFactory = VeichleFactory()
    carrierFactory = CarrierFactory()

    def __init__(self):
        with open('in/cluster_params.txt', 'r') as f:
            reader = ParamReader(f.readlines())
            seed(int(reader.next()[0]))  # type: ignore

    @staticmethod
    def buildFares():
        fares = []
        with open("in/fares.txt") as f:
            fares.extend(FareFactory.createFare(line) for line in f)
        return fares

    def buildClients(self):
        clients = []
        allItems = []
        for index, point in enumerate(PointsGenerator().generate()):  # type: ignore
            items = []
            items.extend(self.itemFactory.create(index)
                         for _ in range(randint(1, 5)))
            allItems.extend(items)
            clients.append(Client(index, point, items))

        return clients, allItems

    def buildCarriers(self):
        carriers = []
        allVeichles = []
        for index in range(5):
            veichles = []
            veichles.extend(self.veichleFactory.create(index)
                            for _ in range(10))
            allVeichles.extend(veichles)
            carriers.append(self.carrierFactory.generate())

        return carriers, allVeichles

    def buildQuadrants(self):
        return [Quadrants(i+1) for i in range(5)]
