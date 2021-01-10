# CoMa - PA_07
# Attila Kekesi (402830)

# Hauptfunktion
# Input:
#   Startpunkt: s = (sy,sx)
#   Endpunkt: t = (ty,tx)
#   File (optional): filename.dat
# Output:
#   Schritte von s bis t, wenn moeglich
#   -1, wenn nicht moeglich
def abstand(s,t,dateiname = "labyrinth.dat"):
    lab_file = open(dateiname, "r")     # file.dat als Matrix L abspeichern
    L = []
    for zeile in lab_file:
        tmp = []
        for n in zeile:
            if n == "P" or n == "U":
                tmp.append(n)
            else:
                L.append(tmp)
    lab_file.close()
    y = s[0]
    x = s[1]
    step = 0                                # Nummerierung der Punkte
    L[y][x] = step                          # Anfangspunkt in L
    L[t[0]][t[1]] = "T"                     # Endpunkt in L
    S = [[y,x]]                             # Anfangspunkte mit gleicher Nummerierung
    schritte = [[0,1],[0,-1],[1,0],[-1,0]]  # 4 moegliche Schritte von einem Punkt (links, rechts, oben, unten)
    S_neu = S                               # naechste Anfangspunkte mit gleicher Nummerierung
    if s == t:
        return 0
    while S_neu != []:                      # bis neue Schritte moeglich
        S_neu = []
        step += 1
        for i in range(len(S)):
            for n in range(len(schritte)):
                y = S[i][0] + schritte[n][0]
                x = S[i][1] + schritte[n][1]
                if x >= 0 and x < len(L[0]) and y >= 0 and y < len(L):  # Schritte muessen in L bleiben
                    if L[y][x] == "P":
                        L[y][x] = step                                  # Schritt in L überschreiben
                        S_neu.append([y,x])                             # neuer Schritt abspeichern
                    elif L[y][x] == "T":                                # Ziel erreicht
                        return step                                     # return Anzahl des Steps
                else:                                                   # Schritt ausserhalb von L
                    continue                                            # naechste Schritt
        S = S_neu
    return -1                                                           # return -1, Ziel kann nicht erreicht werden

# Hilfsfunktion: print Matrix L
def print_L(L):
    for i in range(len(L)):
        print(L[i])
    return None

# Testfunktion
def test_abstand():
    s = [(0,9),(1,4),(0,9),(0,9)]
    t = [(2,2),(2,2),(0,7),(0,9)]
    for i in range(len(s)):
        print(abstand(s[i],t[i]))
        print(abstand(s[i],t[i],"labyrinth_2.dat"))
    print(abstand((1,0),(6,12),"labyrinth_3.dat"))
    print(abstand((1,0),(1,1),"labyrinth_3.dat"))
#test_abstand()