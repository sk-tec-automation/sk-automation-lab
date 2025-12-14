from datetime import date

print("=== Expense Tracker ===")

# Take input
amount = float(input("Enter expense amount: "))
category = input("Enter category (food/travel/coffee/etc): ").lower()

today = date.today()

# -----------------------------
# Save to text file (MASTER LOG)
# -----------------------------
with open("expenses.txt", "a") as file:
    file.write(f"{today} - {amount} - {category}\n")

# -----------------------------
# Prepare calculations
# -----------------------------
total = 0.0
category_totals = {}
monthly_totals = {}

with open("expenses.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" - ")

        expense_date = parts[0]
        expense_amount = float(parts[1])
        expense_category = parts[2]

        # Total
        total += expense_amount

        # Category-wise
        if expense_category in category_totals:
            category_totals[expense_category] += expense_amount
        else:
            category_totals[expense_category] = expense_amount

        # Monthly
        month = expense_date[:7]  # YYYY-MM
        if month in monthly_totals:
            monthly_totals[month] += expense_amount
        else:
            monthly_totals[month] = expense_amount

# -----------------------------
# CSV EXPORT (APPEND MODE)
# -----------------------------
# Create header only if file does not exist
try:
    open("expenses.csv", "r").close()
except FileNotFoundError:
    with open("expenses.csv", "w") as csv:
        csv.write("date,amount,category\n")

# Append only latest entry
with open("expenses.csv", "a") as csv:
    csv.write(f"{today},{amount},{category}\n")

# -----------------------------
# Output
# -----------------------------
print("\nExpense Saved Successfully")
print("Total Expense so far:", round(total, 2))

print("\nCategory-wise Summary:")
for cat, amt in category_totals.items():
    print(cat, ":", round(amt, 2))

print("\nMonthly Summary:")
for month, amt in monthly_totals.items():
    print(month, ":", round(amt, 2))

print("\nCSV updated (expenses.csv)")
