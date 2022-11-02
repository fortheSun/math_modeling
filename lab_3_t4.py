import numpy as np
N = 5
M = 4

dich = np.zeros((N,M))

for n in range(N):
  for m in range(M):
    x1 = np.sin(N * (n + 1) + M * (m + 1))  
    if x1 < 0:
      dich[n,m] = 0
    else:
      dich[n,m] = x1

print(dich)


print()


new_dich = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    new_dich[i, j] = dich[i, j]

    
new_dich[::, 0], new_dich[::, 1] = dich[::, 1], dich[::, 0]
print(dich)
print()
print(new_dich)