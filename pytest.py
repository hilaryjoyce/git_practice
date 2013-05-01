'''I just edited this on fancy.

Let's add another thing!'''
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-100,101)
plt.plot(a, a**2)
plt.plot(a, a**3)
plt.plot(a, a**4)
plt.savefig("a_figure.png")

c = a + 1/a**2 + 0.5/a**3