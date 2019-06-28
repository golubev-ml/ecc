
print("hw")

class ECDH_Domain:
    p = 23
    a = 10
    b = 13
    G = (0, 6)
    n = 30
    h = 1
    def __init__(self, p, a, b, G, n, h):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
