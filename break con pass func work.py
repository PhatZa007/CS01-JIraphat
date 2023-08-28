#1
while True:
    n = int(input("num: "))
    if n == -1:
        break
print("stoped")
print("_____________________________________")

#2
b = 0
for i in range(10):
    n = 0 ; n = int(input("Number: "))
    if n < 0:
        continue
    else:
     b = b + n
print(b)
print("_____________________________________")

#3
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if y < x > z:
    print(x)
elif x < y > z:
    print(y)
elif x < z > y:
    print(z)
else:
    pass
print("_____________________________________")

#4
def add(n1 , n2):
    sum = n1 + n2
    print("Sum: " , sum)

add(5 , 3)
print("_____________________________________")