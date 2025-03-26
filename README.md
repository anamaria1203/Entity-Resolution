# Entity-Resolution

This project was built for the Veridion Entity Resolution Challenge – the goal was to group company names that are written differently but refer to the same business.

---

## 🧠 What I did

- Started with a mini dataset where companies had name variations (like `SSL Pools`, `SSL Pools Ltd.` etc.)
- Cleaned up the names (converted to lowercase, removed extra symbols and spaces)
- Used `rapidfuzz` to compare names and calculate similarity scores
- If two names had over 85% similarity, I considered them duplicates
- Grouped each company into a "cluster" and saved everything in a `.csv` file

---

## 🔧 Technologies used

- Python
- `pandas` – for working with tables
- `rapidfuzz` – for fuzzy matching (text similarity)

---

## ▶️ How to run it

1. Install the required libraries:
   ```bash
   pip install pandas rapidfuzz


   
