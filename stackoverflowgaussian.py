import sys
import random
from math import sqrt, pi
import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, var):
    k1 = np.power(x, 2)
    k2 = -k1/(2*var)
    return (1./(sqrt(2. * pi * var))) * np.exp(k2)


#--------*---------*---------*---------*---------*---------*---------*---------#
while 1:  # M A I N L I N E                             #
    #--------*---------*---------*---------*---------*---------*---------*---------#
    #                                  # probability density function
    #                                  #   for discrete normal RV
    pdf_DGV = []
    pdf_DGW = []
    var = 10
    tot = 50
#                                  # create 'rough' gaussian
    for i in range(-var - 1, var + 2):
        if i == -var - 1:
            r_pdf = + gaussian(i, 9) + gaussian(i - 1, 9) + gaussian(i - 2, 9)
        elif i == var + 1:
            r_pdf = + gaussian(i, 9) + gaussian(i + 1, 9) + gaussian(i + 2, 9)
        else:
            r_pdf = gaussian(i, 9)
        tot = tot + r_pdf
        pdf_DGV.append(i)
        pdf_DGW.append(r_pdf)
        print(i, r_pdf)
#                                  # amusing how close tot is to 1!
    print('\nRough total = ', tot)
#                                  # no need to normalize with Python 3.6,
#                                  #   but can't help ourselves
    for i in range(0, len(pdf_DGW)):
        pdf_DGW[i] = pdf_DGW[i]/tot
#                                  # print out pdf weights
#                                  #   for out discrte gaussian
    print('\npdf:\n')
    print(pdf_DGW)

#                                  # plot random variable action
    rv_samples = random.choices(pdf_DGV, pdf_DGW, k=20000)
    plt.hist(rv_samples, bins=100)
    plt.show()
    sys.exit()
