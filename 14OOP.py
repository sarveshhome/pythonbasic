# Object-oriented programming
# print("Hello ".__add__("World"))

# print((10).__add__(20))

# stuff = list()
# print(dir(stuff))

# x =10
# y =15
# print((x).__add__(y)))

# Starting with programs

# usf = input('Enter the US Floor Number: ')
# wf = int(usf) - 1
# print('Non-US Floor Number is',wf)


# class PartyAnimal:

#     def __init__(self, name):
#         self.x = 0
#         self.name = name

#     def party(self):
#         self.x += 1
#         print(self.name, "has", self.x, "guests")


# class CricketFan(PartyAnimal):

#     def __init__(self, name):
#         super().__init__(name)
#         self.points = 0

#     def six(self):
#         self.points += 6
#         self.party()
#         print(self.name, "points", self.points)


# s = PartyAnimal("Sally")

# s.party()
# s.party()

# j = CricketFan("Jim")

# j.party()
# j.six()

# print(dir(j))

# x=4
# print(r'Hello, World!')


# class Car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def display_info(self):
#     print(f"{self.year} {self.brand} {self.model}")

# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()


# class Calculator:
#   def add(self, a, b):
#     return a + b

#   def multiply(self, a, b):
#     return a * b

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))


# method modify properties of the class

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1
#     print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()

# The __str__() method is a special method that controls what is returned when the object is printed:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)
# print(p1)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} ({self.age})"

# p1 = Person("Tobias", 36)
# print(p1)

# Multiple Methods : -A class can have multiple methods that work together

# class Playlist:
#   def __init__(self, name):
#     self.name = name
#     self.songs = []

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

#   def remove_song(self, song):
#     if song in self.songs:
#       self.songs.remove(song)
#       print(f"Removed: {song}")

#   def show_songs(self):
#     print(f"Playlist '{self.name}':")
#     for song in self.songs:
#       print(f"- {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.add_song("Vvan songs")
# my_playlist.show_songs()

# my_playlist.remove_song("Vvan songs")
# my_playlist.show_songs()


# my_playlist = Playlist("Pop Hits")
# my_playlist.add_song("shape of you")
# my_playlist.show_songs()


# delete objects : - In Python, you can delete an object by using the del statement. When you delete an object, it is removed from memory and can no longer be accessed.

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     print("Hello!")

# p1 = Person("Emil")

# del Person.greet
# print(p1.name)  # This will work
# #p1.greet()  # This will cause an error

# inheritance : - Inheritance allows you to create a new class that is a modified version of an existing class. The new class inherits the attributes and methods of the existing class, and can also have its own attributes and methods.

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()


# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)


# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# p= Student("Ram", "singh")
# print(p.graduationyear)
# p.printname()

### Class Polymorphism 

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()



# Python Encapsulation


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("Emil", 25)
# print(p1.name) #public
# print(p1.__age) # This will cause an error

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

# p1 = Person("Tobias", 25)
# print(p1.get_age())


#. Python Inner Classes

# class Outer:
#   def __init__(self):
#     self.name = "Outer Class"

#   class Inner:
#     def __init__(self):
#       self.name = "Inner Class"

#     def display(self):
#       print("This is the inner class")

# outer = Outer()
# print(outer.name)

# Accessing Inner Class from the Outside

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()
