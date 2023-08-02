#!/usr/bin/python3

import matplotlib.pyplot as plt
import csv
import sys
import os
import shutil

class BarChart():
    def __init__(self, csvPath):
        self.csvPath = csvPath
        self.schemeNames = []
        self.keyGen = []
        self.plots = 0

        with open(self.csvPath, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            lineCount = 0
            for row in csvReader:
                if row[1] != "":
                    self.plots += 1

            print(self.plots)

    def Plot(self, title, coords, data1, data2, data3, tick_labels, kem):
        figure, axis = plt.subplots(3)
        figure.suptitle(title)
        figure.tight_layout()

        axis[0].bar(coords, data1, tick_label=tick_labels, width=0.8, color=["green", "blue"])
        axis[0].set_title("Key Generation")
        axis[0].set_ylabel("Cycles")

        axis[1].bar(coords, data2, tick_label=tick_labels, width=0.8, color=["green", "blue"])
        if not kem:
            axis[1].set_title("Sign")
        else:
            axis[1].set_title("Encapsulation")
        axis[1].set_ylabel("Cycles")


        axis[2].bar(coords, data3, tick_label=tick_labels, width=0.8, color=["green", "blue"])
        if not kem:
            axis[2].set_title("Verify")
        else:
            axis[2].set_title("Decapsulation")
        axis[2].set_ylabel("Cycles")

    def ParseFile(self):
        previous = ""
        keyGenData = []
        encapData = []
        decapData = []
        impl = []
        coords = []
        count = 0
        kem = True

        if os.path.exists("./plots"):
            shutil.rmtree("./plots")
        os.mkdir("./plots")

        with open(self.csvPath, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            plotCount = 0
            for row in csvReader:
                if row[0] == "Memory Evaluation":
                    self.Plot(previous, coords, keyGenData, encapData, decapData, impl, kem)
                    plt.savefig("./plots/" + previous + ".png")
                    return
                if row[1] != "" and row[0] != "Scheme":
                    if row[0] != previous and previous != "":
                        self.Plot(previous, coords, keyGenData, encapData, decapData, impl, kem)

                        plt.savefig("./plots/" + previous + ".png")
                        keyGenData = []
                        encapData = []
                        decapData = []
                        coords = []
                        impl = []
                        count = 0
                    previous = row[0]
                    impl.append(row[1])
                    keyGenData.append(float(row[2]))
                    encapData.append(float(row[5]))
                    decapData.append(float(row[8]))
                    coords.append(count)
                    count += 1
                elif row[0] == "Signature Schemes":
                    kem = False
                

    def PlotScheme(self, scheme, signature=""):
        impl = []
        coords = []
        keyGenData = []
        encapData = []
        decapData = []
        count = 0
        kem = True

        if signature == "-s":
            kem = False

        with open(self.csvPath, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:
                if row[0].split(" ")[0] == scheme:
                    impl.append(row[1])
                    coords.append(count)
                    keyGenData.append(float(row[2]))
                    encapData.append(float(row[5]))
                    decapData.append(float(row[8]))
                    count += 1
                if row[0].split(" ")[0] != scheme and len(keyGenData) > 0:
                    # plot the graph
                    self.Plot(scheme, coords, keyGenData, encapData, decapData, impl, kem)
                    plt.show()
                    return
            print("Cannot find scheme: " + scheme)
                    

chart = BarChart("results.csv")

arg1 = ""
arg2 = ""
try:
    arg1 = sys.argv[1]
except:
    arg1 = "kyber512"

try:
    arg2 = sys.argv[2]
except:
    arg2 = ""

if arg1 == "save":
    chart.ParseFile()
else:
    chart.PlotScheme(arg1, arg2)