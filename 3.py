from math import sqrt, exp, cos, sin
a, x, y = input().split()
a = int(a)
x = float(x)
y = float(y)

tt = sqrt(y ** 2 + exp(x) + sqrt(exp(x) + (a) / (x ** 2 + 2)) + (cos(x) ** 2) / (sin(x ** 2)) + cos(x) ** 3
print("%.2f" % tt)