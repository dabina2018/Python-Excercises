# This program says Hello and asks for my name

print('Hello World!')
print('What is your name?') #ask for thier name
myName = input()

print('Its good to meet you, ' + myName)

print('The length of your name is: ')
print(len(myName))

print('What is your age?') #ask for thier age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')
