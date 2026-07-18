son = int(input())
urunish = 0
while True:
    taxmin = int(input())
    urunish += 1
    if taxmin > son:
        print("KATTA")
    elif taxmin < son:
        print("KICHIK")
    else:
        print("TOPDINGIZ")
        break
print("Urinishlar:" , urunish)