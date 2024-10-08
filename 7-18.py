import math

p = float(input())

if p == 0 or p == 1:
    entropy = 0.0
else:
    entropy = -p * math.log2(p) - (1 - p) * math.log2(1 - p)

print(f"{entropy:.2f}")