# getting the input (age)
newage = input('Enter your age: ')
# converting the string into a float
age = float(newage)
# classifing the person based on the age
if age < 1 :
    print ('NO JOKING')
elif age <= 2 :
    print ('No studys')
elif age <= 4 :
    print ('nursery')
elif age <= 6 :
    print ('kindergarden')
elif age <= 12 :
    print ('primary')
elif age <= 18 :
    print ('secendary')
elif age >124 :
    print ('NO JOKING')
else:
    print ('YOU ARE TO OLD TO BE HERE')
print ('FINISHED')
