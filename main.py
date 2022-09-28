from math import floor
from random import randint, seed

from matplotlib import pyplot as plt

from entities.carrier import Carrier
from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.item import ItemFactory
from entities.veichle import VeichleFactory

clients = []
veichles = []
carriers = []

with open('in/cluster_params.txt', 'r') as f:
    lines = f.readlines()
    seed(int(lines[0].split(":")[1].strip()))

pointsGenerator = PointsGenerator()
itemFactory = ItemFactory()
veichleFactory = VeichleFactory()

for index, point in enumerate(pointsGenerator.generate()):
    items = []
    items.extend(itemFactory.create() for _ in range(randint(1, 4)))
    clients.append(Client(index, point, items))
    veichles.append(veichleFactory.create())

begin = 0
end = 10

for _ in range(floor(len(veichles)/10)):
    veichlesSubset = veichles[begin:end]
    begin = end
    end += 10
    carriers.append(Carrier(veichlesSubset))


with open('out/clients.txt', 'w') as f:
    for client in clients:
        print(client, file=f)

print()

with open('out/carriers.txt', 'w') as f:
    for carrier in carriers:
        print(carrier, file=f)

# Plot item positions
for client in clients:
    plt.scatter(client.position.x, client.position.y,  s=0.2, c='red')

plt.scatter(50, 50, c='green')

plt.show()
