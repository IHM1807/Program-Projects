import speech_recognition as sr
import pyttsx3
import mysql.connector
from difflib import SequenceMatcher

# Initialize TTS engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fuzzy answer checker
def is_answer_similar(correct_answer, user_answer):
    ratio = SequenceMatcher(None, correct_answer.lower(), user_answer.lower()).ratio()
    print(f"Match ratio: {ratio}")  # Debugging
    return ratio > 0.6

# Initialize recognizer
recognizer = sr.Recognizer()

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="study_assistant"
)
cursor = db.cursor(dictionary=True)

def get_question(topic):
    cursor.execute("SELECT * FROM questions WHERE topic=%s ORDER BY RAND() LIMIT 1", (topic,))
    return cursor.fetchone()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("API error.")
        return ""

def run_assistant():
    speak("Hello! What do you want to do?")
    command = listen()

    if "quiz me on" in command:
        topic = command.replace("quiz me on", "").strip()
        question = get_question(topic)
        if question:
            speak(f"Here's a question on {topic}: {question['question']}")
            print("Question pulled:", question['question'])
            print("Correct answer:", question['answer'])

            user_answer = listen()
            print("User answered:", user_answer)

            if user_answer:
                if is_answer_similar(question['answer'], user_answer):
                    speak("Correct!")
                else:
                    speak(f"Not quite. The correct answer is: {question['answer']}")
            else:
                speak("I didn't catch your answer.")
        else:
            speak(f"Sorry, I don't have any questions on {topic}")
    elif "help me write" in command:
        if "loop" in command:
            speak("Here's how to write a Python loop:")
            print("for i in range(5):\n    print(i)")
            speak("I have printed it on your screen.")
    else:
        speak("Sorry, I don't understand. Please try again.")

# Run it!
if __name__ == "__main__":
    run_assistant()
