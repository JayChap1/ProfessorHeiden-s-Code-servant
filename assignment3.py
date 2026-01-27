# Assignment 3 - CSV to JSON Converter
# Jason Chapman - Python Programming I
# Professor Heiden

import json

# ============================================================
# REQUIREMENT 1: Create an empty list called "sales_data"
# ============================================================
sales_data = []
# Define the field names in order as specified
field_names = [
    "Transaction_date",
    "Product",
    "Price",
    "Payment_Type",
    "Name",
    "City",
    "State",
    "Country"
]
# ============================================================
# REQUIREMENT 2: Open the CSV file for processing
# ============================================================
with open("SalesJan2009.csv", "r", encoding="utf-8") as file:
    # Skip the header row
    next(file)
    
    # ============================================================
    # REQUIREMENT 3: Process line-by-line, create dictionaries,
    #                clean up extra quotes, append to sales_data
    # ============================================================
    for line in file:
        line = line.strip()
        values = line.split(",")
        
        record = {}
        for i in range(len(field_names)):
            if i < len(values):
                # Clean up extra quote characters
                cleaned_value = values[i].strip().strip('"').strip("'")
                record[field_names[i]] = cleaned_value
            else:
                record[field_names[i]] = ""
        
        # Append dictionary to sales_data list
        sales_data.append(record)
        # ============================================================
# REQUIREMENT 4: Save sales_data list to "transaction_data.json"
# ============================================================
with open("transaction_data.json", "w", encoding="utf-8") as json_file:
    json.dump(sales_data, json_file, indent=4)

print(f"Processing complete! {len(sales_data)} records saved to transaction_data.json")
