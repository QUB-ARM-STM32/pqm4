import matplotlib.pyplot as plt
import csv
import sys

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

    def ParseFile(self):
        previous = ""
        data = []
        impl = []
        coords = []
        count = 0

        figure, axis = plt.subplots(self.plots)
        with open(self.csvPath, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            plotCount = 0
            for row in csvReader:
                if row[1] != "" and row[0] != "Scheme":
                    if row[0] != previous and previous != "":
                        print(plotCount)
                        axis[plotCount].bar(coords, data, tick_label=impl, width=0.8, color=["red", "blue"])
                        #axis[0, plotCount].xlabel("Implementations")
                        #axis[0, plotCount].ylabel("Cycles")
                        axis[plotCount].set_title(previous)
                        print(plotCount)
                        impl = []
                        data = []
                        coords = []
                        count = 0
                        previous = row[0]
                        impl.append(row[1])
                        data.append(float(row[2]))
                        coords.append(count)
                        count += 1
                        plotCount += 1
                    else:
                        print("Not Plotting")
                        previous = row[0]
                        impl.append(row[1])
                        data.append(float(row[2]))
                        coords.append(count)
                        count += 1
        plt.show()

    def PlotScheme(self, scheme, signature=""):
        impl = []
        coords = []
        keyGenData = []
        encapData = []
        decapData = []
        count = 0

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
                    figure, axis = plt.subplots(3)
                    figure.suptitle(scheme)
                    figure.tight_layout()

                    axis[0].bar(coords, keyGenData, tick_label=impl, width=0.8, color=["green", "blue"])
                    axis[0].set_title("Key Generation")
                    axis[0].set_ylabel("Cycles")

                    axis[1].bar(coords, encapData, tick_label=impl, width=0.8, color=["green", "blue"])
                    if signature == "-s":
                        axis[1].set_title("Sign")
                    else:
                        axis[1].set_title("Encapsulation")
                    axis[1].set_ylabel("Cycles")

                    axis[2].bar(coords, decapData, tick_label=impl, width=0.8, color=["green", "blue"])
                    if signature == "-s":
                        axis[2].set_title("Verify")
                    else:
                        axis[2].set_title("Decapsulation")
                    axis[2].set_ylabel("Cycles")

                    plt.show()
                    return
            print("Cannot find scheme: " + scheme)
                    

chart = BarChart("results.csv")
value = ""
try:
    value = sys.argv[2]
    print(value)
except:
    value = ""
print(value)
chart.PlotScheme(sys.argv[1], value)