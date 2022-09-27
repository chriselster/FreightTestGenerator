from unittest import TestCase

from clusterization import PointsGenerator


class TestItem(TestCase):
    def test_generate_centers(self):
        result = PointsGenerator.generate_centers(4)
        self.assertEqual(len(result), 4)
