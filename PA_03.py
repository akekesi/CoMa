# CoMa - PA_03

#---------------------------------------
# begin - Sieb des Eratosthenes

# Tabelle fuer Sieb des Eratosthenes
def tabelle(n):
    T = [[0]*(n-1),[True]*(n-1)]
    for i in range(2,n+1):
        T[0][i-2] = i
    return T

# Primzahlen auskopieren
def prime_kopieren(T):
    R = []
    for i in range(len(T[0])):
        if T[1][i] == True:
            R.append(T[0][i])
    return R

# Hauptfunktion: Sieb des Eratosthenes
def sieve(n):
    if n < 2:
        return None
    else:
        T = tabelle(n)
        for i in range(2,int(n**(1/2)+1)):
            if T[1][i-2] == True:
                for j in range(2*i,n+1,i):  # lehetne range(i*i,n+1,i)
                    T[1][j-2] = False
        R = prime_kopieren(T)
    return R

# Test: sieve()
def test_sieve():
    Test = [-100,-2,-1,0,1,2,13,15,42,99,100,999,23432]
    for i in range(len(Test)):
        print(str(Test[i]),':\t ',str(sieve(Test[i])))
#test_sieve()

# end - Sieb des Eratosthenes
#---------------------------------------

#---------------------------------------
# begin - Check Prime

# Hauptfunktion: Primzahl
def isprime(n):
    if n < 2:
        return None
    else:
        for i in range(2,int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

# Test: isprime()
def test_isprime():
    Test = [-100,-2,-1,0,1,2,10,13,15,42,99,100,101,997]
    for i in range(len(Test)):
        print(str(Test[i]),':\t ',str(isprime(Test[i])))
#test_isprime()
#print(isprime(23432))

# end - Check Prime
#---------------------------------------

#---------------------------------------
# begin - Primfaktoren

# Primfaktor_Tabelle
def primfaktor_Tabelle(n,P):
    F = []
    for i in range(len(P)):
        tmp_p = P[i]
        tmp_e = 0
        while n % tmp_p == 0:
            n = (n/tmp_p)
            tmp_e = tmp_e + 1
        if tmp_e > 0:
            F.append([tmp_p,tmp_e])
        if n == 1:
            break            
    if len(F) == 0:
        F.append([n,1])
    return F

# Hauptfunktion: Primfaktoren
def factorization(n):
    if n < 2:
        return None
    else:
        P = sieve(round(n/2+0.5))
        F = primfaktor_Tabelle(n,P)
        return F

# Test: factorization()
def test_factorization():
    Test = [-100,-2,-1,0,1,2,10,13,15,23,42,64,99,100,101,997] #23432
    for i in range(len(Test)):
        print(str(Test[i]),':\t ',str(factorization(Test[i])))
#test_factorization()
#print(factorization(23432))

# end - Primfaktoren
#---------------------------------------

#---------------------------------------
# begin - Teilerzahl

# Hauptfunktion: Teilerzahl
def divisornumber(n):
    if n < 1:
        return None
    elif n == 1:
        return 1
    else:
        F = factorization(n)
        tz = 1  # Teilerzahl
        for i in range(len(F)):
            tz = tz * (F[i][1]+1)
        return tz

# Test: factorisation()
def test_divisornumber():
    Test = [-100,-2,-1,0,1,2,10,13,15,23,42,64,99,100,101,997]  # ,23432]
    for i in range(len(Test)):
        print(str(Test[i]),':\t ',str(divisornumber(Test[i])))
#test_divisornumber()

# end - Teilerzahl
#---------------------------------------

#---------------------------------------
# begin - Teilerfremd

# Hauptfunktion: Teilerfremd
def iscoprime(n,m):
    if n < 1 or m < 1:
        return None
    else:
        tz_n = divisornumber(n)
        tz_m = divisornumber(m)
        tz_nm = divisornumber(n*m)
        if abs(tz_nm - tz_n*tz_m) <= 10**(-12):
            return True
        else:
            return False

# Test: factorisation()
def test_iscoprime():
    Test_n = [-1,0,1,1,2,10,13,23432]
    Test_m = [5,64,64,1,3,2,64,64]
    for i in range(len(Test_n)):
        print(str(Test_n[i]),' \t ',str(Test_m[i]),':\t ',str(iscoprime(Test_n[i],Test_m[i])))
        #print(iscoprime(Test_n[i],Test_m[i]))
#test_iscoprime()

# end - Teilerfremd
#---------------------------------------