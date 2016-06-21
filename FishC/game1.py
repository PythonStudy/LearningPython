import random

times = 3 

secret = random.randint(1,10)

print('-----------------------I love FishC ------------------')
guess = 0 
print('Please guess the number in Fishc mind: ')
while(guess != secret) and (times > 0):
    temp = raw_input()
    while not temp.isdigit():
	temp = raw_input("Sorry,please enter a int number: ")
    guess = int(temp)
    times -= 1
    if guess == secret:
	print("You are right!")
    else :
	if guess > secret:
	    print("It's larger!")
	else:
	    print("It's smaller")
	if times > 0:
	    print('Try again!')
	else:
	    print("There is no chance to guess,Game Over!")
print("Game Over, Bye Bye!")
