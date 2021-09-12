##
##
import numpy as np
import matplotlib.pyplot as plt
from random import random

randomNumbers = []
indices = []
dataMean = []
print(randomNumbers)

for index in range(1000):
    randomNumbers.append(random() * 50 * random() ** 2)
    indices.append(index)

print(randomNumbers)
print("mean: ", np.mean(randomNumbers))  # arithmatic mean
ourMean = np.mean(randomNumbers)

for index in range(1000):
    dataMean.append(np.mean(randomNumbers))

plt.scatter(indices, randomNumbers)
plt.plot(indices, dataMean, "r")
plt.show()