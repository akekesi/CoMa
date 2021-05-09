# CoMaII - PA_01 - Binaerbaum
# Attila Kekesi

class Node:
    """
    In dieser Programmieraufgabe geht es um eine erste Implementierung binaerer Baeume.
    Ein Binaerbaum wird dann durch seinen Wurzelknoten dargestellt.
    Konvention: In jedem Baum kommt jeder Schluessel hoechstens einmal vor.
    - key           (ganze Zahl)
    - leftChild     (Instanz der Klasse Node)
    - rightChild    (Instanz der Klasse Node)
    """
    def __init__(self, key, leftChild, rightChild):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def __str__(self):
        return str(self.struktur())
    
    def struktur(self):
        K = [self.key]
        if self.leftChild != None:
            K.append(self.leftChild.struktur())
        else:
            K.append([""])
        if self.rightChild != None:
            K.append(self.rightChild.struktur())
        else:
            K.append([""])
        return K
    
    def keys(self):
        K = [self.key]
        if self.leftChild != None:
            for k in self.leftChild.keys():
                K.append(k)
        if self.rightChild != None:
            for k in self.rightChild.keys():
                K.append(k)
        return K

    def height(self):
        l = 0
        r = 0
        if self.leftChild != None:
            l = self.leftChild.height()
        if self.rightChild != None:
            r = self.rightChild.height()
        if self.leftChild == None and self.rightChild == None:
            return 0
        return max(l,r) + 1

    def leaves_hilf(self):
        L = ""
        if self.leftChild != None:
            l = self.leftChild.leaves_hilf()
            L += l
        if self.rightChild != None:
            r = self.rightChild.leaves_hilf()
            L += r
        if self.leftChild == None and self.rightChild == None:
            return str(self.key) + " "
        return L
    
    def leaves(self):
        return [int(x) for x in self.leaves_hilf().split()]

if __name__ == "__main__":
    bin0 = Node(0,None,None)
    print("bin0:\t",bin0)
    print("keys:\t",bin0.keys())
    print("height:\t ",bin0.height())
    print("leaves: ",bin0.leaves())
    print("---")

    node1RLR = Node(4,None,None)
    node1RL = Node(3,None,node1RLR)
    node1RR = Node(7,None,None)
    node1L = Node(5,None,None)
    node1R = Node(2,node1RL,node1RR)
    bin1 = Node(1,node1L, node1R)
    print("bin1:\t",bin1)
    print("keys:\t",bin1.keys())
    print("height:\t ",bin1.height())
    print("leaves: ",bin1.leaves())
    print("---") 

    node2RLRL = Node(6,None,None)
    node2RLR = Node(4,node2RLRL,None)
    node2RL = Node(3,None,node2RLR)
    node2RR = Node(7,None,None)
    node2L = Node(5,None,None)
    node2R = Node(2,node2RL,node2RR)
    bin2 = Node(1,node2L, node2R)
    print("bin2:\t",bin2)
    print("keys:\t",bin2.keys())
    print("height:\t ",bin2.height())
    print("leaves: ",bin2.leaves())
    print("---") 

    node3LL = Node(7,None,None)
    node3L = Node(5,node3LL,None)
    node3RL = Node(3,None,None)
    node3R = Node(2,node3RL,None)
    bin3 = Node(0,node3L, node3R)
    print("bin3:\t",bin3)
    print("keys:\t",bin3.keys())
    print("height:\t ",bin3.height())
    print("leaves: ",bin3.leaves())
    print("---") 

    node4L = Node(1,None,None)
    bin4 = Node(0,node4L,None)
    print("bin4:\t",bin4)
    print("keys:\t",bin4.keys())
    print("height:\t ",bin4.height())
    print("leaves: ",bin4.leaves())
    print("---") 

    node5L = Node(1,None,None)
    node5R = Node(2,None,None)
    bin5 = Node(0,node5L,node5R)
    print("bin5:\t",bin5)
    print("keys:\t",bin5.keys())
    print("height:\t ",bin5.height())
    print("leaves: ",bin5.leaves())
    print("---") 

    node6LL = Node(3,None,None)
    node6L = Node(1,node6LL,None)
    node6R = Node(2,None,None)
    bin6 = Node(0,node6L,node6R)
    print("bin6:\t",bin6)
    print("keys:\t",bin6.keys())
    print("height:\t ",bin6.height())
    print("leaves: ",bin6.leaves())
    print("---") 

    print(node1RL.height())
    print(node1R.leaves())
    print(node3LL.height())
    print(node3LL.leaves())