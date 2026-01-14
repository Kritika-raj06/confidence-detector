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
```confidence-detector/
├── app.py
├── text_model.py
├── speech_model.py
├── utils.py
├── generate_audio.py
├── requirements.txt
└── data/
├── text_data.csv
└── audio/
├── high_1.wav
├── medium_1.wav
└── low_1.wav```

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/your-username/confidence-detector.git
cd confidence-detector
OR download ZIP and extract.
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

4️⃣ Use the App

Enter a text response

Upload a .wav audio file (optional)

Click Analyze Confidence

View confidence level, score, and feedback

📌 Example Use Cases

Interview practice

Public speaking improvement

Presentation confidence analysis

Student communication skill assessment

🔮 Future Improvements

Real-time microphone input

Larger and more diverse training dataset

Deep learning models for speech analysis

Online deployment for live demo access

👩‍💻 Author

Kriti
B.Tech CSE (AI/ML)

⭐ If you find this project useful, feel free to star the repository!
