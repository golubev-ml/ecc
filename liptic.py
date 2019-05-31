import numpy as np
import matplotlib.pyplot as plt

def mod(t):
    return np.mod(t, 7.0)
def y(x):
    return np.sqrt(np.power(x, 3) + 2 * x + 3)

t = np.arange(-2.0, 7.0, 0.01)

plt.figure(1)
plt.plot(t, y(t), 'b-')
plt.plot(t, -y(t), 'b-')
plt.show()
