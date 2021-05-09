# CoMaII - VL02
# MergeSort

def mergeSort(A):
    if len(A) <= 1:
        return(A)
    else:
        return(merge(mergeSort(A[:len(A)//2]),mergeSort(A[len(A)//2:])))

def merge(left , right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    merged.extend(left + right)
    return merged

if __name__ == "__main__":
    A = [1,5,2,4,3]
    print(mergeSort(A))
    print(A)