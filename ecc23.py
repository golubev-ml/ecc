import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from itertools import product
import networkx as nx
from random import randint

## Y^2 = X^3 + 10x + 13 mod N=23
A = 10
B = 13
O = (22, 11.5)
N = 23
def mod(x):
    return x % N

def ec(x):
    return mod(x*x*x + A*x + B)

inv_arr = [y for x,y in product(range(N),repeat=2) if mod(x*y)==1]
def inv(k):
    return inv_arr[int(mod(k) - 1)]

def index_all(list_, value):
    start = 0
    while True:
        try:
            start = list_.index(value, start)
            yield start
            start += 1
        except ValueError:
            break

sqare_arr = [mod(x*x) for x in range(N)]

sqrt_arr = [list(index_all(sqare_arr, x)) for x in range(N)]

# • If P1 != P2 and x1 = x2, then P1 + P2 = O.
# • If P1 = P2 and y1 = 0, then P1 + P2 = 2P1 = O.
# • If P1 != P2 (and x1 != x2), let λ = y2 − y1 / x2 − x1 and ν = y1x2 − y2x1 / x2 − x1
# • If P1 = P2 (and y1 != 0), let λ = (3x^2 + A) / 2y and ν = −x^3 + Ax + 2B / 2y
# Then P1 + P2 = (λ^2 − x1 − x2 , −λ^3 + λ(x1 + x2) − ν)

def sum(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    λ = 0
    ν = 0
    if p1 == O:
        return p2
    if p2 == O:
        return p1
    if p1 != p2 and x1 == x2:
        return O
    if p1 == p2 and y1 == 0:
        return O
    if p1 != p2 and x1 != x2:
        λ = (y2 - y1) * inv(x2 - x1)
        ν = (y1 * x2 - y2 * x1) * inv(x2 - x1)
    if p1 == p2 and y1 != 0:
        λ = (3 * x1 * x1 + A) * inv(2 * y1)
        ν = (-x1 * x1 * x1 + A * x1 + 2*B) * inv(2*y1)
    return (int(mod(λ * λ - x1 - x2)) , int(mod(-λ * λ * λ + λ * (x1 + x2) - ν)))

ecc_points =[O]
for p in product(range(N),repeat=2):
    x, y = p
    if ec(x) != mod(y*y):
        continue
    ecc_points.append(p)

low_half_ecc_points = [p for p in ecc_points if p[1] < N / 2]
color_posibilities = ['g', 'b', 'r' , 'm', 'c']

G = nx.MultiDiGraph()
# first add some vertices
G.add_node('{}'.format(O), pos=O)
for p in ecc_points:
    G.add_node('{}'.format(p), pos=p)

# then add edges with different colors
colors = []
for p in low_half_ecc_points:
    s = p
    x, y = s
    if ec(x) != mod(y*y):
        continue
    color = color_posibilities[randint(0,4)]
    for i in range(len(ecc_points)):
        x, y = s
        if ec(x) != mod(y*y):
            break
        if s == O:
            break
        #print("i:{0}, s:{1}, ec(x):{2}, y*y:{3}, sqrt:{4}".format(i, s, ec(x), mod(y*y), sqrt_arr[ec(x)]))
        s_new = sum(s, p)
        G.add_edges_from([('{}'.format(s), '{}'.format(s_new))])
        colors.append(color)
        s = s_new

plt.figure(figsize=(50,50))
nx.draw(G,
        nx.get_node_attributes(G, 'pos'),
        with_labels=True, node_size=500,
        arrowsize=50,
        arrowstyle='-|>',
        edge_color = colors,
        width=4)
plt.savefig('ecc23.png')
