n = int(input())
for _ in range(n):
  a,b = map(str, input().split())

  if sorted(str(a)) == sorted(str(b)):
    print(a, "&", b, "are anagrams.")
  else:
    print(a, "&", b, "are NOT anagrams.")

