#Tuple: ordered, immutable, allows duplicate elements

#Init tuple methods
tupleInfo = ("Max", 28, "Boston")

tupleInfo = ("Max",) #need comma to not make it a string

tupleInfo = tuple(["Max", 28, "Boston"])
print(tupleInfo)

#Indexing is same as it was for list object
print(tupleInfo[-1])

#loop through tuple
for i in tupleInfo:
  print(i)

#check element in tuple
if "Max" in tupleInfo:
  print("Max in tuple")

#count occurrence of something in tuple
tupleInfo = ('a', 'p', 'p', 'l', 'e')
print(tupleInfo.count('p'))

#return index of something (first occurence)
print(tupleInfo.index('p'))

#unpacking tuples
tupleInfo = (0, 1, 2, 3, 4)

i1, i2, i3, i4, i5 = tupleInfo
print(i1, i2, i3, i4, i5)

i1, *i2, i3 = tupleInfo

print(i2)

#for the same elements it may be more efficient (time and space wise) to use tuples than lists
