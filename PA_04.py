# CoMa - PA_04
# Attila Kekesi (402830)

# Hilfsfunktion_1
# Berechnung für quadratischen Abstand
# Input: Liste von Punkten_(x,y), Linie_(a,b)
# Output: quadratischer Abstand
def get_linedistance(points,line):
    qa = 0
    for i in range(len(points)):
        #qa = qa + (line[0]*points[i][0]+line[1]-points[i][1])**2   # lieber mit qa += ...
        qa += (line[0]*points[i][0]+line[1]-points[i][1])**2
    return qa  

# Testfunktion: get_linedistance(points,line)
def test_get_linedistance():
    Test_points = [[(-1,1),(0,2),(1,1),(3,-1)],[(0,0),(1,1),(2,2),(3,3)],[(0,0)]]
    Test_line = [[(1,1),(-1,2)],[(-1,2)],[(1,1)]]
    for i in range(len(Test_line)):
        for j in range(len(Test_line[i])):
            for k in range(len(Test_points)):
                print(i)
                print(j)
                print(k)
                print(Test_line[i][j])
                print(Test_points[k])
                print(get_linedistance(Test_points[k],Test_line[i][j]))
#test_get_linedistance()

# Hilfsfunktion_2
# Berechnung für kleinsten Wert von einer Liste
# Input: Liste von Zahlen
# Output: kleinster Wert von der Liste
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

# Testfunktion: get_min(int_list)
def test_get_min():
    Test = [[],[0,0,0,0],[-1,0,1,0],[1,11,111,-1,0],[9,8,7,6,5,4,3,11.0,2,11],[0,0,0,0,1],[1,0],[0]]
    for i in range(len(Test)):
        print(get_min(Test[i]))
#test_get_min()


# Hauptfunktion
# Berechnung für kleinsten quadratischen Abstand
# Input: Liste von Punkten_(x,y), Liste von Linien_(a,b)
# Output: kleinster quadratischer Abstand
def linear_regression(points,lines):
    R = []
    for i in range(len(lines)):
        R.append(get_linedistance(points,lines[i]))
    r = get_min(R)
    return r

# Testfunktion: linear_regression(points,lines)
def test_linear_regression():
    Test_points = [[(-1,1),(0,2),(1,1),(3,-1)],[(0,0),(1,1),(2,2),(3,3)],[(0,0)],[(1,1)],[(0,0)],[(0,0)]]
    Test_lines = [[(1,1),(-1,2)],[(-1,2)],[(1,1)],[(0,0)],[(1,1)],[(0,0)]]
    for i in range(len(Test_points)):
        for j in range(len(Test_lines)):
            #print(i)
            #print(j)
            #print(Test_lines[j])
            #print(Test_points[i])
            print(linear_regression(Test_points[i],Test_lines[j]))
#test_linear_regression()