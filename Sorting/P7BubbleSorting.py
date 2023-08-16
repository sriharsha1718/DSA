#Python Program to implement Bubble Sort

def bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped==False:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 0]
n = len(arr)
print(n)
print("The sorted array using bubble sort is: ", bubble_sort(arr, n))