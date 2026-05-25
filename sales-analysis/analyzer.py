# import pandas as pd
# import json
import os

# # Check if we're in the right place
# print("Current directory:", os.getcwd())

# # Check if our data file exists
# data_path = "data/paris_weather.csv"
# if os.path.exists(data_path):
#     print(f"✅ Found {data_path}")
# else:
#     print(f"❌ Cannot find {data_path}")
#     print("Make sure you're running from the sales-analysis folder!")

# Read the CSV file
# df = pd.read_csv('sales-analysis/data/sales.csv')
# print("CSV Data:")
# print(df)
# print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# df['price'] = df['price'].replace('[\$,s]', '', regex=True)  
# df['price'] = pd.to_numeric(df['price'], errors='coerce')  

# # Quick operation: calculate total for each row
# df['total'] = df['quantity'] * df['price']
# print("\nWith totals:")
# print(df)

# # Create output directory
# os.makedirs('sales-analysis/output', exist_ok=True)

# # Save as different formats
# # 1. JSON format (good for web APIs)
# df.to_json('sales-analysis/output/sales_data.json', orient='records', indent=2)

# # 2. Excel format (good for sharing)
# df.to_excel('sales-analysis/output/sales_data.xlsx', index=False)

# # 3. Updated CSV (with our new total column)
# df.to_csv('sales-analysis/output/sales_with_totals.csv', index=False)

# print("\nFiles saved:")
# print("- output/sales_data.json")
# print("- output/sales_data.xlsx") 
# print("- output/sales_with_totals.csv")



# analyzer.py
import pandas as pd
import sys
sys.path.insert(0, 'sales-analysis')
from helpers import calculate_total, format_currency

print("Current directory:", os.getcwd())

# Read data
df = pd.read_csv('sales-analysis/data/sales.csv')

#  string to float
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")