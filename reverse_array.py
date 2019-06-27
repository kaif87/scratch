arr = [1, 2, 3, 4, 5, 6, 7]


first = 0
last = len(arr) - 1

while first < last:
    (arr[first], arr[last]) = (arr[last], arr[first])
    first += 1
    last -= 1


arr