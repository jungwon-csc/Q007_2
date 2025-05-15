N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

sum = 0

for i in B:
    if i > A[-1]:
        sum += A[-1]
    else:
        found = False
        temp_max = 0
        for x in A:
            if x < i:
                temp_max = x
                found = True
            else:
                break 
        if found:
            sum += temp_max
print(sum)