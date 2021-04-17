import random

def rand2(a,b) :
   for i in range(100) :
       c = random.randint(a,b)
       if c%2 == 1 :
          c += 1
          print(c)
          break

a = int(input("first:"))
b = int(input("second:"))

rand2(a,b)
