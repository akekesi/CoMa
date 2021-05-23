# CoMaII - VL05
# Binaere Suchbaeume

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

class BinTree:
    def __init__(self):
        self.root = None

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

    def treeInsert(self,node):
        """
        Eingabe:
            Zeiger node auf neues Objekt mit node.left = node.right = None
        Resultat:
            Modifikation von T, sodass node neuer Baumknoten ist
        """
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

    def insert(self,k):
        """
        Eingabe:
            Key k (noch keine "Node" Klasse)
        Resultat:
            Modifikation von T, sodass k als "Node" Klasse neuer Baumknoten ist
        """
        if self.root == None:
            self.root = Node(k)
        else:
            self.insert_deep(self.root,k)

    def insert_deep(self,node,k):
        """
        Hilfsfunktion fuer insert(k)
        """
        if k < node.key:
            if node.leftChild == None:
                node.leftChild = Node(k,parent=node)
            else:
                self.insert_deep(node.leftChild,k)
        else:
            if node.rightChild == None:
                node.rightChild = Node(k,parent=node)
            else:
                self.insert_deep(node.rightChild,k)

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



if __name__ == "__main__":
    N1 = Node(7)
    N2 = Node(4,parent=N1)
    N3 = Node(10,parent=N1)
    N1.leftChild = N2
    N1.rightChild = N3
    print(N1.leftChild.key)
    print(N1.rightChild.key)
    print(N1)
    print(N2)

    print("---")
    T = BinTree()
    T.insert(7)
    T.insert(4)
    T.insert(10)
    T.insert(5)
    T.insert(6)
    print(T.root)
    print(T)
    print(T.root.leftChild)
    print(T.root.height())
    print(T.root.keys())
    T.treeWalkInorder(T.root)
    a = T.treeSearch(10,T.root)
    print(type(a))
    print(T.treeSearch(10,a))
    print(T.treeSearch(10,T.root))
    print(T.treeSearch(99,T.root))
    a = T.treeSearch_it(10,T.root)
    print(type(a))
    print(T.treeSearch_it(10,a))
    print(T.treeSearch_it(10,T.root))
    print(T.treeSearch_it(99,T.root))

    print("---")
    print(T.treeMin(T.root))
    print(T.treeMax(T.root))
    print(T.treeSuccessor(T.root))
    print(T.treeSuccessor(T.root.leftChild))
    print(T.treeSuccessor(T.root.leftChild.rightChild))
    print(T.treeSuccessor(T.root.leftChild.rightChild.rightChild))

    print("---")
    print(T.treePredecessor(T.root))
    print(T.treePredecessor(T.root.leftChild))
    print(T.treePredecessor(T.root.leftChild.rightChild))
    print(T.treePredecessor(T.root.leftChild.rightChild.rightChild))

    print("---")
    print(T.root)
    T.treeInsert(Node(1))
    print(T.root)

    print("---")
    T2 = BinTree()
    T2.treeInsert(Node(7))
    T2.treeInsert(Node(4))
    T2.treeInsert(Node(10))
    T2.treeInsert(Node(5))
    T2.treeInsert(Node(6))
    T2.treeInsert(Node(1))
    print(T2.root)
    T2.rotateRight(T2.treeSearch(7,T2.root))
    print(T2.root)
    T2.rotateLeft(T2.treeSearch(4,T2.root))
    print(T2.root)