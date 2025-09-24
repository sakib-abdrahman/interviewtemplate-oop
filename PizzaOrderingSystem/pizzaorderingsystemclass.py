# Pizza Ordering System (Frequency: 5 / 5)
# Problem: Design a customizable pizza ordering system using the Decorator pattern.
# Concepts: Design pattern (Decorator), composition over inheritance

from abc import ABC, abstractmethod

# Step 1: Define the base Pizza interface
class Pizza(ABC):  # foundation class and foundation interface for us
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# Step 2: Create concrete Pizza implementations
class Margherita(Pizza):
    def cost(self) -> float:
        return 8.0

    def description(self) -> str:
        return "Margherita"

class Pepperoni(Pizza):
    def cost(self) -> float:
        return 10.0

    def description(self) -> str:
        return "Pepperoni"

class Veggie(Pizza):
    def cost(self) -> float:
        return 9.0

    def description(self) -> str:
        return "Veggie"

# Step 3: Create a Decorator class
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):  # base class
        self._pizza = pizza

    def cost(self) -> float:
        return self._pizza.cost()

    def description(self) -> str:
        return self._pizza.description()

# Step 4: Add specific toppings as decorators
class Cheese(ToppingDecorator):
    def cost(self) -> float:
        return self._pizza.cost() + 2.0

    def description(self) -> str:
        return self._pizza.description() + ", Cheese"

class Mushroom(ToppingDecorator):
    def cost(self) -> float:
        return self._pizza.cost() + 1.0

    def description(self) -> str:
        return self._pizza.description() + ", Mushroom"

class Pepper(ToppingDecorator):
    def cost(self) -> float:
        return self._pizza.cost() + 1.5

    def description(self) -> str:
        return self._pizza.description() + ", Pepper"

# Step 5: Factory to create base pizzas
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        elif pizza_type == "Veggie":
            return Veggie()
        else:
            raise ValueError("Invalid pizza type")

# Usage Example
if __name__ == "__main__":
    # Create a base pizza using the factory
    base_pizza = PizzaFactory.create_pizza("Margherita")

    # Adding toppings dynamically is very important!!!
    pizza_with_toppings = Cheese(base_pizza)
    pizza_with_toppings = Mushroom(pizza_with_toppings)
    pizza_with_toppings = Pepper(pizza_with_toppings)

    # Output final pizza description and cost
    print(pizza_with_toppings.description())  # Output: Margherita, Cheese, Mushroom, Pepper
    print(pizza_with_toppings.cost())  # Output: 12.5