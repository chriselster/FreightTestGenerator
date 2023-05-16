from random import randint, seed


from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.carrier import Carrier
from entities.fare import FareFactory
from entities.ParamReader import ParamReader
from entities.utils import Quadrants
from factories.VehicleFactory import VehicleFactory
from factories.ItemFactory import ItemFactory
from factories.CarrierFactory import CarrierFactory


class TestGenerator:
    itemFactory = ItemFactory()
    vehicleFactory = VehicleFactory()
    carrierFactory = CarrierFactory()
    fareFactory = FareFactory()

    def __init__(self):
        with open("in/cluster_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
            seed(int(reader.next()[0]))  # type: ignore

    def buildClients(self):
        clients = []
        for index, point in enumerate(PointsGenerator().generate()):  # type: ignore
            clients.append(Client(index, point.x, point.y))
        return clients

    def buildItems(self, clients):
        result = []
        with open("in/item_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        self.itemFactory.set_min_weight(float(reader.next()[0]))  # type: ignore
        self.itemFactory.set_max_weight(float(reader.next()[0]))  # type: ignore
        self.itemFactory.set_types([int(reader.next()[0])])  # type: ignore
        for index, _ in enumerate(clients):
            self.itemFactory.set_client_id(clients[index].index)
            result.extend(self.itemFactory.generate(randint(1, 5)))
        return result

    def buildCarriers(self) -> list[Carrier]:
        with open("in/carriers_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        quantity = int(reader.next()[0])  # type: ignore
        self.carrierFactory.setQuadrants(reader.next())  # type: ignore
        self.carrierFactory.setMinimalContractedLoadPercentages(
            reader.next()
        )  # type: ignore
        self.carrierFactory.setCostsPerAdditionalCustomer(reader.next())  # type: ignore
        self.carrierFactory.setMaxDistanceBetweenCustomers(
            reader.next() * 100
        )  # type: ignore
        self.carrierFactory.setDiscountPerCapacityIncrease(
            reader.next()
        )  # type: ignore
        self.carrierFactory.setBaseCosts(reader.next())  # type: ignore
        return self.carrierFactory.generate(quantity)

    def buildVehicles(self, carriers: list[Carrier]):
        with open("in/vehicle_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        types = reader.next()  # type: ignore
        capacities = reader.next()  # type: ignore
        # map types to int
        types = [int(t) for t in types]  # type: ignore
        self.vehicleFactory.set_possible_types(types)
        self.vehicleFactory.set_capacities(capacities)
        with open("in/fares.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.readlines())
        fares = reader.next()  # type: ignore
        result = []
        for carrier in carriers:
            self.vehicleFactory.set_additional_delivery_costs(
                [carrier.costPerAdditionalCustomer]
            )
            self.vehicleFactory.set_max_distance_between_customers(
                [carrier.maxDistanceBetweenCustomers]
            )
            self.vehicleFactory.set_carrier_id(carrier.index)
            self.vehicleFactory.set_min_capacity_factors(
                [carrier.minimalContractedLoadPercentage]
            )
            self.vehicleFactory.set_cost_per_km_per_weight([carrier.baseCost])
            vehicles = self.vehicleFactory.generate(5)
            for vehicle in vehicles:
                # subtract index of vehicle weight in capacities * carrier.discountPerCapacityIncrease
                vehicle.costPerKmPerWeight = (
                    vehicle.costPerKmPerWeight
                    - capacities.index(vehicle.capacity)
                    * carrier.discountPerCapacityIncrease
                ) * fares[vehicle.type - 1]
            result.extend(vehicles)
        return result

    def buildQuadrants(self):
        return [Quadrants(i + 1) for i in range(5)]
