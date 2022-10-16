class Carrier:
    def __init__(self,  veichles, baseFarePerType, quadrants, minimumCapacity, costPerAdditionalCustomer, allowedItemTypes, maxDistanceBetweenCustomers):
        self.veichles = veichles
        # Cost per weight per km for each veichle type
        self.baseFarePerType = baseFarePerType
        self.quadrants = quadrants
        # Percentage of the veichle capacity that must be filled
        self.minimumCapacity = minimumCapacity
        # Base value +- 10%
        self.costPerAdditionalCustomer = costPerAdditionalCustomer
        # 5% / 2,5%
        self.maxDistanceBetweenCustomers = maxDistanceBetweenCustomers

    def __str__(self):
        return ''.join(f"{str(veichle)}\n" for veichle in self.veichles) + "\n"
