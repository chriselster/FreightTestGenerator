from random import choice
from entities.vehicle import Vehicle


class VehicleFactory:
    def __init__(self):
        self.index = 0
        self.capacities = []
        self.min_capacity_factors = []
        self.cost_per_km_per_weight = []
        self.additional_delivery_costs = []
        self.max_distance_between_customers = []
        self.possible_types = []
        self.carrier_id = 0

    def generate(self, quantity) -> list[Vehicle]:
        return [self.buildVehicle() for _ in range(quantity)]

    def buildVehicle(self) -> Vehicle:
        vehicle = Vehicle.empty()
        vehicle.index = self.index
        self.index += 1
        vehicle.capacity = choice(self.capacities)
        vehicle.min_capacity = choice(self.min_capacity_factors) * vehicle.capacity
        vehicle.costPerKmPerWeight = choice(self.cost_per_km_per_weight)
        vehicle.additionalDeliveryCost = choice(self.additional_delivery_costs)
        vehicle.maxDistanceBetweenCustomers = choice(
            self.max_distance_between_customers
        )
        vehicle.carrierId = self.carrier_id
        vehicle.type = choice(self.possible_types)
        return vehicle

    def set_capacities(self, capacities):
        self.capacities = capacities

    def set_min_capacity_factors(self, min_capacity_factors):
        self.min_capacity_factors = min_capacity_factors

    def set_cost_per_km_per_weight(self, cost_per_km_per_weight):
        self.cost_per_km_per_weight = cost_per_km_per_weight

    def set_additional_delivery_costs(self, additional_delivery_costs):
        self.additional_delivery_costs = additional_delivery_costs

    def set_max_distance_between_customers(self, max_distance_between_customers):
        self.max_distance_between_customers = max_distance_between_customers

    def set_carrier_id(self, carrier_id):
        self.carrier_id = carrier_id

    def set_possible_types(self, possible_types):
        self.possible_types = possible_types
