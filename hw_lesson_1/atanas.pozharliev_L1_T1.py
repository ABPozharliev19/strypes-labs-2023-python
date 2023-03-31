import sys
import cmath

equation = sys.argv[1:]

a = int(equation[0])
b = int(equation[1])
c = int(equation[2])

D = b ** 2 - 4 * a * c

solution = ""

if a != 0:
    if D >= 0:
        x1 = (-b - cmath.sqrt(D)) / (2*a)
        x2 = (-b + cmath.sqrt(D)) / (2*a)

        solution = f"{x1.real} | {x2.real}"
    else:
        solution = "no real roots"
else:
    if b != 0:
        x1 = -c / b

        solution = str(x1)
    else:
        solution = "special case"

print(solution)
