# no. of lives
lives = 5
# Taking input and giving instruions 
name = input('What is your name: ')
print (' ')
print (' Welcome to the guessing game', name)
print ('', name, ', you have to guess a number between 1 & 20')
print (' You have 5 Lives', name,'and each wrong guess will decrease it by 1')
print (' ')

# loop that quit after lives = 0
while lives != 0:
# taking the guess
    a = int(input('Enter your guess: '))
    if a != 15:
        lives = lives - 1
        print (' Try again!')
        print (' You have', count, 'lives')
        print ('Hint:')
        # After the guess is wrong a hint is provided based on the guess
        if a <= 5:
            print (' You are too far away')
        elif a <= 10:
            print (' You are far away')
        elif a <= 13 :
            print (' You are close')
        elif a <= 14:
            print (' You are very close!')
        elif a > 15 :
            print (' You are far away')
        elif a > 17:
            print (' You are far away')
        elif a <= 17 :
            print (' You are very close')
    # Gives the player in how many tries he found the number    
    elif a == 15 :
        print (' You found the number in',(6 - lives),'tries', name)
        break
# if player failed to achive the goal then he is provied with the answer
if lives == 0 :
    print (' Too bad, you lost :(')
    print (' The number you had to guess was 15')
