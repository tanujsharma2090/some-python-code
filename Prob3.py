import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
x = sp.Poisson.random(lam=1, size=100)
# plt.plot(x,'o')
a = 5.  # shape
n = 1000
s = np.random.power(a, n)
count, bins, ignored = plt.hist(s, bins=30)
x = np.linspace(0, 1, 100)
y = a*x**(a-1.)
normed_y = n*np.diff(bins)[0]*y
plt.title("Poisson distribution")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(x, normed_y)
plt.show()
