import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def mod(t):
    #return t
    return np.mod(t, 7.0)

def y(x):
    return np.sqrt(np.power(x, 3) + 2 * x + 3)

# • If P1 != P2 and x1 = x2, then P1 + P2 = O.
# • If P1 = P2 and y1 = 0, then P1 + P2 = 2P1 = O.
# • If P1 != P2 (and x1 != x2), let λ = y2 − y1 / x2 − x1 and ν = y1x2 − y2x1 / x2 − x1
# • If P1 = P2 (and y1 != 0), let λ = (3x^2 + A) / 2y and ν = −x^3 + Ax + 2B / 2y
# Then P1 + P2 = (λ^2 − x1 − x2 , −λ^3 + λ(x1 + x2) − ν)
def inv(k):
    arr = [0, 1, 4, 5, 2, 3, 1]
    return arr[int(mod(k))]

def sum(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    λ = 0
    ν = 0
    A = 2
    B = 3
    if p1 != p2 and x1 == x2:
        return (0.5, 0.5)
    if p1 == p2 and y1 == 0:
        return (0.5, 0.5)
    if p1 != p2 and x1 != x2:
        λ = (y2 - y1) * inv(x2 - x1)
        ν = (y1 * x2 - y2 * x1) * inv(x2 - x1)
    if p1 == p2 and y1 != 0:
        λ = (3 * x1 * x1 + A) * inv(2 * y1)
        ν = (-x1 * x1 * x1 + A * x1 + 2*B) * inv(2*y1)
    return (int(mod(λ * λ - x1 - x2)) , int(mod(-λ * λ * λ + λ * (x1 + x2) - ν)))
p = (2, 1)
s = p
for i in range(8):
    print(s)
    s = sum(s, p)

plt.figure(1)
t_minus = np.arange(-1.0, 0.0, 0.01)
plt.plot(mod(t_minus), mod(y(t_minus)), 'b-')
plt.plot(mod(t_minus), mod(-y(t_minus)), 'r-')

for i in range(0,1):
    t_plus = np.arange(0.0 + i * 7.0, 7.0 + i * 7.0, 0.01)
    plt.plot(mod(t_plus), mod(y(t_plus)), 'y-')
    plt.plot(mod(t_plus), mod(-y(t_plus)), 'c-')

plt.plot([2, 2, 3, 3, 6], [1, 6, 1, 6, 0], 'go', linewidth=5)
plt.grid(color='r', linestyle='-', linewidth=1, alpha=0.5)

# plt.show()
plt.savefig('myfig.png')


