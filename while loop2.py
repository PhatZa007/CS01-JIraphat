#2
b = 0
while True:
    num = int(input("Number: "))
    print(b + num)
    b = b + num
    if b > 100:
        break 