soni = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n < 2:
        continue
    tub = True
    i = 2
    while i < n:
        if n % i == 0:
            tub = False
            break
        i += 1
    if tub:
        soni += 1
print(soni)