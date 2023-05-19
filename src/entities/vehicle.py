from entities.item import Item


class Vehicle:
    @staticmethod
    def header():
        return ["index", "type", "capacity", "carrierId"]

    def __init__(self, index, _type, capacity, carrierId):
        self.index = index
        self.type = _type
        self.capacity = capacity
        self.carrierId = carrierId
        self.min_capacity = 0
        self.costPerKmPerWeight = 0
        self.additionalDeliveryCost = 0
        self.maxDistanceBetweenCustomers = 0
        self.remainingCapacity = capacity

    def toCSVData(self):
        return VehicleCSVData.from_vehicle(self)

    @staticmethod
    # empty vehicle constructor
    def empty():
        return Vehicle(0, 0, 0, 0)

    def __str__(self):
        return f"{str(self.index)},{str(self.type)},{str(self.capacity)},"

    def asList(self):
        return [self.index, self.type, self.capacity, self.carrierId]

    def canAttend(self, item: Item):
        return self.remainingCapacity >= item.weight

    def attend(self, item: Item):
        self.remainingCapacity -= item.weight


class VehicleCSVData:
    def __init__(
        self,
        index: int,
        _type: int,
        capacity: float,
        carrierId: int,
        min_capacity: float,
        costPerKmPerWeight: float,
        additionalDeliveryCost: float,
        maxDistanceBetweenCustomers: float,
    ):
        self.index = index
        self.type = _type
        self.capacity = capacity
        self.carrierId = carrierId
        self.min_capacity = min_capacity
        self.costPerKmPerWeight = costPerKmPerWeight
        self.additionalDeliveryCost = additionalDeliveryCost
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    @staticmethod
    def from_vehicle(vehicle: Vehicle):
        return VehicleCSVData(
            vehicle.index,
            vehicle.type,
            vehicle.capacity,
            vehicle.carrierId,
            vehicle.min_capacity,
            vehicle.costPerKmPerWeight,
            vehicle.additionalDeliveryCost,
            vehicle.maxDistanceBetweenCustomers,
        )
