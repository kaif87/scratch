# max area under historgram
hist = [1, 2, 3, 4, 5, 3, 3, 2]
stack = []
i = 0
anchor = 0
max_area = 0
while i < len(hist):
    if len(stack) == 0 or hist[i] > hist[stack[-1]]:
        stack.append(i)
        i+=1
    else:
        anchor = i - 1
        curr_pos = stack.pop()
        area = hist[curr_pos] * (anchor - (0 if len(stack) == 0 else stack[-1]))
        if max_area < area:
            max_area = area

while len(stack) > 0:
    anchor = i - 1
    curr_pos = stack.pop()
    area = hist[curr_pos] * (anchor - (0 if len(stack) == 0 else stack[-1]))
    if max_area < area:
        max_area = area

