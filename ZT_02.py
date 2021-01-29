# CoMa - ZT_02
# Attila Kekesi (402830)

# Ein Palindrom ist eine Zeichenkette, die vorwaerts wie rueckwaerts gelesen identisch ist.
# Im Rahmen dieser Aufgabe definieren wir zwei Typen von Palindromen:
# Intlist-Palindrom
# Int-Palindrom

def is_Intlist_Palindrom(C):
    s = 0
    for i in range(int(len(C)/2)+1):
        if C[i] == C[-i-1]:
            s += 1
    if s == int(len(C)/2)+1:
        return True
    else:
        return False

C = [1,2,1]
#C = [0]
#C = [6 , -16, 9, 2, -12, 5, 15, 5, -12, 2, 9, -16, 6]
#C = [1 , 11, 4, 14, 7, 0, 10, 3, 13, 6, 16]
#C = [8 , 1, 11, 4, 14, 7, 0, 0, 7, 14, 4, 11, 1, 8]
#C = [3 , 13, 6, 16, 9, 2, -12, 5, 15, -8, 1]
#print(is_Intlist_Palindrom(C))

def is_Int_Palindrom(c):
    if c < 0:
        return None
    else:
        s = str(c)
        C = []
        for i in s:
            C.append(int(i))
        return is_Intlist_Palindrom(C)

#print(is_Int_Palindrom(1))
#print(is_Int_Palindrom(-1))
#print(is_Int_Palindrom(0))
#print(is_Int_Palindrom(-5555))
#print(is_Int_Palindrom(456456456654654654))