# CoMaII - PA_05 - AVL-Baum
# Attila Kekesi + Vorlesungsmaterial
# not for comajudge: Benennung tree...

class Node:
    def __init__(self,key,leftChild=None,rightChild=None,parent=None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def __str__(self):
        return str(self.struktur())

    def struktur(self):
        """
        Hilfsfunktion fuer __str__
        """
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

class AVLTree:
    def __init__(self,key):
        self.key = key
        self.root = Node(key)

    def __str__(self):
        return str(self.root.struktur())

    def treeWalkInorder(self,node):
        """
        Eingabe:
            Zeiger node auf Baumknoten
        Ausgabe:
            Sortierte Liste der Schluessel des Teilbaums unter node
        """
        if node != None:
            self.treeWalkInorder(node.leftChild)
            print(node.key)
            self.treeWalkInorder(node.rightChild)

    def treeInsert(self,key):
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

    def treeSearch(self,k,node=None):
        """
        Tree-Search - Rekursiv
        Eingabe:
            Zeiger node auf Baumknoten, Schluesselwert k
        Ausgabe:
            Zeiger y auf Knoten unterhalb von node mit y.key = k
            oder None, falls kein solcher existiert
        """
        if node == None or k == node.key:
            return node
        if k < node.key:
            return self.treeSearch(k,node.leftChild)
        else:
            return self.treeSearch(k,node.rightChild)

    def treeSearch_it(self,k,node=None):
        """
        Tree-Search - Iterativ
        Eingabe:
            Zeiger node auf Baumknoten, Schluesselwert k
        Ausgabe:
            Zeiger y auf Knoten unterhalb von node mit y.key = k
            oder None, falls kein solcher existiert
        """
        while node != None or k != node.key:
            if k < node.key:
                node = node.leftChild
            else:
                node = node.rightChild
            return node

    def treeMin(self,node):
        """
        Eingabe:
            Eingabe: Zeiger node auf Baumknoten
        Ausgabe:
            Zeiger y auf Knoten unterhalb von node mit y.key minimal
        """
        while node.leftChild != None:
            node = node.leftChild
        return node

    def treeMax(self,node):
        """
        Eingabe:
            Eingabe: Zeiger node auf Baumknoten
        Ausgabe:
            Zeiger y auf Knoten unterhalb von node mit y.key maximal
        """
        while node.rightChild != None:
            node = node.rightChild
        return node

    def treeSuccessor(self,node):
        """
        Eingabe:
            Zeiger node auf Baumknoten
        Ausgabe:
            Zeiger y auf Knoten nach node in inorder-Reihenfolge
            Zeiger y auf Knoten mit naechstgroestem key
        """
        if node.rightChild != None:
            return self.treeMin(node.rightChild)
        y = node.parent
        while y != None and node == y.rightChild:
            node = y
            y = y.parent
        return y

    def treePredecessor(self,node):
        """
        Eingabe:
            Zeiger node auf Baumknoten
        Ausgabe:
            Zeiger y auf Knoten nach node in preorder-Reihenfolge
            Zeiger y auf Knoten mit naechstkleinstem key
        """
        if node.leftChild != None:
            return self.treeMax(node.leftChild)
        y = node.parent
        while y != None and node == y.leftChild:
            node = y
            y = y.parent
        return y

    def treeDelet(self,node):
        """
        Eingabe:
            Zeiger node auf neues Objekt mit node.left = node.right = None
        Resultat:
            Modifikation von T, sodass node neuer Baumknoten ist
        """
        if node.leftChild == None:
            self.transplant(node,node.rightChild)
        elif node.rightChild == None:
            self.transplant(node,node.leftChild)
        else:
            y = self.treeMin(node.rightChild)
            if y.parent != node:
                self.transplant(y,y.rightChild)
                y.rightChild = node.rightChild
                y.rightChild.parent = y
            self.transplant(node,y)
            y.leftChild = node.leftChild
            y.leftChild.parent = y
        
    def transplant(self,node1,node2=None):
        """
        Eingabe:
            Knoten node1 in T
            Knoten node2 oder node2 = None
        Resultat:
            Ersetze Teilbaum unter node1 durch Teilbaum unter node2
        """
        if node1.parent == None:
            self.root = node2
        elif node1 == node1.parent.leftChild:
            node1.parent.leftChild = node2
        else:
            node1.parent.rightChild = node2
        if node2 != None:
            node2.parent = node1.parent

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
        K = [node.key]
        while P[-1] != self.root:
            y = P[-1]
            P.append(y.parent)
            K.append(y.parent.key)
        return P,K

    def treeAVL(self,node):
        """
        Eingabe:
            Knoten node in T
        Resultat:
            von node ausgegangen wurde AVL-Eigenschaften erstellt
        """
        P,_ = self.treePath(node)
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

if __name__ == "__main__":
    T = AVLTree(7)
    T.treeInsert(4)
    T.treeInsert(10)
    T.treeInsert(5)
    T.treeInsert(6)
    print(T.root)

    print(T.treeBalance(T.treeSearch(7,T.root)))
    print(T.treeBalance(T.treeSearch(10,T.root)))
    print(T.treeBalance(T.treeSearch(5,T.root)))
    print(T.treePath(T.treeSearch(6,T.root)))

    T = AVLTree(2)
    print(T.root)
    T.treeInsert(3)
    print(T.root)
    T.treeInsert(4)
    print(T.root)
    T.treeInsert(7)
    print(T.root)
    T.treeInsert(10)
    print(T.root)
    T.treeInsert(8)
    print(T.root)

    T = AVLTree(17)
    T.treeInsert(11)
    T.treeInsert(10)
    T.treeInsert(13)
    T.treeInsert(8)
    T.treeInsert(4)
    T.treeInsert(7)
    T.treeInsert(9)
    T.treeInsert(7)
    T.treeInsert(3)
    T.treeInsert(3)
    print(T.root)
