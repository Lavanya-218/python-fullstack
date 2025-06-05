#single inheritance
 
# class Animal:
#     sound="something"
#     def sound_func(self):
#         print(f"{self.sound} sound")
# class Cat(Animal):
#     def Walking(self):
#         print("The cat is walking")
# c=Cat()
# print(c.sound)
# c.sound_func()
# c.Walking()

#multiple inheritance
# class Animal:
#     sound="something"
#     def sound_func(self):
#         print(f"{self.sound} sound")
# class WildAnimal:
#     type="Wild"
#     def print(self):
#         print("blah blah")

# class Tiger(Animal,WildAnimal):
#     def Walking(self):
#         print("This is tiger")
# c=Tiger()
# print(c.sound)
# c.sound_func()
# c.Walking()
# print(c.type)
# c.print()

#multilevel inheritance
# class Animal:
#     sound="something"
#     def sound_func(self):
#         print(f"{self.sound} sound")
# class Cat(Animal):
#     def Walking(self):
#         print("The cat is walking")
# class kitten(Cat):
#     pass
# c=kitten()
# print(c.sound)
# c.sound_func()
# c.Walking()


#heirarchial inheritance
# class Animal:
#     sound="something"
# class WildAnimal(Animal):
#     type="Wild"
#     def print(self):
#         print("blah blah")

# class Tiger(Animal):
#     def Walking(self):
#         print("This is tiger")
# c=Tiger()
# print(c.sound)
# c.Walking()
# w=WildAnimal()
# w.print()
# print(w.sound)

#Hybrid Inheritance
class Animal:
    sound="something"
class Cat(Animal):
    def Walking(self):
        print("The cat is walking")
class Dog:
    s="Hello"
class Child(Cat,Dog):
    cry="Meow bow"

c=Child()
print(c.sound)
c.Walking()
print(c.s)
print(c.cry)
