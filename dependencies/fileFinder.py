import glob
import os
def findFile(file):
    directory = glob.glob(r"C:\\**\\*")
    for items in directory:
        if file in items:
            print(items)
            with open(items, "r")as file:
                contents = file.read()
            return contents
if __name__ == "__main__":
    findFile("stare.mp4")