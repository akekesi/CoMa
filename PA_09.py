# CoMa - PA_09
# Attila Kekesi (402830)

# Hauptfunktion
# Input:    string z.B.: "[{1}+5]*({2}+[{1*(3)}+2])"
# Output:   (Summe,Tiefe)
def evaluate(string):
    l = len(string)
    if l == 0:                                              # Falls string leer ist: ""
        raise Exception('syntaktisch inkorrekt')
    k1 = 0                                                  # Fuer () Klammern
    k2 = 0                                                  # Fuer [] Klammern
    k3 = 0                                                  # Fuer {} Klammern
    K = [[],[],[]]                                          # Fuer Tiefe berechnen durch Klammern
    Z = []                                                  # Ob string Zahl enthält? wegen"()" 
    for i in range(l):
        if string[i] == " ":                                # space ist moeglich z.B.: "1 +1"
            continue
        elif string[0] == "+" or string[0] == "*" or string[-1] == "+" or string[-1] == "*":    # erste/letzte darf nicht +/* sein
            raise Exception('syntaktisch inkorrekt')
        elif string[i] == "(":                              # von hier: Klammern zusammenzaehlen und duch () ersetzten
            k1 += 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
        elif string[i] == ")":
            k1 -= 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
            if k1 < 0:
                raise Exception('syntaktisch inkorrekt')
        elif string[i] == "[":
            k2 += 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
            string = list(string)
            string[i] = "("
            string = "".join(string)
        elif string[i] == "]":
            k2 -= 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
            string = list(string)
            string[i] = ")"
            string = "".join(string)
            if k2 < 0:
                raise Exception('syntaktisch inkorrekt')
        elif string[i] == "{":
            k3 += 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
            string = list(string)
            string[i] = "("
            string = "".join(string)
        elif string[i] == "}":
            k3 -= 1
            K[0].append(k1)
            K[1].append(k2)
            K[2].append(k3)
            string = list(string)
            string[i] = ")"
            string = "".join(string)
            if k3 < 0:
                raise Exception('syntaktisch inkorrekt')    # bis hier
        elif string[i] == "+" or string[i] == "*":          # wegen "1+*", nicht unbedingt noetig wegen eval()
            if i < l-1:                                     # bis vorletzte geprueft
                if string[i+1] == "+" or string[i+1] == "*":
                    raise Exception('syntaktisch inkorrekt')
        else:
            try:
                int(string[i])                              # check ob es Zahl ist
                Z.append(string[i])                         # zu Z zufuegen
            except:
                raise Exception('syntaktisch inkorrekt')
    if k1 != 0 or k2 != 0 or k3 != 0:                       # wegen falsche Klammern, nicht unbedingt noetig wegen eval()
        raise Exception('syntaktisch inkorrekt')
    if len(Z) == 0:                                         # string enthaelt keine Zahl
        raise Exception('syntaktisch inkorrekt')
    Ksum = summa(K)                                         # Summe von Tiefen
    if len(Ksum) == 0:                                      # falls es keine Klammer gibt
        t = 0
    else:
        t = max(Ksum)                                       # max. Tiefe
    try:
        s = eval(string)                                    # check ob string --> Zahl
        return (s,t)
    except:
        raise Exception('syntaktisch inkorrekt')

# Hilfsfunktion: Summe von Tiefen
def summa(M):
    S = []
    for i in range(len(M[0])):
        tmp = 0
        for j in range(len(M)):
            tmp += M[j][i]
        S.append(tmp)
    return S

# Testfunktion
def test_evaluate():
    string = ["1+(1+1)*(1+1)","{1+1}*[1+1]+38","[{1}+5]*({2}+[{1*(3)}+2])","{3+2)+1"]
#    string = ["01"]
#    string = ["abc"]
#    string = ["1++1"]
#    string = ["1**1"]
#    string = ["2/1"]
#    string = ["1+1"]
#    string = ["3^3"]
#    string = ["(3))"]
#    string = ["+1"]
#    string = ["(1)+"]
#    string = ["(1[+]1)"]
#    string = ["(1%1)"]
#    string = [""]
#    string = [" "]
#    string = ["()"]
#    string = [")("]
#    string = ["1 + 1"]
#    string = ["+)"]
    for i in range(len(string)):
        print(evaluate(string[i]))
#test_evaluate()