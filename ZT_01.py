# CoMa - ZT_01
# Attila Kekesi (402830)

# Geben Sie eine python-Funktion monoton an,
# die zu einer gegebenen int-Liste der Laenge n>=1
# die maximale Laenge einer monotonen Teilliste bestimmt.

def monoton(L):
    S = []
    for i in range(len(L)-1):
        if L[i] >= L[i+1]:
            S.append([i,i+1])
    if len(S) == 0:
        return 1
    R = []
    for i in range(len(S)-1):
        laenge = 2
        R.append(laenge)
        j = i+1
        while j < len(S) and S[i][1] == S[j][0]-j+i+1:
            laenge += 1
            j += 1
        R[i] = laenge

    s = []
    for i in range(len(L)-1):
        if L[i] <= L[i+1]:
            s.append([i,i+1])
    if len(s) == 0:
        return 1
    r = []
    for i in range(len(s)-1):
        laenge = 2
        r.append(laenge)
        j = i+1
        while j < len(s) and s[i][1] == s[j][0]-j+i+1:
            laenge += 1
            j += 1
        r[i] = laenge
    if get_max(r) >= get_max(R):
        return get_max(r)
    else:
        return get_max(R)

def get_max(int_list):
    L = len(int_list)
    m = int_list[0]
    for i in range(1,L):
        if m < int_list[i]:
            m = int_list[i]
    return m    

#L = [0]
#L = [4 ,4, 4, 4, 4, 4, 4, 4]
#L = [4 , 5, 3, 2, 1, 3, 6, 4, 7]
#L = [3 ,6 ,8 ,4 ,11 ,345 ,56 ,7 ,8 ,999 ,4 ,5 ,3]
#L = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,6 ,5 ,4 ,3 ,2 ,1 ,0]
#print(monoton(L))
#print(get_max(L))
