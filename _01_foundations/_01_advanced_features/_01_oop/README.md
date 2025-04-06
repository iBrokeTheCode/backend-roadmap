# OOP

## Theory

**Classes and Objects:**

- A class is a blueprint for creating objects. It defines the attributes (data) and methods (behavior) that objects of that class will have.
- An object is an instance of a class.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)
my_dog.bark()
```

**Important concepts:**

- `init`: The constructor method, called when an object is created.
- `self`: A reference to the current object.
- `super()`: Used to call methods of the superclass.
- `@property`: Used to create getter and setter methods.
- `@classmethod`: Used to create class methods.
- `@staticmethod`: Used to create static methods.

### Encapsulation

- Encapsulation is the bundling of data and methods that operate on that data within a single unit (a class).
- It helps to hide the internal implementation details of an object and expose only the necessary interface.
- In Python, encapsulation is achieved through access modifiers (public, protected, and private). Although python doesn't have really private variables, it uses the convention of underscore to indicate that a variable or method is intended to be internal.

### Inheritance

- Inheritance is a mechanism that allows a class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class).
- It promotes code reuse and helps to create a hierarchy of classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_cat = Cat("Whiskers")
my_cat.speak()
```

### Polymorphism

- Polymorphism is the ability of objects of different classes to respond to the same method call in different ways.
- It allows for more flexible and adaptable code.
- Example: the `speak()` method in the previous example is a polimorphic method.

### Abstraction

- Abstraction is the process of hiding complex implementation details and showing only the essential features of an object.
- Abstract classes and interfaces are used to define abstract methods that must be implemented by subclasses.
- Abstract classes can't be instantiated.

## Exercises

1. Create a Class Hierarchy: [Solution](./exercises/01.py)

   - Design a class hierarchy for different types of vehicles (e.g., Car, Truck, Motorcycle).
   - Include attributes and methods specific to each vehicle type.
   - Include an abstract class called Vehicle, and make the other classes inherit from it.

2. Implement a Bank Account System: [Solution](./exercises/02.py)

   - Create a class called BankAccount with attributes for account number, balance, and owner.
   - Implement methods for depositing, withdrawing, and checking the balance.
   - Create a subclass called SavingsAccount that inherits from BankAccount and adds an interest rate attribute.

3. Design a Shape Class: [Solution](./exercises/03.py)

   - Create an abstract class called Shape with an abstract method called area().
   - Create subclasses for different shapes (e.g., Circle, Rectangle, Triangle) that implement the area() method.

4. Implement a simple inventory system: [Solution](./exercises/04.py)

   - Create a class called Product, with attributes like name, price, and stock.
   - Create a class called Inventory, that manages a list of Product objects.
   - Implement methods to add, remove, and update products, as well as to get the total value of the inventory.

5. Review SOLID principles:
   - Search information about SOLID principles. [Notes](./exercises/README.md)
   - Try to apply them to the previous exercises.
