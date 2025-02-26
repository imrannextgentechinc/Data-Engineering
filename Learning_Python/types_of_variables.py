#namespace is an area where you create and store object/variable 
#class namespace, object/Instance namespace
#There are two types of variables 1.class/static variables and 2. Instance/object variables


#when you define a varible inside class it becomes class variables
#when you define a varible inside __init__ it becomes instance variables



class Car:
    

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

#Here both of the above variables for instance variables because as the object changes this value also changes      