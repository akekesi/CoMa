# CoMaII - PA_06 
# Attila Kekesi + IntVektor from isis
# for comajudge

class IntVektor:
    def __init__(self,x,y,z):
        if type(x) != type(0) or type(y) != type(0) or type(z) != type(0):
           raise TypeError("Vektoreintrag keine ganze Zahl.")
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return '({0:n},{1:n},{2:n})'.format(self.x,self.y,self.z)

    def __getitem__(self,i):
        if type(i) != type(0):
           raise TypeError("Index keine ganze Zahl.")
        if i<0 or i>2:
           raise IndexError("Index nicht im zul. Bereich.")
        elif i==0:
           return self.x
        elif i==1:
           return self.y
        elif i==2:
           return self.z

    def __add__(self,other):
        if isinstance(other,IntVektor):
           return IntVektor(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
           raise TypeError("Formate passen nicht.")

    def __mul__(self,other):
        if isinstance(other,IntVektor):
           return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
           return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
           raise TypeError("Formate passen nicht.")

    def __rmul__(self,other):
        if isinstance(other,IntVektor):
           return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
           return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
           raise TypeError("Formate passen nicht.")

    def copy(self):
        return IntVektor(self.x,self.y,self.z)

class Teilgitter(IntVektor):
    def __init__(self,x,y,z):
        IntVektor.__init__(self,x,y,z) # useful for __str__()
        self.b1 = IntVektor(2,1,1)
        self.b2 = IntVektor(1,0,5)
        self.Koordinate_1 = y
        self.Koordinate_2 = x-self.Koordinate_1*self.b1.__getitem__(0)
        if self.Koordinate_1*self.b1.__getitem__(2) + self.Koordinate_2*self.b2.__getitem__(2) != z:
            raise TypeError("Vektor liegt nicht im Teilgitter.")
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{super().__str__()}; Koordinate 1: {self.Koordinate_1}, Koordinate 2: {self.Koordinate_2}'

    def __add__(self,other):
        x = self.x+other.x
        y = self.y+other.y
        z = self.z+other.z
        return Teilgitter(x,y,z)

    def __mul__(self,other):
        if isinstance(other,Teilgitter):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
            return Teilgitter(self.x * other, self.y * other, self.z * other)

    def __rmul__(self,other):
        if isinstance(other,Teilgitter):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
            return Teilgitter(self.x * other, self.y * other, self.z * other)

    def copy(self):
        return Teilgitter(self.x,self.y,self.z)

if __name__=="__main__":
    A = Teilgitter(10,3,23)
    print(A)
    B = Teilgitter(14,4,34)
    print(B)
    print(A+B)
    print(3*A)
    print(-3*A)
    print(B*7)
    print(A*B)
    print(A.copy())
    print(Teilgitter(9,5,0))
    print(Teilgitter(9,5,1))
    