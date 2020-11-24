# Get Lattice Point Number

from matplotlib import pyplot as plt

# Global Values
x_01 = 0
x_02 = 6
y_01 = 0

# Plot Lattice Points
def plot_lattice_point(X_0,Y_0,X_1,Y_1):
    plt.plot(X_0,Y_0,'k')
    plt.plot(X_1,Y_1,'r')
    plt.scatter(X_0, Y_0,color='k')
    plt.scatter(X_1, Y_1,color='r')
    plt.ylabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# a = links-unten
# b = rechts-oben
def convert_to_standard(a1,a2,b1,b2):
    if a1 > b1:
        tmp = a1
        a1 = b1
        b1 = tmp

    if a2 > b2:
        tmp = a2
        a2 = b2
        b2 = tmp

    T = (a1,a2,b1,b2)
    return T

# Ckeck: Schnittmenge = 0
def intersects(h,a1,a2,b1,b2):
    T = convert_to_standard(a1,a2,b1,b2)    # a = links-unten, b = rechts-oben
    a1 = T[0]
    a2 = T[1]
    b1 = T[2]
    b2 = T[3]

    if a1 > x_02 or b1 < x_01:
        return False
    elif a2 > h or b2 < y_01:
        return False
    else:
        return True

# Get Delta x
def get_delta_x1(a1,b1):
    T = convert_to_standard(a1,0,b1,0)    # a = links-unten, b = rechts-oben
    a1 = T[0]
    b1 = T[2]

    Lx_1 = 0
    Lx_2 = 0

    if a1 <= x_01:
        Lx_1 = x_01
    elif a1 <= x_02:
        Lx_1 = a1

    if b1 >= x_02:
        Lx_2 = x_02
    elif b1 >= x_01:
        Lx_2 = b1

    Lx = Lx_2-Lx_1
    return Lx

# Get Delta y
def get_delta_x2(h,a2,b2):
    T = convert_to_standard(0,a2,0,b2)    # a = links-unten, b = rechts-oben
    a2 = T[1]
    b2 = T[3]

    Ly_1 = 0
    Ly_2 = 0

    if a2 <= y_01:
        Ly_1 = y_01
    elif a2 <= h:
        Ly_1 = a2

    if b2 >= h:
        Ly_2 = h
    elif b2 >= y_01:
        Ly_2 = b2

    Ly = Ly_2-Ly_1
    return Ly

# Get Lattice Points
def get_lattice_point_number(h,a1,a2,b1,b2):
 # Chekc: h < 0
    if h < 0:
        return 'Die Eingabe ist fehlerhaft.'

 # R_(a,b)
    X_0 = [x_01,x_02,x_02,x_01]
    Y_0 = [y_01,y_01,h,h]

 # R_h
    T = convert_to_standard(a1,a2,b1,b2)    # a = links-unten, b = rechts-oben
    a1 = T[0]
    a2 = T[1]
    b1 = T[2]
    b2 = T[3]

    X_1 = [a1,b1,b1,a1]
    Y_1 = [a2,a2,b2,b2]

 # Plot
    plot_lattice_point(X_0,Y_0,X_1,Y_1)

 # Schnittmenge
    intersect = intersects(h,a1,a2,b1,b2)   # Check: Schnittmenge = 0
    if intersect != True:
         return 'Der Schnitt der gegebenen Rechtecke ist leer.'
    else:
        Lx = get_delta_x1(a1,b1)            # Delta x
        Ly = get_delta_x2(h,a2,b2)          # Delta y

    L = (Lx+1)*(Ly+1)

    return 'Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {}.'.format(L)

# Test
def Test():
    Test = [[0,0,0,0,0],[-1,0,0,0,0],[1,1,1,1,1],[6,6,6,6,6],[6,-6,-6,6,6],[6,6,6,7,7],[6,6,6,7,6],[6,6,6,6,7],[11,7,11,7,11],[11,0,11,6,11],[11,1,1,5,10],[11,1,1,1,1],[-11,6,11,6,11],[11,6,11,6,-11],[6,8,9,0,0],[5,-2,5,0,9],[5,-2,4,1,9]]

    for i in range(len(Test)):
        h = Test[i][0]
        a1 = Test[i][1]
        a2 = Test[i][2]
        b1 = Test[i][3]
        b2 = Test[i][4]
        print(get_lattice_point_number(h,a1,a2,b1,b2))
        print('---')

    print(get_delta_x1(10,-10))
    print(get_delta_x2(10,11,-11))
    print(get_delta_x2(10,-11,-11))
    print(get_delta_x2(1,1,-11))
#Test()                                      # Test