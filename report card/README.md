# 📊 Automated Report Card Generator

An efficient, interactive console application built in Python to streamline educational record-keeping. This program automates the tedious process of calculating student performance metrics, evaluating grading benchmarks, and presenting a beautifully structured report card summary that automatically saves to a separate `.csv` file (`report_card.csv`) for easy viewing in Microsoft Excel or Google Sheets.

---

## 🚀 Key Features

* **Dynamic Data Entry:** Prompts for student details (Name, Roll Number, Class) and individual subject marks seamlessly.
* **Smart Performance Analytics:** * Automatically calculates total marks scored.
  * Computes accurate percentage/average scores across all subjects.
  * Determines pass/fail status based on standard academic criteria.
* **Automated Grading System:** Evaluates final percentages and accurately assigns corresponding letter grades (e.g., A+, A, B, C, F) instantly.
* **Dual Output Mode:** * Prints a clean, neatly aligned, and highly readable digital summary directly in the console.
  * Automatically exports and saves the structured data into a `report_card.csv` sheet.

---

## 🛠️ How to Run the Script

### Prerequisites
You only need **Python 3.x or higher** installed on your system. This script relies entirely on Python's built-in libraries (like `csv`), meaning no external library installations or `pip` commands are required!

### Execution Steps
1. Copy the code from `report_card.py`.
2. Paste it into your preferred IDE (like VS Code) and save the file.
3. Click the **Run** button or open your terminal and execute:
   ```bash
   python report_card.py
4. Follow the on-screen prompts to input details and marks.
5. Once finished, check your project folder for the newly generated `report_card.csv` file!

## 📝 Roadmap & Future Updates

This script is actively being updated! Upcoming features include:
* 📈 **Class-Wide Analytics:** Allowing data entry for an entire classroom to calculate class averages, highest scores, and lowest scores within the same sheet.

* 🛡️ **Input Validation:** Preventing accidental typos (like entering a negative number or a string where numbers belong) from crashing the script.

*Streamlining data management one script at a time!*