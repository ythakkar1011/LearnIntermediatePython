#List: ordered, mutable, allows duplicate elements

fruitList = ["banana", "cherry", "apple"]

#prints list object to terminal
print(fruitList)

#prints fruit at index 0: banana
print(fruitList[0])

#prints fruit at index 1: cherry
print(fruitList[1])

#prints fruit at index -1: apple
print(fruitList[-1])

#loop over items in list and print
for i in fruitList:
  print(i)

#check if something is in list
if "apple" in fruitList:
  print("apple in fruitList")
else:
  print("apple not in fruitList")

#append orange to the fruitList; Always at end
fruitList.append("orange")
print(fruitList)

#insert blueberry in specified index
fruitList.insert(1, "blueberry")
print(fruitList)

#pop orange from the fruitList; Always at end
orange = fruitList.pop()
print(fruitList)

#remove bluberry in specified index
fruitList.remove("blueberry") 
print(fruitList)

#remove everything from the wipeList
wipeList = fruitList.copy()
wipeList.clear()
print(wipeList)

#reverse fruitList
fruitList.reverse()
print(fruitList)
fruitList.reverse

#sort wipeList in alpha order; you can use sorted or .sort() method of lists
wipeList = sorted(fruitList)
print(wipeList)

#Create new numbers list and init with 5 zeros
numList = [0] * 5
print(numList)

#combine 2 lists end to end
numList2 = [1, 2, 3, 4, 5]
numList3 = numList + numList2
print(numList3)

#slicing your lists list[start:end:step]
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#prints first 4 items last index not included
print(numList[0:4])

#prints every other element starting with the first element
print(numList[::2])

#prints the list backwards
print(numList[::-1])

#To copy a list there are a few ways

# WILL NOT WORK as it points to the same address in memory
# numList2 = numList 

numList2.clear()
numList2 = numList.copy()
print(numList2)

numList2.clear()
numList2 = list(numList)
print(numList2)

numList2.clear()
numList2 = numList[:]
print(numList2)

#List Comprehension example
squaredList = [i*i for i in numList]
print(squaredList)

