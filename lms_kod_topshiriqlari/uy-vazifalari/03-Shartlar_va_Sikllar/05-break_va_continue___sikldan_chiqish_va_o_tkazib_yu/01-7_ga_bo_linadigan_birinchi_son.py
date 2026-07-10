n = int(input())
topildi = False
i = 0
while i < n:
    son = int(input())
    if son % 7 == 0:
        print(son)
        topildi = True
        break
    i += 1
if not topildi:
    print("yo'q")