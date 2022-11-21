import csv

from entities.carrier import Carrier
from entities.client import Client
from entities.fare import Fare
from entities.item import Item
from entities.ItemTypePerVeichleType import ItemTypePerVeichleType
from entities.TestGenerator import TestGenerator
from entities.veichle import Veichle

generator = TestGenerator()
clients, items = generator.buildClients()
carriers, veichles = generator.buildCarriers()
fares = generator.buildFares()
quadrants = generator.buildQuadrants()

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
    for item in items:
        writer.writerow(item.asList())

with open('out/veichles.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Veichle.header())
    for veichle in veichles:
        writer.writerow(veichle.asList())

with open('out/fares.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Fare.header())
    for fare in fares:
        writer.writerow(fare.asList())

with open('out/quadrants.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(quadrants[0].header())
    for quadrant in quadrants:
        writer.writerow(quadrant.asList())

with open('out/items_per_veichle.csv', 'w', encoding='UTF8') as f:
    itemsPerVeichle = ItemTypePerVeichleType()
    writer = csv.writer(f)
    writer.writerow(itemsPerVeichle.header())
    for item in itemsPerVeichle.asList():
        writer.writerow(item)


# # Plot item positions
# for client in clients:
#     plt.scatter(client.position.x, client.position.y,  s=0.2, c='red')
#
# plt.scatter(50, 50, c='green')
#
# plt.show()
