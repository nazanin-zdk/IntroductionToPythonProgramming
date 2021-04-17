import math
a = int(input("please enter a :"))
b = int(input("please enter b :"))
c = int(input("please enter c :"))

delta = (b**2) - (4*a*c)

if delta > 0 :
    z = math.sqrt(delta)
    ans1 = (-b+z) / (2*a)
    ans2 = (-b-z) / (2*a)
    print ('delta is positive and answers are : ' , ans1 , ans2)
    
elif delta == 0 :
        ans3 = (-b) / (2*a)
        print ('delta is 0 and equation has one answer : ' , ans3)

else : 
    print('delta is negative and equation has no answer ')
