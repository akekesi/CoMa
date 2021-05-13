# CoMaII - PA_03 - Topologische Sortierung
# Attila Kekesi + Vorlesungsmaterial
# https://www.youtube.com/watch?v=I6gjCZl7xFw
# https://www.youtube.com/watch?v=4hAqEjj7IdE

class Node:
    def __init__(self,successors=[],name="",color="white"):
        self.name = name
        self.color = color
        self.successors = successors

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

def eingang(adj):
    """
    Args:
        adj: Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    Returns:
        E: Eingangskanten pro Knoten
        K: Pos. von Knoten ohne Eingangskanten
    """
    E = [] # Eingang pro Knoten
    K = [] # Knoten ohne Eingang
    for i in range(len(adj)):
        e = 0
        for a in adj:
            if i in a:
                e += 1
        E.append(e)
        if e == 0:
            K.append(i)
    return E,K

def top_sort_teil(adj, r):
    """
    Es wurde nur bis auf Teilbereiche untersucht.
    Tiefensuche mit Stack
    Topologische Sortierung mit Tiefensuche
    Kreissuche
    Args:
        r:   Startpunkt
        adj: Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    Returns:
        R: Knotenmenge von Tiefensuche
        F: Kantenmenge von Tiefensuche
        T: Topologische Sortierung
        C: Es gibt Kreis (True) oder nicht (False)
    """
    R = [r]     # Knotenmenge
    F = []      # Kantenmenge
    Q = Stack() # dyn. Menge
    Q.push(r)
    T = []      # topologische Sortierung
    C = False   # is Circle: Flase = No
    while not Q.isEmpty():
        v = Q.peek()
        i = 0
        while len(adj[v]) > i and adj[v][i] in R:   # van hova tovabb es ez a celpont a mar megjart pontok kozott van? Igen --> i+1 
            if adj[v][i] in Q.items:                # Elerhetunk innen egy mar volt kiindulopontba? Igen --> Kreis
                C = True
            i += 1
        if len(adj[v]) > i:                         # ha meg van pont ami meg nem lett megjarva
            w = adj[v][i]
            R.append(w)
            Q.push(w)
            F.append((v, w))
        else:                                       # ha minden pont meg lett mar jarva, akkor kivesszuk a Q-bol
            T.append(Q.pop())
    return (R, F, T[::-1],C)

def top_sort_ganze(adj):
    """
    Args:
        adj: Adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    Returns:
        T: Topologische Sortierung, oder [-1], wenn adj Kreis enthaelt 
    """
    T = []
    _,K = eingang(adj)
    if len(K) == 0:
        K = [0]
    while len(K) != 0:                          # amig van 0 bejovovel csomopont
        _,_,L,C = top_sort_teil(adj,K.pop(0))
        if C == True:
            return [-1]
        T += L
        if len(L) != len(adj):                  # kivesszuk a mar felhasznalt csp-okat, hogy oda mar nem menjunk
            for a in adj:
                for l in L:
                    if l in a:
                        a.remove(l)
        if len(K) == 0 and len(T) != len(adj):  # ha nincs mar csp 0 bejovovel, de meg nem vizsgaltunk meg minden cp-ot
            return [-1]                         # akkor kell uj K ertek a kovi loop-hoz (ahol valoszinu Kreis lesz)
    return T

def class_to_adj(G):
    """
    Args:
        G: Liste von Objekte
    Returns:
        D:   Dictionary Obj-Name:Number
        D_:  Dictionary Number:Obj-name
        adj: adjazenzliste: Liste von Knoten, die Listen ueber Nachbarn sind
    """
    D = {}
    D_ = {}
    for n,g in enumerate(G):
        D[g.name] = n
        D_[n] = g.name
    adj = []
    for g in G:
        tmp = []
        for s in g.successors:
            tmp.append(D[s.name])
        adj.append(tmp)
    return D,D_,adj

