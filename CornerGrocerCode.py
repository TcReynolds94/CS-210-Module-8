# Choyce Reynolds
# 10/19/2025

# I wanted Python to hadnle all of the logic for this program. It pulls the information from the input file, C++ calls the information based on user input, and the Python writes the output file

import sys

class ItemFrequency:
    def __init__(self):
        self.frequency = {}  
        with open("InputFile.txt", "r") as file:
            items = file.read().splitlines()
        for item in items:
            if item in self.frequency:
                self.frequency[item] += 1
            else:
                self.frequency[item] = 1

    # Shows all itmes and counts their quantities
    def CountAllItems(self):
        for item, count in self.frequency.items():
            print(f"{item}: {count}")

    # Shows one item and counts its quantity
    def CountOneItem(self, ItemName):
        count = self.frequency.get(ItemName, 0)
        print(f"{ItemName}: {count}")

     # Puts items and their quantities into a data file
    def WriteFrequencyFile(self, OutputFile = "frequency.dat"):
        with open("frequency.dat", "w") as out:
            for item, count in self.frequency.items():
                out.write(f"{item} {count}\n")


    # Shows a histogram of items and their quantities    
    def ShowHistogram(self):
        self.WriteFrequencyFile()
        with open("frequency.dat", "r") as file:
            for line in file:
                item, count = line.strip().split()
                print(f"{item:15} {'*' * int(count)}")

# Handles the arguments that are called in the cpp file
if __name__ == "__main__":
    FrequencyMap = ItemFrequency()

    if len(sys.argv) < 2:
        print("Usage: python CornerGrocerCode.py [all|one <item>|histogram]")
    elif sys.argv[1] == "all":
        FrequencyMap.CountAllItems()
    elif sys.argv[1] == "one" and len(sys.argv) == 3:
        FrequencyMap.CountOneItem(sys.argv[2])
    elif sys.argv[1] == "histogram":
        FrequencyMap.ShowHistogram() 