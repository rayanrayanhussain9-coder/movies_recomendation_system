
import pandas as pd
import ast

# 1. Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# 2. Merge datasets
movies = movies.merge(credits, on="title")

# 3. Select required columns
movies = movies[
    ['movie_id', 'title', 'overview', 'genres',
     'keywords', 'cast', 'crew']
]

# 4. Remove missing values and duplicates
movies = movies.dropna()
movies = movies.drop_duplicates()
movies = movies.reset_index(drop=True)

# 5. Convert string data into Python lists
def names(text):
    return [item['name'] for item in ast.literal_eval(text)]

def directors(text):
    return [
        item['name']
        for item in ast.literal_eval(text)
        if item['job'] == 'Director'
    ]

# 6. Extract genres, keywords, cast and directors
movies['genres'] = movies['genres'].apply(names)
movies['keywords'] = movies['keywords'].apply(names)

movies['cast'] = movies['cast'].apply(
    lambda x: names(x)[:3]
)

movies['crew'] = movies['crew'].apply(directors)

# 7. Process movie overview
movies['overview'] = movies['overview'].apply(
    lambda x: x.split()
)

# 8. Remove spaces from names
for col in ['genres', 'keywords', 'cast', 'crew']:
    movies[col] = movies[col].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

# 9. Combine all features into tags
movies['tags'] = (
    movies['overview']
    + movies['genres']
    + movies['keywords']
    + movies['cast']
    + movies['crew']
)

# 10. Convert tags into strings
movies['tags'] = movies['tags'].apply(
    lambda x: " ".join(x)
)

# 11. Convert tags to lowercase
movies['tags'] = movies['tags'].apply(
    lambda x: x.lower()
)

# 12. Apply stemming
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])

movies['tags'] = movies['tags'].apply(stem)

# 13. Convert text into numerical vectors
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = cv.fit_transform(movies['tags']).toarray()

# 14. Calculate cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

# 15. Movie recommendation function
def recommend(movie):

    movie = movie.strip().lower()

    matches = movies[
        movies['title'].str.lower() == movie
    ]

    if matches.empty:
        return None

    index = matches.index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []

    for i in scores[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies