# CoMa - PA_12
# Attila Kekesi (402830)

# Hauptfunktion
# Input:    Liste
# Output:   Zahl: Laenge der unimodularen Liste
# O(n^2) ???
def maxunimod(M):
    S = ['<']                       # Hilfsliste fuer '<','=','>'
    for i in range(1,len(M)):
        if M[i-1] < M[i]:
            S.append('<')
        elif M[i-1] > M[i]:
            S.append('>')
        else:
            S.append('=')
    if len(M) == 0:
        return 0
    elif len(M) == 1:
        return 1
    else:
        s = 0                       # Laenge der unimodularen Liste
    TMP = S[:]                      # originale S behalten, da '=' in S bei jeder Schleife umschrieben wird
    for i in range(len(M)):         # check die Laenge der unimodularen Liste von vorne
        S = TMP[:]                  # originale S
        S[i] = '<'                  # erste Element soll immer '<' sein
        tmp = 1
        for j in range(i+1,len(M)):
            if S[j] == '=':         # '='
                tmp += 1
                S[j] = S[j-1]
            elif S[j-1] == '<':     # vorherige: '<'
                if S[j] == '<':
                    tmp += 1
                else:
                    tmp += 1
            elif S[j-1] == '>':     # vorherige: '>'
                if S[j] == '>':
                    tmp += 1
                else:               # Ender der unimodularen Liste
                    if s < tmp:
                        s = tmp
                    break
            if j == len(M)-1:       # if es Ende der Liste erreicht
                if s < tmp:
                    s = tmp
    return s

# Testfunktion
def test_maxunimod():
    M = [[4,5,3,2,1,3,6,4,7],[10,9,8,10,6,5,4,3,2,3],[10,9,8,7,6,5,4,3,2,3],[10,9,8,7,6,5,4,3,2,1],[1,1,1,0,0],[0,0,1,1,1],[1,1],[1],[],[0, 0, 1, 0]]
    for i in range(len(M)):
        print(maxunimod(M[i]))
#test_maxunimod()
#M = [0, 0, 1, 0]
#M = [1, 0, 0, 1, 0]
#print(maxunimod(M))