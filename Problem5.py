import pyttsx3
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Ask user what to search
query = input("What do you want to know about? ")

try:
    # Get summary from Wikipedia
    result = wikipedia.summary(query, sentences=2)
    print("Wikipedia says:", result)
    speak(result)
except wikipedia.exceptions.DisambiguationError as e:
    speak("Your query was too broad. Please be more specific.")
    print("Too many options:", e.options[:5])
except wikipedia.exceptions.PageError:
    speak("Sorry, I couldn't find anything on that topic.")
except Exception as e:
    print("Error:", e)
    speak("Something went wrong.")