n = int(input())
i = 0
yigindi = 0
while i < n:
    son = int(input())
    i += 1
    if son <= 0:
        continue
    yigindi += son
print(yigindi)