#Python Program to implement Selection Sort

def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
n = len(arr)
print(n)
print("The Selection sort of the given array is:",selection_sort(arr, n))