a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if 80 <= sum >= 100:
    print("A")
elif 75 <= sum >= 79:
    print("B+")
elif 70 <= sum >= 74:
    print("B")
elif 65 <= sum >= 69:
    print("C+")
elif 60 <= sum >= 64:
    print("C")
elif 55 <= sum >= 59:
    print("D+")
elif 50 <= sum >= 54:
    print("D")
elif 0 <= sum >= 49:
    print("F")