successful = True
for number in range(3):
    print("Attemp")
    if successful:
        print("Successful")
        break
else:
    print("Attemp 3 time and failed")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even number")

A = int(input())
for i in range (100):
    print(A+i)