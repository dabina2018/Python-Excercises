
adict = {"Joe":175, "Tom":190, "Dick":150}
print(adict)

adict["Harry"] = 180
print(adict)

del adict["Joe"]
print(adict)

print(adict["Dick"])


print("")
## break
sum = 0
for value in adict:
    sum = adict[value] + sum
    print(sum)

print("")
rti = adict.items()
print (rti)
print(type(rti))

print("")
## print all items in dict
print("using FOR LOOP to print Dictionary items")
for i in rti:
    print(i)
    print(type(i))


print("")
##convert rti to a list...
print("converting dictionary to a LIST")
rti_l = list(rti)
print(rti_l)

print("")
## print new type... it is now a list
print(type(rti_l))

print("")
##print item in list using index
print("printing LIST item using its index")
print(rti_l[0])

print("")
##print the key values
print("printing key values")
my_vals = adict.values()
print(my_vals)

print("")
## print value types
print("printing value types") 
for k in my_vals:
    print(k, type(k))

##second method
my_vals_l = list(my_vals)
print(type(my_vals_l))