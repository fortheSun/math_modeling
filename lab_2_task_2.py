b1 = int(input())
q = int(input())
n = int(input())

for i in range(1, n):
  b = b1 * q ** (n-1)
  print(b)