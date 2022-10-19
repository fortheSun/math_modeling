f1 = f2 = 1
n = int(input())

for i in range(n - 2):
  f3 = f1 + f2
  print(f3)
  f1 = f2
  f2 = f3