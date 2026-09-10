from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass

# Load model and vectorizer
try:
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    print("✓ Model and Vectorizer loaded successfully!")
except FileNotFoundError as e:
    print(f"❌ Error loading model: {e}")
    model = None
    vectorizer = None

# Initialize preprocessing tools
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

def preprocess_text(text):
    """Preprocess text for prediction"""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = word_tokenize(text)
    return " ".join([stemmer.stem(word) for word in words if word not in stop_words])

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if news is real or fake"""
    try:
        data = request.json
        news_text = data.get('news', '').strip()
        
        if not news_text:
            return jsonify({'error': 'Please provide news text'}), 400
        
        if model is None or vectorizer is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        # Preprocess and predict
        cleaned_text = preprocess_text(news_text)
        tfidf_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(tfidf_vector)[0]
        
        result = "Real News" if prediction == 1 else "Fake News"
        confidence = model.predict_proba(tfidf_vector)[0]
        
        return jsonify({
            'prediction': result,
            'confidence': round(max(confidence) * 100, 2),
            'probability': {
                'fake': round(confidence[0] * 100, 2),
                'real': round(confidence[1] * 100, 2)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Check if API is running"""
    return jsonify({'status': 'API is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
