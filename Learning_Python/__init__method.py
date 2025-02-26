#__init__ is a special variable (predefined)
#Normally we use __init__ to initialize the variables 

#Here we have created __init__ 
#com1 is an example for basic function of __init__ 
#com2,com3 are example of the after def any config and calling 

class Computer:
   def __init__(self):
      print("Using __init__")
com1 = Computer()



class Computer:
   def __init__(self, cpu,ram):
      self.cpu = cpu
      self.ram = ram

   def config(self):
      print("Config is: " , self.cpu, self.ram)


com2 = Computer('RYZEN','8gb')
com3 = Computer('i5', '16gb')
com2.config()
com3.config()