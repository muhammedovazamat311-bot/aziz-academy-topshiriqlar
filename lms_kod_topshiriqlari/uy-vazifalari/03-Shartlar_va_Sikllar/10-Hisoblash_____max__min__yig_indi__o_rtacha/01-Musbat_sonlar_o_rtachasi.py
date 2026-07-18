n = int(input())
s = 0
cnt = 0
for _ in range(n):
    x = int(input())
    if x > 0:
        s += x
        cnt += 1
if cnt == 0 :
    print(0)
else:
    print(s // cnt)