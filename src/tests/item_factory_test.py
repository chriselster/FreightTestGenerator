from unittest import TestCase

from entities.item import Item
from factories.ItemFactory import ItemFactory


class ItemFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(ItemFactoryTest, self).__init__(*args, **kwargs)
        self.factory = ItemFactory()

    def setUp(self) -> None:
        self.factory = ItemFactory()
        self.factory.set_client_id(1)
        self.factory.set_types([1, 2, 3])
        return super().setUp()

    def test_generate(self):
        items = self.factory.generate(2)
        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], Item)
        self.assertEqual(items[0].index, 0)
        self.assertEqual(items[1].index, 1)

    def test_set_client_id(self):
        self.factory.set_client_id(1)
        item = self.factory.generate(1)[0]
        self.assertEqual(item.clientId, 1)

    def test_set_type(self):
        self.factory.set_types([1, 2, 3])
        item = self.factory.generate(1)[0]
        self.assertIn(item.type, [1, 2, 3])

    def test_set_weight_range(self):
        self.factory.set_min_weight(1)
        self.factory.set_max_weight(25)
        item = self.factory.generate(1)[0]
        self.assertGreaterEqual(item.weight, 1)
        self.assertLessEqual(item.weight, 25)
