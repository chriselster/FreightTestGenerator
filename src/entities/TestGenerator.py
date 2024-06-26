from random import randint

from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.carrier import Carrier
from entities.fare import FareFactory
from entities.ParamReader import ParamReader
from entities.item import Item
from entities.vehicle import Vehicle
from entities.utils import Quadrants
from entities.point import Point

from factories.VehicleFactory import VehicleFactory
from factories.ItemFactory import ItemFactory
from factories.CarrierFactory import CarrierFactory


class TestGenerator:
    def __init__(self):
        self.itemFactory = ItemFactory()
        self.vehicleFactory = VehicleFactory()
        self.carrierFactory = CarrierFactory()
        self.fareFactory = FareFactory()

    def buildClients(self, amount, clusterType):
        clients = []
        for index, point in enumerate(PointsGenerator().generate(amount, clusterType)):
            clients.append(Client(index, point.x, point.y))
        return clients

    def buildItems(self):
        result = []
        with open("in/item_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        self.itemFactory.set_min_weight(float(reader.next()[0]))
        self.itemFactory.set_max_weight(float(reader.next()[0]))
        self.itemFactory.set_types([int(reader.next()[0])])
        quantity = int(reader.next()[0])
        total = 0
        clientId = 0
        while total < quantity:
            numberOfItems = min(randint(1, 5), quantity - total)
            self.itemFactory.set_client_id(clientId)
            result.extend(self.itemFactory.generate(numberOfItems))
            clientId += 1
            total += numberOfItems
        return result, clientId

    def buildCarriers(self) -> list[Carrier]:
        with open("in/carriers_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        quantity = int(reader.next()[0])
        self.carrierFactory.setQuadrants(reader.next())
        self.carrierFactory.setMinimalContractedLoadPercentages(reader.next())
        self.carrierFactory.setCostsPerAdditionalCustomer(reader.next())
        self.carrierFactory.setMaxDistanceBetweenCustomers(reader.next() * 100)
        self.carrierFactory.setDiscountPerCapacityIncrease(reader.next())
        self.carrierFactory.setBaseCosts(reader.next())
        return self.carrierFactory.generate(quantity)

    def buildVehicles(
        self,
        carriers: list[Carrier],
        items: list[Item],
        clients: list[Client],
        itemTypePerVehicleType: dict,
    ):
        with open("in/vehicle_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        types = reader.next()
        capacities = reader.next()
        # map types to int
        types = [int(t) for t in types]
        self.vehicleFactory.carriers = carriers
        self.vehicleFactory.item_type_per_vehicle_type = itemTypePerVehicleType
        self.vehicleFactory.set_capacities(capacities)
        with open("in/fares.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        fares = reader.next()
        result = list[Vehicle]()
        for item in items:
            if self.anyVehicleCanAttend(carriers, itemTypePerVehicleType, result, item):
                continue
            vehicle = self.vehicleFactory.generate_vehicle_that_attends_item(
                item, clients[item.clientId]
            )
            vehicle.attend(item)
            result.append(vehicle)
        for vehicle in result:
            vehicle.costPerKmPerWeight = (
                vehicle.costPerKmPerWeight
                - capacities.index(vehicle.capacity)
                * carriers[vehicle.carrierId].discountPerCapacityIncrease
            ) * fares[vehicle.type - 1]
            vehicle.costPerKmPerWeight = round(vehicle.costPerKmPerWeight,2)
        return result

    def anyVehicleCanAttend(
        self, carriers, itemTypePerVehicleType, result: list[Vehicle], item
    ):
        for vehicle in result:
            if (
                vehicle.canAttend(item)
                and carriers[vehicle.carrierId].canAttend(item.clientId)
                and item.type in itemTypePerVehicleType[vehicle.type]
            ):
                vehicle.attend(item)
                return True

    def buildQuadrants(self):
        return [Quadrants(i + 1) for i in range(5)]

    def setItemDestinations(self, items: list[Item], clients: list[Client]):
        for item in items:
            client = clients[item.clientId]
            item.destination = Point(client.x, client.y)
