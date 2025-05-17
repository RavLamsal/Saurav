import pyttsx3
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Step 1: Ask what the user wants to know
query = input("What do you want to know about? ")
speak("You asked about " + query)

try:
    # Step 2: Try to get a summary directly
    result = wikipedia.summary(query, sentences=2)
    print("Wikipedia says:", result)
    speak(result)

except wikipedia.exceptions.DisambiguationError as e:
    # Step 3: If too many meanings, ask user to choose
    speak("Your word is confusing. Here are some options.")
    print("Too many options found for your query. Please pick one:")

    options = e.options[:5]  # show only first 5 to keep it simple
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    try:
        choice = int(input("Enter the number of the option you meant (1-5): "))
        if 1 <= choice <= len(options):
            new_query = options[choice - 1]
            result = wikipedia.summary(new_query, sentences=2)
            print("Wikipedia says:", result)
            speak(result)
        else:
            speak("Invalid choice. Please try again.")
    except:
        speak("Oops. I couldn't understand your number.")

except wikipedia.exceptions.PageError:
    speak("Sorry, I couldn't find anything on that topic.")
except Exception as e:
    print("Unexpected error:", e)
    speak("Something went wrong.")