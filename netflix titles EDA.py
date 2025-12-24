import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib

# upload data
netflix_titles_df = pd.read_csv('netflix_titles.csv')

# data profiling and check  nulls
print(netflix_titles_df.head())
print(netflix_titles_df.info())

print(netflix_titles_df.nunique())
print(netflix_titles_df.isnull().sum())

# view nulls
sns.heatmap(netflix_titles_df.isnull(), cbar=False)
plt.title('Null Values Heatmap')
plt.show()
# data cleaning remove nulls
netflix_titles_df['director'].fillna('No Director', inplace=True)
netflix_titles_df['cast'].fillna('No Cast', inplace=True)
netflix_titles_df['country'].fillna('Country Unavailable', inplace=True)
netflix_titles_df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

print(netflix_titles_df.isnull().sum().sum())

x = netflix_titles_df[netflix_titles_df['duration'].str.contains('min', case=False, na=False)]
print(netflix_titles_df.isnull().any())

# splitting data int tv shows and movie
netflix_movies_df = netflix_titles_df[netflix_titles_df['type'] == 'Movie'].copy()
netflix_shows_df = netflix_titles_df[netflix_titles_df['type'] == 'TV Show'].copy()

# data preparation
netflix_movies_df.duration = netflix_movies_df.duration.str.replace(' min', '').astype(int)
netflix_shows_df.rename(columns={'duration': 'seasons'}, inplace=True)
netflix_shows_df.replace({'seasons': {'1 Season': '1 Seasons'}}, inplace=True)
netflix_shows_df.seasons = netflix_shows_df.seasons.str.replace(' Seasons', '').astype(int)
print(netflix_shows_df.seasons)

# EDA and visualization
plt.figure(figsize=(7, 5))
sns.countplot(data=netflix_titles_df, x="type",
              hue="type",
              palette="pastel",
              )
plt.title("Count of Movies and TV Shows")
plt.xlabel("Type (Movie/TV Show)")
plt.ylabel("Total Count")
plt.show()

netflix_titles_df['date_added'] = netflix_titles_df['date_added'] = pd.to_datetime(
    netflix_titles_df['date_added'],
    errors='coerce'
)

dfs = {
    "All Titles": netflix_titles_df,
    "Movies": netflix_movies_df,
    "TV Shows": netflix_shows_df
}

for name, df in dfs.items():
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    df['month'] = df['date_added'].dt.month
    df['month_name'] = df['date_added'].dt.month_name()

    monthly_releases = df['month_name'].value_counts().sort_index()

    print(f"\n{name} monthly releases:")
    print(monthly_releases)

    best_month = monthly_releases.idxmax()
    print(f"Best month to release content for {name}: {best_month}")

# Top 10 Countries by Movie Count
netflix_movies_df = netflix_movies_df[netflix_titles_df['country'] != 'Country Unavailable'].copy()
movies_exploded = netflix_movies_df.explode('country')

top_10_countries = (
    movies_exploded['country']
        .value_counts()
        .head(10)
)

print(top_10_countries)
sns.barplot(
    x=top_10_countries.values,
    y=top_10_countries.index
)

plt.title("Top 10 Movie Producing Countries on Netflix")
plt.xlabel("Number of Movies")
plt.ylabel("Country")
plt.show()

# IMDB ratings  for netflix

netflix_rates_df = pd.read_csv(r'C:/Users/galal/Desktop/data analysis/Internship/UneeQ/netflix/Netflix TV Shows and '
                               r'Movies.csv')
netflix_rates_df['imdb_score'] = pd.to_numeric(
    netflix_rates_df['imdb_score'],
    errors='coerce'
)
netflix_rates_df = netflix_rates_df.dropna(subset=['imdb_score'])

netflix_movies_rates_df = netflix_rates_df[netflix_rates_df['type'] == 'MOVIE'].copy()

top_rated_movies = (
    netflix_movies_rates_df
        .sort_values(by='imdb_score', ascending=False)
        .head(10)[['title', 'imdb_score', 'age_certification', 'release_year']]
)

print(top_rated_movies)

plt.figure(figsize=(15, 5))
sns.barplot(
    x=top_rated_movies.imdb_score,
    y=top_rated_movies.title,
)

plt.title("Top 10 Movie rates on Netflix")
plt.xlabel("Movie")
plt.ylabel("Rate")
plt.show()
