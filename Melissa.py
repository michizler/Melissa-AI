import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Yes sir! I'm pleased to have you back.")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon Sir!")
    elif hour >= 17 and hour <= 20:
        speak("Good Evening Sir!")
    else:
        speak("Goodnight Sir!")

    speak("Melissa is always here for you. How may I be of service Sir?")

 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again Sir...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('brightuzosike@gmail.com', 'bright12345')
    server.sendmail('brightuzosike@gmail.com', to, content)
    server.close()

def introduce():
    speak("That would really be nice sir. Love to know the person's name")
    takecommand()
    speak("Wow! You really do have a beautiful name. I'll ensure not to forget it. Mine is Melissa. Bright created me to be his assistant.")
    speak("But I'll love to show you what I can do. What would you like?")
    return query

def GuessMe():
    speak("Welcome to my challenge.")
    # --- Measures to handle exceptions ---- #
    speak("Here are some things to take note of before we begin:")
    print("\n** You are required to select a difficulty to begin your challenge.")
    speak("You are required to select a difficulty to begin your challenge.")
    print("\n** All guesses should be entered in integers.")
    speak("All guesses should be entered in integers. Great. Now you know the rules, let's begin!!")

    PlayOneRound()

    while True:     # --- Allow for continous playing till user says otherwise --- #
        speak("Say 'Yes' to continue or 'No' to quit")
        goAgain = takecommand().upper()
        if 'NO' in goAgain:
            speak("Thank you for playing my challenge. Till next time. Cheers.")
            break
        else:
            PlayOneRound()

def PlayOneRound():
    levels = ["Easy", "Medium", "Hard", "Legend", "Wizard"]     # --- Difficulty to make the game challenging and interesting --- #
    speak("These are the levels I have for you")
    print("\nDifficulty:-")

    for level in levels:
        print("=> {}".format(level))
        speak("{}".format(level))

    speak("Please select a difficulty")
    difficulty = takecommand().title()
    if "Easy" in difficulty:
        MAX_GUESS = 5
        MAX_RANGE = 25
    elif "Medium" in difficulty:
        MAX_GUESS = 5
        MAX_RANGE = 50
    elif "Wizard" in difficulty:
        MAX_GUESS = 5
        MAX_RANGE = 200
    elif "Legend" in difficulty:
        MAX_GUESS = 5
        MAX_RANGE = 100
    else:
        MAX_GUESS = 5
        MAX_RANGE = 75
    maxrange_comment = "Here's how it goes; I'll pick a number between 1 and ",MAX_RANGE,". Try guessing the number."
    maxguess_comment = "Alright, let's see how lucky you feel. You have",MAX_GUESS,"trials."
    print("Alright, let's see how lucky you feel. You have",MAX_GUESS,"trials.")
    print("\nHere's how it goes; I'll pick a number between 1 and ",MAX_RANGE,". Try guessing the number.")
    speak(maxguess_comment)
    speak(maxrange_comment)
    
    target = random.randrange(1,MAX_RANGE + 1)
    guesscounter = 0
    trials = 5
    while True:     # ---- Loop the guessing process --- #
        speak("Take a guess")
        userGuess = int(input("Your guess? "))
        guesscounter += 1
        trials -= 1
        congrats_comment = "Congrats!! You got the number right in",guesscounter,"attempt"
        correct_answer = "The number I had in mind was",target,". Better Luck in the future."
        trials_comment = "You have",trials,"trials left."
        
        if userGuess == target and guesscounter == 1:
            speak("Boy!! You must be a Wizard because that is incredible and definitely not natural")
            print(congrats_comment)
            speak(congrats_comment)
            break

        elif userGuess == target and guesscounter == 2:
            speak("Hot stuff man! You are blazing. Who got some ice please?")
            print(congrats_comment)
            speak(congrats_comment)
            break

        elif userGuess == target and guesscounter == 3:
            speak("Nice going. You're good at this.")
            print(congrats_comment)
            speak(congrats_comment)
            break

        elif userGuess == target and guesscounter == 4:
            speak("Spot on. Shows how adaptable you are.")
            print(congrats_comment)
            speak(congrats_comment)
            break

        elif userGuess == target and guesscounter == 5:
            speak("LOL!! You must really be lucky today because this was your last try. All the same, nice job.")
            print(congrats_comment)
            speak(congrats_comment)
            break
        
        elif userGuess > target and guesscounter != MAX_GUESS:
            speak("Nice effort. Just a bit high off.")
            speak(trials_comment)
            speak("Go again.")

        elif userGuess < target and guesscounter != MAX_GUESS:
            speak("Not a chance. That's too low.")
            speak(trials_comment)
            speak("Try a higher guess this time.")

        else:       # ---- Gameover ---- #
            speak("Sorry, you've exhausted your chances. Maybe next time, you'll get it right.")
            print(correct_answer)
            speak(correct_answer)
            speak("Try playing again.")
            break

def Quit():
    speak("You got it sir. Going offline.")
    quit()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'search' in query:
            speak("Give me a second sir!")
            query = query.replace("search", "")
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(result)
        elif 'send an email' in query:
            try:
                speak("What should I say sir?")
                content = takecommand()
                to = 'cassandrauzosike@yahoo.com'
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Unable to send email sir")
            

        elif 'website' in query:
            speak("What website sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')


        elif 'logout' in query:
            try:
                speak("Logging out sir")
                os.system("shutdown -1")
            except Exception as e:
                print(e)
                speak("Unable to do that sir")

        elif 'shutdown' in query:
            try:
                speak("Shutting down sir")
                os.system("shutdown /s /t 1")
            except Exception as e:
                print(e)
                speak("Unable to do that sir")

        elif 'restart' in query:
            try:
                speak("Restarting sir")
                os.system("shutdown /r /t 1")
            except Exception as e:
                print(e)
                speak("Unable to do that sir")

        elif 'play music' in query or 'play a song' in query:
            songs_dir = 'C:/Users/BRIGHT UZOSIKE/Music'
            songs = random.choice(os.listdir(songs_dir))
            os.startfile(os.path.join(songs_dir,songs))
            Quit()

        elif 'introduce you' in query or 'introduce' in query:
            introduce()
           
        elif 'game' in query:
            speak("Oh lovely. I'm positive about the challenge I have for you.")
            GuessMe()   

        elif 'offline' in query:
            Quit()
            

        

        