import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
data = pd.read_csv("sample_data.csv")

# Display summary
print("=== Portfolio Dashboard Summary ===")
print(data.describe())
print("\nTotal Revenue: $", data['Revenue'].sum())
print("Total Expenses: $", data['Expenses'].sum())
print("Total New Clients:", data['New_Clients'].sum())

# Plot Revenue vs Expenses
plt.figure(figsize=(8,5))
plt.plot(data['Month'], data['Revenue'], marker='o', label='Revenue')
plt.plot(data['Month'], data['Expenses'], marker='o', label='Expenses')
plt.title('Revenue vs Expenses')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.savefig("assets/revenue_vs_expenses.png")  # save chart
plt.show()
