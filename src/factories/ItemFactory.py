from random import choice, randint, uniform
from entities.item import Item


class ItemFactory:
    def __init__(self):
        self.client_id = 0
        self.types = []
        self.min_weight = 0
        self.max_weight = 0

    def generate(self, quantity):
        return [self.buildItem(index) for index in range(quantity)]

    def buildItem(self, index):
        item = Item.empty()
        item.index = index
        item.clientId = self.client_id
        item.type = choice(self.types)
        item.weight = uniform(self.min_weight, self.max_weight)  # type: ignore
        return item

    def set_client_id(self, client_id):
        self.client_id = client_id

    def set_types(self, types):
        self.types = types

    def set_min_weight(self, weight):
        self.min_weight = weight

    def set_max_weight(self, weight):
        self.max_weight = weight
