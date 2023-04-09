import matplotlib.pyplot as plt
import csv

from entities.carrier import Carrier
from entities.client import Client
from entities.fare import Fare
from entities.item import Item
from entities.ItemTypePerVehicleType import ItemTypePerVehicleType
from entities.TestGenerator import TestGenerator
from entities.vehicle import Vehicle

generator = TestGenerator()
clients, items = generator.buildClients()
carriers, vehicles = generator.buildCarriers()
for carrier in carriers:
    carrier.generateClientList(clients)
fares = generator.buildFares(len(carriers))
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

with open('out/vehicles.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Vehicle.header())
    for vehicle in vehicles:
        writer.writerow(vehicle.asList())

with open('out/fares.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Fare.header())
    for fare in fares:
        writer.writerow(fare.asList())

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
