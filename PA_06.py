# CoMa - PA_06
# Attila Kekesi (402830)

from random import random

"""
Hilfsfunktion_1:
    pos kann >= n*m sein? --> nein

Hilfsfunktion_2 & Hilfsfunktion_3:
    ohne Rueckgabewert?
        --> azzal is megy
        --> nelkul is megy (250-251)
    
Hauptfunktion:
    retrun print('...')
        oder
    print('...')
    return None --> muekoedik igy
"""

# Hilfsfunktion_1
# Manipulation von "positions"
# Input:
#   n:      Reihen-Zahl des Welt-Rechtecks,
#   m:      Spalten-Zahl des Welt-Rechtecks,
#   pos:    Position der Figur als nichtnegative ganze Zahl,
#   rnd:    Float im halboffenen Intervall [0;1).
#               rnd2[0;0:25): Figur geht nach rechts,
#               rnd2[0:25;0:5): Figur geht nach links,
#               rnd2[0;5;0:75): Figur geht nach unten,
#               rnd2[0:75;1): Figur geht nach oben.
# Output:   neue Position
def updatePosition(n,m,pos,rnd):
    if 0 <= rnd < 0.25:
        if pos % m == m-1:
            pos += -(m-1)
        else:
            pos += 1 
    elif 0.25 <= rnd < 0.5:
        if pos % m == 0:
            pos += m-1
        else:
            pos += -1
    elif 0.5 <= rnd < 0.75:
        if pos + m >= n*m:
            pos += -(n-1)*m  
        else:
            pos += m
    elif 0.75 <= rnd < 1:
        if pos - m < 0:
            pos += (n-1)*m  
        else:
            pos += -m
    return pos

def test_updatePosition():
    rnd = random()
    Test = [[3,1,2,0.8],[1,8,14,0.51],[3,5,0,0.3],[3,5,4,0.8],[3,5,7,0.8],[3,5,14,0.0],[3,5,10,0.3],[3,5,10,0.5],[3,5,10,0.3],[3,5,4,0.1],[3,5,7,rnd]]
    for i in range(len(Test)):
        print(updatePosition(Test[i][0],Test[i][1],Test[i][2],Test[i][3]))
    print(rnd)
#test_updatePosition()

# Hilfsfunktion_2
# Fuehrt "updatePosition" fuer alle Elemente in "positions" durch.
# Als Parameter "rnd" wird jeweils eine Zufallszahl im Intervall [0;1) an "updatePosition" uebergeben.
# Output:   neue Position
def updatePositions(n,m,positions):
    for i in range(len(positions)):
        rnd = random()
        positions[i][1] = updatePosition(n,m,positions[i][1],rnd)
    return positions

# Hilfsfunktion_3
# Sortiert die Liste "positions" aufsteigend nach den zweiten Eintraegen der Teillisten.
def sortPositions(positions):
    l = len(positions)
    for i in range(l-1,0,-1):
        for j in range(i):
            if positions[j][1] > positions[j+1][1]:
                tmp = positions[j]
                positions[j] = positions[j+1]
                positions[j+1] = tmp
    return positions

def test_sortPositions():
    positions = []
    positions.append([['Z', 184], ['Z', 161], ['Z', 160], ['Z', 160]])
    positions.append([['Z', 160], ['Z', 160]])
    positions.append([['Z', 160]])
    positions.append([])
    for i in range(len(positions)):
        print(sortPositions(positions[i]))
#test_sortPositions()

# Hilfsfuntion_4
# Gibt alle Figuren auf dem Feld mit dem hoechsten Index in "positions" zurueck.
# Dies wird realisiert, indem aus einer geordneten Liste "positions" alle letzten Elemente mit dem gleichen Eintrag in der zweiten Position entfernt
# und zu einer neuen Liste "square" zusammengefasst werden.
def extractSquare(positions):
    l = len(positions)
    square = []
    if l == 0:
        square
    elif l == 1:
        square.append(positions[0])
        del positions[-1]
    else:
        square.append(positions[-1])
        del positions[-1]
        while len(positions) > 0 and square[-1][1] == positions[-1][1]:
            square.append(positions[-1])
            del positions[-1]
    return square       

def test_extractSquare():
    positions = []
    positions.append([['Z', 184], ['Z', 161], ['Z', 160], ['Z', 160]])
    positions.append([['Z', 160], ['Z', 160]])
    positions.append([['Z', 160]])
    positions.append([])
    positions.append([['H',51],['ZH',21],['H',1],['HH',51],['Z',0]])
    for i in range(len(positions)):
        pos = sortPositions(positions[i])
        print(pos)
        print(extractSquare(pos))
        print(pos)
#test_extractSquare()

