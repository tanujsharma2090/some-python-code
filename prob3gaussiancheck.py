import matplotlib.pyplot as plt
import random
import math as math

N = int(input("Enter value of N:"))
mean = int(input("Enter value of u:"))
sd = int(input("Enter value of standard deviation:"))
theGaussianList = []
for i in range(0, N+1):
    y = random.randint(0, 100)
    z = ((1 / (math.pow(0.5, math.pi) * sd)) *
         math.exp(-0.5 * (1 / sd) * (y - mean)**2))
    theGaussianList.append(z)

plt.hist(theGaussianList, 100)
plt.show()
