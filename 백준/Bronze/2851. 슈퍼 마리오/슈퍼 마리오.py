hap = 0
i = 0
num = []
cndi = []

for _ in range(10):
    num.append(int(input()))

while True :
    if i>=len(num):
        break
    

    hap += num[i]

    if hap <= 100 :
        i+=1
        continue
    else : 
        cndi.append(hap)
        cndi.append(hap-num[i])
        break
if len(cndi)==0:
    print(hap)
else :
    if (cndi[0]-100 < 100-cndi[1]):
        print(cndi[0])
    elif (cndi[0]-100 == 100-cndi[1]):
        print(cndi[0])
    else :
        print(cndi[1])



#처음에 10~11행을 잘못 처리했어서 오류가 발생했음
#i가 리스트의 길이를 초과하지 않도록 체크해야하는데 이 부분을 놓침
#근데 사실 없어도 되는거 아닌가 싶긴한데
#일단 저 부분은 숫자를 다 더해도 100이 되지 않는 경우를 고려한 것.


#두 번째 예외처리도 수정한 것.
#cndi에 아무것도 추가되지 않을 경우를 고려해야 함 (다더해도 100이 되지 않는 경우)