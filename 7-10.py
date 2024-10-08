import math

pi = math.pi
a, b, c = map(int, input().split(" "))
d, e, f = map(str, input().split(" "))
# pi/2
v1 = a * b * c / 6
v2 = 1 - math.cos(eval(d)) ** 2 - math.cos(eval(e)) ** 2 - math.cos(eval(f)) ** 2 + 2 * math.cos(eval(d)) * math.cos(
    eval(
        e)) * math.cos(eval(f))
v3 = math.sqrt(v2)
v = v1 * v3
print(f"{v:.2f}")
