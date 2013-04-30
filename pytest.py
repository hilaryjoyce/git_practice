import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-100,101)
plt.plot(a, a**2)
plt.plot(a, a**3)
plt.plot(a, a**4)
plt.savefig("a_figure.png")