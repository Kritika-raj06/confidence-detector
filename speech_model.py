import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ---------- FEATURE EXTRACTION ----------
def extract_features(file_path):
    audio, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)

# ---------- TRAINING DATA ----------
X = []
y = []

audio_files = {
    "data/audio/high_1.wav": "High",
    "data/audio/medium_1.wav": "Medium",
    "data/audio/low_1.wav": "Low"
}

for file_path, label in audio_files.items():
    features = extract_features(file_path)
    X.append(features)
    y.append(label)

# ---------- LABEL ENCODING ----------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ---------- MODEL TRAINING ----------
model = RandomForestClassifier()
model.fit(X, y_encoded)

# ---------- PREDICTION FUNCTION ----------
def predict_audio_confidence(file_path):
    features = extract_features(file_path).reshape(1, -1)
    prediction = model.predict(features)[0]
    confidence_score = model.predict_proba(features).max()
    label = label_encoder.inverse_transform([prediction])[0]
    return confidence_score * 100, label
