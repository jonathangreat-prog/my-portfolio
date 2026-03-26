import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
data = pd.read_csv("sample_data.csv")

# === Summary ===
print("=== Portfolio Dashboard Summary ===")
print(data.describe())
print("\nTotal Revenue: $", data['Revenue'].sum())
print("Total Expenses: $", data['Expenses'].sum())
print("Total New Clients:", data['New_Clients'].sum())

# === Line Chart: Revenue vs Expenses ===
plt.figure(figsize=(8,5))
plt.plot(data['Month'], data['Revenue'], marker='o', label='Revenue', color='green')
plt.plot(data['Month'], data['Expenses'], marker='o', label='Expenses', color='red')
plt.title('Revenue vs Expenses')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.savefig("assets/revenue_vs_expenses.png")
plt.close()  # closes the figure

# === Pie Chart: Monthly Expenses Breakdown ===
plt.figure(figsize=(6,6))
plt.pie(data['Expenses'], labels=data['Month'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Monthly Expenses Breakdown")
plt.savefig("assets/expenses_pie.png")
plt.close()

print("\nCharts saved in assets/ folder ✅")
