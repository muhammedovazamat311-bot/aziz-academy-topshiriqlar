n = int(input())
mx = int(input())
pos = 1
for i in range(2, n + 1):
    x = int(input())
    if x > mx:
        mx = x
        pos = i
print(pos)