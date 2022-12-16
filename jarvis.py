import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as pydict
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate' ,150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak( " Good Morning!")

    elif hour >= 12 and hour < 16 :
        speak( " Good Afternoon ")

    elif hour >= 16 and hour < 20 :
        speak( " Good Evening ")

    else :
        speak ( " Good Night ")

    speak(" I am Jarvis How are you How may I help you ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing... ")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said : {query}\n ")
        

    except Exception as e:
        #print(e)

        print(" Say that again please....")
        return "None"
    return query

def Music():
    speak( "Tell me the name of the song")
    musicname = takeCommand().lower()

    if 'music' in musicname:
        speak("Playing")
        print(musicname)
        os.startfile('C:\\Users\\swastik\\Music\\favsongs\\ChaandBaaliyan.mp3')

    elif 'song' in musicname:
        speak("Playing")
        print(musicname)
        os.startfile('C:\\Users\\swastik\\Music\\favsongs\\HaleDil.mp3')

    else:
        speak(f"Playing{musicname}")
        print(musicname)
        pywhatkit.playonyt(musicname)


def openapplication():

    speak("Tell me the name of the application")
    app = takeCommand().lower()

    if 'dev' in app:
        print(app)
        speak(f"opening{app}")
        os.startfile("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")

    elif 'internet' in app:
        print(app)
        speak(f"Opening{app}")
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    elif 'youtube' in app:
        print(app)
        speak(f"Opening{app}")
        webbrowser.open("https://www.youtube.com")

    elif 'instagram' in app:
        print(app)
        speak(f"Opening{app}")
        webbrowser.open("https://www.instagram.com")

    elif 'google maps' in app:
        print(app)
        speak(f"Opening{app}")
        webbrowser.open("https://www.googlemaps.com")
    
    elif 'paint' in app:
        print(app)
        speak(f"Opening{app}")
        webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint")

    

def closeApplication():
    
    speak(" Tell me the name of the application to be closed! ")
    app = takeCommand().lower()

    if 'dev' in app:
        print(app)
        speak(f"closing{app}")
        os.system("TASKKILL /F /im devcpp.exe")

    elif 'chrome' in app:
        print(app)
        speak(f"Closing{app}")
        os.system("TASKKILL /F /im chrome.exe" )

def youtubeAutomate():
    speak("Tell me your Command")
    command = takeCommand().lower()

    if 'stop' in command:
        keyboard.press('space bar')

    elif 'restart' in command:
        keyboard.press('0')

    elif 'forward' in command:
        keyboard.press('l')

    elif 'backward' in command:
        keyboard.press('j')

    elif 'full screen' in command:
        keyboard.press('f')

def chromeAutomate():

    speak("Tell me your command!")
    command = takeCommand().lower()

    if 'close this tab' in command:
        speak("Executing")
        keyboard.press_and_release('ctrl + w')

    if 'open new tab' in command:
        speak("Executing")
        keyboard.press_and_release('ctrl + t')

    if 'history' in command:
        speak("Executing")
        keyboard.press_and_release('ctrl + h')

def dictionary():
    speak("Tell me your query!")
    word = takeCommand().lower()

    if 'meaning' in word:
        word = word.replace("what is the meaning of" , " ")
        result = pydict.meaning(word)
        print(result)
        speak(f" the meaning of {word} is {result}")

    elif 'synonym' in word:
        word = word.replace("what is the synonym of" , " ")
        print(word)
        
        '''synonyms = []
        for syn in wordnet.synsets(word.lower()):
            print(f"hello {word}")
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        print(synonyms)
        speak(synonyms)'''

        result = pydict.synonym(word)
        print(result)
        speak(f" the synonym of {word} is {result}")

    elif 'antonym' in word:
        word = word.replace("what is the antonym of" , " ")
        result = pydict.antonym(word)
        print(result)
        speak(f" the antonym of {word} is {result}")



if __name__ == '__main__':
    #print(pyautogui.size())

    speak(" Hello ")
    wishMe()
    while True:
    #takeCommand()
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak( ' Searching Wikipedia.... ')
            query = query.replace("wikipedia" , " ")
            results = wikipedia.summary(query , sentences = 2)
            speak( " According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play song' in query:
            Music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The Time Now is {strTime}")

        elif 'youtube search' in query:
            speak(" This is what I found on youtube search!")
            query = query.replace("youtube search" , " ")
            web ='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)

        elif 'google search' in query:
            speak(" This is what I found on google search!")
            query = query.replace("google search" , " ")
            pywhatkit.search(query)

        elif 'website' in query:
            query = query.replace("website" , "")
            query = query.replace(" " , " ")
            web1 = query.replace("open" , "")
            print(web1)
            web2 = 'https://' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched")

        elif 'open application' in query:
            openapplication()

        elif 'close application' in query:
            closeApplication()

        elif 'youtube automation' in query:
            youtubeAutomate()

        elif 'chrome automation' in query:
            chromeAutomate()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            print(get)
            speak(get)

        elif 'repeat my word' in query:
            speak( "Speak Sir!")
            get = takeCommand().lower()
            print(f"You Said {get}")
            speak(f"You Said : {get}")

        elif 'dictionary' in query:
            dictionary()
        
        elif 'mouse automation' in query:
            '''d1 = {"zero" : "0" , "one" : "100" , "200" : "hgtfcvhjgjdyt" , "three" : "300" ,
                   "four" : "400" , "five": "500" , "six" : "600" , "seven" : "700" ,
                    "eight": "800" , "nine" : "900" , "ten" : "1000" , "eleven" : "1100" ,
                     "twelve" : "1200" , "thirteen" : "1300" , "fourteen" : "1400"}'''
            speak("The size of the screen is ")
            print(pyautogui.size(),end = '\n')
            speak(pyautogui.size())
            #print("speak the coordinates in the multiple of hundreds" , end = '\n')
            #print(d1)
            speak(" The current position of the mouse pointer is ")
            print(pyautogui.position() , end = '\n')
            speak(pyautogui.position())
            speak("Tell the x coordinate where you want to move ")
            x = takeCommand().lower()
            print('x = ' , x , end = '\n')
            #print(d1[x] , end = '\n')
            speak(" Tell the y coordinate where you want to move ")
            y = takeCommand().lower()
            print('y =' , y , end = '\n')
            #print(d1[y] , end = '\n')
            #pyautogui.moveTo(int(x) , int(y) , duration = 3)
            pyautogui.click(int(x) , int(y) , duration = 2)

        elif 'paint' in query:
            webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint")
            time.sleep(5)
            print("How many sides you want to draw" , end = '\n')
            speak("How many sides you want to draw")
            sides = takeCommand().lower()
            print(" sides = " , sides)

            print(pyautogui.position() , end = '\n')
            speak(" Your current position is " )
            speak(pyautogui.position())

            speak("Enter the starting coordinates of first side ")
            speak(" Enter x coordinate")
            x = takeCommand().lower()
            print(x)
            speak(" Enter y coordinate")
            y = takeCommand().lower()
            print(y)
            pyautogui.moveTo(int(x) , int(y) , duration = 2)
 
            p=int(sides)
            for i in range(p):
                speak(f"Enter the end coordinates of side number {i+1}")
                speak(" Enter x coordinate")
                r = takeCommand().lower()
                print(r)
                speak(" Enter y coordinate")
                s = takeCommand().lower()
                print(s)
                pyautogui.dragTo(int(r) , int(s) , duration = 1)
                if ( i == (p-1)):
                    break
            
            pyautogui.dragTo(int(x) , int(y) , duration = 1)

            



        

        

        

        
        

        


        

        


        

        


        




