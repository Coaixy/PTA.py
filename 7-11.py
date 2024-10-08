a = input()
b = input()
# a = Tom
# 0 1 2
# 0 1 2
# Tom ['T','o','m']
# &
result = ''
for i in range(len(a)):
    result = result + a[i] + b
print(result[:-1])