# Sets: unordered, mutable, no duplicates

#init set
numSet = {1, 2, 3} #prints {1, 2, 3}

numSet = {1, 2, 3, 1, 2} #prints {1, 2, 3}

numSet = set([1, 2, 3, 1]) #prints {1, 2, 3}

stringSet = set("Hello") #prints random order of {'H', 'e', 'l', 'o'}

emptySet = set() #can't do this: emptySet = {} -> type(dict)

#add elements
emptySet.add(1)
emptySet.add(2)
emptySet.add(3)

#remove elements
emptySet.remove(1)
emptySet.remove(2)

#discard to remove an element that you are unsure of
emptySet.discard(4) #no 4 in the set but it will not give error

#clear the entire set
emptySet.clear() #{3} -> {}

#pop method removes and returns random value in set
emptySet = {"H", "E"}
emptySet.pop() #Left over could be {"H"} or {"E"}

#loop as usual for set
for i in {1, 2, 3}:
  x = i #a print statement here would print the the elements line by line

#check if in set
if 1 in {1, 2, 3}:
  x = "yes" #x would be yes in this scenario

#Unions and Intersections with sets
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

#Unions with sets (combine)
u = odds.union(evens) #u = {0, 1, 2, 3, 4, ..., 8, 9}

#Intersection with sets (present in both)
u = odds.intersection(evens) #u = set() -> empty set

u = odds.intersection(primes) #u = {3, 5, 7}

#difference with sets
setA = set([i for i in range(1,10)]) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = setA - setB #setC = {4, 5, 6, 7, 8, 9}
setC = setB.difference(setA) #setC = {10, 11, 12}

#symmetric difference (union of the values not present in the other set)
setC = setA.symmetric_difference(setB) #setC = {4, 5, 6, 7, 8, 9, 10, 11, 12}

#To modify a set in place we can add _update to the method
#examples (don't care about output here)
setA.symmetric_difference_update(setB) 
setA.intersection_update(setB)
setA.difference_update(setB)
setA.update(setB)

#Use issubset to check if a set is included in another
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
TorF = setA.issubset(setB) #TorF = False
TorF = setB.issubset(setA) #TorF = True

#Use issuperset to check if a set includes an another
TorF = setA.issuperset(setB) #TorF = True
TorF = setB.issuperset(setA) #TorF = False

#Use disjoint to check if 2 sets have nothing shared
TorF = setA.isdisjoint(setB) #TorF = False as they share {1, 2, 3}

#To copy use .copy() or set()
setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy() #setB = {1, 2, 3, 4, 5, 6}
setC = set(setA) #setC = {1, 2, 3, 4, 5, 6}

#Use frozenset() to create a set that is immutable
frozenSet = frozenset([1, 2, 3])
#can't add, remove, or update elements
#can do union, difference, intersection
