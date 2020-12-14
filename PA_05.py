# CoMa - PA_05

# Nachbarschaft in Liste
def get_classes(n,E):
    L = []
    for i in range(n):
        L.append([i])           # Nachbarschaft mit sich selbst
    for i in range(len(E)):
        n = E[i][0]
        m = E[i][1]
        L[n].append(m)
    return L

# Liste vergleichen --> gleich?
def are_equal(list1,list2):
    list1 = list_sort(list1)    # Liste sortieren
    list2 = list_sort(list2)    # Liste sortieren
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                if i == len(list1)-1:
                    return True
            else:
                return False
    else:
        return False

# Liste vergleichen --> disjunkt?
def are_disjoint(list1,list2):
    list1 = list_sort(list1)    # Liste sortieren
    list2 = list_sort(list2)    # Liste sortieren
    if len(list1) == 0 or len(list2) == 0:  # Nullmenge
        return True
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] != list2[j]:
                if i == len(list1)-1 and j == len(list2)-1:
                    return True
            else:
                return False

def get_eqclasses(n,E):
    L = get_classes(n,E)
    L_kom = [1]*len(L)      # Kommentar zum L
    Res = []
    for i in range(len(L)):
        if len(L[i]) == 1:
            L_kom[i] = 1    # nicht unbedingt nötig, bleibt 1 --> continue
        elif L_kom[i] == 1:
            for j in range(i+1,len(L)):
                if L_kom[j] == 1:
                    if are_equal(L[i],L[j]):
                        L_kom[i] += 1
                        L_kom[j] = '+'      # schon gezaehlt
    for i in range(len(L)):
        if L_kom[i] != '+':
            if L_kom[i] == len(L[i]):
                Res.append(L[i])
            else:
                return []
    return Res

def list_sort(L):
    n = len(L)
    for i in range(n-1,0,-1):
        for j in range(i):
            if L[j] > L[j+1]:
                tmp = L[j]
                L[j] = L[j+1]
                L[j+1] = tmp
    return L

# Test
#n = 4
#E = [(1,2),(2,1),(3,1),(1,3),(2,3),(3,2)]
#E = [(1,2),(3,1),(1,3),(2,3),(3,2)]
#E = [(1,2),(2,1),(2,3),(3,2)]
#E = [(1,2),(2,1)]
#E = [(1,2)]
#E = [(1,0),(2,0),(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)]
#E = [(1,0),(2,0),(1,2),(2,1),(1,3),(3,1),(2,3),(3,2),(0,3),(3,0)]
#E = [(1,0),(2,0),(1,2),(2,1)]
#print(get_eqclasses(n,E))
#print(get_eqclasses(0,[]))

#print(list_sort([11,2,3,4,4,4,3,2,1]))
#print(are_equal([11,2,3,4,4,4,3,2,1],[2,11,4,3,4,4,3,2,1]))
#print(are_equal([2,1],[1,2]))
#print(are_disjoint([11,2,3,4,4,4,3,2,1],[22]))
#print(are_disjoint([0],[11,2,3,4,4,4,3,2,1]))
#L = get_classes(n,E)
#print(L)
