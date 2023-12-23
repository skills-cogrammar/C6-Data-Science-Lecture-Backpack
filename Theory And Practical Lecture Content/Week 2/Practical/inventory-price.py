# Task: Return the total inventory cost of the data
import csv

def calculate_inventory_cost(csv_file):
    total_inventory_cost = 0
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            print(f"{row['quantity_in_stock']}      {row['unit_price']}")
            total_inventory_cost+=int(row['quantity_in_stock']) * float(row['unit_price'])
    return total_inventory_cost

result = calculate_inventory_cost('data.csv')
print(f"Total cost of the inventory is ${result}")