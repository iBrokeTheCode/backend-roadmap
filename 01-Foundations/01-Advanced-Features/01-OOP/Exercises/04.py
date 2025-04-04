"""
Implement a simple inventory system:

- Create a class called Product, with attributes like name, price, and stock.
- Create a class called Inventory, that manages a list of Product objects.
- Implement methods to add, remove, and update products, as well as to get the total value of the inventory.
"""

from functools import reduce


class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

    @stock.setter
    def stock(self, stock: int) -> None:
        self.__stock = stock


class Inventory:
    def __init__(self, products: list[Product]) -> None:
        self.__products = products

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('You must add an Product instance')
        self.__products.append(product)

    def remove_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('You must add an Product instance')

        if product not in self.__products:
            raise ValueError('Product is not in the List Products')
        self.__products.remove(product)

    def update_product(self, product_name: str, new_price: float = 0, new_stock: int = 0) -> None:
        for product in self.__products:
            if product_name == product.name:
                if new_price is not None:
                    product.price = new_price
                if new_stock is not None:
                    product.stock = new_stock
                return
        raise ValueError(f"Product '{product_name}' not found in inventory.")

    def get_total_value(self) -> float:
        return reduce(lambda total, product: total + (product.price * product.stock), self.__products, 0)


if __name__ == '__main__':
    # Create some product instances
    product1 = Product("Laptop", 2000, 10)
    product2 = Product("Smartphone", 1000, 20)
    product3 = Product("Headphones", 100, 15)

    # Create an inventory instance
    inventory = Inventory([product1, product2])

    # Add a product to the inventory
    inventory.add_product(product3)

    # Remove a product from the inventory
    inventory.remove_product(product2)

    # Update a product
    inventory.update_product("Laptop", new_price=2200)

    # Get the total value of the inventory
    print(f"Total inventory value: ${inventory.get_total_value():.2f}")
