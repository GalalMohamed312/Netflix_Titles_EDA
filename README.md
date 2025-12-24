# Netflix Movies & TV Shows Data Analysis 🎬📊

## Project Overview
This project focuses on performing **Exploratory Data Analysis (EDA)** on Netflix Movies and TV Shows datasets to uncover insights related to:
- Content release timing
- Global content production
- IMDb ratings analysis
- Movies vs TV Shows distribution

The project demonstrates end-to-end data analysis, starting from data cleaning to visualization and business insight generation.

---

## Datasets Used
1. **netflix_titles.csv**
   - Contains information about Netflix titles such as type, country, director, cast, duration, and date added.

2. **Netflix TV Shows and Movies.csv**
   - Contains IMDb ratings and additional metadata for Netflix content.

---

## Data Cleaning & Preparation
The following steps were performed:
- Handling missing values for:
  - `director`, `cast`, and `country`
- Dropping records with missing:
  - `date_added`, `rating`, and `duration`
- Converting `date_added` to datetime format
- Separating data into:
  - Movies dataset
  - TV Shows dataset
- Cleaning and converting:
  - Movie duration to numeric minutes
  - TV Show duration to number of seasons

---

## Exploratory Data Analysis (EDA)

### Q1: Best Month to Release Content
Based on historical release patterns:

- **Best month to release TV Shows:** **December**
- **Best month to release Movies:** **July**

📌 Insight:  
Netflix appears to strategically release TV shows toward the end of the year, while movies peak during mid-year periods.

---

### Q2: Distribution of Movies vs TV Shows
- Visual comparison shows a higher number of **Movies** compared to **TV Shows** on Netflix.

---

### Q3: Top 10 Content-Producing Countries
Top countries by number of movies available on Netflix:

| Rank | Country | Number of Titles |
|----|--------|----------------|
| 1 | United States | 2055 |
| 2 | India | 893 |
| 3 | United Kingdom | 206 |
| 4 | Canada | 122 |
| 5 | Spain | 97 |
| 6 | Egypt | 92 |
| 7 | Nigeria | 86 |
| 8 | Indonesia | 77 |
| 9 | Turkey | 76 |
| 10 | Japan | 76 |

📌 Insight:  
Netflix content is dominated by the US and India, with increasing contributions from MENA and emerging markets.

---

### Q4: Top 10 Highest Rated Movies on Netflix (IMDb)
Some of the highest-rated movies include:
- *David Attenborough: A Life on Our Planet (2020)*
- *C/o Kancharapalem (2018)*
- *No Longer Kids (1979)*
- *Inception (2010)*
- *Forrest Gump (1994)*

📌 Insight:  
High-quality storytelling transcends release year, with both classic and modern films ranking highly.

---

## Visualizations
The project includes:
- Null values heatmap
- Count plot for Movies vs TV Shows
- Monthly release analysis
- Bar chart of top content-producing countries
- IMDb rating visualization for top movies

---

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Key Skills Demonstrated
- Exploratory Data Analysis (EDA)
- Data Cleaning & Wrangling
- Feature Engineering
- Data Visualization
- Insight-driven storytelling

---

## Conclusion
This analysis provides valuable insights into Netflix’s content strategy, highlighting:
- Seasonal release trends
- Global content distribution
- The importance of content quality over release timing

---

## Author
**Ahmed Galal**  
Data Analyst  
Intern @ Uneeq  

---

## Acknowledgment
Special thanks to **Uneeq** for the learning opportunity and mentorship throughout this project.
