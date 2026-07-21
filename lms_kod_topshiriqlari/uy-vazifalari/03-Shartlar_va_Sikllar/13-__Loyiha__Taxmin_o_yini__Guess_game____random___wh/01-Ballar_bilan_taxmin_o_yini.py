yashirin_son = int(input())
ball = 100
while True:
    taxmin = int(input())
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
        print(f"Ball: {ball}")
        break
    elif taxmin > yashirin_son:
        print("KATTA")
        ball = max(0, ball - 10)
    else:
        print("KICHIK")
        ball = max(0, ball - 10)