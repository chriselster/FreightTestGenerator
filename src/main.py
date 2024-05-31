import csv
import matplotlib.pyplot as plt
import os
from entities.clusterization import ClusterType

from entities.CSVGenerator import CSVGenerator
from entities.ItemTypePerVehicleType import ItemTypePerVehicleType
from entities.TestGenerator import TestGenerator

outDir = "instances/200-items/"

for index in range(1, 6):
    for clusterType in ClusterType.__members__.values():
        directory = outDir + clusterType.name + "/" + str(index)
        generator = TestGenerator()
        itemsPerVehicle = ItemTypePerVehicleType()
        items, numberOfClients = generator.buildItems()
        clients = generator.buildClients(numberOfClients, clusterType)
        generator.setItemDestinations(items, clients)
        carriers = generator.buildCarriers()
        quadrants = generator.buildQuadrants()
        for carrier in carriers:
            carrier.generateClientList(clients)
        vehicles = generator.buildVehicles(
            carriers, items, clients, itemsPerVehicle.allowedItems
        )

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + "/clients.csv", "w", encoding="UTF8", newline="") as f:
            f.write(CSVGenerator().generate(clients))

        with open(directory + "/items.csv", "w", encoding="UTF8", newline="") as f:
            itemCsvData = [item.toCSVData() for item in items]
            f.write(CSVGenerator().generate(itemCsvData))

        with open(directory + "/vehicles.csv", "w", encoding="UTF8", newline="") as f:
            vehicleCsvData = [vehicle.toCSVData() for vehicle in vehicles]
            f.write(CSVGenerator().generate(vehicleCsvData))

        with open(
            directory + "/items_per_vehicle.csv", "w", encoding="UTF8", newline=""
        ) as f:
            writer = csv.writer(f)
            writer.writerow(itemsPerVehicle.header())
            for item in itemsPerVehicle.asList():
                writer.writerow(item)

        with open(
            directory + "/clients_per_carrier.csv", "w", encoding="UTF8", newline=""
        ) as f:
            writer = csv.writer(f)
            writer.writerow(["carrier_id", "client_id"])
            for carrier in carriers:
                for client in carrier.clients:
                    writer.writerow([carrier.index, client.index])

        #print(len(clients))
        #for client in clients:
        #    plt.scatter(client.x, client.y, s=0.5, c="red")
        #plt.scatter(0, 0, c="green")
        #plt.show()
