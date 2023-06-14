import speech_recognition as sr
import pyttsx3
import requests
import json
import socket

class Adam:
    def __init__(self):
        if check_internet_connection():
            speak("All Systems online")
        else:
            speak("cannot connect to the internet")
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
        
        return ""

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def get_weather(self, location):
        api_key = "YOUR_WEATHER_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)
        weather_data = json.loads(response.text)
        
        if weather_data["cod"] == "404":
            return "Sorry, I couldn't retrieve the weather information for that location."

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        result = f"The current weather in {location} is {description} with a temperature of {temperature} degrees Celsius."
        return result

    def get_news(self):
        api_key = "YOUR_NEWS_API_KEY"
        url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        news_data = json.loads(response.text)

        if news_data["status"] == "ok":
            articles = news_data["articles"]
            headlines = [article["title"] for article in articles]
            return headlines

        return "Sorry, I couldn't retrieve the latest news headlines."

    
    def task_management(self, task):
        command = task.lower().split()
        action = command[0]
        app_name = " ".join(command[1:])

        try:
            if action == "open":
                subprocess.Popen(app_name)
                self.speak(f"{app_name} has been opened.")
            elif action == "close":
                subprocess.call(["taskkill", "/f", "/im", app_name])
                self.speak(f"{app_name} has been closed.")
            else:
                self.speak("Sorry, I couldn't understand the task command.")
        except Exception as e:
            self.speak(f"An error occurred: {str(e)}")
    

    def check_internet_connection():
        try:
            # Create a socket object to establish a connection
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False


    def start(self):
        self.speak("Hello, I'm Adam, your virtual helping bot. How can I assist you today?")
        while True:
            user_input = self.listen()
            if user_input.lower() == "quit":
                self.speak("Goodbye!")
                break
            elif "task management" in user_input.lower():
                self.speak("Sure, what task would you like me to manage?")
                task = self.listen()
                response = self.task_management(task)
                self.speak(response)
            elif "information retrieval" in user_input.lower():
                self.speak("What would you like to know?")
                question = self.listen()
                response = self.general_knowledge(question)
                self.speak(response)
            elif "weather updates" in user_input.lower():
                self.speak("Sure, what is your location?")
                location = self.listen()
                response = self.get_weather(location)
                self.speak(response)
            elif "news updates" in user_input.lower():
                self.speak("Here are the latest news headlines:")
                headlines = self.get_news()
                if isinstance(headlines, list):
                    for headline in headlines:
                        self.speak(headline)
                else:
                    self.speak(headlines)
            else:
                self.speak("Sorry, I couldn't understand your request.")
if __name__=="__main__":
    # Create an instance of Adam and start the interaction
    adam_bot = Adam()
    adam_bot.start()
