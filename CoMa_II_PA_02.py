# CoMaII - PA_02 - MaxHeap
# Attila Kekesi

import math

class MaxHeap():
    def __init__(self,keys):
        self.keys = keys
        self.maxHeapifyIter(self.keys)

    def maxHeapifyIter(self,A,i=None):
        if i == None or i == -1:
            i = int(len(A)/2)
        for i in range(i,-1,-1):
            self.maxHeapify(A,i)

    def maxHeapify(self,A,i):
        l = 2*i+1   # index left
        r = 2*i+2   # index right
        n = len(A)  # index last+1
        largest = i # index largest
        if l < n and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < n and A[r] > A[largest]:
            largest = r
        if largest != i:
            tmp = A[largest]
            A[largest] = A[i]
            A[i] = tmp
            self.maxHeapify(A,largest)

    def __str__(self):
        return f'{self.keys}'

    def maxHeapPrint(self):
        n = int(math.log(len(self.keys),2))
        T = []
        for i in range(n+1):
            t = []
            for j in range(2**i):
                if j == 0:
                    t.append(2**(n-i))
                else:
                    t.append(t[-1]+2**(n-i+1))
            T.append(t)
        P = []
        S = 0
        for t in T:
            s = 0
            p = []
            for i in range(2**(n+1)):
                if s < len(t) and i == t[s]-1 and S < len(self.keys):
                    p.append(str(self.keys[S]))
                    s += 1
                    S += 1
                else:
                    p.append("_")
            P.append(p)
        for p in P:
            print(p)

    def maximum(self):
        return self.keys[0]

    def extractMax(self):
        m = self.keys[0]
        self.keys[0] = self.keys.pop()
        self.maxHeapify(self.keys,0)

        return m

    def increaseKey(self,i,k):
        if self.keys[i] < k:
            self.keys[i] = k
            if i > 0:
                self.maxHeapifyIter(self.keys,i)
        else:
            return print(f'k too small')

    def insert(self,k):
        self.keys.append(k)
        self.maxHeapifyIter(self.keys)

    def heapSort(self):
        n = len(self.keys)-1
        while n >= 1:
            m = self.keys[0]
            self.keys[0] = self.keys[n]
            self.keys[n] = m
            A = self.keys[:n]
            self.maxHeapify(A,0)
            self.keys[:n] = A
            n -= 1
        self.keys.reverse()

if __name__ == "__main__":
    #L = [5,4,3,6,7]
    L = [12,122,133,144,111,99,54,51,32,30,33,10,11]
    print(L)
    H = MaxHeap(L)
    print(H)
    print(H.maximum())
    print(H)
    print(H.extractMax())
    print(H)
    H.increaseKey(-1,222)
    print(H)
    H.increaseKey(1,0)
    print(H)
    H.insert(0)
    print(H)
    H.insert(7)
    print(H)
    H.heapSort()
    print(H)
    print(L)
    L = [4,1,3,2,0,9,5,6,8,7]
    H = MaxHeap(L)
    H.maxHeapPrint()