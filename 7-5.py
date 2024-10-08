s = input()
# s 20,3
# split
s_list = s.split(",")
# ['20','3']
x = int(s_list[0])
y = int(s_list[1])
product = x * y

print(f"{x}*{y}={product}")
