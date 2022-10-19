x1 = int(input())
x2 = int(input())
x3 = int(input())

D = (x2 ** 2) - (4 * x1* x3)
if D < 0:
  print("нет решений")
else:
  if x2 > 0:
    x3 = x2 - x2 - x2
    xf1 = ((x3) + (D ** 0.5)) / (2 * x1)
    xf2 = ((x3) - (D ** 0.5)) / (2 * x1)
  elif x2 < 0:
    xf1 = ((x2) + (D ** 0.5)) / (2 * x1)
    xf2 = ((x2) - (D ** 0.5)) / (2 * x1)
print(f"Ответ x1 и x2 {xf1}, {xf2}")