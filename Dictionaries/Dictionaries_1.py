
##Given a string value, return a dictionary that has the count of each letter in the word
print("Given Mississippi, get count of each letter and return as dictionary key-value pairs")
s = 'Mississippi'
count_dict = {}
for c in s:
    count_dict[c] = count_dict.get(c,0) + 1  ## counting each letter

for k in count_dict.keys():
    print(k,count_dict[k])   ## printing the result

print("")
print("No idea what this is doing...")
for k in count_dict.keys():
        count_dict[k] = count_dict.get(k,0) + 1
        print(k,'new',count_dict[k])
print(k)

print("")
print(" find occurnece of each digit in given integer string")
s = '2727130252053142514510171943'
count_dict = {}
for c in s:
    count_dict[c] = count_dict.get(c,0) + 1  ##counts occurence of digits
    
for k in count_dict.keys():
    print(k,count_dict[k])   ## prints results

##find percentage of occurences

##find the percentage
print("")
print("Find the percentage of occurences in a given number string")
s = '2727130252053142514510171943'
count_dict = {}
for c in s:
    count_dict[c] = count_dict.get(c,0) + 1

# Let's look at the results

for k in count_dict.keys():
    kk = print(k,count_dict[k])

    avg = count_dict[k]/len(s)
    print(kk, avg)

## Given string.. do what it do
print("")
print("Given Mississippi...")
s = 'Mississippi'
count_dict = {}
for c in s:
    if c in count_dict:
        count_dict[c] = count_dict[c] + 1
    else:
        count_dict[c] = 1

# Let's look at the results

print('Number of Occurrences for each Item')
for k in count_dict.keys():
    print(k,count_dict[k])
    
# What is the maximum count?
maxcount = max(count_dict.values())
print(' ')
print('Maximum Count')
print(maxcount)

Win_list = []
for i in count_dict.keys():
    if count_dict[i] >= maxcount:
        Win_list.append(i)
print(' ')
print("Most Frequent Items")
print(Win_list)


# create a list of numbers between 1 and 100 as strings
print("")
print("# create a list of numbers between 1 and 100 as strings")

numlist =[]
digitlist = []
for i in range(1,101):
    s = str(i)
    numlist.append(s)
    digitlist.append(s[0])
print(numlist)
print(digitlist)