num = input("")
count = 0

while len(num) > 1:
    temp = 0
    for i in range(len(num)):
        temp += int(num[i])
    count += 1
    num = str(temp)

print(count)

if int(num) % 3 == 0:
    print("YES")
else:
    print("NO")
