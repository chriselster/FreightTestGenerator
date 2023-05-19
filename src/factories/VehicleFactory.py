from random import choice
from entities.carrier import Carrier
from entities.client import Client
from entities.item import Item

from entities.vehicle import Vehicle


class VehicleFactory:
    def __init__(self):
        self.index = 0
        self.capacities = []
        self.min_capacity_factors = []
        self.cost_per_km_per_weight = []
        self.additional_delivery_costs = []
        self.max_distance_between_customers = []
        self.item_type_per_vehicle_type = {}
        self.carriers = list[Carrier]()

    def set_capacities(self, capacities):
        self.capacities = capacities

    def generate_vehicle_that_attends_item(self, item: Item, client: Client) -> Vehicle:
        vehicle = Vehicle.empty()
        vehicle.capacity = next(
            (capacity for capacity in self.capacities if capacity >= item.weight), None
        )
        vehicle.type = self.get_possible_type(item.type)
        selectedCarrier = self.get_carrier_that_attends_item(client)
        vehicle.carrierId = selectedCarrier.index
        self.set_parameters(selectedCarrier)
        return self.build(vehicle)

    def get_carrier_that_attends_item(self, client) -> Carrier:
        possibleCarriers = list(
            filter(
                lambda carrier: carrier.attends(client),
                self.carriers,
            )
        )
        return choice(possibleCarriers)

    def set_parameters(self, selectedCarrier: Carrier):
        self.min_capacity_factors = selectedCarrier.minimalContractedLoadPercentage
        self.cost_per_km_per_weight = selectedCarrier.baseCost
        self.additional_delivery_costs = selectedCarrier.costPerAdditionalCustomer
        self.max_distance_between_customers = (
            selectedCarrier.maxDistanceBetweenCustomers
        )
        self.possible_types = selectedCarrier.accepted_types

    def build(self, vehicle: Vehicle):
        vehicle.index = self.index
        self.index += 1
        vehicle.min_capacity = self.min_capacity_factors * vehicle.capacity
        vehicle.costPerKmPerWeight = self.cost_per_km_per_weight
        vehicle.additionalDeliveryCost = self.additional_delivery_costs
        vehicle.maxDistanceBetweenCustomers = self.max_distance_between_customers

        return vehicle

    def get_possible_type(self, item_type: int) -> int:
        possible_types = self.item_type_per_vehicle_type[item_type]
        return choice(possible_types)
