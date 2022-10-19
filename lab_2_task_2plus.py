x = int(input())
y = int(input())
z = int(input())

if x + y < c z or z + y < x or x + z < y:
  print("Несуществует")
  if x == y == z:
    print("Равносторонний")
  elif x != y != z:
    print("Произвольный")
  elif y or z == x:
    print("Равнобедренный")