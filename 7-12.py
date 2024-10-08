import math
r = int(input("请输入圆的半径:"))
area = math.pi * r * r
perimeter = 2 * math.pi * r
print(f"周长:{perimeter:.2f},面积:{area:.3f}")