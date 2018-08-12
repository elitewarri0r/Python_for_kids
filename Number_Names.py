# input
xx = input('Enter a number from 0 to 9: ')
# If input can be converted into int, then carry on, if not, then quit
try:
    x = int(xx)
except:
    print ("Please enter only numbers")
    quit()

# giving the names of the numbers
if x == 0:
    print ('zero')
elif x == 1:
     print ('one')
elif x == 2:
     print ('two')
elif x == 3:
    print ('three')
elif x == 4:
    print ('four')
elif x == 5:
    print ('five')
elif x == 6:
    print ('six')
elif x == 7:
    print ('seven')
elif x == 8:
    print ('eight')
elif x == 9:
    print ('nine')
else:
    print ('Please enter a number')
    
