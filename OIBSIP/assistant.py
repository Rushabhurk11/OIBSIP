import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen_command():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Wait for 1 second after speaking ends before processing
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Speech Recognition
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except sr.UnknownValueError:
        # If speech is unintelligible, return None
        print("Sorry, I did not understand that. Please try again.")
        return None
    except sr.RequestError:
        # If there's an error in recognizing the speech, notify the user
        print("Sorry, the speech service is not available right now.")
        return None

    return command.lower()

# Function to perform tasks based on the command
def execute_command(command):
    # Respond to greeting
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    # Tell the current time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # Tell the current date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")

    # Open a website
    elif "open" in command:
        if "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        else:
            speak("Which website would you like to open?")
            website = listen_command()
            if website:
                speak(f"Opening {website}")
                webbrowser.open(f"https://{website}.com")

    # Search the web
    elif "search" in command:
        speak("What would you like to search for?")
        query = listen_command()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # Exit the assistant
    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        exit()

    # Respond if command is unrecognized
    else:
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")

# Main loop to run the voice assistant
if __name__ == "__main__":
    speak("Initializing voice assistant. How can I help you today?")
    while True:
        command = listen_command()
        if command:
            execute_command(command)
