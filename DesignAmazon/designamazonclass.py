# Design Amazon (Frequency: 3 / 5)
# Problem: Design a basic Amazon e-commerce system
# Requirements:
# 1. user information
# 2. cart information
# 3. order information
# 4. payment information
# 5. product information
# user can have 1 cart and many orders.
# cart can have many products.
# every order can have 1 payment.
# Concepts: Entity Modeling, Single-Responsibility / SOLID, State-Lifecycle Management

class User:
    def __init__(self, userID, name, email):
        self.cart = Cart(self)  # we will create a cart class later
        self.userID = userID
        self.name = name
        self.email = email
        self.orders = []

    def addtocart(self, cart, product, quantity):
        self.cart.addproduct(product, quantity)  # we will create an add product function in a product class

    def removefromcart(self, cart, product, quantity):
        self.cart.removeproduct(product, quantity)  # we will create a remove product function

    def placeorder(self):
        order = Order(self.cart.products, Order.ordercount)  # we will create an order later
        self.orders.append(order)
        self.cart.emptycart()  # we will create empty cart function in cart
        return order

    def vieworder(self):
        return self.orders

class Product:
    def __init__(self, productID, name, price, stock):
        self.productID = productID
        self.name = name
        self.price = price
        self.stock = stock

class Cart:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def addproduct(self, product, quantity):
        if quantity > product.stock:
            print(f'There are only {product.stock} left.')
        else:
            self.products[product] = quantity + self.products.get(product, 0)
            product.stock -= quantity

    def removeproduct(self, product, quantity):
        if product not in self.products or quantity > self.products[product]:
            cart_quantity = self.products.get(product, 0)
            print(f'There are only {cart_quantity} of this product in your cart.')
        else:
            self.products[product] -= quantity
            if self.products[product] == 0:
                del self.products[product]
            product.stock += quantity

    def viewcart(self):
        return self.products

    def emptycart(self):
        self.products.clear()

class Order:
    ordercount = 0

    def __init__(self, products, orderid):
        self.orderid = orderid
        Order.ordercount += 1
        self.products = products
        self.status = 'Placed'

class Payment:
    def __init__(self, order, amount, paymenttype):
        self.order = order
        self.amount = amount
        self.paymenttype = paymenttype
        self.status = 'Pending'

    def processpayment(self):
        self.status = 'Completed'

# Example usage
if __name__ == "__main__":
    # Create products
    product1 = Product("P001", "Laptop", 1000, 10)
    product2 = Product("P002", "Mouse", 25, 100)
    product3 = Product("P003", "Keyboard", 75, 50)

    # Create user
    user1 = User("U001", "John Doe", "john@example.com")

    # Add products to cart
    user1.addtocart(user1.cart, product1, 1)
    user1.addtocart(user1.cart, product2, 2)

    # View cart
    print("Cart contents:", user1.cart.viewcart())

    # Place order
    order = user1.placeorder()
    print(f"Order placed with ID: {order.orderid}")

    # Process payment
    payment = Payment(order, 1050, "Credit Card")
    payment.processpayment()
    print(f"Payment status: {payment.status}")