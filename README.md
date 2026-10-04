# 🎬 Netflix Catalog Analysis – Power BI Dashboard

An end-to-end data analytics project that cleans the public Netflix titles dataset with **Python (Pandas)** and presents it as an interactive, Netflix-themed **Power BI** dashboard.

> Internship project – Besant Technologies

---

## 📸 Dashboard Preview

![Netflix Power BI Dashboard](images/dashboard.png)

---

## 📌 Project Overview

This project analyses **8,807 Netflix titles** (movies and TV shows released between **1925 and 2021**, added to Netflix between **January 2008 and September 2021**).

The raw CSV is cleaned with Python and loaded into Power BI, where a single-page dashboard answers questions such as:

- How big is the catalog, and how does it split between movies and TV shows?
- When were titles released, and in which months were they added?
- Which countries and genres dominate the library?
- Which individual titles sit behind each number?

---

## 🎯 Objectives

- Create a complete, null-free analytical dataset from the original Netflix file.
- Measure the balance between movies and TV shows.
- Identify historical growth, seasonal loading patterns and leading countries.
- Find the most common genres and maturity ratings.
- Deliver an interactive dashboard with filtering by **date, type and country**.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3 | Data preparation and validation |
| Pandas | CSV ingestion, duplicate removal, missing-value handling |
| Power BI Desktop | Interactive dashboard and DAX measures |
| CSV | Source and cleaned data format |

---

## 🔄 Project Workflow

```
Raw CSV  →  Python/Pandas cleaning  →  Cleaned CSV  →  Power BI model  →  Interactive dashboard
```

---

## 🧹 Data Cleaning

The script [`datasetcleaning.py`](datasetcleaning.py) performs seven steps:

1. Load the raw CSV into a DataFrame
2. Standardise column names (`snake_case`)
3. Remove duplicate rows
4. Fill missing text values with `"Unknown"` and numeric values with the median
5. Trim whitespace from text columns
6. Assert that **zero** missing values remain
7. Export the cleaned CSV

**Result:** 8,807 rows × 12 columns with 0 missing values.

> ⚠️ The script uses local Windows paths. Update the input/output paths before running it on your machine.

---

## 📂 Dataset

| Column | Description |
|--------|-------------|
| `show_id` | Unique catalog identifier |
| `type` | Movie or TV Show |
| `title` | Program name |
| `director` | Credited director |
| `cast` | Credited performers |
| `country` | Production country |
| `date_added` | Date the title was added to Netflix |
| `release_year` | Original release year |
| `rating` | Maturity classification |
| `duration` | Minutes (movies) or seasons (TV shows) |
| `listed_in` | Genre / category labels |
| `description` | Short synopsis |

---

## 📊 Dashboard Components

| Element | Visual | Fields |
|---------|--------|--------|
| Total Shows / Movies / TV Shows | KPI Cards | Count of `show_id`, `type` |
| Filters | Dropdown Slicers | `date_added`, `type`, `country` |
| Count of Shows by Month | Clustered Bar Chart | Month of `date_added` |
| Count of Shows by Type | Pie Chart | `type` |
| Count of Shows by Year [2000–25] | Line Chart | `release_year` |
| Top 5 Countries by Shows | Clustered Column Chart | `country` (Top N = 5) |
| Total Shows by Genre | Clustered Bar Chart | `listed_in` (Top N = 10) |
| Title Detail Table | Table | `show_id`, `title`, `type`, `release_year` |

**Design:** Netflix red background with black rounded panels, red gradient colouring for higher values, data labels on every chart, and full cross-filtering between visuals.

---

## 🔍 Key Findings

- **Scale:** 8,807 titles across 12 attributes.
- **Type mix:** Movies – **6,131 (69.62%)**, TV Shows – **2,676 (30.38%)**.
- **Release trend:** Slow growth in the 2000s, sharp rise after 2015, **peak of 1,147 titles in 2018**.
- **Monthly pattern:** **July** has the most additions (827); **February** has the fewest (563).
- **Geography:** The **United States** leads, followed by **India** (972) and the **United Kingdom**; 831 titles have an *Unknown* country.
- **Genres:** *Dramas, International Movies* (362), *Documentaries* (359) and *Stand-Up Comedy* (334) lead the genre groups.
- **Ratings:** TV-MA and TV-14 together make up about **60.9%** of the catalog.

---

## ⚠️ Limitations

- The dataset ends on **25 September 2021** and doesn't represent the current Netflix catalog.
- Missing values were labelled `Unknown`, not recovered from another source.
- `country` and `listed_in` contain comma-separated values, which complicates exact category counts.
- The data describes catalog availability only – not viewership, subscribers or revenue.

---

## 🚀 Future Scope

- Automate dataset refresh and show a refresh timestamp.
- Normalise country, genre, cast and director fields into separate tables.
- Add movie-duration and TV-season distributions.
- Add a maturity-rating chart.
- Add drill-through pages for countries, genres, directors and titles.

---

## 📁 Repository Structure

```
├── images/
│   └── dashboard.png                          # Dashboard screenshot
├── netflix_titles.csv                         # Raw dataset
├── cleaned_netflix_dataset.csv                # Cleaned dataset
├── datasetcleaning.py                         # Python cleaning script
├── Netfilx_Dashboard.pbix                     # Power BI dashboard file
├── Netflix_Dashboard_Analysis_Report.pdf      # Detailed project report
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository:
```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
```
2. Install the dependency:
```bash
   pip install pandas
```
3. Edit the file paths in `datasetcleaning.py`, then run:
```bash
   python datasetcleaning.py
```
4. Open `Netfilx_Dashboard.pbix` in **Power BI Desktop** and point the data source to the cleaned CSV if prompted.

---

## 📄 Full Report

A detailed chapter-by-chapter write-up (data acquisition, cleaning, step-by-step dashboard build, findings) is available in [`Netflix_Dashboard_Analysis_Report.pdf`](Netflix_Dashboard_Analysis_Report.pdf).

---

## 👤 Author

**Vishnu Vardhan**
📧 vishnuvardhan5rt@gmail.com

---

## 🙏 Acknowledgements

- Public Netflix Titles dataset
- Besant Technologies – internship program
