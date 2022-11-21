
from copy import copy
from enum import Enum
from math import ceil
from random import uniform

from sklearn.datasets import make_blobs

from entities.client import Position


class GenerationMethod(Enum):
    RANDOM = 0
    UNIFORM = 1
    REAL = 2


class PointsGenerator:
    def __init__(self):
        self.read_params()

    def generate(self):
        if (self.method == GenerationMethod.UNIFORM):
            return self.generate_uniform_clusters()
        if (self.method == GenerationMethod.RANDOM):
            return self.generate_random_points()
        if (self.method == GenerationMethod.REAL):
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

    def create_random_points(self):
        # random points around 50,50
        points = []
        for _ in range(self.amount):
            point = [50, 50]
            point[0] += uniform(-50, 50)    # type: ignore
            point[1] += uniform(-50, 50)    # type: ignore
            points.append(point)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def create_cities(self):
        portion = ceil(self.amount / self.centers*2)
        points, _ = make_blobs(n_samples=[portion*(self.centers+1)] + [portion for _ in range(self.centers-1)], centers=self.generate_centers(),  # type: ignore
                               cluster_std=self.cluster_std, random_state=self.seed)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def create_uniform_clusters(self):
        portion = ceil(self.amount / self.centers)
        centers = self.generate_centers()
        print(centers)
        points, _ = make_blobs(n_samples=[portion for _ in range(self.centers)], n_features=2, centers=centers,  # type: ignore
                               cluster_std=self.cluster_std, random_state=self.seed)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def generate_centers(self):
        centers = []
        point = [uniform(0, 100), uniform(0, 100)]
        for _ in range(self.centers):
            point[0] = (point[0]+uniform(70, 90)) % 100
            point[1] = (point[1]+uniform(70, 90)) % 100
            centers.append(copy(point))
        return centers

    def read_params(self):
        with open('in/cluster_params.txt', 'r') as f:
            lines = f.readlines()
            self.seed = int(self.parse_value(lines[0]))
            self.amount = int(self.parse_value(lines[1]))
            self.centers = int(self.parse_value(lines[2]))
            self.method = GenerationMethod(int(self.parse_value(lines[3])))
            self.cluster_std = float(self.parse_value(lines[4]))

    def parse_value(self, line):
        return line.split(":")[1].strip()
