from fastapi import FastAPI

app = FastAPI()
inventory = {}


#Hashmap#

#Low stock count#
def count_low_stock(inventory):
    if not inventory:
        return 0
    count = 0
    for product in inventory.values():
        if product["quantity"] < 5:
            count = count + 1
    return count

#Total Inventory quantity
def total_inventory_quantity(inventory):
    if not inventory:
        return 0
    total = 0
    for product in inventory.values():
        total += product["quantity"]
    return total

#Find low stock
def lowest_stock_product(inventory):
    if not inventory:
        return None
    low_product = next(iter(inventory.values()))
    for product in inventory.values():
        if product["quantity"] < low_product["quantity"]:
            low_product = product
    return low_product

#Find Highest stock#
def highest_stock_product(inventory):
    if not inventory:
        return None
    high_product = next(iter(inventory.values()))
    for product in inventory.values():
        if product["quantity"] > high_product["quantity"]:
            high_product = product
    return high_product

#searchs hashmap for products
def search_item(inventory, UPC):
    if UPC in inventory:
        return inventory[UPC]
    else:
        return None

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
            return True
        else:
            return False

#Searches through Hashmap for key value pairs#
def Locate_item(inventory, UPC):
    if UPC in inventory:
        product = inventory[UPC]

        return product["location"]
    else:
        return None

def view_inventory(inventory):
        return list(inventory.values())

def delete_item(inventory, UPC):
    if UPC in inventory:
        product = inventory[UPC]
        del inventory[UPC]
        return product
    else:
        return None

def edit_item(inventory, UPC, field, new_value):
    if UPC in inventory:
        product = inventory[UPC]
        if field in product:
            product[field] = new_value
        else:
            return None
        return product
    else:
        return None

# Menu function
def _menu_():
    while True:

        print("Welcome to Inventory Management System\n"
              "What would you like to do today?\n"
              "Options: Add Item, Search, Locate, View, Delete, Edit, Low Stock Search, Quit")
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

        elif choice == "search":
            UPC = input("Enter UPC: ")
            product = search_item(inventory, UPC)
            if product:
                print(product["product_name"])
                print(product["quantity"])
                print(product["price"])
                print(product["category"])
                print(product["location"])
            else:
                print("No products found")

        elif choice == "locate":
            UPC = input("Enter UPC: ")
            product = Locate_item(inventory, UPC)
            if product:
                print(product)
            else:
                print("No products found")

        elif choice == "view":
            products = view_inventory(inventory)
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found")

        elif choice == "delete":
            UPC = input("Enter UPC: ")
            product = delete_item(inventory, UPC)
            if product:
                print(product)
            else:
                print("No products found")

        elif choice == "edit":
            UPC = input("Enter UPC: ")
            field = input("Enter which field your editing: ")
            if field == "quantity":
                new_value = int(input("Enter new value: "))
            elif field == "price":
                new_value = float(input("Enter new value: "))
            else:
                new_value = input("Enter new value: ")
            product = edit_item(inventory, UPC, field, new_value)
            if product:
                print(product)
            else:
                print("No products found")

        elif choice == "low stock search":
            product = lowest_stock_product(inventory)
            if product:
                print(product)
            else:
                print("No products found")

        elif choice == "quit":

            print("Thank you for using the Inventory Management System!")
            break



if __name__ == "__main__":
    _menu_()
