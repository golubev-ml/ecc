import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from itertools import product
import networkx as nx

A = 2
B = 3
O = (0.5, 0.5)
def mod(x):
    return x % 31

def ec(x):
    return mod(x*x*x + A*x + B)

inv_arr = [y for x,y in product(range(31),repeat=2) if mod(x*y)==1]
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

sqare_arr = [mod(x*x) for x in range(31)]

sqrt_arr = [list(index_all(sqare_arr, x)) for x in range(31)]
#print(sqrt_arr)



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

G = nx.MultiDiGraph()
G.add_node('{}'.format(O), pos=O)
for p in product(range(31),repeat=2):
    G.add_node('{}'.format(p), pos=p)

p = (19, 24)
s = p
for p in product(range(31),repeat=2):
    s = p
    for i in range(34):
        x, y = s
        if ec(x) != mod(y*y):
            break
        if s == O:
            break
        print("i:{0}, s:{1}, ec(x):{2}, y*y:{3}, sqrt:{4}".format(i, s, ec(x), mod(y*y), sqrt_arr[ec(x)]))
        s_new = sum(s, p)
        G.add_edges_from([('{}'.format(s), '{}'.format(s_new))])
        s = s_new


plt.figure(figsize=(100,100))
nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=0)
plt.savefig('ecc31.png')
