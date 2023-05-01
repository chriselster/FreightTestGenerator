
from random import randint, seed

from entities.carrier import CarrierFactory
from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.fare import FareFactory
from entities.item import ItemFactory
from entities.ParamReader import ParamReader
from entities.utils import Quadrants
from Vehicle import VehicleFactory


class TestGenerator:
    itemFactory = ItemFactory()
    vehicleFactory = VehicleFactory()
    carrierFactory = CarrierFactory()
    fareFactory = FareFactory()

    def __init__(self):
        with open('in/cluster_params.txt', 'r', encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
            seed(int(reader.next()[0]))  # type: ignore

    def buildFares(self, carriersLength):
        self.fareFactory.readParams()
        fares = []
        for carrierId in range(1, carriersLength + 1):
            fares.extend(self.fareFactory.createFares(carrierId))

        return fares

    def buildClients(self):
        clients = []
        allItems = []
        for index, point in enumerate(PointsGenerator().generate(), 1):  # type: ignore
            items = []
            items.extend(self.itemFactory.create(index)
                         for _ in range(randint(1, 5)))
            allItems.extend(items)
            clients.append(Client(index, point, items))

        return clients, allItems

    def buildCarriers(self):
        carriers = []
        allVehicles = []
        for index in range(1, 6):
            vehicles = []
            vehicles.extend(self.vehicleFactory.create(index)
                            for _ in range(10))
            allVehicles.extend(vehicles)
            carriers.append(self.carrierFactory.generate())

        return carriers, allVehicles

    def buildQuadrants(self):
        return [Quadrants(i+1) for i in range(5)]
