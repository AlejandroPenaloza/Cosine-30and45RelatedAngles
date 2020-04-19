#THIS IS Cosine-30and45RelatedAngles.py, where you can get the value of the cosine of a given angle related from
#30 degrees - pi/6 and 45 degrees - pi/4
print("\nCOSINE OF PI/6 (30 degrees) AND PI/4 (45 degrees) RELATED ANGLES\n")

angle = float(input("Input your angle in degrees\n"))
cosine_inner_signs = []
var_angle = angle

if var_angle == 30.0:
    print("Cosine = square root(3)/2")
elif var_angle == 45.0:
    print("Cosine = 1/2")
else:
    while True:
        if var_angle == 30.0:
            print("Cosine = ", "".join(cosine_inner_signs), 3)
            break
        elif var_angle == 45.0:
            print("Cosine = ", "".join(cosine_inner_signs), 2)
            break
        elif var_angle != 15.0 and str(var_angle).split(".")[1] == "0":
            print("Angle not related")
            break
        elif var_angle < 45.0:
            var_angle *= 2
            cosine_inner_signs.append("+")
        else:
            var_angle = 2*(90.0 - var_angle)
            cosine_inner_signs.append("-")
