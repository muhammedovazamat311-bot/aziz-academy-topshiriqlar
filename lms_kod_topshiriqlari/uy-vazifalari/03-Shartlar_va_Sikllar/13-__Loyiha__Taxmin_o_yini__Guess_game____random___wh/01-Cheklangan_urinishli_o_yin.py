x = int(input())
n = int(input())
found = False
for _ in range(n):
    t = int(input())
    if t < x:
        print("KICHIK")
    elif t > x:
        print("KATTA")
    else:
        print("TOPDINGIZ")
        found = True
        break
if not found:
    print("YUTQAZDINGIZ")