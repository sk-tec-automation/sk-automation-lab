import csv
import os
from datetime import date

# ================== PATH SETUP ==================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXPENSE_FILE = os.path.join(BASE_DIR, "expenses.csv")
INCOME_FILE = os.path.join(BASE_DIR, "income.csv")
SAVINGS_FILE = os.path.join(BASE_DIR, "savings.csv")
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")

EXPENSE_FIELDS = ["date", "amount", "category", "event"]

# ================== BUDGETS ==================

BUDGETS = {
    "food": 3000,
    "snack": 500,
    "entertainment": 500,
    "bike_rent": 1000,
    "travel": 1000,
    "electronics": 1000,
    "household": 500,
    "rent": 8500,
    "loan": 10000,
    "mom": 4000
}

# ================== FILE INIT ==================

def init_csv(file_name, headers):
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def init_files():
    init_csv(EXPENSE_FILE, EXPENSE_FIELDS)
    init_csv(INCOME_FILE, ["year", "month", "income"])
    init_csv(SAVINGS_FILE, ["year", "month", "change", "balance"])

# ================== INCOME ==================

def income_exists(year, month):
    with open(INCOME_FILE, "r") as f:
        reader = csv.DictReader(f)
        return any(int(r["year"]) == year and int(r["month"]) == month for r in reader)

def ask_and_store_income(year, month):
    while True:
        try:
            income = float(input(f"Enter income for {year}-{month:02d}: "))
            break
        except ValueError:
            print("❌ Invalid amount")

    with open(INCOME_FILE, "a", newline="") as f:
        csv.writer(f).writerow([year, month, income])

    return income

def get_current_month_income():
    today = date.today()
    with open(INCOME_FILE, "r") as f:
        for r in csv.DictReader(f):
            if int(r["year"]) == today.year and int(r["month"]) == today.month:
                return float(r["income"])
    return None

def ensure_income_for_current_month():
    today = date.today()
    if not income_exists(today.year, today.month):
        ask_and_store_income(today.year, today.month)

# ================== SAVINGS ==================

def get_last_savings_balance():
    with open(SAVINGS_FILE, "r") as f:
        rows = list(csv.DictReader(f))
        return float(rows[-1]["balance"]) if rows else 0.0

def record_savings(year, month, change):
    balance = get_last_savings_balance() + change
    with open(SAVINGS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([year, month, round(change, 2), round(balance, 2)])

# ================== MONTH ROLLOVER ==================

def handle_month_change():
    today = date.today()
    current, old = [], []

    with open(EXPENSE_FILE, "r") as f:
        for row in csv.DictReader(f):
            try:
                d = date.fromisoformat(row["date"])
                (current if (d.year, d.month) == (today.year, today.month) else old).append(row)
            except Exception:
                continue

    if not old:
        return

    last_month = date.fromisoformat(old[0]["date"])
    total_spent = sum(float(r["amount"]) for r in old)

    income = None
    with open(INCOME_FILE, "r") as f:
        for r in csv.DictReader(f):
            if int(r["year"]) == last_month.year and int(r["month"]) == last_month.month:
                income = float(r["income"])
                break

    if income is not None:
        record_savings(last_month.year, last_month.month, income - total_spent)

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    archive_file = os.path.join(ARCHIVE_DIR, f"expenses_{last_month.year}_{last_month.month:02d}.csv")

    with open(archive_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EXPENSE_FIELDS)
        writer.writeheader()
        writer.writerows(old)

    with open(EXPENSE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EXPENSE_FIELDS)
        writer.writeheader()
        writer.writerows(current)

# ================== ADD EXPENSE ==================

def add_expense():
    ensure_income_for_current_month()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❌ Invalid amount")
        return

    category = input("Category: ").strip().lower()
    event = input("Event (optional): ").strip().lower()

    if category not in BUDGETS:
        print(f"⚠️ No budget set for '{category}'")
        if input("Save anyway? (y/n): ").strip().lower() != "y":
            print("❌ Cancelled")
            return
    else:
        if input("Confirm expense? (y/n): ").strip().lower() != "y":
            print("❌ Cancelled")
            return

    with open(EXPENSE_FILE, "a", newline="") as f:
        csv.writer(f).writerow([date.today().isoformat(), amount, category, event])

    print("✅ Expense saved")

# ================== SUMMARY ==================

def monthly_summary():
    summary = {}
    events = {}

    with open(EXPENSE_FILE, "r") as f:
        for r in csv.DictReader(f):
            amt = float(r["amount"])
            summary[r["category"]] = summary.get(r["category"], 0) + amt

            evt = r["event"].strip()
            if evt:
                events[evt] = events.get(evt, 0) + amt

    total = sum(summary.values())
    income = get_current_month_income()

    print("\n📊 Monthly Summary")
    print("-" * 60)

    for cat, spent in summary.items():
        budget = BUDGETS.get(cat)
        if budget:
            left = budget - spent
            status = "🚨 OVER" if left < 0 else "⚠️ Near" if spent / budget >= 0.8 else "✅ OK"
            print(f"{cat:12}: ₹{spent:8.2f} / ₹{budget:<7} | Left ₹{left:8.2f} {status}")
        else:
            print(f"{cat:12}: ₹{spent:8.2f} (no budget)")

    print("-" * 60)
    print(f"TOTAL SPENT  : ₹{total:.2f}")
    if income is not None:
        print(f"INCOME       : ₹{income:.2f}")
        print(f"BALANCE LEFT : ₹{income - total:.2f}")

    if events:
        print("\n🎯 Event Summary")
        for e, a in events.items():
            print(f"{e:15}: ₹{a:.2f}")

# ================== MAIN ==================

def main():
    init_files()
    handle_month_change()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
