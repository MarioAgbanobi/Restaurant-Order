class Restaurant:
    def __init__(self):
        self.menu = {
            "burger": 5.99,
            "pizza": 8.99,
            "pasta": 7.49,
            "salad": 4.99,
            "soda": 1.99,
        }

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")

    def take_order(self):
        order = {}
        print("\nPlease place your order. Type 'done' when finished.")
        while True:
            item = input("Enter item: ").lower()
            if item == "done":
                break
            if item not in self.menu:
                print("Item not found in the menu. Please try again.")
                continue
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity should be a positive number. Please try again.")
                    continue
            except ValueError:
                print("Invalid quantity. Please try again.")
                continue
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        return order

    def calculate_total(self, order):
        total = 0
        print("\nYour Order Summary:")
        for item, quantity in order.items():
            price = self.menu[item]
            item_total = price * quantity
            total += item_total
            print(f"{item.capitalize()} x {quantity} = ${item_total:.2f}")
        print(f"Total amount: ${total:.2f}")
        return total

    def run(self):
        print("Welcome to our restaurant!")
        self.display_menu()
        order = self.take_order()
        self.calculate_total(order)
        print("Thank you for dining with us! Enjoy your meal!")

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()
