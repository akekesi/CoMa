# Get Lattice Point Number

# Global Values
x_01 = 0
x_02 = 6
y_01 = 0

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
        b2 = a2

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

    # R_h
    T = convert_to_standard(a1,a2,b1,b2)    # a = links-unten, b = rechts-oben
    a1 = T[0]
    a2 = T[1]
    b1 = T[2]
    b2 = T[3]

    # Schnittmenge
    intersect = intersects(h,a1,a2,b1,b2)   # Check: Schnittmenge = 0
    if intersect != True:
         return 'Der Schnitt der gegebenen Rechtecke ist leer.'
    else:
        Lx = get_delta_x1(a1,b1)            # Delta x
        Ly = get_delta_x2(h,a2,b2)          # Delta y

    L = (Lx+1)*(Ly+1)

    return 'Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {}.'.format(L)
