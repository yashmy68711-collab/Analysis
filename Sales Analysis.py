import pandas as pd
import numpy as np

df = pd.read_csv("internship project/data.csv.csv")

print("Original Data:")
print(df)

df = df.dropna()
df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Sales"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.month_name()

print("\nProcessed Data:")
print(df)
print("\nTotal rows after cleaning:", len(df))

sales_array = np.array(df["Sales"])

print("\nRevenue Summary:")
print("Total Revenue:", np.sum(sales_array))
print("Average Revenue:", np.mean(sales_array))
print("Highest Sale:", np.max(sales_array))
print("Lowest Sale:", np.min(sales_array))