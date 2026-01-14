import pandas as pd
import re
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

nltk.download('stopwords')
from nltk.corpus import stopwords

# STEP 1: Read the dataset
data = pd.read_csv("data/text_data.csv")

# STEP 2: Clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    text = ' '.join(
        word for word in text.split()
        if word not in stopwords.words('english')
    )
    return text

data["cleaned_text"] = data["text"].apply(clean_text)

# STEP 3: Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["cleaned_text"])

# STEP 4: Convert labels into numbers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data["confidence"])

# STEP 5: Train the ML model
model = LogisticRegression()
model.fit(X, y)

# STEP 6: Prediction function
def predict_text_confidence(user_text):
    cleaned = clean_text(user_text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    confidence_score = model.predict_proba(vector).max()

    label = label_encoder.inverse_transform([prediction])[0]
    return confidence_score * 100, label
