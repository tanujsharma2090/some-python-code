import matplotlib.pyplot as plt
import random
import math as math

# choose type of distribution
distribution = input("Enter your distribution P for Poisson , G for Gaussian:")
if distribution.upper() == "P":  # If Poisson Distribution is choosen
    N = int(input("Enter value of N:"))  # No. of trials
    mean = int(input("Enter value of lambda:"))  # mean of the distribution
    thePoissonList = []
    for i in range(0, N+1):  # Till all trials have been done
        # Generate a random number between 0 and 100
        x = random.randint(0, 100)
        # Probability of each random number as per Poisson distribution
        p = ((math.exp(-mean))*(pow(mean, x)))/(math.factorial(x))

        thePoissonList.append(p)  # All probabilities saved in a list

    plt.hist(thePoissonList, 100)  # Plot the histogram
    plt.show()  # Show the histogram

elif distribution.upper() == "G":  # If Gaussian Distribution is choosen
    N = int(input("Enter value of N:"))  # No. of trials
    mean = int(input("Enter value of u:"))  # mean of the distribution
    
    sd = int(input("Enter value of standard deviation:")) # standard deviation of the distribution
    theGaussianList = []
    for i in range(0, N+1):  # Till all trials have been done
        # Generate a random number between 0 and 100
        y = random.randint(0, 100)
        z = ((1 / (math.pow(0.5, math.pi) * sd)) *
             math.exp(-0.5 * (1 / sd) * (y - mean)**2))  # Probability of each random number as per Normal distribution
        theGaussianList.append(z)  # All probabilities saved in a list

    plt.hist(theGaussianList, 100)  # Plot the histogram
    plt.show()  # Show the histogram
else:
    print("Please re run the program and enter either P or G")
