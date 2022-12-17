import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import keyboard
import pyjokes
import requests
import geocoder
import subprocess
import time
import sys
from PyDictionary import PyDictionary as pydict
from subprocess import Popen
from bs4 import BeautifulSoup
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import warnings
warnings.filterwarnings("ignore")


# import random
# import nltk
# from nltk.corpus import wordnet

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate' ,150)


def speak(audio):
    engine.say(audio)
    print(f" Assistant: {audio}")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning User!")

    elif hour >= 12 and hour < 16 :
        speak("Good Afternoon User!")

    elif hour >= 16 and hour < 21 :
        speak("Good Evening User!")

    else :
        speak("Hello User!")

    speak("I am your virtual assistant. How may I help you today?") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(" \n Listening....")
        audio = r.listen(source)

    try:
        print(" Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f" \n User said: {query}\n")
        
    except:
        print(" \n I didn't catch that, say that again please....")
        return "None"
    
    return query.lower()

def music():
    speak("Please tell me the name of the song?")
    musicname = takeCommand()
    while musicname == "None":
        musicname = takeCommand()
    else:
        speak(f"Playing {musicname}")
        pywhatkit.playonyt(musicname)

def openApplication():

    speak("Please tell me the name of the application?")
    app = takeCommand()

    if 'browser' in app or 'chrome' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    
    elif 'edge' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    elif 'note' in app or 'notes' in app or 'notepad' in app or 'editor' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Windows\System32\notepad.exe")

    elif 'vlcplayer' in app or 'player' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files\VideoLAN\VLC\vlc.exe")

    elif 'telegram' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Users\mayan\AppData\Roaming\Telegram Desktop\Telegram.exe")

    elif 'excel' in app or 'msexcel' in app or 'sheet' in app or 'winexcel' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

    elif 'slide' in app or 'mspowerpoint' in app or 'ppt' in app or 'powerpnt' in app or 'powerpoint' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
    
    elif 'word' in app or 'msword' in app:
        speak(f"Opening {app}")
        Popen(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

def closeApplication():
    
    speak("Please tell me the name of the application to be closed?")
    app = takeCommand()
    
    if 'browser' in app or 'chrome' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im chrome.exe")

    elif 'edge' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im msedge.exe")
    
    elif 'note' in app or 'notes' in app or 'notepad' in app or 'editor' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im notepad.exe")
       
    elif 'vlcplayer' in app or 'player' in app or 'vlc' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im vlc.exe")
        
    elif 'telegram' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im Telegram.exe")

    elif 'excel' in app or 'msexcel' in app or 'sheet' in app or 'winexcel' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im excel.exe")

    elif 'slide' in app or 'mspowerpoint' in app or 'ppt' in app or 'powerpnt' in app or 'powerpoint' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im powerpnt.exe")
    
    elif 'word' in app or 'msword' in app:
        speak(f"Closing {app}")
        os.system("TASKKILL /F /im winword.exe")

def youtubeAutomate():
    speak("Please tell me your command?")
    command = takeCommand()

    if 'stop' in command:
        keyboard.press('space bar')

    elif 'start' in command:
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

    speak("Please tell me your command?")
    command = takeCommand()

    if 'close tab' in command:
        speak("Executing...")
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        speak("Executing...")
        keyboard.press_and_release('ctrl + t')

    elif 'history' in command:
        speak("Executing...")
        keyboard.press_and_release('ctrl + h')

def screenshot():
    speak("Okay! What should be the name of the file?")
    name = takeCommand()
    while name == "None":
        name = takeCommand()
    else:
        filename = name + ".png"
        path = "C:\\Users\\mayan\\Desktop\\"+filename
        ss = pyautogui.screenshot()
        ss.save(path)
        speak("Screenshot saved successfully on Desktop!")
    
        speak("Do you want me to open that screenshot?")
        reply = takeCommand()
        while reply == "None":
            reply = takeCommand()
        else:
            if 'yes' in reply or 'okay' in reply or 'ok' in reply or 'alright' in reply:
                speak("Here is your screenshot.")
                os.startfile("C:\\Users\\mayan\\Desktop\\"+filename)
            elif 'no' in reply:
                speak("Alright")
                return None

def weather():
    speak("Which city's weather you want to know?")
    city=takeCommand()
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=e7edd9a0f2ca05ffc0cfa070120cc387".format(city)
    res=requests.get(url)
    data=res.json()
    climate=data["weather"][0]["description"]
    temp=data['main']['temp']
    temp=round(temp-273.15,2)    
    wind=data["wind"]["speed"]
    humidity=data["main"]["humidity"]
    cloud=data["clouds"]["all"]
    pressure=data['main']["pressure"]
    speak("Todays climate is "+climate+
    "\n\t    Average Temperature is "+str(temp)+" Degree Celcius"+ 
    "\n\t    WindSpeed is "+str(wind)+" meters per second"+
    "\n\t    Humidity is "+str(humidity)+"%"+
    "\n\t    Its "+str(cloud)+" percent cloudy"+
    "\n\t    Air pressure is at "+ str(pressure)+"hpa")

def My_Location():
    ip_add = requests.get("https://api.ipify.org").text
    url = "http://api.ipapi.com/" + ip_add + '?access_key=7f5bf971c5dc162849260a87a2871c1d'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country_name']
    speak(f"Your current location is {state, country}.")

def GoogleMaps(Place):
    url_place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place, addressdetails= True)
    target_latlon = location.latitude , location.longitude
    webbrowser.open(url=url_place)
    location = location.raw['address']
    target = {'City' : location.get('city',''),
                'State' : location.get('state',''),
                'Country' : location.get('country','')}
    current_loc = geocoder.ip('me')
    current_latlon = current_loc.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    speak(target)
    speak(f'{Place} is {distance} kilometers away from your location.')

def Notepad():
    speak("Please tell me the query?")
    speak("I am ready to write.")
    writes = takeCommand()
    time = datetime.datetime.now().strftime("%H:%M")
    filename = str(time).replace(":","-") + "-note.txt"
    with open("C:\\Users\\mayan\\Desktop\\"+filename, 'w') as file:
        file.write(writes)
    path = "C:\\Users\\mayan\\Desktop\\" +str(filename)
    os.startfile(path)

def Alarm(query):
    timehere = open("C:\\Users\\mayan\\Desktop\\assistant\\data.txt",'a')
    timehere.write(query)
    timehere.close()
    Popen([sys.executable, 'C:\\Users\\mayan\\Desktop\\assistant\\alarm.py'], stderr=subprocess.STDOUT)
    speak("Your alarm has been set successfully!")


if __name__ == '__main__': 
    print("")
    wishMe()

    while True:
        query = takeCommand()

        if 'hello' in query or 'hi' in query:
            speak("Hello User! What would you like me to do?")
        
        elif 'how are you' in query:
            speak("I am great! What about you?")

        elif 'bye' in query:
            speak("Goodbye! You can call me anytime you need.")
            break
        
        elif 'what can you do' in query or 'help' in query:
            speak("I can do many things to help you in your daily life! Here is a list of them: ")
            print("  1. Play music\n  2. Search Wikipedia\n  3. Open Applications\n  4. Close Applications\n  5. Open Websites\n  6. Tell you time")
            print("  7. Youtube search\n  8. Google search\n  9. Youtube Automation\n  10. Chrome Automation\n  11. Crack Jokes :)") 
            print("  12. Repeat your word\n  13. Find meanings\n  14. Take screenshots\n  15. Set Reminder\n  16. Check weather")
            print("  17. Search location via Google Maps\n  18. Write a note\n  19. Set Alarm (eg. set alarm for 10 and 30 AM)\n  20. Control mouse cursor (mouse automation)")

        elif 'wikipedia' in query:
            try:
                speak("Searching Wikipedia.... ")
                query = query.replace("wikipedia" , " ")
                results = wikipedia.summary(query , sentences = 2)
                speak("According to Wikipedia:")
                speak(results)
            
            except:
                speak("I am sorry! I didn't find any matching results on Wikipedia.")

        elif 'open youtube' in query:
            query = query.replace("open","").replace(" ","")
            speak(f"Opening {query}")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            query = query.replace("open","").replace(" ","")
            speak(f"Opening {query}")
            webbrowser.open("https://www.google.com")

        elif 'instagram' in query:
            speak(f"Opening {query}")
            webbrowser.open("https://www.instagram.com")

        elif 'google map' in query:
            speak(f"Opening {query}")
            webbrowser.open("https://www.googlemaps.com")
        
        elif '.com' in query or '.org' in query or '.in' in query or '.net' in query:
            speak("Okay! Launching website...")
            query = query.replace("open","").replace("launch","").replace("website","").replace(" ","")
            web = "https://www."+query
            webbrowser.open(web)
        
        elif 'song' in query or 'music' in query:
            music()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time now is {strTime}")

        elif 'youtube search' in query:
            speak("This is what I found on youtube search!")
            query = query.replace("youtube search" , " ")
            web ='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)

        elif 'google search' in query:
            import wikipedia as googleScrap
            speak("This is what I found on google search!")
            query = query.replace("google search","").replace("google","")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No speakable data available!")

        elif 'open application' in query:
            openApplication()

        elif 'close application' in query:
            closeApplication()

        elif 'youtube automation' in query:
            youtubeAutomate()
        
        elif 'stop' in query or 'pause' in query:
            keyboard.press('space bar')

        elif 'start' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'forward' in query:
            keyboard.press('l')

        elif 'backward' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'chrome automation' in query:
            chromeAutomate()

        elif 'close tab' in query:
            speak("Executing...")
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            speak("Executing...")
            keyboard.press_and_release('ctrl + t')

        elif 'history' in query:
            speak("Executing...")
            keyboard.press_and_release('ctrl + h')

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my word' in query:
            speak("Okay! Please tell me the word to repeat?")
            get = takeCommand()
            speak(f"You Said : {get}")

        elif 'meaning' in query:
            query = query.replace("find","").replace("what","").replace("is","").replace("the","").replace("meaning","").replace("of","").replace(" ","")
            result = pydict.meaning(query)
            speak(f"The meaning of {query} is {result}")
        
        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query or 'set reminder' in query:
            rememberMsg = query.replace("remember that","").replace("set reminder","")
            speak(f"Following reminder has been set: {rememberMsg}")
            file = open('data.txt','w')
            file.write(rememberMsg)
            file.close()
        
        elif 'what do you remember' in query or 'remind me' in query:
            file = open('data.txt','r')
            speak(f"Here is your reminder: {file.read()}")

        elif 'temperature' in query or 'weather' in query:
            weather()

        elif 'my location' in query:
            My_Location()
        
        elif 'where is' in query or 'search location' in query:
            Place = query.replace("where is ","").replace("where is the location ","").replace("search location ","")
            GoogleMaps(Place)
        
        elif 'write a note' in query:
            Notepad()
        
        elif 'set alarm' in query:
            Alarm(query)

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
            Popen(r"C:\Windows\System32\notepad.exe")
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