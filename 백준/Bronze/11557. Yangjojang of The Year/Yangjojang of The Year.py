T = int(input())

for i in range(T):
    alcohol = {}
    N = int(input())
    for _ in range(N) :
        name, amt  = map(str, input().split())
        amt = int(amt)
        alcohol[name] = amt

    win = dict(sorted(alcohol.items(), key = lambda item: item[1], reverse = True))
    #alcohol.items() 를 호출해 2차원 리스트의 형태로 나타냄
    #그리고 나서 sorted()함수로 리스트 정렬
    #여기서 정렬 기준 item은 키 또는 값을 명시
    #값을 기준으로 내림차순 정렬한 후 다시 딕셔너리로 변환
    
    winner = list(win.keys())[0]
    #win.keys는 딕셔너리의 모든 키 반환
    #list()함수로 키들을 리스트로 변환
    #[0]으로 첫 번째 요소 가져옴
    
    print(winner)
