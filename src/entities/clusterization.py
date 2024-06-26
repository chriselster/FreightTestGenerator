from copy import copy
from enum import Enum
from math import ceil
from random import uniform, randint

from sklearn.datasets import make_blobs

from entities.client import Position


class ClusterType(Enum):
    RANDOM = 0
    UNIFORM = 1
    REAL = 2


class PointsGenerator:
    def __init__(self):
        self.read_params()

    def generate(self, amount, clusterType: ClusterType):
        self.amount = amount

        if clusterType == ClusterType.UNIFORM:
            return self.generate_uniform_clusters()
        if clusterType == ClusterType.RANDOM:
            return self.generate_random_points()
        if clusterType == ClusterType.REAL:
            return self.generate_real_cities()

    def generate_real_cities(self):
        for point in self.create_cities():
            yield Position(point[0], point[1])

    def generate_uniform_clusters(self):
        for point in self.create_uniform_clusters():
            yield Position(point[0], point[1])

    def generate_random_points(self):
        for point in self.create_random_points():
            yield Position(point[0], point[1])

    def normalize(self, points):
        min_x = min(points, key=lambda x: x[0])[0]
        max_x = max(points, key=lambda x: x[0])[0]
        min_y = min(points, key=lambda x: x[1])[1]
        max_y = max(points, key=lambda x: x[1])[1]
        return [
            [
                (point[0] - min_x) / (max_x - min_x) * 100,
                (point[1] - min_y) / (max_y - min_y) * 100,
            ]
            for point in points
        ]

    def create_random_points(self):
        points = []
        for _ in range(self.amount):
            point = [50, 50]
            point[0] += uniform(-50, 50)
            point[1] += uniform(-50, 50)
            points.append(point)

        for point in self.normalize(points):
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def create_cities(self):
        points, _ = make_blobs( #olhar aqui
            n_samples=self.generate_city_sizes(),
            centers=self.generate_centers(),  # type: ignore
            cluster_std=self.cluster_std,
        )

        for point in self.normalize(points):
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def generate_city_sizes(self):
        self.centers = min(self.centers, self.amount)
        result = []
        max_size = self.amount
        for index in range(self.centers - 1):
            quantity = randint(1, max_size - (self.centers - (index + 1)))
            max_size -= quantity
            result.append(quantity)
        result.append(max_size)
        return result

    def create_uniform_clusters(self):
        points, _ = make_blobs(
            n_samples=self.generate_uniform_center_sizes(),
            n_features=2,
            centers=self.generate_centers(),
            cluster_std=self.cluster_std,
        )

        for point in self.normalize(points):
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def generate_uniform_center_sizes(self):
        size = self.amount // self.centers
        result = [size] * self.centers
        result[-1] += self.amount - (size * self.centers)
        return result

    def generate_centers(self):
        centers = []
        for _ in range(self.centers):
            point = [uniform(0, 100), uniform(0, 100)]
            centers.append(copy(point))
        return centers

    def read_params(self):
        with open("in/cluster_params.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # self.seed = int(self.parse_value(lines[0]))
            self.amount = int(self.parse_value(lines[1]))
            self.centers = int(self.parse_value(lines[2]))
            self.method = ClusterType(int(self.parse_value(lines[3])))
            self.cluster_std = float(self.parse_value(lines[4]))

    def parse_value(self, line):
        return line.split(":")[1].strip()
