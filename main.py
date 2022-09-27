from math import floor
from random import randint

from entities.carrier import Carrier
from entities.client import Client
from entities.clusterization import PointsGenerator
from entities.item import ItemFactory
from entities.veichle import VeichleFactory

clients = []
veichles = []
carriers = []
NUMBER_OF_CLIENTS = 2000

pointsGenerator = PointsGenerator(NUMBER_OF_CLIENTS)
itemFactory = ItemFactory()
veichleFactory = VeichleFactory()

for index, point in enumerate(pointsGenerator.generate()):
    items = []
    items.extend(itemFactory.create() for _ in range(randint(1, 4)))
    clients.extend(Client(index, point, items))
    veichles.append(veichleFactory.create())

begin = 0
end = 10

for _ in range(floor(NUMBER_OF_CLIENTS/10)):
    veichlesSubset = veichles[begin:end]
    begin = end
    end += 10
    carriers.append(Carrier(veichlesSubset))


for client in clients:
    print(client)

print()

for carrier in carriers:
    print(carrier)

# Plot item positions
# for item in items:
#     plt.scatter(item.position.x, item.position.y,  s=0.2, c='red')
#
# plt.scatter(50, 50, c='green')
#
# plt.show()
