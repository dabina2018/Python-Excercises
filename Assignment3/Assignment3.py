

##Problem 1
##Create a python function summer(n). Its single parameter is a positive integer. The function
# returns the sum of all the integers between 1 and n inclusive which are multiples of 3 or 5. 
# test it with the input values 10, 150, and 975.

def summer(n):
    sum = 0

    for i in range(1, n+1):
        if (i%3) == 0 or (i%5) == 0:
            sum = sum + i

    return sum



print(summer(10))
print(summer(150))
print(summer(975))