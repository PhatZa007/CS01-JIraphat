#3
b = 0
while True:
    num = int(input("Number: "))
    if num != 0:
        print(b + 1)
        b = b + 1
    elif num == 0:
        print(b)
        break