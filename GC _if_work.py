#1
age = int(input("Your age: "))
if age >= 18:
    print("You can entry.")
else:
    print("You can not entry.")

#2
x = int(input("Number: "))
if x < 0:
    print("Negative number")
elif x > 0:
    print("Positive number")
elif x == 0:
    print("Zero number")

#3
x = int(input("Enter age: "))
if 18 <= x <= 25:
    print("อายุ x อยู่ในช่วง 18-25")
else:
    print("อายุ x ไม่อยู่ในช่วง 18-25")