stn = int(input())
cnt = 0

while stn :
    cnt += 1
    if stn < 3 : 
        stn -= 1
    else :
        stn -= 3

if cnt % 2 ==1 :
    print("CY")
elif cnt %2 ==0 :
    print("SK")
