def combine_scores(text_score, speech_score):
    # Take average of both
    final_score = (text_score + speech_score) / 2

    if final_score < 40:
        label = "Low"
    elif final_score < 70:
        label = "Medium"
    else:
        label = "High"

    return final_score, label


def generate_feedback(text):
    feedback = []

    weak_words = ["maybe", "try", "think", "not sure"]

    for word in weak_words:
        if word in text.lower():
            feedback.append("Try to avoid uncertain words like 'maybe' or 'try'.")

    if len(text.split()) < 8:
        feedback.append("Try to give a slightly longer and clearer answer.")

    if not feedback:
        feedback.append("Your response sounds confident and clear.")

    return feedback
