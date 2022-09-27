
from enum import Enum
from math import ceil
from random import uniform

from sklearn.datasets import make_blobs

from client import Position


class GenerationMethod(Enum):
    RANDOM = 0
    UNIFORM = 1
    REAL = 2


class PointsGenerator:
    def __init__(self, amount, method=GenerationMethod.UNIFORM, centers=6):
        self.amount = amount
        self.centers = centers
        self.method = method

    def generate(self):
        if (self.method == GenerationMethod.UNIFORM):
            return self.generate_uniform_clusters()
        elif (self.method == GenerationMethod.RANDOM):
            return self.generate_random_points()
        elif (self.method == GenerationMethod.REAL):
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
            point[0] += uniform(-50, 50)
            point[1] += uniform(-50, 50)
            points.append(point)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def create_cities(self):
        portion = ceil(self.amount / 8)
        points, _, _ = make_blobs(n_samples=[portion*5, portion, portion, portion], centers=[
            (0, 0), (30, 100), (70, 20), (100, 100)],
            cluster_std=20, random_state=0)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def create_uniform_clusters(self):
        portion = ceil(self.amount / 6)
        centers = self.generate_centers()
        print(centers)
        points, _, _ = make_blobs(n_samples=[portion, portion, portion, portion, portion, portion], n_features=2, centers=centers,
                                  cluster_std=10, random_state=0)

        for point in points:
            point[0] = round(point[0], 3)
            point[1] = round(point[1], 3)
            yield point

    def generate_centers(self):
        point = [uniform(0, 100), uniform(0, 100)]
        for _ in range(self.centers):
            point[0] = point[0]+uniform(25, 40)
            point[1] = point[1]+uniform(25, 40)
            yield point
