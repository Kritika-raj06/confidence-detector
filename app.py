import streamlit as st

from text_model import predict_text_confidence
from speech_model import predict_audio_confidence
from utils import combine_scores, generate_feedback

st.title("🎤 Confidence Detector (Text + Voice)")

st.write("Enter your answer and upload your voice to check confidence level.")

# TEXT INPUT
user_text = st.text_area("✍️ Enter your answer here:")

# AUDIO INPUT
audio_file = st.file_uploader("🎧 Upload your voice file (.wav)", type=["wav"])

# BUTTON
if st.button("Analyze Confidence"):
    if not user_text:
        st.warning("Please enter some text.")
    else:
        # TEXT PREDICTION
        text_score, text_label = predict_text_confidence(user_text)

        # AUDIO PREDICTION
        if audio_file:
            with open("temp.wav", "wb") as f:
                f.write(audio_file.read())
            speech_score, speech_label = predict_audio_confidence("temp.wav")
        else:
            speech_score, speech_label = text_score, text_label

        # COMBINE RESULTS
        final_score, final_label = combine_scores(text_score, speech_score)

        # SHOW RESULTS
        st.success(f"Confidence Level: {final_label}")
        st.metric("Confidence Score", f"{final_score:.2f}%")

        # FEEDBACK
        st.subheader("💡 Feedback")
        feedback = generate_feedback(user_text)
        for f in feedback:
            st.write("•", f)
