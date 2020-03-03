

##Problem 2
##Following the example we did in class, use the actual information in the syllabus for this 
#class to write a function gcf(ng). The parameter ng is a numerical grade between 0 and 100. 
#Your function should be fruitful and return a letter grade. In the cell below, I have placed
# three commands to test your function.


def gcf(ng):

    if ng>=95:
        return("A")
    elif ng>=90:
        return("A-")
    elif ng>=86:
        return("B+")
    elif ng>=83:
        return("B")
    elif ng>=80:
        return("B-")
    elif ng>=76:
        return("C+")
    elif ng>=73:
         return("C")    
    elif ng>=70:
        return("C-")
    elif ng>=65:
        return("D+") 
    elif ng>=60:
        return("D")    
    elif ng>=0:
        return("F")   
    else:
        return("No Grade")
# print(" awarded for this assignment")


print(gcf(93), 'awarded for this assignment')
print(gcf(86), 'awarded for this assignment')
print(gcf(59), 'awarded for this assignment')
