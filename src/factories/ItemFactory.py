from random import choice, randint, uniform
from entities.item import Item


class ItemFactory:
    def __init__(self):
        self.client_id = 0
        self.types = []
        self.weights = []

    def generate(self, quantity):
        return [self.buildItem() for _ in range(quantity)]

    def buildItem(self):
        item = Item.empty()
        item.clientId = self.client_id
        item.type = choice(self.types)
        item.weight = choice(self.weights)
        return item

    def set_client_id(self, client_id):
        self.client_id = client_id

    def set_types(self, types):
        self.types = types

    def set_weights(self, weights):
        self.weights = weights
