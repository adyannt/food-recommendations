# Gourmet Guru 🍲✨

Gourmet Guru is a web app designed to help users discover recipes based on ingredients they have available. Simply enter your ingredients, and Gourmet Guru will generate a list of delicious recipes to explore.

## Features 🌟

- **Recipe Suggestions by Ingredients:** Input your ingredients, and Gourmet Guru will suggest recipes that you can make with what you have on hand.
- **Versatile Search Options:** Supports a wide variety of ingredients, making it easy to find recipes that fit your pantry’s contents.
- **Comprehensive Recipe Details:** View full recipe details, including title, description, cooking time, ingredients, and instructions.
- **Intuitive User Interface:** Enjoy a user-friendly interface that simplifies searching for recipes and discovering new dishes.

## Technologies Used 🛠️

- **Python:** Backend development.
- **Flask:** Framework for building the backend server.
- **Pandas:** Data manipulation and analysis for managing recipe data.
- **scikit-learn:** Machine learning library for text vectorization and similarity calculations.
- **HTML/CSS:** Frontend design and styling.
- **JavaScript:** Client-side scripting for interactive elements.
- **Render:** Platform for deploying the application.

## Project Details 📝

1. **Data Collection** 📊
   - Recipe data was scraped from [Pinch of Yum](https://pinchofyum.com/) using Python tools like Scrapy and Beautiful Soup.
   - Key steps included identifying essential recipe attributes, scraping data, and saving it in CSV format for processing.

2. **Data Preprocessing** 🍅
   - Prepared the collected data through:
     - **Tokenization:** Breaking down ingredient text into individual words.
     - **Stopword Removal:** Excluding common English words that don’t add meaning.
     - **Stemming:** Reducing words to their root forms.
     - **Unwanted Terms Removal:** Excluding common measurements and irrelevant terms.
     - **Regex Cleaning:** Removing non-alphabetic characters and parentheses.

3. **Text Vectorization and Similarity Calculation** 🔍
   - Recommended recipes based on ingredient similarity:
     - **TF-IDF Vectorization:** Converted ingredient lists into numerical vectors, giving more weight to unique ingredients.
     - **Cosine Similarity:** Measured similarity between input ingredients and recipes to rank recommendations.

4. **Building the Web Application with Flask** 🌐
   - **Backend:** Developed a Flask app to process user requests, calculate similarity scores, and return top recipe suggestions.
   - **Frontend:** Designed an HTML/CSS interface with JavaScript for interactive features like modals for recipe details.

5. **Deploying the Application on Render** 🚀
   - **Render Setup:** Created a Render account and linked this Git repository.
   - **Deployment:** Followed Render’s deployment guide to push and deploy the application.

- Recipe data was sourced from [Pinch of Yum](https://pinchofyum.com/).
