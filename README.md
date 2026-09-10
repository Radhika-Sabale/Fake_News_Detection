# 📰 Fake News Detection System

An end-to-end Machine Learning web application designed to detect whether a given news article or headline is **Real** or **Fake**. Built with Natural Language Processing (NLP), Scikit-Learn, Flask, and an interactive front-end web interface.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Project Architecture](#project-architecture)
- [Features](#features)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Example Predictions](#example-predictions)
- [License](#license)

---

## 📖 Overview
With the exponential rise of social media and online journalism, misinformation and fake news have become a significant challenge. This project aims to combat misinformation by leveraging NLP and supervised Machine Learning algorithms to classify news articles with high precision and reliability.

---

## 📊 Dataset
The dataset used for training and evaluating this project is sourced from Kaggle:

- **Dataset**: [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) by Clément Bisaillon.
- **Details**:
  - Contains over **44,000+** news articles across categories such as politics, world news, government secrets, etc.
  - Divided into two datasets: `Fake.csv` and `True.csv`.
  - Fields include `title`, `text`, `subject`, and `date`.

---

## ⚙️ Project Architecture & Pipeline

1. **Data Cleaning & Exploration**:
   - Merging True and Fake datasets with binary labels (`0` for Fake, `1` for Real).
   - Removing missing values, duplicates, and irrelevant attributes.
2. **Text Preprocessing**:
   - Lowercasing text.
   - Removing special characters, punctuation, and digits (`regex`).
   - Tokenization via NLTK (`word_tokenize`).
   - Stopword removal (`stopwords.words('english')`).
   - Word stemming using `PorterStemmer`.
3. **Feature Engineering**:
   - Term Frequency-Inverse Document Frequency (`TfidfVectorizer`) with `max_features=5000`.
4. **Model Training & Evaluation**:
   - Trained with **Logistic Regression** (`class_weight='balanced'`, `max_iter=1000`).
   - Evaluated on an 80-20 train-test split.
5. **Deployment & Interface**:
   - RESTful API built with **Flask** and **Flask-CORS**.
   - Clean, responsive web UI with **HTML5** & **CSS3** for instant user verification.

---

## ✨ Features
- 🚀 **Real-time News Verification**: Paste any headline or news article text and get immediate predictions.
- 🎯 **High Accuracy**: Over **98.5%** accuracy on test data.
- 📈 **Confidence Score**: Provides prediction probabilities for both Real and Fake classes.
- 🌐 **RESTful API**: Easily integrate prediction capabilities into other services or mobile applications.
- 💻 **Interactive Web Interface**: Clean, accessible, and user-friendly interface.

---

## 📈 Model Performance

| Metric | Score |
| :--- | :--- |
| **Model** | Logistic Regression |
| **Accuracy** | **~98.57%** |
| **Vectorization** | TF-IDF (5,000 features) |

### Confusion Matrix on Test Set:
- **True Negatives (Fake classified as Fake)**: 3,542
- **False Positives (Fake classified as Real)**: 64
- **False Negatives (Real classified as Fake)**: 48
- **True Positives (Real classified as Real)**: 4,167

---

## 🛠️ Tech Stack
- **Programming Language**: Python 3.10+
- **Machine Learning & NLP**: Scikit-learn, NLTK, Pandas, NumPy
- **Backend API**: Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Model Serialization**: Pickle

---

## 📂 Project Structure

```text
Fake_News_Detection/
├── data/                      # Dataset directory (raw and processed data)
│   ├── Fake.csv
│   ├── True.csv
│   └── preprocessed_news.csv
├── model/                     # Serialized model & vectorizer
│   ├── model.pkl
│   └── vectorizer.pkl
├── notebooks/                 # Jupyter notebooks for experimentation
│   ├── data_cleaning.ipynb
│   ├── text_preprocessing.ipynb
│   ├── feature_engineering.ipynb
│   ├── model_training.ipynb
│   └── predict.ipynb
├── app.py                     # Flask API backend
├── interface.html             # Frontend user interface
├── style.css                  # UI styling
├── prediction.txt             # Sample headlines for quick testing
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Radhika-Sabale/Fake_News_Detection.git
cd Fake_News_Detection
```

### 2. Create and Activate Virtual Environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(If you don't have a `requirements.txt`, install core packages: `pip install flask flask-cors scikit-learn nltk pandas`)*

---

## 🏃 Running the Application

### 1. Start the Flask Backend Server
```bash
python app.py
```
The server will start running at `http://127.0.0.1:5000`.

### 2. Launch the Web Interface
Open [interface.html](file:///d:/python_clg/python%20cp/interface.html) directly in any web browser or use a live server extension.

---

## 🔌 API Endpoints

### `POST /predict`
Predicts whether the submitted text is Real or Fake news.

- **Request Body:**
  ```json
  {
    "news": "Scientists have discovered water ice on the surface of the Moon."
  }
  ```

- **Response:**
  ```json
  {
    "prediction": "Real News",
    "confidence": 99.12,
    "probability": {
      "fake": 0.88,
      "real": 99.12
    }
  }
  ```

### `GET /health`
- **Response:**
  ```json
  {
    "status": "API is running"
  }
  ```

---

## 🧪 Example Test Inputs

You can try the model using sample statements from [prediction.txt](file:///d:/python_clg/python%20cp/prediction.txt):

- **Real News Sample**:
  > *"The stock market saw a slight increase after economic reforms."*  
  > Result: **Real News**

- **Fake News Sample**:
  > *"Drinking only coffee for a week makes you immortal."*  
  > Result: **Fake News**

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).