# from math import log, fabs, sqrt, cos
# x, y = input().split()
# x = int(x)
# y = int(y)

# z = log(fabs((x + y) ** 2 + sqrt(fabs(y) + 2) - (x - (x * y) / ((x ** 2) / (2) - 5)))) + (cos(x + y) ** 2) / ((x + y) ** 1 / 3)
# print("%.2f" % z)




from math import sqrt
def mean(a, b):
    x = (a + b) / 2
    y = sqrt(a * b)
    print(x, y)
A, B, C, D = map(float, input().split())
mean(A, B)
mean(A, C)
mean(A, D)