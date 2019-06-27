arr = [1, 6, 2, 1, 6, 1]
k = 2

freq = dict()

for i in arr:
    if i in freq.keys():
        freq[i] += 1
    else:
        freq[i] = 1

temp = [None] * len(arr)

for k, v in freq.items():
    if temp[v]:
        temp[v].append(k)
    else:
        temp[v] = [k]

result = []

for i in range(1, len(temp)):
    if temp[-i]:
        result.extend(temp[-i])

result[:k]