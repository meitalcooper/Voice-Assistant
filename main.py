import pyttsx3 as tts
import speech_recognition as sr
from selenium_web import *
import datetime
from News import *
from weather import Weather



 
# Initialize the pyttsx3 engine
engine = tts.init()
rate = engine.getProperty('rate') # Get the current speech rate
engine.setProperty('rate', 150)   # Set the speech rate
voices = engine.getProperty('voices') # Get available voices
engine.setProperty('voice', voices[0].id)  # Set to the first voice (male)

def speak(text):
    """Use the text-to-speech capability to say something."""
    engine.say(text)
    engine.runAndWait()



def listen_to_user():
    """
    Convert spoken language into text using the Google speech recognition API.
    This function continuously listens to the microphone and attempts to recognize spoken words.
    """
    r = sr.Recognizer() 
    while True: 
        with sr.Microphone() as source: # Use the default microphone as the audio source
            r.energy_threshold = 10000   # Set the minimum energy level threshold for considering whether a frame is speech
            r.adjust_for_ambient_noise(source, 1.2) # Adjust the recognizer sensitivity to ambient noise
            print("listening..")
            try:
                audio = r.listen(source) # Listen for the first phrase and extract it into audio data
                return r.recognize_google(audio)    # Use Google's API to convert the audio to text            
            except sr.UnknownValueError:
                speak("I'm sorry, I didn't understand you. Could you please repeat that?") # Error handling for unrecognized speech
            except sr.RequestError as e: 
                speak(f"sorry, There was a request error {e} ")   # Error handling for issues with the Google API
                return None

def current_time_of_day():
    """Get the current part of the day."""
    now = datetime.datetime.now()
    hour = int(now.strftime("%H"))

    if hour > 5 and hour < 12:
        return("morning")
    elif hour > 12 and hour < 16:
        return("afternoon")
    else:
        return("evening")
    

def main():
    """ 
    Main function to operate the voice assistant. The function engages in a conversational interface with the user,
    offering various services such as providing information, playing music or videos, delivering news updates,
    and fetching weather forecasts."""
    part_of_day = current_time_of_day()
    speak(f"Good {part_of_day}, I'm your voice assistant. How are you?")
    user_said = listen_to_user()

    if "you" in user_said:
        speak("I'm good, thank you")

    speak("what can I do for you?")
    user_said = listen_to_user()

    if "information" in user_said:
        speak("you need information related to which topic?")
        info = listen_to_user()
        print(info)

        if info:
            print(f"searching {info} in wikipidia ")
            speak(f"searching {info} in wikipidia ")
            information_assistant = Infoweb()
            information_assistant.get_info(info)
   
    elif "play" in user_said or "video" in user_said or "music" in user_said:
        speak("Which one would you like to listen to?")
        video = listen_to_user()
        print(video)

        if video:
            print(f"playing {video} on YouTube")
            speak(f"playing {video} on YouTube")
            music_assistant = Music()
            music_assistant.get_music(video)

    elif "news" in user_said:
        speak("Would you like to hear the news regarding business in the US, TechCrunch, or Wall Street Journal?")
        topic = listen_to_user()
        print(topic)

        if topic:
            if "business" in topic:
                titles = business()
                print(titles)
                speak(titles)
            elif "Tech" in topic:
                titles = techcrunch()
                print(titles)
                speak(titles)
            elif "Wall" in topic :
                titles = wsj()
                print(titles)
                speak(titles)
            else:
                speak("There is no such topic at the moment")
    
    elif "weather" in user_said or "forecast" in user_said:
        speak("What city would you like to know the weather for?")
        city = listen_to_user()
        print(city)
        
        weather_assistant = Weather(city)
        degrees = weather_assistant.get_temperature()
        description = weather_assistant.get_description()

        speak(f"the temperature today in Tel Aviv is {degrees} degrees , and with {description}")
        print(f"the temperature today in Tel Aviv is {degrees} degrees , and with {description}")
        
        
        
        

    

if __name__ == "__main__":
    main()