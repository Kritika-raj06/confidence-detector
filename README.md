# 🎤 Confidence Detector (Text + Voice)

A Machine Learning–based application that detects a person’s **confidence level** by analyzing both **text responses** and **speech (audio)**.  
The system predicts whether the confidence level is **Low, Medium, or High** and provides **actionable feedback** to help improve communication skills.

---

## 🚀 Features
- 📝 **Text-based confidence detection** using NLP
- 🎧 **Speech-based confidence detection** using audio features
- 🔗 **Combined confidence score** from text and voice
- 📊 Confidence score displayed as percentage
- 💡 Feedback suggestions for improvement
- 🌐 Simple and interactive **Streamlit web application**

---

## 🧠 How It Works

1. **Text Analysis**
   - Cleans and preprocesses input text
   - Converts text into numerical features using TF-IDF
   - Predicts confidence using a Machine Learning classifier

2. **Speech Analysis**
   - Extracts audio features (MFCC) from `.wav` files
   - Uses a trained ML model to estimate confidence from voice tone

3. **Final Decision**
   - Combines text and speech confidence scores
   - Classifies confidence as **Low / Medium / High**
   - Generates feedback based on detected patterns

---

## 🛠️ Tech Stack
- **Python**
- **Scikit-learn**
- **NLTK**
- **Librosa**
- **Streamlit**
- **Pandas & NumPy**

---

## 📂 Project Structure
