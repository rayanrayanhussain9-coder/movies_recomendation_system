# Movie Recommendation System 🎬

A Python-based Content-Based Movie Recommendation System that suggests similar movies based on movie metadata, including genres, keywords, plot descriptions, cast, and directors.

## 📌 Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning techniques to recommend movies similar to a movie selected by the user.

It analyzes movie information, combines relevant features into text tags, processes the text using stemming, and calculates similarity scores using Cosine Similarity.

## 🚀 Features

- Recommends five similar movies.
- Uses movie genres and keywords.
- Considers plot descriptions and cast information.
- Includes director information.
- Uses text processing and stemming.
- Provides recommendations through a simple command-line interface.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- CountVectorizer
- Cosine Similarity

## 📂 Project Structure

```text
Movie-Recommendation-Model/
│
├── movie-recommender.py
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd Movie-Recommendation-Model
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the project**

```bash
python movie-recommender.py
```

## 💻 How It Works

1. Loads movie information from CSV datasets.
2. Combines movie details with cast and director information.
3. Creates tags containing relevant movie features.
4. Applies stemming using NLTK.
5. Converts text into numerical vectors using CountVectorizer.
6. Calculates similarity using Cosine Similarity.
7. Displays the five most similar movies.

## 📊 Dataset

The project uses the TMDB 5000 Movie Dataset, containing movie metadata and credits.

Dataset source: [TMDB 5000 Movie Dataset – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 🎯 Learning Outcomes

- Understanding content-based recommendation systems.
- Working with Pandas and CSV datasets.
- Learning basic Natural Language Processing.
- Understanding text vectorization.
- Applying Cosine Similarity.
- Building a practical Python-based machine learning project.

## 👨‍💻 Author

**Mohammad Rayan**

B.Tech Computer Science and Engineering

Chandigarh University

---

*This project was developed as part of my journey in learning Python, Data Science, and Machine Learning.*