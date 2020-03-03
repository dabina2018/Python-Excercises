

##Problem 2
##Write a python program which reads the file "Pride and Prejudice.txt" and produces a list of
# all of the lines in the file which contain either the word "and" or the word "the". 
# Be carefult to see these words even if they are capitalized. Also be careful to to see the 
# first letters of "these" or "there" as the word "the". Print the first 10 lines in this list.

fhand = open("Pride and Prejudice.txt", "r")
lines = []
count = 0

for line in fhand:
    if " and " in line.lower() or " the " in line.lower():
        lines.append(line)

for line in lines:
    if count < 10:
        print(line)
        count += 1