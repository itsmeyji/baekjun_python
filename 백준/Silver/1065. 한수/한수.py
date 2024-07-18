#한수

def hansu(k):
    if k < 100:
        return True
    else :
        n = list(map(int, str(k)))
        cm = n[1]-n[0]
        for i in range(1, len(n)-1):
            if n[i+1] - n[i] != cm:
                return False
        return True
    
n = int(input())
cnt = 0

for j in range(1, n+1):
    if hansu(j):
        cnt+=1


print(cnt)