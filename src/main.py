import csv
import matplotlib.pyplot as plt

from entities.CSVGenerator import CSVGenerator
from entities.ItemTypePerVehicleType import ItemTypePerVehicleType
from entities.TestGenerator import TestGenerator

generator = TestGenerator()
clients = generator.buildClients()
items = generator.buildItems(clients)
carriers = generator.buildCarriers()
vehicles = generator.buildVehicles(carriers)
quadrants = generator.buildQuadrants()

for carrier in carriers:
    carrier.generateClientList(clients)

with open('out/clients.csv', 'w', encoding='UTF8', newline='') as f:
    f.write(CSVGenerator().generate(clients))

with open('out/items.csv', 'w', encoding='UTF8', newline='') as f:
    f.write(CSVGenerator().generate(items))

with open('out/vehicles.csv', 'w', encoding='UTF8', newline='') as f:
    f.write(CSVGenerator().generate(vehicles))

with open('out/items_per_vehicle.csv', 'w', encoding='UTF8', newline='') as f:
    itemsPerVehicle = ItemTypePerVehicleType()
    writer = csv.writer(f)
    writer.writerow(itemsPerVehicle.header())
    for item in itemsPerVehicle.asList():
        writer.writerow(item)

with open('out/clients_per_carrier.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['carrier_id', 'client_id'])
    for carrier in carriers:
        for client in carrier.clients:
            writer.writerow([carrier.id, client.index])

# # Plot item positions
for client in clients:
    plt.scatter(client.position.x, client.position.y,  s=0.2, c='red')

plt.scatter(50, 50, c='green')

plt.show()
