#class is like basic design(as like design of car model plan like blueprint) and we have to create an object using it(object as car)
#Note: Everytime you create an object it is allocated to new space (In Heap memory)
#Here Computer() is a constructor
#self is used as a pointer to show the compiler which object we are calling (self.name or self.job)
#For compare function it requires who is calling it and whom to compare with

#Here we are learning about what is a constructor and self and comparing objects

class Computer:
    def __init__(self):
        self.name = 'Imran'
        self.job = 'software engineer'

    def compare(self,other):
        if self.job == other.job:
            return True
        else:
            return False


    #def update(self):
        #self.name = 'Ali'
        #self.job = 'senior software engineer'
     
     
 

c1 = Computer()
c1.job = 'Data Engineer' 
c2 = Computer()

if c1.compare(c2):
    print("They are on similar job")
else:
    print('They are on different job')

c1.name = 'Ali'
c2.job = 'senior software engineer'

#c1.update()
#c2.update()

print(c1.name)
print(c2.job)
