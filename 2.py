class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability  # Кількість товару в наявності

    def __str__(self):
        return f"Товар: {self.name}, Ціна: {self.price}, Наявність: {self.availability} шт."

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.availability >= quantity:
            self.items.append((product, quantity))
            product.availability -= quantity
        else:
            print(f"Немає достатньо товару '{product.name}' в наявності.")

    def remove_product(self, product_name):
        self.items = [item for item in self.items if item[0].name != product_name]

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def view_cart(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            for product, quantity in self.items:
                print(f"{product.name} - {quantity} шт. - {product.price * quantity} грн")

# Приклад використання
product1 = Product("Ноутбук", 25000, 5)
product2 = Product("Смартфон", 15000, 10)

cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)

# Переглядаємо кошик
print("Кошик:")
cart.view_cart()

# Підраховуємо загальну вартість
total = cart.calculate_total()
print(f"\nЗагальна вартість: {total} грн")

# Видаляємо товар
cart.remove_product("Ноутбук")

# Переглядаємо оновлений кошик
print("\nОновлений кошик:")
cart.view_cart()
