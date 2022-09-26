from math import floor
from random import randint

from carrier import Carrier
from clusterization import generateUniformClusters
from item import Item

from entities.veichle import Veichle

items = []
veichles = []
carriers = []
NUMBER_OF_CLIENTS = 2000

for currentId, position in enumerate(generateUniformClusters(NUMBER_OF_CLIENTS)):
    items.extend(Item(currentId, position) for _ in range(randint(1, 4)))
    veichles.append(Veichle(currentId))

begin = 0
end = 10

for _ in range(floor(NUMBER_OF_CLIENTS/10)):
    veichlesSubset = veichles[begin:end]
    begin = end
    end += 10
    carriers.append(Carrier(veichlesSubset))


for item in items:
    print(item)

print()

# for carrier in carriers:
#     print(carrier)

# Plot item positions
# for item in items:
#     plt.scatter(item.position.x, item.position.y,  s=0.2, c='red')
#
# plt.scatter(50, 50, c='green')
#
# plt.show()
