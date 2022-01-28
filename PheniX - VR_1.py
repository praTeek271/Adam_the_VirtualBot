# modules--------
import datetime
import os
import random
import urllib
import webbrowser

try :
    import pyttsx3
    import speech_recognition as sr
    import socket
    from dialog_box1 import *
    from log_file_Generator import log_gen
except ImportError as e:
    from setup import setup_invr
    setup_invr.install()



class Phenix_initiate:
    name=os.getlogin()
    gender="Sir"  # <------------------  CHANGE IT TO YOUR PREFERENCE

    def __init__(self):
        '''defines voice for phenix'''
                    
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        print("initialising'\t'--PheniX---'\t'databases")
        self.engine.setProperty('voice', self.voices[0].id)


    def say(self,text):
        '''speaks up the text given by the user using *Pyttsx3* module'''
        self.engine.say(text)
        self.engine.runAndWait()



    def test_connection(self):
        try:
            socket.create_connection(('Google.com',80))
            return True
        except OSError:
            return False

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            say(f"Good Morning {self.gender}!")
            print(f"Good Morning {self.gender}!!!! nice to meet u")

        elif hour >= 12 and hour < 18:
            say(f"Good Afternoon {self.gender} !!!!!nice to meet u")
            print(f"Good Afternoon {self.gender} !!!!!nice to meet u")

        else:
            say("Good Evening")
            print("Good Evening nice to meet u")

# for speech command-----------------------------------------------************___***************
    def takecommand_from_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Your command'\t'--> ",end="")
            say("Your command   .. ")
            audio = r.listen(source)
        try:
            text_data = r.recognize_google(audio)
            print(text_data)
            say(f"({obj.gender} U asked me to {text_data} ")
            return text_data
        except:
            print("Sorry could not recognize what you said")
            say(f'sorry {obj.gender} i was feeling dizzy , please repeat')
            

# for written commands --------------------------------------------***********___****************
    def takecommand_from_text(self):

        say("tell me how may i help u") 
        a=Recieve_inputData()
        # a = str(input("type your command"))
        return (a)



obj=Phenix_initiate()
say=obj.say

say("Trying to connect to the satellites  ")
say(f"checking for {obj.name}   databases ........")
say('')
say(f" Hello {obj.name} {obj.gender} ,     I am     YOUR VIRTUALY PROGRAMED software bot ...")
obj.wishMe()
#---------------------------------------------------------
while True:
    w=obj.test_connection()
    if w==True:
        say('I am connected online so we can go on with voice commands')
        q = str(obj.takecommand_from_speech())
    else:
        say('I am not connected online so by default we will go on with text commands')
        q=str(obj.takecommand_from_text())
    query = q.lower()
    log_gen(query)


    if 'hello' or 'hi' or 'how r u' or 'how are you' in query:
        answer = random.choice(['whats up dood', 'helo how r u ', 'hi', 'hey'])
        say(answer)
        output=(str(answer))
   
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
        say("opening youtube in chrome browser")
        output=("opening youtube in chrome browser")

    elif "open google" in query:
        webbrowser.open("google.com")
        output=str('opening Google')
    elif " show darkmatter" in query:

        webbrowser.open("wikipedia/darkmatter.com")
        

    elif "play music" in query:

        #CHANGE------------------PATH
        music_dir = 'C:\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        e = random.randint(0, 12)
        os.startfile(os.path.join(music_dir, songs[e]))
        output=str(songs[e])

    elif 'time' or 'tell the time' or 'what is the time' in query:
        strTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
        say(strTime)
        output=str(strTime)

    elif 'who are you' in query:
        say('I am PheniX your assistant ,U can proivide me with any task to ')
        say('i am always ready to do')
        output=str('''I am PheniX your assistant ,U can proivide me with any task to
         i am always ready to do''')

    elif 'who is your creator' or 'your creator details' in query:
        say('i am an advanced system controlled pyhthon virtual machine program which can performs muliple tasking.')
        print("Lusifer Tenison  has used many websites to create me")
        say('Lusifer tenison  has created me')
        output=str(''' i am an advanced system controlled pyhthon virtual machine program which can performs muliple tasking.
                      Lusifer tenison  has created me ''')

    elif 'show your code' in query:
        for i in range(0, 3, 1):
            say('enter the master code')
            print("enter the master code to view the code file:")
            print()
            print()
            input1 = input()
            if input1 == "0078":

                os.startfile('D:\\_cache_\\code.txt')
                say('here i present the code')
                say('do not try to manupulate it')

            else:
                print("ERROR MASTER CODE DOESN`T MACHES THE ORIGINAL CODE")
                say('error in code:')
                print("TRY AGAIN")

        say('Sorry,I cannot show you the sourcecode as you were not able to tell the master code')
        say('...... You are not concidered as authenticate')
        output=str("-------Authentication Revoked-------")

    elif 'tell me about history of india' in query:
        webbrowser.open(
            'https://knowindia.gov.in/culture-and-heritage/ancient-history.php')
        output=str('showing data on the chrome web browser')
    
    elif 'calculate the following' in query:
        os.startfile('C:\\Windows\\system32\\calc.exe')

    elif 'shutdown the pc' or 'shutdown' in query:
        os.system("shutdown")
        output=str('Shutdowning...........')

    elif 'quit' or 'close' in query:
        break
   
quit()