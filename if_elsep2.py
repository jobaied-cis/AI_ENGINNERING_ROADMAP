mark = int(input("Enter your mark: "))
attendance = int(input("Enter your attendance: "))
if mark >= 80 and attendance >= 75:
    print("A+")
elif mark >= 70 and attendance >= 65:
    print("A")
elif mark >= 60 and attendance >= 55:
    print("B")
elif mark >= 50 and attendance >= 45:
    print("C")
elif mark < 50 and attendance < 45:
    print("Fail")
else:
    print("You have not met the attendance requirement for your mark.")