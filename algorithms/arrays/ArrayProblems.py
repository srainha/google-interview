
def windowAverages(arr, windowSize=1, exclusive=False):
    averages = []
    stepSize = windowSize if exclusive else 1
    for i in range(0, len(arr), stepSize):
        upTo = min(len(arr), i + windowSize)
        averages.append(sum(arr[i:upTo])/(upTo - i))
    return averages

def binarySearchIt(arr, val):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = low + ((high - low) // 2)
        midValue = arr[mid]
        if (val == midValue):
            return mid
        elif (midValue < val):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# average = O(nlogn), worst = O(n2) 
def quickSort(arr):
    less = []
    equal = []
    greater = []

    if (len(arr) <= 1): return arr
    pivot = arr[0]
    for x in arr:
        if x < pivot:
            less.append(x)
        elif pivot < x:
            greater.append(x)
        else:
            equal.append(x)
    return quickSort(less) + equal + quickSort(greater)

# top down
# average=O(nlogn)
def mergeSort(arr):
    if (len(arr) <= 1):
        return arr
    left = arr[:int(len(arr)/2)]
    right = arr[int(len(arr)/2):]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while (left != [] and right != []):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while (left != []):
        result.append(left.pop(0))
    while (right != []):
        result.append(right.pop(0))
    return result

def rotateArray(arr, n):
    return (arr[(len(arr)  - n):]) + (arr[:(len(arr) - n)])


def rotate_array(arr, n):
    n = n % len(arr)
    # rule: i swap (i + len(arr) -1) % len(arr)
    for i in range(len(arr)//2):
        new_i = (i + len(arr) - n) % len(arr)
        temp = arr[i]
        arr[i] = arr[new_i]
        arr[new_i] = temp
    return arr

def find_dups(arr):
    dups = set()
    arr_set = set()
    for i in arr:
        if (i in arr_set):
            dups.add(i)
        else:
            arr_set.add(i)
    return dups(i)

def remove_dups(arr):
    return list(set(arr))


