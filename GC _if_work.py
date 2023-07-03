#1
age = int(input("Your age: "))
if age >= 18:
    print("You can entry.")
else:
    print("You can not entry.")
print("________________________________________")

#2
x = int(input("Number: "))
if x < 0:
    print("Negative number")
elif x > 0:
    print("Positive number")
elif x == 0:
    print("Zero number")
print("________________________________________")

#3
x = int(input("Enter age: "))
if 18 <= x <= 25:
    print("อายุ x อยู่ในช่วง 18-25")
else:
    print("อายุ x ไม่อยู่ในช่วง 18-25")
print("________________________________________")

#4
x = int(input("Number: "))
if x < 10:
    print("เป็นเลขหลักเดียว")
elif x >= 10:
    print("เป็นเลขสองหลัก")
print("________________________________________")

#5
x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))
if x == y == z:
    print("x, y และ z เท่ากัน")
else:
    print("x, y และ z ไม่เท่ากัน")
print("________________________________________")
