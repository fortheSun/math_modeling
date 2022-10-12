x = int(input())
y = int(input())

if y == 0:
  print("ошибка")
elif x % y == 0:
  print("без остатка")
elif x % y != 0:
  print(x // y, "остаток", x % y)