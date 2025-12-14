# Expense Tracker Automation (Python)

A simple Python-based expense tracker that helps record daily expenses,
categorize them, and generate category-wise and monthly summaries.

This project focuses on clean logic, correct categorization, and safe
handling of personal expense data.

---

## 🚀 Features
- Add daily expenses with category
- Store expenses in CSV format (local only)
- Category-wise expense summary
- Monthly expense summary
- Two-decimal currency formatting using `round()`

---

## 🛠 Tech Stack
- Python
- CSV module
- Datetime module

---

## 💡 Decimal Precision Handling

This project currently uses Python `float` values along with the `round()`
function to format monetary values up to two decimal places.

This approach is suitable for:
- Learning purposes
- Small personal projects

> Future Improvement:  
> Upgrade calculations to use Python’s `Decimal` module for
> production-grade financial accuracy.

---

## 🔒 Data Safety
Expense data files such as `expenses.csv` are excluded from GitHub using
`.gitignore` to protect personal financial information.

---

## 📂 Project Structure

automation/expense-tracker/
├── expense_tracker.py
├── README.md
├── .gitignore


---

## 👤 Author
**Sanjay Kumar**  
Aspiring Automation & Python Developer
