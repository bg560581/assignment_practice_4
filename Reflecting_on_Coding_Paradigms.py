# Functional Prompt
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order

myList = [[1,2,3],[4,7,8],[2,9,8,5]]

def getList(myList):
    theList=[]
    for item in myList:
        for i in item:
            theList.append(i)

    return sorted(theList)

print(getList(myList))

# print(f"original list = {getList}")


# Once a functional solution to this problem has been implemented, answer the following questions.
# How does this solution ensure data immutability?
# because the list is not changes the function uses this list to create totally different one 

# Is this solution a pure function? Why or why not?
# yes because there is no other outside actions that are acting upon it. 

# Is this solution a higher order function? Why or why not?
# yes. it returns another funtion with another operation

# Would it have been easier to solve this problem using a different programming style?
# I think this is a question based on preference. In my opinion the answer is no 

# Why in particular is functional programming a helpful paradigm when solving this problem?
# because it is easier to break apart this function into separate functions








# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
    def __init__(self, max_speed,condition, price_attributes) -> None:
        self.max_speed = max_speed
        self.condition = condition
        self.price_attributes = price_attributes





# Define a repair() method that will update the condition of the podracer to "repaired".

    def repair(self):
        self.condition = condition.repaired

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price_attributes) -> None:
        super().__init__(max_speed, condition, price_attributes)

    def boost(self):
        self.max_speed += 2

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price_attributes) -> None:
        super().__init__(max_speed, condition, price_attributes)

    def flameJet(self):
        self.condition = condition.trashed


# Once an Object Oriented solution has been implemented, answer the following questions:
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)




# Encapsulation
# this is when you take information and create an object out of it, ie a class 

# Abstraction
# it is the process of taking data and hiding it so the only code that is relevant at the time will be shown and is easier to manage

# Inheritance
# this is the process of creating a hierarchy of related classes 

# Polymorphism
# this method allows the user to create objects that respond to the same method differently 


# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# no, because you are creating an object/class that will be implemented on and used in separate objects. this is the easiest way of doing it

# How in particular did Object Oriented Programming assist in the solving of this problem?
# you are using encapsulation to create an class that will be used amoungst other objects, inheritance because you are using the super method to call the parent class