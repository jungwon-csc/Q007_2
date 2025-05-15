N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

sum = 0

for i in B:
    if i > A[-1]:
        sum += A[-1]
    else:
        temp_max = 0
        for x in A:
            if x <= i:
                temp_max = x
            else:
                break 
        sum += temp_max
print(sum)