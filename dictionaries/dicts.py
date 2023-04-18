#Dictionary: Key-Value pairs, Unordered, Mutable, no duplicate keys

#init a dictionary
infoDict = {"name" : "Max", "age" : 28, "city": "New York"}
print(infoDict)

infoDict2 = dict(name="Mary", age=27, city="Boston")
print(infoDict2)

#identify value with key name as index
maxName = infoDict["name"]
print(maxName)

#add key:value pair
infoDict["email"] = "max@gmail.com"
print(infoDict)

#del key:value pair
del infoDict["email"]
print(infoDict)

#pop specific key:value pair
infoDict.pop("age")
print(infoDict)

#popitem from end of dict
infoDict.popitem()
print(infoDict)

#check if key in dict
if "name" in infoDict:
  print(infoDict["name"])

#try except statement with dict
keySearch = "lastname"
try:
  print(infoDict[keySearch])
except:
  print("No " + keySearch + " found!")

#loop through dict
for key in infoDict2:
  print(key+":"+str(infoDict2[key]))

for key, value in infoDict2.items():
  print(key+":"+str(value))

for key, value in infoDict2.items():
  print(key, value)

#loop over just keys or just values:
for key in infoDict2.keys():
  print(key)

for value in infoDict2.values():
  print(value)

#copy a dict
cpyDict = infoDict2.copy()

cpyDict = dict(infoDict2)

#merge dicts with update
infoDict = {"name" : "Max", "age" : 28, "city": "New York", "email": "max@gmail.com"}
infoDict2 = dict(name="Mary", age=27, city="Boston")

infoDict.update(infoDict2)
#prints {'name': 'Mary', 'age': 27, 'city': 'Boston', 'email': 'max@gmail.com'}
print(infoDict)

#tuples can be keys as well because it is immutable and hashable unlike lists
add_dict = {(1, 2): 3, (3, 6): 9, (7, 8): 15}
print(add_dict)