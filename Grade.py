score_work = float(input("กรุณาใส่คะแนนของคุณ 1: "))
score_mid = float(input("กรุณาใส่คะแนนของคุณ 2: "))
score_final = float(input("กรุณาใส่คะแนนของคุณ 3: "))
score = score_work+score_mid+score_final
if score >= 101:
    grade = "Why your score is more than 100? Are you cheating."
elif score >= 80:
    grade = "A"
elif score >= 75:
    grade = "B+"
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = "C+"
elif score >= 60:
    grade = "C"
elif score >= 55:
    grade = "D+"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print("เกรดของคุณคือ:", grade)