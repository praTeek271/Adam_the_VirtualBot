import csv
import speech_recognition as sr
import pyttsx3
import requests
import json
import random

class Adam:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.weather_api_key = "YOUR_WEATHER_API_KEY"
        self.news_api_key = "YOUR_NEWS_API_KEY"
        self.conversations = []

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
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}"
        response = requests.get(url)
        weather_data = json.loads(response.text)
        
        if weather_data.get("cod") == "404":
            return "Sorry, I couldn't retrieve the weather information for that location."

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        result = f"The current weather in {location} is {description} with a temperature of {temperature} degrees Celsius."
        return result

    def get_news(self):
        url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={self.news_api_key}"
        response = requests.get(url)
        news_data = json.loads(response.text)

        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
            headlines = [article["title"] for article in articles]
            return headlines

        return "Sorry, I couldn't retrieve the latest news headlines."

    def task_management(self, task):
        # Implement task management functionality here
        return f"Task '{task}' has been added and will be managed for you."

    def general_knowledge(self, question):
        # Implement general knowledge functionality here
        return f"I don't have the answer to that question at the moment."

    def entertainment(self):
        # Implement entertainment functionality here
        options = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you know that the Earth's atmosphere is primarily composed of nitrogen and oxygen?",
            "What do you call a fish with no eyes? Fsh!",
            "Knock, knock. Who's there? Lettuce. Lettuce who? Lettuce in, it's cold out here!",
            "Did you know that the Great Wall of China is over 13,000 miles long?",
        ]
        return random.choice(options)

    def save_conversations_to_csv(self):
        with open("dataset.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.conversations)

    def start(self):
        self.speak("Hello, I'm Adam, your virtual helping bot. How can I assist you today?")
        while True:
            user_input = self.listen()
            if user_input.lower() == "quit":
                self.speak("Goodbye!")
                self.save_conversations_to_csv()
                break
            elif "task management" in user_input.lower():
                self.speak("Sure, what task would you like me to manage?")
                task = self.listen()
                response = self.task_management(task)
                self.speak(response)
                self.conversations.append([user_input, response])
            elif "information retrieval" in user_input.lower():
                self.speak("What would you like to know?")
                question = self.listen()
                response = self.general_knowledge(question)
                self.speak(response)
                self.conversations.append([user_input, response])
            elif "weather updates" in user_input.lower():
                self.speak("Sure, what is your location?")
                location = self.listen()
                response = self.get_weather(location)
                self.speak(response)
                self.conversations.append([user_input, response])
            elif "news updates" in user_input.lower():
                self.speak("Here are the latest news headlines:")
                headlines = self.get_news()
                if isinstance(headlines, list):
                    for headline in headlines:
                        self.speak(headline)
                        self.conversations.append([user_input, headline])
                else:
                    self.speak(headlines)
                    self.conversations.append([user_input, headlines])
            elif "entertainment" in user_input.lower():
                response = self.entertainment()
                self.speak(response)
                self.conversations.append([user_input, response])
            else:
                self.speak("Sorry, I couldn't understand your request.")
                self.conversations.append([user_input, "Sorry, I couldn't understand your request."])

# Create an instance of Adam and start the interaction
adam_bot = Adam()
adam_bot.start()
