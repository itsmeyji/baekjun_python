def same(num):
    Rnum = int(str(num)[::-1])
    temp = num + Rnum
    temp = str(temp)
    half = len(temp) // 2

    for i in range(half):
        if temp[i] != temp[-(i + 1)]:
            return "NO"
    return "YES"

retry = int(input())
for _ in range(retry):
  num = int(input())
  print(same(num))