def topsort_to_str(T_num,D_):
    """
    Args:
        T:  Topologische Sortierung mit Zahlen
        D_: Dictionary Number:Obj-name
    Returns:
        S:  Topologische Sortierung mit orig. Benennung oder [-1], wenn adj Kreis enthaelt
    """
    if T_num == [-1]:
        return T_num
    T_str = []
    for t in T_num:
        if t == -1:
            tmp = t
        else:
            tmp = D_[t]
        T_str.append(tmp)
    return T_str

def top_order(G):
    if G == []:
        return []
    _,D_,adj = class_to_adj(G)
    T_num = top_sort_ganze(adj)
    T_str = topsort_to_str(T_num,D_)
    return T_str

if __name__ == "__main__":

    adj = [[1,3],[0,2],[1,3],[0,2]]
    print(top_sort_ganze(adj))
    adj = [[1],[2],[5,9],[],[11],[3,7],[4],[3,10],[4],[6,8],[],[]]
    print(top_sort_ganze(adj))
    adj = [[1],[0]]
    print(top_sort_ganze(adj))
    adj = [[1],[2],[3],[],[3],[4],[5]]
    print(top_sort_ganze(adj))
    n = Node()
    m = Node()
    n.name = "Quelle"
    m.name = "Senke"
    n.color = m.color = "white"
    n.successors = [m]
    m.successors = []
    G = [m,n]
    D,D_,adj = class_to_adj(G)
    T_num = top_sort_ganze(adj)
    T_str = topsort_to_str(T_num,D_)
    print("-->",top_order(G))
    n = Node()
    m = Node()
    n.name = "links"
    m.name = "rechts"
    n.color = m.color = "white"
    n.successors = [m]
    m.successors = [n]
    G = [m,n]
    D,D_,adj = class_to_adj(G)
    T_num = top_sort_ganze(adj)
    T_str = topsort_to_str(T_num,D_)
    print("-->",top_order(G))

    a = Node()
    b = Node()
    c = Node()
    d = Node()
    e = Node()
    f = Node()
    g = Node()
    h = Node()
    i = Node()
    j = Node()
    k = Node()
    l = Node()
    m = Node()
    a.name = "0"
    b.name = "1"
    c.name = "2"
    d.name = "3"
    e.name = "4"
    f.name = "5"
    g.name = "6"
    h.name = "7"
    i.name = "8"
    j.name = "9"
    k.name = "10"
    l.name = "11"
    m.name = "12"

    a.successors = [b]
    b.successors = [c]
    c.successors = [d]
    d.successors = []
    e.successors = [d]
    f.successors = [e]
    g.successors = [f]
    #adj = [[1],[2],[3],[],[3],[4],[5]]
    G = [a,b,c,d,e,f,g]
    print(top_order(G))

    a.successors = []
    b.successors = [f]
    c.successors = [b]
    d.successors = []
    e.successors = [b,c,i]
    f.successors = [d,g]
    g.successors = []
    h.successors = [c,j]
    i.successors = [c]
    j.successors = [i]
    #adj = [[],[5],[1],[],[1,2,8],[3,6],[],[2,9],[2],[8]]
    G = [b,c,d,e,f,g,h,i,j]
    print(top_order(G)) 
    print(["4","7","9","8","2","1","5","3","6"])

    a.successors = [b,c,f,g]
    b.successors = []
    c.successors = []
    d.successors = []
    e.successors = [d]
    f.successors = [d,e]
    g.successors = [c,e,h]
    h.successors = [i]
    i.successors = []
    j.successors = [g,k,l,m]
    k.successors = []
    l.successors = []
    m.successors = []
    G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    print(top_order(G))
    b.successors = [a]
    m.successors = []
    G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    print(top_order(G))
    b.successors = []
    m.successors = [j]
    G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    print(top_order(G))
    m.successors = []
    j.successors = [j]
    G = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    print(top_order(G))