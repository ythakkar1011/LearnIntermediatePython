# Strings: ordered, immutable, text representation

#init string
hello = 'Hello World'
strOne = str(1) #

#access characters in string like list
wChar = hello[6] #wChar = 'W'
#Cannot change characters like you would with lists
#hello[6] = 'M' gives an error because strings are immutable

#slicing with strings
justHello = hello[0:5] #justHello = 'Hello'

#reverse string
revString = hello[::-1] #revString = dlroW olleH

#combine strings
justHello = 'Hello'
justWorld = 'World'
helloWorld = justHello + ' ' + justWorld #helloWorld = 'Hello World'

#loop through chars in str
for i in helloWorld:
  charHW = i

#check if exact substring in str
if 'Hello' in helloWorld:
  helloBool = True

#strip method to remove white space
hello = '   Hello    '
hello = hello.strip() #hello = 'Hello' / strings are immutable, doesn't change in place

#change all characters to upper or lower
hello = hello.upper() #hello = 'HELLO'
hello = hello.lower() #hello = 'hello'

#check if string startswith or endswith substring 
hello = 'Hello'
helloBool = hello.startswith('Hell') #helloBool = True
helloBool = hello.endswith('o') #helloBool = True

#find first index where substring begins / returns -1 if not found
indexString = hello.find('lo') #indexSting = 3

#count to count how many occurrences there are of substring
countString = hello.count('ll') #countString = 1

#replace substring if found and return new string
hello = hello.replace("ll", "pp") #hello = 'Heppo'

#split a string to list
newString = 'my name is yash'
newList = newString.split('m') #newList = ['', 'y na', 'e is yash']
newList = newString.split() #newList = ['my', 'name', 'is', 'yash']
newString = ''.join(newList) #newString = 'mynameisyash'
newString = ' '.join(newList) #newString = 'my name is yash'


#.join method much less expensive space and time wise compare to for loop

#formatting strings
#old way
var = "Tom"
my_string = "the variable is %s" % var #my_string = "the variable is Tom"

var = 3
my_string = "the variable is %d" % var #my_string = "the variable is 3"

var = 3.1234
my_string = "the variable is %.2f" % var #my_string = "the variable is 3.12"

#new way
var = 3.1234
my_string = "the variable is {:.2f} and {}".format(var, "Tom") #my_string = "the variable is 3.12 and Tom"

#newest way python 3.6+
my_string = f"the variable is {var} and {2}" #the variable is 3.1234 and 2



