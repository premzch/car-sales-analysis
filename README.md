# Car Sales Data Analysis & Dashboard

I built this project to practice going from a messy raw dataset all the way to a working business dashboard — basically the full pipeline you'd use in a real analyst role.

The dataset is car sales records (customer info, dealer region, vehicle details, price, etc.). It came in pretty messy, so most of the actual work went into cleaning it up before I could do anything useful with it in Power BI.

## What's in this repo

- `car_sales.py` — Python script that cleans the raw data
- `Car_Sales_Cleaned.csv` — the cleaned output
- `car_sales.pbix` — the Power BI dashboard built on top of the cleaned data

## The cleaning process (Python)

The raw file had a bunch of typical real-world data problems:

- Column names were inconsistent (mixed casing, spaces), so I standardized all of them to lowercase with underscores.
- Text fields like customer name, company, model, engine, and color weren't consistently formatted, so I converted them to proper Title Case.
- The engine column had weird corrupted characters (like stray `Â` symbols from an encoding issue) that I had to strip out.
- Dates, annual income, and price were
