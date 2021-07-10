class UF:

    def __init__(self, n):
        self.N = list(range(0, n))
        self.components = [[i] for i in range(n)]

    def union(self, p, q):
        if not self.connected(p, q):
            p_component = self.find(p)
            q_component = self.find(q)
            p_component.extend(q_component)
            self.components.remove(q_component)

    def connected(self, p, q):
        p_component = self.find(p)
        q_component = self.find(q)
        return p_component == q_component

    def find(self, p):
        for component in self.components:
            if p in component:
                return component

    def count(self):
        return len(self.components)


with open('tinyUF.txt') as f:
    N = int(next(f))
    test = UF(N)
    array = []
    for line in f:  # read rest of lines
        if line != '':
            p, q =[int(x) for x in line.split()]
            test.union(p, q)


print(test.components)
