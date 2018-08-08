# Getting input
a = input('Enter a number : ')
sq = int(a)

# Answer to cross check
import math
ans = math.sqrt(sq)
print (ans)

c = 1
found = 0
sqq = 0

if sq > 0 :
  # This loop will manuually multiply numbers and check it with the original number
    while found == 0 :
        tmp = c * c
        if (tmp > sq):
            break
        if tmp == sq :
            found = 1  
            break
        
        c = c + 1
# Giving the ouput
if found == 0 :
     print ('No squareroot for', sq, '. But the answer is', ans)
else :
    print ('Sqroot of ', sq, 'is ', c)
