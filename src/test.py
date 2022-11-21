from unittest import TestCase

from entities.fare import Fare
from entities.ParamReader import ParamReader


class TestItem(TestCase):
    def testFareCreation(self):
        fare = Fare(1, 2)
        assert fare.asList() == [1, 2]

    def testParamReading(self):
        result = ParamReader.getTokens("test: 1,2,3,4")
        assert result == [1, 2, 3, 4]

    def testGetTokensWithLists(self):
        result = ParamReader.getTokens("test: [1/2/3/4], [5/6/7/8]")
        assert result == [[1, 2, 3, 4], [5, 6, 7, 8]]

    def testReadLines(self):
        lines = ["test: 1,2,3,4", "test: [5/6/7/8]"]
        reader = ParamReader(lines)
        result = reader.next()
        assert result == [1, 2, 3, 4]
        result = reader.next()
        assert result == [[5, 6, 7, 8]]
