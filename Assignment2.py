

##Assignment 2
##Problem 1
##The code in the first cell below is one of the examples of conditional execution templates 
##we went over in class. Your task is to use the code to build an equivalent function. 
#In this function, the logical variables, which are set in the example, become parameters of 
#the function. Name your function "ex1". Place your code in the code cell below the cell 
#containing the original code. There are three commands I have already placed in that cell,
# where you will write. These commands serve to test the function you construct. Note that
#  your function is void


cond1 = True
cond2 = True
cond3 = True
if cond1:
    print("Point A")
elif cond2:
    print("Point B")
elif cond3:
    print("Point C")
else:
    print("Point D")
print("Point E")



# Place your code here.
def ex1(black, brown, white):
    if black:
        print("Wear a black belt")
    elif brown:
        print("Wear a brown belt")
    elif white:
        print("Wear a black or brown belt")
    else:
        print("Any color is fine")
        
    print("to match those shoes.")



# Here are the three test commands
print(ex1(True,True,True))
print(ex1(False,False,False))
print(ex1(False,True,False))
