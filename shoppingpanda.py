import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales.csv")

# Create total column
df["total"] = df["price"] * df["quantity"]

print("\nSales Data")
print(df)

# Total sales
total_sales = df["total"].sum()
print("\nTotal Sales:", total_sales)

# Product wise sales
product_sales = df.groupby("product")["total"].sum()
print("\nProduct Wise Sales")
print(product_sales)

# Best selling product
best_product = df.groupby("product")["quantity"].sum().idxmax()
print("\nBest Selling Product:", best_product)

# Daily sales report
daily_sales = df.groupby("date")["total"].sum()
print("\nDaily Sales Report")
print(daily_sales)
product_sales.plot(kind="pie")
plt.title("Product Sales Report")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
