import matplotlib.pyplot as plt
import numpy as np
mu = int(input("Enter value of mu:"))
sigma = int(input("Enter value of sigma:"))
N = int(input("Enter value of N:"))
a = np.random.normal(mu, sigma, N)
print(a)
# plt.hist(a, 100)
# plt.show()


# Draw samples from the distribution:

# import matplotlib.pyplot as plt
# mu, sigma = 0, 0.1  # mean and standard deviation
# s = np.random.normal(mu, sigma, 1000)

# # Verify the mean and the variance:

# abs(mu - np.mean(s)) < 0.01
# # True

# abs(sigma - np.std(s, ddof=1)) < 0.01
# # True

# # Display the histogram of the samples, along with
# # the probability density function:

# count, bins, ignored = plt.hist(s, 30)
# print(bins)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#          np.exp(- (bins - mu)**2 / (2 * sigma**2)),
#          linewidth=2, color='r')
# plt.show()
