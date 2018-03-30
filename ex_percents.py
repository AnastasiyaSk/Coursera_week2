p = int(input())
x = int(input())
y = int(input())
t = x * 100 + y
year = p * 0.01 * t + t
print(int(year // 100), int(year % 100))
