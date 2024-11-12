from flask import Flask, render_template, request, url_for
import pickle
import sys
import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from ast import literal_eval
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

# Download NLTK data files (only needed the first time)
nltk.download('stopwords')
nltk.download('punkt')

app = Flask(__name__)

# Get the directory of the current Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one directory to access the data directory
data_dir = os.path.join(current_dir, "..", "data")

# Load all the pickle files using relative paths
recipes_path = os.path.join(data_dir, "processed", "recipes.pkl")
tfidf_matrix_path = os.path.join(data_dir, "processed", "tfidf_matrix.pkl")
vectorizer_path = os.path.join(data_dir, "processed", "vectorizer.pkl")

with open(recipes_path, 'rb') as file:
    recipe_df = pickle.load(file)

with open(tfidf_matrix_path, 'rb') as file:
    tfidf_matrix = pickle.load(file)

with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

# Define the preprocessing function
def preprocess_user_ingredients(ingredients):
    # Lowercase the ingredients text
    ingredients = ingredients.lower()
    # Tokenize the text
    words = word_tokenize(ingredients)
    # Remove stopwords and apply stemming
    stop_words = set(stopwords.words("english"))
    ps = PorterStemmer()
    processed = [ps.stem(word) for word in words if word.isalpha() and word not in stop_words]
    # Join the processed words back into a single string
    return " ".join(processed)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_ingredients = request.form['ingredients']
        # Process the user input ingredients
        preprocessed_user_ingredients = preprocess_user_ingredients(user_ingredients)
        # Transform the processed ingredients into a vector
        user_ingredients_vector = vectorizer.transform([preprocessed_user_ingredients])
        # Calculate cosine similarity
        similarity_scores = cosine_similarity(user_ingredients_vector, tfidf_matrix)
        # Get the indices of the top 5 recommended recipes
        top_indices = similarity_scores.argsort()[0][-5:][::-1]
        recommended_recipes = recipe_df.iloc[top_indices]
        # Convert instructions to list if needed
        recommended_recipes['instructions'] = recommended_recipes['instructions'].apply(literal_eval)
        return render_template('results.html', recipes=recommended_recipes)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
