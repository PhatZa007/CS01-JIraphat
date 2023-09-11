while True:
    num = str(input())
    if num == "W":
        print("ติด ร")
        break
    else:
        num2 = int(input())
        num3 = int(input())
        num4 = int(input())
        sum = int(num) + num2 + num3 + num4
        if sum >= 80:
            print("เกรด 4")
            break
        elif sum >= 75:
            print("เกรด 3.5")
            break
        elif sum >= 70:
            print("เกรด 3")
            break
        elif sum >= 65:
            print("เกรด 2.5")
            break
        elif sum >= 60:
            print("เกรด 2")
            break
        elif sum >= 55:
            print("เกรด 1.5")
            break
        elif sum >= 50:
            print("เกรด 1")
            break
        elif sum >= 0:
            print("เกรด 0")
            break  