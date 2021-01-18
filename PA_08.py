# CoMa - PA_08
# Attila Kekesi (402830)

# Hauptfunktion
# Input:
#   Matrix als String: '2 5 9, 8 6 1'
# Output:
#   Matrix als String: '2 5 9, 8 6 1'
def multiply(A,B):
    if A == '':
        return''
    A = str_to_matrix(A)
    B = str_to_matrix(B)
    M = []
    for i in range(len(A)):
        tmp2 = []
        for j in range(len(B[0])):
            tmp1 = []
            for k in range(len(B)):
                tmp1.append(A[i][k] + B[k][j])
            tmp2.append(get_min(tmp1))
        M.append(tmp2)
    s = matrix_to_str(M)
    return s

# Hauptfunktion
# Input:
#   Matrix als String: '2 5 9, 8 6 1'
#   Zahl >= 1
# Output:
#   Matrix als String: '2 5 9, 8 6 1'
def power(A,m):
    if m == 1:
        M = A
    else:
        M = A
        for i in range(1,m):
            M = multiply(M,A)
    return M

# Hilfsfunktion: String to Matrix
def str_to_matrix(A):
    M = []      # output Matrix
    tmp1 = ''   # Elemente
    tmp2 = []   # Zeilen
    for i in range(len(A)):
        if i > 0 and A[i-1] == ',': # nach Komma eine leere Schleife
            continue
        elif A[i] == ' ':           # Element in Zeile speichern
            tmp2.append(int(tmp1))
            tmp1 = ''
        elif A[i] == ',':
            tmp2.append(int(tmp1))  # Zeile in Matrix speichern
            tmp1 = ''
            M.append(tmp2)
            tmp2 = []
        else:                       # Element speichern
            tmp1 += A[i]
    tmp2.append(int(tmp1))          # letzte Element in letzte Zeile speichern
    M.append(tmp2)                  # letzte Zeile in Matrix speichern
    return M

# Hilfsfunktion: Matrix to String
def matrix_to_str(M):
    s = ''
    for i in range(len(M)):
        for j in range(len(M[0])):
            s += str(M[i][j])
            if j == len(M[0])-1:
                if i == len(M)-1:
                    break
                else:
                    s += ', '
            else:
                s += ' '
    return s

# Hilfsfunktion: Get Min
def get_min(int_list):
    L = len(int_list)
    if L == 0:
        return None
    else:
        m = int_list[0]             # kleinster Wert
        for i in range(1,L):
            if m > int_list[i]:
                m = int_list[i]
        return m

# Testfunktion
def test_multiply():
    A = '4 3, 1 7'
    B = '2 5 9, 8 6 1'
    print(str_to_matrix(A))
    print(str_to_matrix(B))
    print(multiply(A,B))
    print('---')
    A = '-4 3, 1 7'
    B = '2 5 9, 8 6 1'
    print(str_to_matrix(A))
    print(str_to_matrix(B))
    print(multiply(A,B))
    print('---')
    A = '4 3'
    B = '2, 1'
    print(str_to_matrix(A))
    print(str_to_matrix(B))
    print(multiply(A,B))
    print('---')
    P = '4 3, 1 7'
    m = 3
    print(str_to_matrix(P))
    print(power(P,m))
    print('---')
    P = '4 3, 1 7'
    m = 1
    print(str_to_matrix(P))
    print(power(P,m))
    print('---')
    P = ''
    m = 1
    #print(str_to_matrix(P))
    print(power(P,m))
#test_multiply()