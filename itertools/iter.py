#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

#product
#-----------------------------#
a = [1, 2]
b = [3, 4]
prod = list(product(a,b)) #prod = [(1, 3), (1, 4), (2, 3), (2, 4)]
#you can give product a repetitions argument to do it again


#permutations
#-----------------------------#
a = [1, 2, 3]
perm = list(permutations(a)) #perm = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = list(permutations(a, 2)) #perm = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


#combinations
#-----------------------------#
a = [1, 2, 3, 4]
combA = list(combinations(a, 2)) #combA = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

combAWReplace = list(combinations_with_replacement(a,2)) #combAWReplace = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


#accumulate
#-----------------------------#
a = [1, 2, 3, 4]
acc = list(accumulate(a)) #acc = [1, 3, 6, 10]

accMut = list(accumulate(a, func=operator.mul)) #accMut = [1, 2, 6, 24]

a = [1, 2, 5, 3, 4]
accMax = list(accumulate(a, func=max)) #accMax = [1, 2, 5, 5, 5]

#groupby
#-----------------------------#
def smaller_than_3(x):
  return x < 3

a = [1, 2, 3, 4]
groupObj = groupby(a, key=smaller_than_3)

for key, value in groupObj:
  print(key, list(value))
#True [1, 2]
#False [3, 4]

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

personGroups = groupby(persons, key= lambda x: x['age'])
for key, value in personGroups:
  print(key, list(value))
# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]

#count, cycle, repeat
#-----------------------------#
#starts counting at 5 onwards
for i in count(5):
  print(i)
  if i == 10:
    break

#infinitely cycles through iterable of 1, 2, 3, 1, 2...
a = [1, 2, 3]
for i in cycle(a):
  print(i)
  if i == 3:
    break

#repeats an action x # of times
for i in repeat(1, 4):
  print(i)