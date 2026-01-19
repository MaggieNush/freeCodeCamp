"""
add_item(menu, item_info) - tuple is (item_name, price)
Convert item name to lowercase
Price should remain as a number
Return appropriate messages
"""
def add_item(menu, item_info):
    item_name = item_info[0].lower()
    price = item_info[1]

    if item_name in menu:
        return f"Item '{item_name}' already exists!"
    else:
        menu[item_name] = price
        return f"Item '{item_name}' was added successfully!"
    
"""
update_price(menu, item_info) - change price of existing item
"""
def update_price(menu, item_info):
    item_name = item_info[0].lower()
    price = item_info[1]

    if item_name in menu:
        menu[item_name] = price
        return f"{price} was updated successfully!"
    else:
        return f"'{item_name}' does not exist!"
    
"""
remove_item(menu, item_name) - remove from menu
"""
def remove_item(menu, item_name):
    item_name = item_name.lower()

    if item_name in menu:
        del menu[item_name]
        return f"Item {item_name} deleted successfully!"
    else:
        return f"{item_name} does not exist!"
    
"""
get_total_cost(menu, items_list)

Takes a list of item names: ["chapati", "chai", "mandazi"]
Calculate and return total cost
If any item not found, return "Item '[name]' not available!"
"""
def get_total_cost(menu, items_list):
    total_cost = 0

    # Checks each item on the list
    for item_name in items_list:
        item_name = item_name.lower()

        # If item not found, return an error message
        if item_name not in menu:
            return f"Item '{item_name}' not available!"
        
        # If found, add it's price to total cost
        total_cost += menu[item_name]
    # After checking all items, return the total cost
    return (total_cost)
   
        
        

"""
view_menu(menu) - display all items with prices formatted as "Ksh [price]"
"""
def view_menu(menu):
    if not menu:
        return "No items were found"
    
    result = "Main Menu:\n"

    for item_name, price in menu.items():
        result += f"{item_name.capitalize()}: Ksh {price}\n"
    return result

menu = {}

print(add_item(menu, ("chapati", 15)))
print(add_item(menu, ("chai", 10)))
print(add_item(menu, ("mandazi", 5)))
print(add_item(menu, ("soda", 50)))
print(get_total_cost(menu, ["chapati", "chapati", "chai", "mandazi"]))
print(update_price(menu, ("chapati", 20)))
print(view_menu(menu))
