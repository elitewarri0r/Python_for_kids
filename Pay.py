# input
x = input('Please enter how many hours you have worked: ')
work_hrs = int(x)

print ("Today you worked for " + x + " Hrs")

# if the work hrs is below twelve, pay = $25
if work_hrs <= 12:
    print ('Your pay will be $25')
    
# if the work hrs is above thirteen, pay = $50    
if work_hrs >= 13:
    print ('Your pay will be $50')
