
#Hashmap#
inventory = {}

def search_(inventory, UPC):
    UPC = input("Enter the UPC: ")
    if UPC in inventory:
        product = inventory[UPC]

        print("Quantity:", product["quantity"])
        print("Product:", product["product_name"])
        print("Price:", product["price"])
        print("Category:", product["category"])

# Adds items to hashmap #
def add_item(inventory, category, product_name, quantity, UPC, price):
    inventory[UPC] = {
        'product_name': product_name,
        'quantity': quantity,
        'price': price,
        'category': category,
    }
    print(f"{product_name} added to inventory!\n")


# Menu function
def _menu_():
    while True:

        print("Welcome to Inventory Management System\n"
              "What would you like to do today?\n"
              "Options: Add Item, Search, Locate, List, Quit")
        choice = input("Enter your choice: ").lower()

        if choice == "add item":
            # Ask user for input
            category = input("Enter category: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            UPC = input("Enter UPC: ")
            price = float(input("Enter price: "))

            add_item(inventory, category, name, quantity, UPC, price)

            choice2 = input("Would you lie to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "search":

            search_(inventory, UPC)
            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break




_menu_()