def rotate_primitive(arr, n):
    """
    Rotation using Python's built in list slicing
    """
    part1 = arr[0:n]
    part2 = arr[n:-1]
    arr = part2 + part1
    return arr

def rotate_one(arr):
    """
    Rotation by one elem at a time
    """
    if not arr:
        return []
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr) - 1] = temp
    return arr

def rotate(arr, n):
    """
    Rotate by one N times
    """
    for x in range(n):
        rotate_one(arr)
    return arr

def rotate_rev(arr, n):
    """
    Reverse array from one to n, get ArB
    then reverse array from n to len, get ArBr
    reverse whole array, get BA
    """
    print(arr[0:n-1])
    print(arr[n: len(arr) -1])
    reverse(arr, 0, n - 1)
    reverse(arr, n, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr

def reverse(arr, begin, end):
    """
    Reverse an array in place
    """
    if begin > end:
        return arr
    else:
        while(begin < end):
            temp = arr[begin]
            arr[begin] = arr[end]
            arr[end] = temp
            begin += 1
            end -= 1
    return arr

a = [1,2,3,4,5,6,7,8,9]
print(rotate_rev(a, 3))
