sum1 = int(input())
n = int(input())
sum2 = 0

for i in range(n):
    a, b = map(int, input().split())
    sum2 += a * b

if sum1 == sum2:
    print("Yes")
else:
    print("No")