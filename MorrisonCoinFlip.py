import random
coin = 0
tails = 0
heads = 0
while coin <= 100:
   flip = random.randint(1,2)
   coin+=1
   if flip == 1:
      heads+=1
   else:
      tails+=1
   if coin == 100:
      print("Heads =", heads, "Tails =", tails)
      