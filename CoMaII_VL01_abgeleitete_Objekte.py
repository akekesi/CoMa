# CoMaII - VL01
# abgeleitete Objekte

class AbstractSet:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items ==[]
    
    def insert(self, item):
        pass
    
    def pop(self):
        pass
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

class Queue(AbstractSet):
    def insert(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop()

class Stack(AbstractSet):
    def insert(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()


def traverse(adj, r, Q):
    """
    r:      Startpunkt
    adj:    Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    Q:      Datenstruktur fuer dyn. Datenmenge, (Objekt)
    """
    R = [r]     # Knotenmenge
    F = []      # Kantenmenge
    Q.insert(r)
    while not Q.isEmpty():
        v = Q.peek()
        i = 0
        while len(adj[v]) > i and adj[v][i] in R:
            i += 1
        if len(adj[v]) > i:
            w = adj[v][i]
            R.append(w)
            Q.insert(w)
            F.append((v, w))
        else:
            Q.pop()
    return (R, F)

if __name__ == "__main__":
    adj = [[1,3],[0,2],[1,3],[0,2]]
    r = 0
    Q_q = Queue()
    Q_s = Stack()
    print(traverse(adj,r,Q_q))
    print(traverse(adj,r,Q_s))