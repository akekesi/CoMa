# CoMaII - PA_04 - Union-Find-Datenstruktur
# Attila Kekesi + Vorlesungsmaterial

class Set:
    def __init__(self,elements):
        self._elements = elements

    def Elements(self):
        self.sort()
        return self._elements
    
    def sort(self):
        for i in range(1,len(self._elements)):                  # sort nach ersten Elementen
            if self._elements[i][0] < self._elements[i-1][0]:
                tmp = self._elements[i]
                self._elements[i] = self._elements[i-1]
                self._elements[i-1] = tmp
        for i in range(1,len(self._elements)):                  # sort nach zweiten Elementen, falls die ersten gleich sind
            if self._elements[i][0] == self._elements[i-1][0]:
                if self._elements[i][1] < self._elements[i-1][1]:
                    tmp = self._elements[i]
                    self._elements[i] = self._elements[i-1]
                    self._elements[i-1] = tmp

class Partition:
    def __init__(self,V):
        self.Sets = []
        if len(V) == len(set(V)):                       # es gibt kein doppelt vorkommendes Element
            for v in V:
                self.Sets.append(Set([v]))              # elementweise append von V zu self.Sets als Set-Ojbekt
        else:
            raise Exception('invalid operation')        # es gibt doppelt vorkommendes Element

    def __str__(self):
        Sets_str = []
        for s in self.Sets:
            Sets_str.append(s._elements)
        return str(Sets_str)

    def MakeSet(self,s):                                # append s (Set-Objekt)   ??? nur s = [(x,y)], oder kann s = [(x1,y1),(x2,y2),...] auch sein???
        for S in self.Sets:
            if s in S._elements:
                raise Exception('invalid operation')    # es gibt doppelt vorkommendes Element
        self.Sets.append(Set([s]))

    def GetSet(self,s):                                 # get S (Liste von Partition-Objekt = Set-Objekt), das s (x,y) enthaelt
        for S in self.Sets:
            if s in S._elements:
                return S
        raise Exception('invalid operation')            # es gibt doppelt vorkommendes Element

    def FindSet(self,s):                                # get erstes Element vom Set-Objekt, das s = (x,y) enthaelt
        return self.GetSet(s)._elements[0]

    def DelSet(self,s):                                 # delet S vom Sets, die s = (x,y) enthaelt
        try:
            self.Sets.remove(self.GetSet(s))
        except:
            raise Exception('invalid operation')        # Falls es kein s gitb --> Fehler

    def Union(self,s1,s2):
        S1 = self.GetSet(s1)
        S2 = self.GetSet(s2)
        self.DelSet(s1)
        self.DelSet(s2)
        V = S1._elements+ S2._elements
        S = Set(V)
        S.Elements()
        self.Sets.append(S)
        
if __name__ == "__main__":
    V = [(0,3),(0,1),(1,3),(1,0)]
    S = Set(V)
    print('V:\t',V)
    print('S._el:\t',S._elements)
    print('S.El:\t',S.Elements())
    print("---")
    V = [(0,3),(0,1),(1,3),(1,0)]
#    V = [(0,3),(0,1),(1,3),(1,0),(1,0)]
#    V = [(0,3)]
    S = Partition(V)
    print(S)
    S.Union((1,3),(0,1))
    print(S)
    S.Union((0,3),(0,1))
    print(S)
    print(S.FindSet((1,3)))
    S.MakeSet((300,1))
    print(S)
    S.Union((300,1),(0,1))
    print(S)
    print(S.FindSet((300,1)))
    S.MakeSet((0,0))
    print(S)
    S.Union((0,0),(0,1))
    print(S)
    print(S.FindSet((300,1)))
    print(S)