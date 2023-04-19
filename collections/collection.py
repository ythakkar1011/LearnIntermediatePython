#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

#counter
#-----------------------------#
a = "aaaaabbbbccc"
charCounter = Counter(a) #charCounter = Counter({'a': 5, 'b': 4, 'c': 3})
getMostCommon = charCounter.most_common(1) #returns list with tuples [('a', 5)]

#get list with all different elements
listEle = list(charCounter.elements()) #listEle = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']


#namedtuple
#-----------------------------#
point = namedtuple('Point', 'x,y')
pt = point(1, -4) #pt = Point(x=1, y=-4)

#OrderedDict (no use in python 3.7->forward, dicts do the job now)
#-----------------------------#
#this order will always remain
order_dict = OrderedDict()
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['d'] = 4

#defaultdict (set default value if key not set)
#-----------------------------#
default = defaultdict(int)
default['a'] = 1
default['b'] = 2
val = default['c'] #doesn't exist will return default value for type
#int->0 | float->0.0 | list->[] | str->''

#deque ()
#-----------------------------#
deq = deque()
#reguar append right
deq.append(1) #deq = deque([1])
deq.append(2) #deq = deque([1, 2])

#append left
deq.appendleft(3) #deq = deque([3, 1, 2])

#pop methods right and left
deq.pop() #deq = deque([3, 1])
deq.popleft() #deq = deque([1])

#extend methods on right and left
deq = deque([1, 2, 3]) #deq = deque([1, 2, 3])
deq.extend([4, 5, 6]) #deq = deque([1, 2, 3, 4, 5, 6])
deq.extendleft([4, 5, 6]) #deq = deque([6, 5, 4, 1, 2, 3, 4, 5, 6])

#rotate method to shift poitions right and left of contents
deq = deque([1, 2, 3, 4, 5])
deq.rotate(1) #deq = deque([5, 1, 2, 3, 4])
deq.rotate(-2) #deq = deque([2, 3, 4, 5, 1])
