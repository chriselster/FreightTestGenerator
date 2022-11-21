from unittest import TestCase

from entities.fare import Fare


class TestItem(TestCase):
    def fareCreation(self):
        fare = Fare(1, 2)
        assert fare.asList() == [1, 2]
