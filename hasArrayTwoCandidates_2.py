# solution 2
# sorting and two pointer

# Top 5 sorting alth

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped =True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i -1, i)
                swapped = True

    return arr


def selection_sort(arr):
    
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # break and do the final swap
        arr[pos] = cursor
    
    return arr

def insertion_sort():
    pass

def merge_sort():
    # the last array split
    

def quick_sort():
    pass

def twoSum(array, sum):
    pass