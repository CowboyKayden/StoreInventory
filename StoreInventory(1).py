from fontTools.feaLib import location

#Hashmap#
inventory = {}

#searchs hashmap for products
def search_item(inventory):
    UPC = input("Enter the UPC: ")
    if UPC in inventory:
        product = inventory[UPC]

        print("Quantity:", product["quantity"])
        print("Product:", product["product_name"])
        print("Price:", product["price"])
        print("Category:", product["category"])
    else:
        print("Product not found")

# Adds items to hashmap #
def add_item(inventory, category, product_name, quantity, UPC, price, location,):
        if UPC not in inventory:
            inventory[UPC] = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'category': category,
                'location': location,
            }
            print(f"{product_name} added to inventory!\n")
        else:
            print("UPC already exists!")

def Locate_item(inventory):
    UPC = input("Enter the UPC you would like to locate: ")
    if UPC in inventory:
        product = inventory[UPC]

        print("Aisle: ", product["location"])

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty")
        return

    for upc, product in inventory.items():
        print("----------------")
        print("UPC:", upc)
        print("Product:", product["product_name"])
        print("Quantity:", product["quantity"])
        if product["quantity"] < 5:
            print("⚠ LOW STOCK")
        print("Price:", product["price"])
        print("Category:", product["category"])
        print("Location:", product["location"])

def delete_item(inventory):
    UPC = input("Enter the UPC you would like to delete: ")
    if UPC in inventory:
        product = inventory[UPC]
        del inventory[UPC]
        print(f"{product['product_name']} deleted from inventory!")
        print("-------------")
        print("UPC:", UPC)
        print("Product:", product["product_name"])
        print("Quantity:", product["quantity"])
        print("Price:", product["price"])
        print("Category:", product["category"])
        print("Location:", product["location"])
    else:
        print("Product not found")

def edit_item(inventory):
    UPC = input("Enter the UPC you would like to edit: ")
    if UPC in inventory:
        product = inventory[UPC]
        print("What would you like to change?")
        print("UPC, Product Name, Quantity, Price, Category, Location")
        change = input("Enter the change: ").lower()
        if change == "upc":
            new_UPC = input("Enter the new UPC: ")
            inventory[new_UPC] = inventory.pop(UPC)
            print("UPC updated")
        elif change == "product name":
            new_name = input("Enter the new product name: ")
            product["product_name"] = new_name
            print("Product name updated")
        elif change == "quantity":
            quantity = int(input("Enter the new quantity: "))
            product["quantity"] = quantity
            print("Quantity updated")
        elif change == "price":
            price = float(input("Enter the new price: "))
            product["price"] = price
            print("Price updated")
        elif change == "category":
            category = input("Enter the new category: ")
            product["category"] = category
            print("Category updated")
        elif change == "location":
            location = input("Enter the new location: ")
            product["location"] = location
            print("Location updated")
        else:
            print("Invalid input")
    else:
        print("Product not found")

# Menu function
def _menu_():
    while True:

        print("Welcome to Inventory Management System\n"
              "What would you like to do today?\n"
              "Options: Add Item, Search, Locate, View, Delete, Edit, Quit")
        choice = input("Enter your choice: ").lower()


        if choice == "add item" or choice == "add":
            # Ask user for input
            category = input("Enter category: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            UPC = input("Enter UPC: ")
            price = float(input("Enter price: "))
            location = input("Enter aisle: ")

            add_item(inventory, category, name, quantity, UPC, price, location)

            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "search":

            search_item(inventory)
            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "locate":

            Locate_item(inventory)
            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "view":
            view_inventory(inventory)
            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "delete":
            delete_item(inventory)
            choice2 = input("Would you like to continue? (Y/N): ").lower()
            if choice2 == "n":
                print("Thank you for using the Inventory Management System!")
                break

        elif choice == "edit":
            edit_item(inventory)

        elif choice == "quit":
            print("Thank you for using the Inventory Management System!")
            break




_menu_()