import csv
from datetime import date
import os

# ===== CONFIG =====
FILENAME = "2026-01.csv"

# ===== FILE INIT =====
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "amount", "category", "event"])

# ===== ADD EXPENSE =====
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ").strip().lower()
    event = input("Enter event name (leave empty if none): ").strip().lower()

    today = date.today().isoformat()

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, amount, category, event])

    print("Expense saved successfully ✅")

# ===== TOTAL EXPENSE =====
def total_expense():
    total = 0.0
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["amount"])

    print(f"\nTotal Expense: {round(total, 2)}")

# ===== CATEGORY SUMMARY =====
def category_summary():
    totals = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            totals[category] = totals.get(category, 0) + amount

    print("\nCategory-wise Summary:")
    for cat, amt in totals.items():
        print(f"{cat} : {round(amt, 2)}")

# ===== EVENT SUMMARY (CORRECT & NULL-SAFE) =====
def event_summary():
    events = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            note = row.get("event", "").strip().lower()

            if note == "":
                continue  # non-event entry

            amount = float(row["amount"])
            events[note] = events.get(note, 0) + amount

    if not events:
        print("\nNo event expenses found.")
        return

    print("\nEvent-wise Summary:")
    for evt, amt in events.items():
        print(f"{evt} : {round(amt, 2)}")

# ===== MONTH END REVIEW =====
def month_end_review():
    print("\n===== MONTH END REVIEW =====")
    total_expense()
    category_summary()
    event_summary()
    print("\nWrite your 1-line verdict manually 🧠")

# ===== MAIN MENU =====
def main():
    init_file()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Total Expense")
        print("3. Category Summary")
        print("4. Event Summary")
        print("5. Month End Review")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            total_expense()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            event_summary()
        elif choice == "5":
            month_end_review()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice ❌")

if __name__ == "__main__":
    main()
