inventory = [

    ["Apple", 50, 500],
    ["Banana", 100, 1500],
    ["Orange", 75, 0.75]

]


def Display_Inventory(inventory):
    for i in inventory:
        print(i)


def update_inventory(inventory,item_name,quality_sold):
    found = False
    for i in inventory:
        if item_name.lower() == i[0].lower():
            i[1] = quality_sold
            print('Updated Successfully.')
    if found == False:
        print('Not Item. in inventory')
        
    Display_Inventory(inventory)

def calculate_total_value(inventory):
    total_value = 0
    for i in inventory:
        total_value += i[1]

    print(f'Totally Items In inventory : {total_value}')
        
def find_most_expensive(inventory):
    max_item = inventory[0]
    for item in inventory:
        if item[2] > max_item[2]:
            max_item = item
    print(f'Most Expensive : {max_item}')


def add_item(inventory,item_name,quanlity,price):
    found = False
    item = [item_name,quanlity,price]
    for i in inventory:
        if item_name.lower() == i[0].lower():
            found = True
            i[1] += quanlity
            i[2] += price

    if found == False:
        inventory.append(item)
        print('Added Successfully.')
    
    Display_Inventory(inventory)


