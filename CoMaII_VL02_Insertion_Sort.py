# CoMaII - VL02
# InsertionSort

def insertionSort(A):
    # Sort the given list A
    n = len(A)
    for i in range(1,n):
        s = A[i]
        k = i
        while k > 0 and s < A[k-1]:
            A[k] = A[k-1]
            k -= 1
        A[k] = s

if __name__ == "__main__":
    A = [1,4,2,3]
    insertionSort(A)
    print(A)