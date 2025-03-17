from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load movies dataset
movies_data = pd.read_csv("movies.csv")

# Data processing
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres'] + " " + movies_data['keywords'] + " " + movies_data['tagline'] + " " + movies_data['cast'] + " " + movies_data['director']

# Convert text features into vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)

@app.route('/')
def home():
    return "Movie Recommendation API is Running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_name = data.get("movie_name")

    if not movie_name:
        return jsonify({"error": "No movie name provided"}), 400

    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match].index[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        recommended_movies = []
        for i, movie in enumerate(sorted_similar_movies[1:11]):  # Get top 10 recommendations
            index = movie[0]
            title_from_index = movies_data.iloc[index]['title']
            recommended_movies.append(title_from_index)

        return jsonify({"recommended_movies": recommended_movies})
    
    else:
        return jsonify({"error": "No close match found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
