#desktop voice assistant 3

import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
from selenium import webdriver
import webbrowser
import os
import random
import PyPDF2
import subprocess
import pywhatkit
import winsound
from win10toast import ToastNotifier
import screen_brightness_control as bright
import wolframalpha
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

app_id = "7RJRAX-P7G25YPP33"
client = wolframalpha.Client(app_id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello Sir, this is SUGAR, your desktop assistant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
    print(Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)

    speak(day)
    speak(month)
    speak(year)

def greet():
    speak("Today is ")
    date()
    speak("Current time")
    time()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir")
        speak("How can I help you")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
        speak("How can I help you")
    elif 18 <= hour < 20:
        speak("Good Evening Sir")
        speak("How can I help you")
    else:
        speak("Good Night Sir")

def takeCommand():
    recog = speech.Recognizer()
    with speech.Microphone() as source:
        print('Listening...')
        recog.pause_threshold = 2
        audio = recog.listen(source)

    try:
        query = recog.recognize_google(audio)
        print("Processing, please wait...")
        print(query)

    except Exception as e:
        print("Could not fetch the command, please repeat...")
        speak("Could not fetch the command, please repeat...")
        return "None"
    return query

greet()
while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("what would you like to search")

            def get_audio():
                note = speech.Recognizer()
                with speech.Microphone() as source:
                    note.pause_threshold = 2
                    audio = note.listen(source)
                    text = ""
                try:
                    print('Searching wikipedia, please wait')
                    speak('Searching wikipedia, please wait')
                    text = note.recognize_google(audio)
                    print(text)
                except Exception as ex:
                    speak('Could not fetch the command')
                return text

            text = get_audio()
            if text != "":
                results = wikipedia.summary(text, sentences=3)
                speak("Wikipedia says, ")
                print(results)
                speak(results)
            else:
                pass

        elif query == 'yt browser':
            webbrowser.open("youtube.com")

        elif query == 'chrome browser':
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            speak('opening youtube')
            path = "C:\\chromewebdrivers\\chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get("https://www.youtube.com")

            speak("what would you like to search")

            def yt_request():
                note = speech.Recognizer()
                with speech.Microphone() as source:
                    note.pause_threshold = 2
                    yt = note.listen(source)
                    text = ""
                try:
                    text = note.recognize_google(yt)
                    print(text)
                    print('searching results')
                    speak('searching results, please wait')
                except Exception as e:
                    speak('Could not fetch the command...')
                return text

            text = yt_request()
            if text != "":
                searchbox = driver.find_element_by_xpath('//*[@id="search"]')
                searchbox.send_keys(text)
                searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
                searchButton.click()
            else:
                pass

        elif 'open google' in query:
            speak('opening google')
            path = "C:\\chromewebdrivers\\chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get("https://www.google.com")

            speak("what would you like to search")

            def get_audio():
                note = speech.Recognizer()
                with speech.Microphone() as source:
                    print('processing request')
                    note.pause_threshold = 2
                    audio = note.listen(source)
                    text = ""
                try:
                    print('searching web, please wait')
                    speak('searching web, please wait')
                    text = note.recognize_google(audio)
                    print(text)
                except Exception as e:
                    speak('Could not fetch the command...')
                return text

            text = get_audio()
            if text != "":
                searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
                searchbox.send_keys(text)
                searchButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
                searchButton.click()
            else:
                pass

        elif query == "play movie" or query == "watch movie":

            speak("which of the following movies would you like to watch?")
            movie_dir = "E:\\AdiTya\\Movies"
            movies_available = os.listdir(movie_dir)
            join_1 = ",\n"
            print(join_1.join(movies_available))

            def movies():
                global movie
                Mov = speech.Recognizer()
                with speech.Microphone() as source:
                    print('select a movie')
                    Mov.pause_threshold = 3
                    audio = Mov.listen(source)
                    movie = ""
                try:
                    movie = Mov.recognize_google(audio)
                    print("playing movie, please wait...")
                    print(movie)
                except Exception as e:
                    print("movie name not recognised")
                return movie

            movie = movies()
            if movie != "":
                if movie == "your name":
                    os.startfile("E:\\AdiTya\\Movies\\Kimi no na wa (Your Name).mp4")
                elif movie == "a silent voice":
                    os.startfile("E:\\AdiTya\\Movies\\Koe no Katachi (A silent voice).mp4")
                elif movie == "i want to eat your pancreas":
                    os.startfile("E:\\AdiTya\\Movies\\Kimi no Suizo o Tabetai (I want to eat your pancreas).mp4")
                elif movie == "weathering with you":
                    os.startfile("E:\\AdiTya\\Movies\\Tenki no ko (Weathering with you).mp4")
                elif movie == "the girl who leapt through time":
                    os.startfile("E:\\AdiTya\\Movies\\Toki o Kakeru Shojo (The Girl who leapt through time).mp4")
                elif movie == "a whisker away":
                    os.startfile("E:\\AdiTya\\Movies\\Nakitai Watashi wa Neko o Kaburu (A Whisker away).mp4")
            else:
                pass

        elif 'play music' in query:
            music_dir = "E:\\AdiTya\\Media\\Music_2"
            music = os.listdir(music_dir)
            join_1 = ",\n"
            print(join_1.join(music))
            os.startfile(os.path.join(music_dir, random.choice(music)))

        elif query == "vs code":
            code_path = "C:\\Users\\TUF\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(code_path)

        elif "play valorant" in query:
            valo_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\VALORANT.lnk"
            os.startfile(valo_path)

        elif query == "covid-19 status" or query == "covid data" or query == "covid-19 cases" or query == "covid-19 updates":
            data = True
            result = None
            globalSummary = None
            countries = None
            while (data):
                try:
                    result = requests.get('https://api.covid19api.com/summary')
                    print(result.json()['Global'])
                    speak(result.json()['Global'])
                    data = False
                except Exception as e:
                    data = True

        elif query == "meeting" or query == "join meeting" or query == "google meet":
            speak("Which meet do you want to join in?")

            def g_meet():
                meeting = speech.Recognizer()
                with speech.Microphone() as source:
                    print('select a meeting')
                    meeting.pause_threshold = 2
                    audio = meeting.listen(source)
                    meet = ""
                try:
                    meet = meeting.recognize_google(audio)
                    print("Joining meeting, please wait...")
                    print(meet)
                except Exception as e:
                    print("could not recognise the meeting id")
                return meet

            meet = g_meet()
            if meet != "":
                if "project" in meet:
                    webbrowser.open("https://meet.google.com/gas-mfmp-pnc")
                elif "mechatronics" in meet:
                    webbrowser.open("https://meet.google.com/nhz-jfnf-bgf")
                elif "python" in meet:
                    webbrowser.open("https://meet.google.com/xow-pdxg-jvy")
            #    elif "psychology" in meet:
            #        webbrowser.open("https://meet.google.com/fzb-poxb-pxe")
            #    elif "philosophy" in meet:
            #        webbrowser.open("https://meet.google.com/pfw-dgog-fsv")
            else:
                pass

        elif query == 'read pdf':
            path = open("C:\\Users\\DELL\\OneDrive\\Desktop\\sy_sem_II\\SDP\\SDP_docs\\SDP_SY_S2_EnTc_Roll. No. 11.pdf", 'rb')
            os.startfile("C:\\Users\\DELL\\OneDrive\\Desktop\\sy_sem_II\\SDP\\SDP_docs\\SDP_SY_S2_EnTc_Roll. No. 11.pdf")

            pdfReader = PyPDF2.PdfFileReader(path)
            from_page = pdfReader.getPage(0)
            text = from_page.extractText()

            speak = pyttsx3.init()
            speak.say(text)
            speak.runAndWait()

        elif query == 'turn off' or query == 'shutdown' or query == 'power off':
            speak("Your computer will shut down in less than a minute")
            os.system("shutdown /s /t 5")

        elif query == 'restart':
            speak("Your computer will restart in less than a minute")
            os.system("shutdown /r /t 5")

        elif query == 'toss a coin' or query == 'coin toss':
            toss = ("Heads", "Tails")
            toss_res = random.choice(toss)
            print(toss_res)
            speak(toss_res)

        elif query == 'roll a dice' or query == 'dice roll':
            roll = ("1", "6", "2", "5", "3", "4")
            roll_face = random.choice(roll)
            print(roll_face)
            speak(roll_face)

        elif query == "what time is it" or query == "what's the time":
            Time = datetime.datetime.now().strftime("%I:%M:%S")
            speak(Time)
            print(Time)

        elif query == "who are you":
            print("I'm SUGAR, your desktop assistant")
            speak("I'm SUGAR, your desktop assistant")

        elif query == "who created you":
            print("I was created as a Project, by Mrunal Sondur")
            speak("I was created as a Project, by Mrunal Sondur")

        elif query == "what is your goal" or query == "what is your aim" or query == "why were you created":
            print("I was created to assist you in your desktop tasks")
            speak("I was created to assist you in your desktop tasks")

        elif query == "are you a robot":
            print("No, I am just a basic computer program")
            speak("No, I am just a basic computer program")

        elif query == "send a text" or query == "send whatsapp":

            def message():
                msg = speech.Recognizer()
                with speech.Microphone() as source:
                    print("what message would like to send")
                    speak("what message would like to send")
                    msg.pause_threshold = 2
                    audio = msg.listen(source)
                    message_wa = ""
                try:
                    print("composing message, please wait")
                    speak("composing message, please wait")
                    message_wa = msg.recognize_google(audio)
                    print(message_wa)
                except Exception as e:
                    speak("did not understand the message...try again")
                return message_wa

            dm = message()

            try:
                pywhatkit.sendwhatmsg_instantly("+91 9689935672", ("Hello there!\nThis is python trial message.\n"+str(dm)))
                print("message sent")
            except Exception as e:
                print("something went wrong")

        elif query == "reminder" or query == "set reminder" or query == "remind me":
            def remind_me_of():
                remind = speech.Recognizer()
                with speech.Microphone() as source:
                    print("what do you want to be reminded of")
                    speak("what do you want to be reminded of")
                    remind.pause_threshold = 2
                    audio = remind.listen(source)
                    notification = ""
                try:
                    notification = remind.recognize_google(audio)
                    print(notification)
                except Exception as e:
                    print("could not recognise the string")
                return notification

            def remind_me_in():
                remind_time = speech.Recognizer()
                with speech.Microphone() as source:
                    print("set reminder timer in seconds")
                    speak("set reminder timer in seconds")
                    remind_time.pause_threshold = 2
                    audio = remind_time.listen(source)
                    rem_time = ""
                try:
                    rem_time = remind_time.recognize_google(audio)
                    print(str(rem_time)+" seconds")
                except Exception as e:
                    print("could not recognise the string")
                return rem_time

            words = remind_me_of()
            sec = int(remind_me_in(), base=10)

            def timer(reminder, duration):
                notificator = ToastNotifier()
                notificator.show_toast("Remainder", "Timer will go off in "+str(sec)+" seconds.", duration=10)
                notificator.show_toast(f"Reminder", reminder, duration=10)
                # for the alarm
                frequency = 2500
                duration = 1000
                winsound.Beep(frequency, duration)

            timer(words, sec)

        elif query == 'change screen brightness' or query == "adjust brightness" or query == "set brightness":
            current_brightness = bright.get_brightness()
            print(current_brightness)
            speak("current screen brightness is")
            speak(current_brightness)
            speak("do you want to change brightness")
            t1 = takeCommand()
            if t1 == 'yes':
                speak("to what level do you want to set brightness")
                t2 = takeCommand()
                bright.set_brightness(t2)
                print(bright.get_brightness())
                speak("brightness level set")

        elif query == "answer this":

            def get_answer():
                question = speech.Recognizer()
                with speech.Microphone() as source:
                    print("ask a question")
                    speak("ask a question")
                    question.pause_threshold = 2
                    audio = question.listen(source)
                    quest = ""
                try:
                    print('searching for answers, please wait')
                    speak('searching for answers, please wait')
                    quest = question.recognize_google(audio)
                    print(quest)
                except Exception as e:
                    speak('did not get the question...try again')
                return quest

            quest = get_answer()
            if quest != "":
                response = client.query(quest)
                answer = next(response.results).quest
                print(answer)
                speak(answer)
            else:
                pass

        elif query == 'make a note' or query == 'write a note' or query == 'notepad' or query == 'open notepad':
            speak("opening notepad")
            speak("select a language")
            print("\nCurrently available languages: \nEnglish\nFrench\nGerman\nSpanish\n")
            lang = takeCommand().lower()

            def get_audio_en():  # for notepad, audio english
                r = speech.Recognizer()
                with speech.Microphone() as source:
                    print("speak the note...")
                    speak("speak the note...")
                    audio = r.listen(source)
                    r.pause_threshold = 2
                    text_notepad = ""
                try:
                    print("Recognizing..")
                    text_notepad = r.recognize_google(audio, language="en-in")
                    print(text_notepad)
                except Exception as e:
                    speak("user took too long to respond...")
                return text_notepad

            def get_audio_fr():  # for getting audio in french
                r = speech.Recognizer()
                with speech.Microphone() as source:
                    print("speak the note...")
                    speak("speak the note...")
                    audio = r.listen(source)
                    r.pause_threshold = 2
                    text_notepad = ""
                try:
                    print("Recognizing..")
                    text_notepad = r.recognize_google(audio, language="fr-fr")
                    print(text_notepad)
                except Exception as e:
                    speak("user took too long to respond...")
                return text_notepad

            def get_audio_de():  # for notepad, audio german
                r = speech.Recognizer()
                with speech.Microphone() as source:
                    print("speak the note...")
                    speak("speak the note...")
                    audio = r.listen(source)
                    r.pause_threshold = 2
                    text_notepad = ""
                try:
                    print("Recognizing..")
                    text_notepad = r.recognize_google(audio, language="de-de")
                    print(text_notepad)
                except Exception as e:
                    speak("user took too long to respond...")
                return text_notepad

            def get_audio_es():  # for notepad, audio spanish
                r = speech.Recognizer()
                with speech.Microphone() as source:
                    print("speak the note...")
                    speak("speak the note...")
                    audio = r.listen(source)
                    r.pause_threshold = 2
                    text_notepad = ""
                try:
                    print("Recognizing..")
                    text_notepad = r.recognize_google(audio, language="es-es")
                    print(text_notepad)
                except Exception as e:
                    speak("user took too long to respond...")
                return text_notepad

            def note(text_notepad):
                date = datetime.datetime.now()
                file_name = str(date).replace(':', '-') + '-note.txt'
                with open(file_name, 'w') as f:
                    f.write(text_notepad)
                subprocess.Popen(["notepad.exe", file_name])

            if lang == "english":
                text_notepad = get_audio_en().lower()
                note(text_notepad)
                print("took a note in english")
                speak("made note of it")

            elif lang == "french":
                text_notepad = get_audio_fr()
                note(text_notepad)
                print("en a pris note")
                speak("took a french note,")

            elif lang == "german":
                text_notepad = get_audio_de()
                note(text_notepad)
                print("habe es mir notiert")
                speak("took a german note")

            elif lang == "spanish":
                text_notepad = get_audio_es()
                note(text_notepad)
                print("tomó nota de ello")
                speak("took a spanish note")

            else:
                speak("The language is currently unavailable!")

        elif query == "stop" or query == "end" or query == "exit":
            exit()