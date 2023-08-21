#5
n = int(input("Number: "))
while True:
    if n <= 1000:
        print(n * 2)
        n = n * 2
    if n > 1000:
        break