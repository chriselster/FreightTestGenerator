class Vehicle:
    @staticmethod
    def header():
        return ['index', 'type', 'capacity', 'carrierId']

    def __init__(self, index, _type, capacity, carrierId):
        self.index = index
        self.type = _type
        self.capacity = capacity
        self.carrierId = carrierId
        self.min_capacity = 0
        self.costPerKmPerWeight = 0
        self.additionalDeliveryCost = 0
        self.maxDistanceBetweenCustomers = 0

    @staticmethod
    # empty vehicle constructor
    def empty():
        return Vehicle(0, 0, 0, 0)

    def __str__(self):
        return f"{str(self.index)},{str(self.type)},{str(self.capacity)},"

    def asList(self):
        return [self.index, self.type, self.capacity, self.carrierId]
