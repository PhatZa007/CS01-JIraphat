#1
n = int(input("number: "))
for count in range(1,n):
    count += n
    print(count)
print("_______________________________")

#2
n = int(input("num: "))
for number in range(1,11):
    print(n,"x",number,"=",n*number)
print("_______________________________")

#3
n = int(input("num: "))
count = 0
for number in range(1,n+1):
    if number % 2 != 0:
        count += 1
        print(number)

#4
n = int(input("num: "))
for count in range(n+1):
    print(count*"*")
