# SOLID Principles

## 1. Single Responsibility Principle (SRP)

- **Description:** A class should have only one reason to change, meaning it should have only one responsibility.
- **Example:** Instead of a User class that handles both user data and email notifications, create separate UserData and EmailService classes.

```python
class UserData:
      def __init__(self, user_id, name, email):
          self.user_id = user_id
          self.name = name
          self.email = email

  class EmailService:
      def send_email(self, email, message):
          # Send email logic
          print(f"Sending email to {email}: {message}")
```

## 2. Open/Closed Principle (OCP):

- **Description:** Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
- **Example:** Instead of modifying an existing Shape class to add a new shape, create a new subclass that inherits from Shape.

```python
class Shape:
      def area(self):
          pass

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius

      def area(self):
          return 3.14 * self.radius * self.radius
```

## 3. Liskov Substitution Principle (LSP):

- **Description:** Subtypes must be substitutable for their base types without altering the correctness of the program.
- **Example:** If you have a function that works with a Bird class, it should also work with any subclass of Bird (e.g., Eagle, Penguin) without unexpected behavior.

```python
class Bird:
      def fly(self):
          pass

  class Eagle(Bird):
      def fly(self):
          print("Eagle is flying high")

  class Penguin(Bird):
      #Penguin can't fly, but we can avoid error, or implement a walk method.
      def walk(self):
          print("Penguin is walking")

  def make_bird_fly(bird: Bird):
      try:
          bird.fly()
      except AttributeError:
          print("This bird cannot fly")

  make_bird_fly(Eagle())
  make_bird_fly(Penguin())
```

## 4. Interface Segregation Principle (ISP):

- **Description:** Clients should not be forced to depend on interfaces they do not use.
- **Example:** Instead of a large Worker interface with methods for different types of work, create smaller, more specific interfaces (e.g., Eater, Worker, Sleeper).

```python
class Eater:
      def eat(self):
          pass

  class Worker:
      def work(self):
          pass

  class Sleeper:
      def sleep(self):
          pass

  class Human(Eater, Worker, Sleeper):
      def eat(self):
          print("Human is eating")

      def work(self):
          print("Human is working")

      def sleep(self):
          print("Human is sleeping")
```

## 5. Dependency Inversion Principle (DIP):

- **Description:** High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **Example:** Instead of a ReportGenerator class depending directly on a specific database class, it should depend on an abstract Database interface.

```python
from abc import ABC, abstractmethod

  class Database(ABC):
      @abstractmethod
      def get_data(self):
          pass

  class MySQLDatabase(Database):
      def get_data(self):
          return "Data from MySQL"

  class ReportGenerator:
      def __init__(self, database: Database):
          self.database = database

      def generate_report(self):
          data = self.database.get_data()
          print(f"Generating report from: {data}")

  mysql_db = MySQLDatabase()
  report_generator = ReportGenerator(mysql_db)
  report_generator.generate_report()
```

These examples should give you a clearer understanding of the SOLID principles. Remember that applying them leads to more maintainable, flexible, and robust code.

# Exercises

1. Review SOLID principles:
   - Search information about SOLID principles, and try to apply them to the previous exercises.
