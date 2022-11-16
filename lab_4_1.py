def num(a):
  sum = 0
  for i in a:
    sum += i
  return sum / len(a)
a = (1, 3, 4)

print(num(a))