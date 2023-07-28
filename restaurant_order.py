def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def take_order(menu):
    order = {}
    print("\nPlease place your order. Type 'done' when finished.")

    while True:
        item = input("Enter item: ").lower()
        if item == "done":
            break

        if item not in menu:
            print("Item not found in the menu. Please try again.")
            continue

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity should be a positive number. Please try again.")
            continue

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

    return order


def calculate_total(order, menu):
    total = 0
    print("\nYour Order Summary:")

    for item, quantity in order.items():
        price = menu[item]
        item_total = price * quantity
        total += item_total
        print(f"{item} x {quantity} = ${item_total:.2f}")

    print(f"Total amount: ${total:.2f}")


def main():
    # Define the restaurant's menu
    restaurant_menu = {
        "burger": 5.99,
        "pizza": 8.99,
        "pasta": 7.49,
        "salad": 4.99,
        "soda": 1.99,
    }

    # Greeting message
    print("Welcome to Our Restaurant!")

    # Display the menu
    display_menu(restaurant_menu)

    # Take the order from the customer
    order = take_order(restaurant_menu)

    # Calculate and display the total amount
    calculate_total(order, restaurant_menu)
    print("Thank you for dining with us! Enjoy your meal!")


if __name__ == "__main__":
    main()
