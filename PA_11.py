# CoMa - PA_11
# Attila Kekesi (402830)

# Hauptfunktion
# Input:    Matrix als str
# Output:   L und U Matrizen in ein Matrix als str
# O(n^3)
def LU_decomposition(M):
    M = str_to_matrix(M)            # str_to_matrix
    L = []                          # L Matrix
    U = []                          # U Matrix
    R = []                          # R Matrix = L und U zusammen
    for i in range(len(M)):         # L,U,R Anfangsmatrix
        tmpL = []
        tmpU = []
        tmpR = []
        for j in range(len(M[0])):
            tmpU.append(M[i][j])
            if i == j:
                tmpL.append(1)
            else:
                tmpL.append(0)
            tmpR.append(0)
        L.append(tmpL)              # L = ones(size(M))
        U.append(tmpU)              # U = M
        R.append(tmpR)              # R = zeros(size(M))

    for i in range(len(M)):                     # LU-Zerlegung
        for k in range(i+1,len(M)):
            tmp = round(U[k][i] / U[i][i],1)    # Werte fuer L
            if str(tmp)[-1] == '0':             # x.0 --> x
                tmp = int(tmp)
            for j in range(len(M[0])-1,-1,-1):
                U[k][j] = U[k][j] - tmp * U[i][j]
                L[k][i] = tmp
    
    for i in range(len(M)):         # L und U zusammenfuegen
        for j in range(len(M[0])):
            if j >= i:
                R[i][j] = U[i][j]
            else:
                R[i][j] = L[i][j]
    s = matrix_to_str(R)            # matrix_to_str
    return s

# Hilfsfunktion: matrix_to_str
def matrix_to_str(M):
    s = ''
    for i in range(len(M)):
        for j in range(len(M[0])):
            s += str(M[i][j])
            if i*j < (len(M)-1) * (len(M[0])-1):    # nicht Ende der Matrix
                if j < len(M[0])-1:                 # nicht Ende der Zeile
                    s += ' '
                else:                               # Ende der Zeile
                    s += ', '
    return s

# Hilfsfunktion: str_to_matrix
def str_to_matrix(s):
    M = []
    S = '[['                    # str als Matrix umschreiben
    for i in range(len(s)):
        if s[i] == ' ':
            if s[i-1] == ',':   # Erste Zahl der neuen Zeile am Anfang ohne ' ' 
                continue
            else:
                S += ','        # ',' zwischen den Zahlen
        elif s[i] == ',':       # neue Zeile '],['
            S += '],['
        else:
            S += str(s[i])
    S += ']]'
    M = eval(S)                 # str --> Matrix
    return M

# Testfunktion
def test_LU_decomposition():
    M = ['2 4 -7, -4 -7 13, 34 71 -131','5 -3, 35 -29','17 4, -17 42','-1 -7 4, -6 -32 22, 9 3 -33']
    for i in range(len(M)):
        print(LU_decomposition(M[i]))
#test_LU_decomposition()
#M = (str_to_matrix('2 4 -7, -4 -7 13, 34 71 -131'))
#print(M)
#s = matrix_to_str([[2,4,-7],[-4,-7,13],[34,71,-131]])
#print(s)