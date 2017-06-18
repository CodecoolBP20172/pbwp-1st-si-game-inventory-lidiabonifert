from collections import OrderedDict
import csv


def display_inventory(inventory):
    print("\nInventory: \n")
    items_count = 0

    for key, value in inventory.items():
        items_count += value
        print(value, "\t", key)

    print("\nTotal number of items: ", items_count, "\t")


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] += 1
    display_loot(added_items)
    return inventory


def print_table(inventory, order=None):
    items = inventory.keys()
    leftside = 6
    rightside = len(max(items, key=len)) + 3
    items_count = 0

    print("\nInventory:")
    print("Count".rjust(leftside) + "Item name".rjust(rightside))
    print("-".center(leftside + rightside, "-"))

    if order == "count,desc":
        rev_ordered = OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
        for k, v in rev_ordered.items():
            items_count += v
            print(str(v).rjust(leftside) + k.rjust(rightside))

    elif order == "count,asc":
        ordered = OrderedDict(sorted(inventory.items(), key=lambda t: t[1]))
        for k, v in ordered.items():
            items_count += v
            print(str(v).rjust(leftside) + k.rjust(rightside))

    else:
        for k, v in inventory.items():
            items_count += v
            print(str(v).rjust(leftside) + k.rjust(rightside))

    print("-".center(leftside + rightside, "-"))
    print("Total number of items: ", items_count)


def display_loot(loot):
    print("\nReceived loot: ")
    print(loot)


def import_inventory(inventory, filename="test_inventory.csv"):
    read_inv = open(filename, "r")
    reader = csv.reader(read_inv, quoting=csv.QUOTE_NONE)
    imported_inv = []

    for row in reader:
        for item in row:
            imported_inv.append(item)

    add_to_inventory(inventory, imported_inv)
    read_inv.close()
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    archive = []
    open_inv = open(filename, "w")
    writer = csv.writer(open_inv)

    for k, v in inventory.items():
        for i in range(v):
            archive.append(k)

    writer.writerow(archive)
    open_inv.close()


inv = {"rope": 1,
       "torch": 6,
       "gold coin": 42,
       "dagger": 1,
       "arrow": 12}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

display_inventory(inv)
print_table(add_to_inventory(inv, dragon_loot), "count,asc")
print_table(import_inventory(inv), "count,desc")
export_inventory(inv)
