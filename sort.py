#sort algorithm implement

def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selection_sort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1, len(l)):
            if(l[j] < l[min]):
                min = j
        if(min != i):
            l[i], l[min] = l[min], l[i]
    return l
    
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':

    l = [5, 6, 8, 1]
    #print(bubble_sort(l))
    #print(selection_sort(l))
    mergeSort(l)
    print(l)
