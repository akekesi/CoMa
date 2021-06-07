# CoMaII - PA_07 - Triangulierung
# Attila Kekesi

class ngonTriang:
    def __init__(self,n,triangles):
        self.n = n
        self.triangles = sorted(triangles)      # sorted
        self.walls, self.edges,self.B = self.get_walls_edges()
        if not self._is_triangulation():
            raise ValueError("no triangulation")

    def n_walls(self):
        """
        number of walls
        """
        return len(self.walls)

    def flip(self,wall):
        if wall == []:
            return ngonTriang(self.n,self.triangles)
        Node = []
#        Tri = copy.deepcopy(self.triangles)    # mit deepcopy
        Tri = self.triangles.copy()             # ohne deepcopy
        for b in self.B:
            if wall in b[-1]:
                Node.append(b[0])
            if len(Node) == 2:
                break
#        tri1 = Tri[Node[0]]                    # mit deepcopy
#        tri2 = Tri[Node[1]]                    # mit deepcopy
        tri1 = Tri[Node[0]].copy()              # ohne deepcopy
        tri2 = Tri[Node[1]].copy()              # ohne deepcopy
        for i in range(3):
            if wall[1] == tri1[i]:
                pos1 = i
            if wall[0] == tri2[i]:
                pos2 = i
            if wall[0] != tri1[i] and wall[1] != tri1[i]:
                tmp1 = tri1[i]
            if wall[0] != tri2[i] and wall[1] != tri2[i]:
                tmp2 = tri2[i]
        tri1[pos1] = tmp2
        tri2[pos2] = tmp1
        Tri[Node[0]] = sorted(tri1)             # ohne deepcopy und sorted
        Tri[Node[1]] = sorted(tri2)             # ohne deepcopy und sorted
        return ngonTriang(self.n,Tri)

    def get_walls_edges(self):
        """
        get walls and edges as list
        """
        walls = []
        edges = []
        B = []
        s = 0                                   # number of nodes of tree
        for triangle in self.triangles:
            b = []
            t = triangle.copy()
            t.append(t[0])                                                  # t=(t0,t1,t2,t0)
            for i in range(len(t)-1):
                if abs(t[i+1]-t[i]) != 1 and abs(t[i+1]-t[i]) != self.n-1:  # not edge --> wall 
                    w = [min(t[i],t[i+1]),max(t[i],t[i+1])]
                    b.append(w)
                    if w not in walls:                                      # count wall only once 
                        walls.append(w)
                else:                                                       # edge --> not wall
                    e = [min(t[i],t[i+1]),max(t[i],t[i+1])]
                    if edges != False and e not in edges:                   # walls do not cross eachother
                        edges.append(e)
                    else:                                                   # walls cross eachother
                        edges = False
            B.append((s,triangle,b))            # tuple(node,triangle,[wall1],...)
            s += 1
        return sorted(walls),edges,B

    def _is_triangulation(self):
        """
        True:   if triangulation
        False:  if not triangulation
        """
        if len(self.triangles) != self.n-2:     # number of triangles == n-2
            return False
        elif self.n_walls() != self.n-3:        # number of walls == n-3
            return False
        elif self.edges == False:               # edges not only once --> edges cross eachother 
            return False
        else:
            return True

if __name__=="__main__":
    n = 4
    triangles = [[0,1,2],[0,2,3]]
    #n = 3
    #triangles = [[0,1,2]]
    T = ngonTriang(n,triangles)
    print(T.triangles)
    print(T.walls)
    print(T.n_walls())
    S = T.flip([0,2])
    print(S.triangles)
    print(T.triangles)
    W = ngonTriang(n,[[0,1,2],[0,2,3],[1,2,3]])