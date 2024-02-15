import csv
def calculate_total_cost(csv_file):
    total_inv_cost = 0
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['quantity_in_stock']} - {row['unit_price']}")
            total_inv_cost += int(row['quantity_in_stock']) + float(row['unit_price'])
    return total_inv_cost
csv_file_path = 'data.csv'  # Replace with the actual path to your CSV file
total_cost = calculate_total_cost(csv_file_path)
print(f'Total cost of inventory: ${total_cost}')