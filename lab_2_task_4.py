x = y = 1

n = int(input())

print(x, y, end=' ')

for i in range(1, n):
  x, y = y, x + y
  print(y, end=' ')

print()