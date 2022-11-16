def num(a, n):
  x = 1
  if n > 1:
    for i in range (n):
      x *= a
      print(x)
  elif n == 0:
    print(x)
  else:
    for i in range(n):
      x *= a
      x = 1/x
      print(x)
num(2, 8)