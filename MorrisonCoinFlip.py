import random
coin = 0
tails = 0
heads = 0
q1 =  ''
q2 =  ''
while coin <= 100:
   flip = random.randint(1,2)
   coin+=1
   if flip == 1:
      heads+=1
   else:
      tails+=1
   if coin == 100:
      print("What are the two choices are you struggling with?")
      q1 = input()
      q2 = input()

      print("You flip a coin because you don't know if you want to", q1, "or", q2)
      if heads > tails :
         print("It landed on Heads so",q1)
      if heads < tails :
         print("It landed on Tails so",q2)
         
      