
total_points = float(input("Total Points Possible: "))
points_achieved = float(input("Points Student Achieved: "))
total = (points_achieved/total_points)
if 1 > total > 0.89:
    print("A")
elif 0.88 > total > 0.76:
    print("B")
elif 0.76 > total > 0.61:
    print("C")
elif 0.60 > total > 0.51:
    print("D")
elif 0.5 > total:
    print("F")



