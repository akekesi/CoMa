# CoMaII - PA_05 - AVL-Baum
# Attila Kekesi + Vorlesungsmaterial
# for comajudge

class Node:
    def __init__(self,key,leftChild=None,rightChild=None,parent=None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

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

class AVLTree:
    def __init__(self,key):
        self.key = key
        self.root = Node(key)

    def insert(self,key):
        """
        Eingabe:
            Schluesselwert key von neuem Knoten node mit node.left = node.right = None
        Resultat:
            Modifikation von T, sodass node neuer Baumknoten ist
        """
        node = Node(key)
        y = None
        x = self.root
        while x != None:
            y = x
            if node.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.leftChild = node
        else:
            y.rightChild = node
        self.treeAVL(node)

    def rotateRight(self,node):
        """
        Eingabe:
            Knoten node in T mit node.left != None
        Resultat:
            node.left nimmt Platz von node ein
            node wird rechtes Kind von node.left
        """
        y = node.leftChild
        if node.parent == None:
            self.root = y
        elif node.parent.leftChild == node:
            node.parent.leftChild = y
        else:
            node.parent.rightChild = y
        y.parent = node.parent
        node.leftChild = y.rightChild
        if node.leftChild != None:
            node.leftChild.parent = node
        y.rightChild = node
        node.parent = y

    def rotateLeft(self,node):
        """
        Eingabe:
            Knoten node in T mit node.right != None
        Resultat:
            node.right nimmt Platz von node ein
            node wird linkes Kind von node.right
        """
        y = node.rightChild
        if node.parent == None:
            self.root = y
        elif node.parent.leftChild == node:
            node.parent.leftChild = y
        else:
            node.parent.rightChild = y
        y.parent = node.parent
        node.rightChild = y.leftChild
        if node.rightChild != None:
            node.rightChild.parent = node
        y.leftChild = node
        node.parent = y

    def treeBalance(self,node):
        """
        Eingabe:
            Knoten node in T
        Ausgabe:
            balance fuer node
        """
        hr = 0
        hl = 0
        if node.leftChild == None:
            hl = -1
        else:
            hl = node.leftChild.height()
        if node.rightChild == None:
            hr = -1
        else:
            hr = node.rightChild.height()
        return hr-hl

    def treePath(self,node):
        """
        Eingabe:
            Knoten node in T
        Ausgabe:
            Pfad von Knoten node bis root
        """
        P = [node]
        while P[-1] != self.root:
            y = P[-1]
            P.append(y.parent)
        return P

    def treeAVL(self,node):
        """
        Eingabe:
            Knoten node in T
        Resultat:
            von node ausgegangen wurde AVL-Eigenschaften erstellt
        """
        P = self.treePath(node)
        for i in range(1,len(P)):
            y = P[i]
            yChild = P[i-1]
            yBalance = self.treeBalance(y)
            yChildBalance = self.treeBalance(yChild)
            if abs(yBalance) == 2:                          # Balance = -2,2
                if y.leftChild == yChild:                   # leftChild
                    if abs(yBalance+yChildBalance) == 3:    # Balance = -2,-1 oder 2,1
                        self.rotateRight(y)
                    else:                                   # Balance = -2,1 oder 2,-1
                        self.rotateLeft(y.leftChild)
                        self.rotateRight(y)
                else:                                       # rightChild
                    if abs(yBalance+yChildBalance) == 3:    # Balance = -2,-1 oder 2,1
                        self.rotateLeft(y)
                    else:                                   # Balance = -2,1 oder 2,-1
                        self.rotateRight(y.rightChild)
                        self.rotateLeft(y)