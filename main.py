import csv
from random import randint, seed

from entities.carrier import Carrier, CarrierFactory
from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.item import Item, ItemFactory
from entities.quadrants import Quadrants
from entities.veichle import Veichle, VeichleFactory

clients = []
carriers = []

with open('in/cluster_params.txt', 'r') as f:
    lines = f.readlines()
    seed(int(lines[0].split(":")[1].strip()))

pointsGenerator = PointsGenerator()
itemFactory = ItemFactory()
veichleFactory = VeichleFactory()
carrierFactory = CarrierFactory()
allItems = []
allVeichles = []
fares = set()
quadrants = []

for index, point in enumerate(pointsGenerator.generate()):
    items = []
    items.extend(itemFactory.create(index) for _ in range(randint(1, 5)))
    allItems.extend(items)
    clients.append(Client(index, point, items))

for i in range(5):
    quadrants.append(Quadrants(i+1))

for index in range(5):
    veichles = []
    veichles.extend(veichleFactory.create(index) for _ in range(10))
    allVeichles.extend(veichles)
    carriers.append(carrierFactory.generate(veichles))
    fares.add(carriers[-1].baseFarePerType)

faresList = list(fares)
# replace fares with index
for carrier in carriers:
    carrier.baseFarePerType = faresList.index(carrier.baseFarePerType)

with open('out/clients.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Client.header())
    for client in clients:
        writer.writerow(client.asList())

with open('out/carriers.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Carrier.header())
    for carrier in carriers:
        writer.writerow(carrier.asList())

with open('out/items.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Item.header())
    for item in allItems:
        writer.writerow(item.asList())

with open('out/veichles.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Veichle.header())
    for veichle in allVeichles:
        writer.writerow(veichle.asList())

with open('out/fares.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(faresList[0].header())
    for fare in fares:
        writer.writerow(fare.asList())

with open('out/quadrants.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(quadrants[0].header())
    for quadrant in quadrants:
        writer.writerow(quadrant.asList())


# # Plot item positions
# for client in clients:
#     plt.scatter(client.position.x, client.position.y,  s=0.2, c='red')
#
# plt.scatter(50, 50, c='green')
#
# plt.show()
