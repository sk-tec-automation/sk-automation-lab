# Expense Tracker Automation (Python)

A personal, offline **CLI-based expense tracker** built in Python using CSV files.  
The project evolved from a simple expense logger into a **full personal finance tracker** with income enforcement, budgeting, savings calculation, and month-wise archiving.

This project emphasizes **clean logic, data safety, and practical financial insight**.

---

## 🚀 Features

- Add daily expenses with:
  - amount
  - category
  - optional event (context)
- Enforces **monthly income entry**
- Category-wise **budget tracking with warnings**
- Monthly expense summary
- Event-wise expense insights (optional & non-intrusive)
- Automatic **month rollover and expense archiving**
- Savings calculation based on income vs expenses
- Safe cancel flow (no accidental data writes)
- Local CSV storage (offline, private)

---

## 🛠 Tech Stack

- Python 3
- `csv` module
- `datetime` module
- Standard library only (no external dependencies)

---

## 📂 Project Structure

```
expense-tracker/
│
├── expense_tracker.py        # Main (current) tracker
├── expenses.csv              # Expense data (gitignored)
├── income.csv                # Monthly income data (gitignored)
├── savings.csv               # Savings history (gitignored)
│
├── archive/
│   └── expenses_YYYY_MM.csv  # Auto-archived monthly expenses
│
├── legacy/
│   └── simple_tracker.py     # Initial prototype (preserved for learning)
│
├── README.md
└── .gitignore
```

---

## 📄 CSV Formats

### `expenses.csv`
```
date,amount,category,event
```

- `event` is optional (used for special occasions like trips, repairs, etc.)

### `income.csv`
```
year,month,income
```

### `savings.csv`
```
year,month,change,balance
```

---

## ▶️ How to Run

1. Ensure **Python 3** is installed
2. Open a terminal in the project directory
3. Run:
   ```bash
   python expense_tracker.py
   ```
4. Follow the menu options

---

## 💡 Design Notes

- Categories are free-text but checked against predefined budgets
- If a category has no budget, the user is warned and can cancel safely
- `event` is optional and used only for insight, not budgeting
- All file paths are resolved relative to the script location for safety

---

## 🔒 Data Safety & Privacy

- All financial data is stored **locally**
- CSV files are excluded from GitHub using `.gitignore`
- No cloud sync, no external services

---

## 📈 Project Evolution

This project started as a **simple CSV-based expense tracker**.

As learning progressed, it evolved into a more complete personal finance tool with:
- income enforcement
- budgeting
- savings tracking
- month-wise archiving
- improved data integrity

The original prototype is preserved in the `/legacy` folder for reference.

---

## 👤 Author

**Sanjay Kumar**  
Aspiring Automation & Python Developer  

---

## ✅ Project Status

- Feature-complete
- Actively used for real expense tracking
- Marked **Done** after consistent real-world usage
