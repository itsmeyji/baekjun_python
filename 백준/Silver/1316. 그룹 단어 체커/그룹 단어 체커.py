#1316 그룹 단어 체커

rep = int(input())

Fcount = 0

for k in range(rep):
  text = list(input())
  count = []

  i = 0
  while i < len(text)-1:
    if (text[i] == text[i+1]):
      del text[i+1]
    else:
      i+=1

  for j in range(len(text)):
    num = text.count(text[j])
    if num > 1:
      count.append(num)

  if len(count) == 0:
    Fcount+=1


print(Fcount)