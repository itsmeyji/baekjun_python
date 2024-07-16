#3040 백설 공주와 일곱 난쟁이

dwf = []
for i in range(9):
  d = int(input())
  dwf.append(d)

for i in range(0, len((dwf))):
  for j in range(0, len(dwf)):
    if (sum(dwf) - dwf[i] - dwf[j] == 100 and i!=j) :
      fake_a = i
      fake_b = j
      break
    else :
      continue
del dwf[fake_a]
del dwf[fake_b]

for i in range(7):
  print(dwf[i])