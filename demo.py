import csv
import random

with open('Periodic Table of Elements.csv', mode='r') as f:
    reader = csv.reader(f)

    elements = []
    for data in reader:
        elements.append([data[0],data[1]])

print(elements.index('Neon'))