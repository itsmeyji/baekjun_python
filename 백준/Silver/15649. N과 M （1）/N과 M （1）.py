# 백준15649 N과M
# dfs기반의 백트래킹 기법을 사용하여 특정 순열 구하기
#백트래킹 공부, dfs 활용 ==> 재귀 이용 탐색


n, m = map(int, input().split())

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))        #스택의 길이가 m과 같다면 (한 줄이 다 찾아졌다면)
    return

  for i in range(1, n + 1):
    if i in s:
      continue                  #이 부분이 가지치기 ==> 이미 선택한 숫자는 다시 찾지 않고 넘어가도록 함
    s.append(i)             #dfs를 사용하기 때문에 스택을 이용 -> 스택 push
    f()
    s.pop()                 #스택 pop

f()