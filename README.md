# 🎬 Movie Recommendation System

## 📌 Overview
This is a **Movie Recommendation System** that suggests similar movies based on user input. It utilizes **TF-IDF Vectorization** and **Cosine Similarity** to find movies with similar genres, keywords, cast, and directors.

## 🚀 Features
- Users can enter a movie name to get similar movie recommendations.
- Uses **Natural Language Processing (NLP)** techniques for better accuracy.
- Built using **Python (Flask), Pandas, and Scikit-Learn**.
- Frontend created using **HTML, CSS, and JavaScript**.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Libraries:** Pandas, NumPy, Scikit-Learn, Difflib
- **Database:** CSV file (movies dataset)

## 📂 Project Structure
```
Movie-Prediction/
│-- styles.css
│-- index.html       # Main UI
│-- movies.csv       # Movie dataset
│-- app.py           # Flask backend
│-- requirements.txt # Dependencies
│-- README.md        # Project Documentation
```

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Himashree05/movie-recommendation.git
cd movie-recommendation
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

### 4️⃣ Open in Browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🎯 API Endpoints
| Endpoint        | Method | Description |
|---------------|--------|-------------|
| `/`           | GET    | Renders homepage |
| `/recommend`  | POST   | Takes movie name & returns similar movies |

## 📝 Example Usage
```json
{
    "movie_name": "Inception"
}
```
**Response:**
```json
{
    "recommendations": ["Interstellar", "The Prestige", "Memento", "Shutter Island"]
}
```

## 🛠️ Troubleshooting
- If CORS errors occur, enable it in **Flask**:
```python
from flask_cors import CORS
CORS(app)
```
- Ensure **movies.csv** exists in the project directory.
- Check Python & Flask versions using:
```bash
python --version
pip freeze | grep Flask
```

---
🙌 **Contributions are welcome!** Feel free to fork the repo and submit a PR.

### ⭐ Happy Coding! 🎥

