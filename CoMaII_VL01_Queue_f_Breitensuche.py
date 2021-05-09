# CoMaII - VL01
# Queue fuer Breitensuche
# Stack - FIFO First-In First-Out

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items ==[]
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

def bfs(adj, r):
    """
    Breitensuche mit Queue
    r:      Startpunkt
    adj:    Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    """
    R = [r]     # Knotenmenge
    F = []      # Kantenmenge
    Q = Queue() # dyn. Menge
    Q.enqueue(r)
    while not Q.isEmpty():
        v = Q.peek()
        i = 0
        while len(adj[v]) > i and adj[v][i] in R:
            i += 1
        if len(adj[v]) > i:
            w = adj[v][i]
            R.append(w)
            Q.enqueue(w)
            F.append((v, w))
        else:
            Q.dequeue()
    return (R, F)

if __name__ == "__main__":
    adj = [[1,3],[0,2],[1,3],[0,2]]
    r = 0
    print(bfs(adj,r))