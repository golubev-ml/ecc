import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 16 * np.sin(t) * np.sin(t) * np.sin(t)

def y(t):
    return 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

t1 = np.arange(0.0, 5.0, 0.01)

plt.figure(1)
plt.plot(x(t1), y(t1), 'bo')

plt.show()
