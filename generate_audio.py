import pyttsx3

engine = pyttsx3.init()

samples = {
    "high_1.wav": "I am confident in my ability to complete this task successfully and deliver good results.",
    "medium_1.wav": "I have some experience with this task and I believe I can handle it with proper effort.",
    "low_1.wav": "I think I can try to do this task, but I am not fully sure if I will be able to do it properly."
}

for file_name, text in samples.items():
    engine.save_to_file(text, f"data/audio/{file_name}")

engine.runAndWait()

print("Audio files generated successfully!")

