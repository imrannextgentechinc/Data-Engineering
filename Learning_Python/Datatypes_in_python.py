#Different types of Datatypes in Python


# NoneType
my_none = None
print("NoneType:", my_none)

# Complex
my_complex = 3 + 4j
print("Complex:", my_complex)

# Integer
my_int = 10
print("Integer:", my_int)

# Float
my_float = 10.5
print("Float:", my_float)

# Range
my_range = range(1, 10)
print("Range:", list(my_range))


# String
my_string = "Hello, World!"
print("String:", my_string)

# Boolean (It consists of True and False)
my_bool = True
print("Boolean:", my_bool)

# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Dictionary
my_dict = {"name": "John", "age": 30}
print("Dictionary:", my_dict)

# Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)


#Practising the datatypes
#Methods to convert datatypes

a =1
print (type(a))

b = 4.2
print (type(b))

c = 2+6j               #Complex type means a number +or- an imaginary number ex: j
print(type(c))


#we can convert int to float and float to int

a = int(b) #converting to float
b = float(a) #converting to int

print (a,b) #converted output 

a = complex(a,b) #converting into complex
print (a) 

#lets try boolean 
a = 2
b = 4

bool = b>a
print(bool)

bool = a>b
print(bool)

#In python we use True as 1 and Flase as 0
#lets try

print (int(True))
print (int(False))


#trying list

lst = [1,2,3,4]
print(type(lst))

t = (5,6,7,8)
print(type(t))

str = "Imran Ali"
print (type(str))

range1= range(0,10)
print("Range:", list(range1))


#Dictionary is used to assign and fetch values (Key is main and values are values assigned to key)

d = {'Imran' : 'Iphone', 'Ali' : 'Macbook', 'Aslan' : 'AI'}
print("Dictionary: ", d)
print("Dictionary Keys:", d.keys())
print("Dictionary values:", d.values())

