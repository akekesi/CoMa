# CoMaII - VL01
# Stack fuer Tiefensuche
# Stack - LIFO Last-In First-Out

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

def dfs(adj, r):
    """
    Es wurde nur bis auf Teilbereiche untersucht.
    Tiefensuche mit Stack
    Args:
        r:   Startpunkt
        adj: Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    Returns:
        R: Knotenmenge von Tiefensuche
        F: Kantenmenge von Tiefensuche
    """
    R = [r]     # Knotenmenge
    F = []      # Kantenmenge
    Q = Stack() # dyn. Menge
    Q.push(r)
    while not Q.isEmpty():
        v = Q.peek()
        i = 0
        while len(adj[v]) > i and adj[v][i] in R:   # van hova tovabb es ez a celpont a mar megjart pontok kozott van? Igen --> i+1 
            i += 1
        if len(adj[v]) > i:                         # ha meg van pont ami meg nem lett megjarva
            w = adj[v][i]
            R.append(w)
            Q.push(w)
            F.append((v, w))
        else:                                       # ha minden pont meg lett mar jarva, akkor kivesszuk a Q-bol
            Q.pop()
    return (R, F)

if __name__ == "__main__":
    adj = [[1,3],[0,2],[1,3],[0,2]]
    r = 0
    print(dfs(adj,r))