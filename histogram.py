B = input('Enter a number: ')
# converting the input to a str
b = str(B)
c = 0

# this loop prints the asterisk for the number in the input 
while c < len(B):
    d = int(b[c])
    print ('*' * d)
    c = c + 1
