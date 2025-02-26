#before creating an object we have to create a class. 
#We have created a class Computer and defined the class Computer as def and here defining the config of Computer
#Here com1,com2 are objects for the class Computer
#objects will be having two stuff : 1. It will be having an attributes (Means variables) and 
# 2. It will be having a behaviour (It will be having Methods)


class Computer:

    def Config(self):
        print("RYZEN5_CPU", "8gb_RAM", "64bit_OS")

#Lets create another def and defining other details of the computer

    def details(self, name, os):
        print("HP", 'Windows')

com1 = Computer()
com2 = Computer()

Computer.Config(com1)
Computer.details('name', 'os', 'os')

com1.details('name', 'os')
com2.Config()
