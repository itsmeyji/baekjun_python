def mini(a,b):

  a = str(a)
  a = a.replace('6','5')
  mina=int(a)

  b = str(b)
  b = b.replace('6','5')
  minb=int(b)

  minab = mina + minb

  return minab

def maxi(a,b):
  a = str(a)
  a = a.replace('5','6')
  maxa=int(a)

  b = str(b)
  b = b.replace('5','6')
  maxb=int(b)

  maxab = maxa + maxb

  return maxab

#print
a, b = map(int, input().split())
print(mini(a,b), maxi(a,b))