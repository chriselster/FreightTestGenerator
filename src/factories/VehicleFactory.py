from random import choice
from entities.Vehicle import Vehicle

class VehicleFactory:
	def __init__(self):
		self.capacities = []
		self.min_capacity_factors = []
		self.cost_per_km_per_weight = []

	def generate(self, quantity):
		vehicle = Vehicle.empty()
		vehicle.capacity = choice(self.capacities)
		vehicle.min_capacity = choice(self.min_capacity_factors) * vehicle.capacity
		vehicle.costPerKmPerWeight = choice(self.cost_per_km_per_weight)
		return [vehicle]

	def set_capacities(self, capacities):
		self.capacities = capacities
  
	def set_min_capacity_factors(self, min_capacity_factors):
		self.min_capacity_factors = min_capacity_factors
  
	def set_cost_per_km_per_weight(self, cost_per_km_per_weight):
		self.cost_per_km_per_weight = cost_per_km_per_weight