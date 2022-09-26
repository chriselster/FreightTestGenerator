
from math import ceil
from random import uniform

from sklearn.datasets import make_blobs

from client import Position


def generateRealCityClusters(amount):
    for point in createCities(amount):
        yield Position(point[0], point[1])


def generateUniformClusters(amount):
    for point in createUniformClusters(amount):
        yield Position(point[0], point[1])


def generateRandomPoints(amount):
    for point in createRandomPoints(amount):
        yield Position(point[0], point[1])


def createRandomPoints(amount):
    # random points around 50,50
    points = []
    for _ in range(amount):
        point = [50, 50]
        point[0] += uniform(-50, 50)
        point[1] += uniform(-50, 50)
        points.append(point)

    for point in points:
        point[0] = round(point[0], 3)
        point[1] = round(point[1], 3)
        yield point


def createCities(amount):
    portion = ceil(amount / 8)
    points, _, _ = make_blobs(n_samples=[portion*5, portion, portion, portion], centers=[
        (0, 0), (30, 100), (70, 20), (100, 100)],
        cluster_std=20, random_state=0)

    for point in points:
        point[0] = round(point[0], 3)
        point[1] = round(point[1], 3)
        yield point


def createUniformClusters(amount):
    portion = ceil(amount / 6)
    centers = generateCenters(6)
    print(centers)
    points, _, _ = make_blobs(n_samples=[portion, portion, portion, portion, portion, portion], n_features=2, centers=centers,
                              cluster_std=10, random_state=0)

    for point in points:
        point[0] = round(point[0], 3)
        point[1] = round(point[1], 3)
        yield point


def generateCenters(amount):
    return [(10, 10), (10, 90), (90, 10), (90, 90), (50, 50), (70, 30)]
