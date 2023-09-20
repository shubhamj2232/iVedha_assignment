import csv

# Define the input and output file paths
input_file = 'assignment data.csv'
output_file = 'output.csv'

# Read the CSV file and calculate the average price per square foot
data = []
with open(input_file, 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        try:
            price = float(row['price'])
            sq_ft = float(row['sq__ft'])

            if sq_ft == 0:
                continue

            price_per_sq_ft = price / sq_ft
            data.append(row)
        except ValueError:
            # Handle cases where price or sq_ft is not a valid float
            continue

# Calculate the average price per square foot
average_price_per_sq_ft = sum(float(row['price']) / float(row['sq__ft']) for row in data) / len(data)

# Filter rows where the price per square foot is less than the average
filtered_data = [row for row in data if float(row['price']) / float(row['sq__ft']) < average_price_per_sq_ft]

# Write the filtered data to a new CSV file
with open(output_file, 'w', newline='') as csv_output_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)

print(f"Filtered data saved to {output_file}")
