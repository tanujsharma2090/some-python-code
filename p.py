# import numpy as np
# import matplotlib.pyplot as plt
# np.random.poisson(4)
import matplotlib.pyplot as plt
import random
import seaborn as sns
from scipy.stats import poisson

data_poisson = poisson.rvs(mu=3, size=10000)
ax = sns.displot(data_poisson,
                 kde=False,
                 color='green')
ax.set(xlabel='Poisson', ylabel='Frequency')
plt.show()
