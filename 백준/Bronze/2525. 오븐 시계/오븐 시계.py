h, m = map(int, input().split())
n = int(input())

num = m + n

h += num // 60
num = num % 60

if h >= 24 : h = h - 24
print(h, num)