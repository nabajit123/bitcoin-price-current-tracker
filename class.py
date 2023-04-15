"""
The difference between this code and the previous code is that the checking_1 method in this code sets the age and name attributes of the Person object (self.age = age and self.name = name), whereas the previous code did not set any attributes on the object.

Setting attributes on the object allows you to store data on the object that can be accessed and
modified by other methods in the class. In this case, the checking_1 method sets the name and 
age attributes based on the input parameters, and then prints out the name and age using the attributes
that were just set.

When the p1 object is created and the checking_1 method is called on it with the arguments "John" and 36, the name and age attributes of the p1 object are set to "John" and 36, respectively. The checking_1 method then prints out the string "John(36)" using these attributes.
"""

"""
Class Variables are variables that are shared among all instances of a class. 
They are defined within the class, but outside of any methods, and are accessed using the class name, not the instance name. 
Class variables are typically used to store data that is common to all instances of the class, such as configuration settings or constants. Here's an example of a class variable:
class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
"""
"""
Instance Variables (also known as constructor variables) are variables that are unique to each instance of a class. They are defined within the class constructor (__init__ method) and are accessed using the instance name. 
Instance variables are typically used to store data that is specific to each instance of the class, such as user input or data that varies between instances. Here's an example of an instance variable:
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

"""

"""
It's important to note that class variables are shared among all instances of a class, 
so if you change the value of a class variable in one instance, 
it will be changed for all instances. On the other hand, instance variables are unique to each instance, so changing the value of an instance variable in one instance will not affect the value of that variable in other instances.

In general, you should use class variables when you want to store data that is common to all instances of a class, 
and instance variables when you want to store data that is specific to each instance of a class.
"""
class Person:

  def checking_1(self, name, age):
    self.age = age
    self.name = name
    
    print(f"{self.name}({self.age})")  
    
  def checking_1(self, name, age):

    print(f"{name}({age})")  
    


p1 = Person()
p1.checking_1("John", 36)
p2 = Person()
p2.checking_1("John", 36)

# -----------------------------------------
class Person:
	
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def checking_1(self):
    age = self.age
    name = self.name
    
    print(f"{name}({age})")  
    

    


p1 = Person("John", 36)
p1.checking_1()
# -----------------------------------------------


"""
In this example, we define a class variable count with an initial value of 0.
We also define an __init__ method that takes in two arguments, name and age, and 
sets instance variables self.name and self.age to these values. Additionally, 
we increment the Person.count class variable by 1 each time a new Person object is created.

With this code, you can create instances of the Person class and 
the count variable will keep track of how many instances have been created:
"""
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(Person.count)  # output: 2

#Note that you can access a class variable either by prefixing it with the name of the class (e.g. Person.count) or by prefixing it with an instance of the class (e.g. p1.count). However, when you access a class variable using an instance of the class, you are actually accessing the same variable that is stored in the class, so any changes made to the variable using one instance will be reflected in all instances and in the class itself.
# ---------------------------------------------------------------------------------
""""
This class definition simply uses the pass keyword, which is a placeholder statement that does nothing. This means that the class doesn't have any methods or attributes defined, and therefore doesn't have any behavior associated with it
"""
class MyClass:
    pass

# ------------------------
"""This class defines a Rectangle object with a width and a height. It includes an __init__ method, which is called when a new Rectangle object is created and initializes the width and height attributes. It also includes two additional methods, area and perimeter, which calculate the area and perimeter of the rectangle, respectively."""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(10, 5)
print(r1.area())      # Output: 50
print(r1.perimeter()) # Output: 30

#------------------------------