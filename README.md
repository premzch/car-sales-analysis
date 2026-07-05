# Car Sales Data Analysis & Visualization

An end-to-end data analytics project focused on cleaning raw automotive sales data using Python and building an interactive dashboard in Power BI to track key performance indicators (KPIs).

---

## 📊 Project Overview
This project takes raw car sales records and transforms them into actionable business insights. The process is split into two distinct stages:
1. **Data Cleaning & Preprocessing:** Standardizing data formats and treating anomalies using Python.
2. **Data Visualization:** Designing a robust dashboard to track sales metrics, regional performance, and vehicle trends.

---

## 🛠️ Tech Stack & Tools
* **Python (VS Code):** Used for data cleaning, text formatting, and datatype corrections.
  * *Libraries:* `pandas`, `numpy`
* **Power BI Desktop:** Used for data modeling, DAX measures, and interactive reporting.

---

## 🐍 Step 1: Data Cleaning (Python)
The `car_sales.py` script executes the following preprocessing steps to ensure data integrity:
* **Structural Cleaning:** Strips whitespace, converts column names to lowercase, and replaces spaces with underscores for uniform coding.
* **Text Formatting:** Standardizes categorical text columns (like Customer Name, Company, Model, Engine, Transmission, and Color) into proper Title Case.
* **Anomalies Fixed:** Cleans corrupt encoding symbols (e.g., removing `Â` characters from the `engine` details).
* **Datatype Correction:** Explicitly converts dates, `annual_income`, and `price` into correct numeric/datetime formats for seamless analysis.

---

## 📈 Step 2: Business Dashboard (Power BI)
The `car_sales.pbix` file contains an interactive reporting layout built to analyze business health. 

### Key Insights Tracked:
* **Sales Overview:** Total Revenue, Total Cars Sold, and Average Selling Price.
* **Performance Breakdown:** Sales tracking by vehicle body style, color, transmission type, and engine configuration.
* **Geographical Distribution:** Sales performance mapped out across dealer regions.

---

## 🚀 How to Run this Project

### To run the Python Script:
1. Clone this repository.
2. Make sure you have your raw dataset named `Car Sales.csv` in the same directory.
3. Run the script via VS Code or your terminal:
   ```bash
   python car_sales.py
