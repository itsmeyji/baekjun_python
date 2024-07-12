#팰린드롬수
while True :
  pali = input()

  if pali =="0" :
    break
  
  else : 
    Rpali = pali[::-1]
    if pali == Rpali:
      print("yes")
    else:
      print("no")
