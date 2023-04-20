#lambda arguments: expression
from functools import reduce
#init and small example
add10 = lambda x: x + 10 #add10() is a function now
fifteen = add10(5) #fifteen = 15

#lambda function with multiple inputs
add = lambda x,y: x+y
sum = add(2,3) #sum = 5

#lambda functions usually used in scenarios where you need quick funcitons or arguments for higher order funcitons

#example with sorted(seq, func)
points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_points2D = sorted(points2D, key=lambda x: x[1]) #[(5, -3), (4, 1), (10, 2), (1, 9)]

#example with map(func, seq)
a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x*2, a)) #[2, 4, 6, 8, 10]
b = [i*2 for i in a] #prefer this way tbh

#example with filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = list(filter(lambda x: x<3, a))

#example with reduce(func, seq)
a = [1, 2, 3, 4]
prod_a = reduce(lambda x,y: x*y, a)
print(prod_a)