# Hilfsfunktion_5
# Realisiert die Begegnung von Figuren auf dem gleichen Feld nach folgenden Regeln in
def giftExchange(square):
    check_H = []
    check_HH = []
    check_Z = []
    check_ZH = []
    for i in range(len(square)):
        if square[i][0] == 'H':
            check_H.append(i)
        elif square[i][0] == 'HH':
            check_HH.append(i)
        elif square[i][0] == 'Z':
            check_Z.append(i)
        elif square[i][0] == 'ZH':
            check_ZH.append(i)

    if len(check_H) > 0 and len(check_ZH) > 0:
        for i in range(len(check_H)):
            square[check_H[i]][0] = 'HH'
            check_HH.append(check_H[i])
        check_H = []

    if len(check_Z) > 0 and (len(check_H) > 0 or len(check_HH) > 0):
        if len(check_Z) >= 2 * len(check_HH):
            for i in range(len(check_H)):
                square[check_H[i]][0] = 'Z'
            for i in range(len(check_HH)):
                square[check_HH[i]][0] = 'Z'
        elif len(check_Z) < 2 * len(check_HH):
            for i in range(len(check_Z)):
                square[check_Z[i]][0] = 'ZH'
    return square

def test_giftExchange():
    square = []
    square.append([['Z', 160], ['H', 160], ['Z', 160], ['ZH', 160]])
    square.append([['H', 160], ['H', 160], ['Z', 160], ['ZH', 160]])
    square.append([['Z', 160], ['ZH', 160], ['Z', 160], ['H', 160]])
    square.append([['Z', 160], ['ZH', 160], ['H', 160], ['HH', 160]])
    square.append([['H', 160], ['ZH', 160], ['H', 160], ['H', 160]])
    square.append([['H', 160], ['Z', 160], ['Z', 160], ['ZH', 160]])
    square.append([['H', 160], ['ZH', 160]])
    square.append([['H', 160], ['HH', 160]])
    square.append([])
    for i in range(len(square)):
        print(giftExchange(square[i]))
#test_giftExchange()

# Hilfsfunktion_6
# Gibt True zurueck, falls einer der folgenden zwei Faelle eintritt:
#   Es gibt nur noch Zombies 'Z' oder 'ZH' in positions.
#   Es gibt keine Zombies 'Z' mehr in positions.
# Ansonsten gibt die Funktion False zuruck.
def christmasFated(positions):
    check_H = []
    check_HH = []
    check_Z = []
    check_ZH = []
    for i in range(len(positions)):
        if positions[i][0] == 'H':
            check_H.append(i)
        elif positions[i][0] == 'HH':
            check_HH.append(i)
        elif positions[i][0] == 'Z':
            check_Z.append(i)
        elif positions[i][0] == 'ZH':
            check_ZH.append(i)

    if len(check_H) == 0 and len(check_HH) == 0:
        return True
    elif len(check_Z) == 0:
        return True
    else:
        return False

def test_christmasFated():
    print(christmasFated([['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]))
    print(christmasFated([['HH', 160], ['HH', 160], ['Z', 160], ['ZH', 160]]))
#test_christmasFated()

# Hilfsfunktion_7
# Fuegt square an eine gegebe Liste an. Der Grundgedanke dabei ist folgender:
# Extrahiere so oft ein "square" aus "positions", bis letztere Liste leer ist.
# Fuege die "square"'s jeweils einer Zwischenspeicher-Liste an
# und setze die Zwischenspeicher-Liste als neue "positions"-Liste, sobald positions leer ist.
def mergeSquare(square,intermediate):
    for i in range(len(square)):
        intermediate.append(square[i])
    return intermediate

def test_mergeSquare():
    intermediate = [['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]
    mergeSquare([['Z', 159], ['Z', 159]],intermediate)
    print(intermediate)
#test_mergeSquare()

# Hilfsfunktion_8
# Nimmt eine Liste "positions" entgegen,
# fuer welche "christmasFated" den Wert True ausgibt
# und gibt einen der folgenden Strings (als return-Wert) zurueck:
def christmasFate(positions):
    for i in range(len(positions)):
        if positions[i][0] == 'Z' or (positions[i][0] == 'ZH' and len(positions) == 1):
            return 'Zombies ate my Christmas!'
        elif positions[i][0] == 'H' or positions[i][0] == 'HH':
            return 'Ho, ho, ho, and a merry Zombie-Christmas!'
    return 'Zombies ate my Christmas!' # ??? Falls len(positions) == 0

def test_christmasFate():
    print(christmasFate([['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]))
    print(christmasFate([['Z', 160], ['Z', 160], ['ZH', 160], ['ZH', 160]]))
    print(christmasFate([['ZH', 1], ['Z', 2]]))
    print(christmasFate([['ZH', 0], ['HH', 2], ['HH', 3]]))
#test_christmasFate()

# Hauptfunktion
def zombieChristmas(n,m,positions):
    while christmasFated(positions) == False:           # Ende?
        updatePositions(n,m,positions)                  # neue Positionen durch random Zahlen
        sortPositions(positions)                        # sort Positionen
        intermediate = []                               # tmp-Liste für Positionen nach while-Schleife
        while len(positions) != 0:
            square = extractSquare(positions)           # letzte gleiche Positionen abnehmen, square von Positionen abgezogen durch del
            square = giftExchange(square)               # square wirken lassen                                
            intermediate = mergeSquare(square,intermediate)
        positions = intermediate
    antwort = christmasFate(positions)                  # Ende
    print(antwort)
    return None                                         # Was kommt hier?

def test_zombieChristmas():
    positions = [['Z',0],['ZH',4],['H',10],['HH',14]]
    n = 3
    m = 5
    zombieChristmas(n,m,positions)
#test_zombieChristmas()