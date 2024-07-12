std = []

for _ in range(28):
  n = int(input())
  std.append(n)

std.sort()
for i in range(1,31):
    if i not in std:
      print(i)