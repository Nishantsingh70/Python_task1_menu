import os
import pyttsx3
import time


print()
head = "Welcome To My App" 
print(head)
print()
pyttsx3.speak("There are these much functions available which is giving in the list please choose which you want?")
print("1: To open Chrome Browser")
print("2: to open Notepad")
print("3: to open Window Media Player")
print("4: to open Firefox Browser")
print("5: to open Microsoft Edge")
print("6: to open Visual Studio Code")
print("7: to open Microsoft Teams")
print("8: to open Slack")
print("9: to open Virtual Box")
print("10: to open Paint")
print("11: to open Wordpad")
print("12: to open File Explorer")
print()
pyttsx3.speak("Please enter what you want to run")


while True:
     print("Enter your choise: ", end='  ')
     p = input()

     if ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("chrome" in p) or ("chrome browser" in p) or ("Chrome" in p) or ("Chrome Browser" in p):
             pyttsx3.speak("Please wait I am Opening Chrome Browser")
             os.system("chrome")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")

     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("notepad" in p) or ("text editor" in p or "editor" in p) or ("Notepad" in p) or ("Text Editor" in p) or ("Editor" in p):
             pyttsx3.speak("Please wait I am Opening Notepad Text Editor")
             os.system("notepad")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("media player" in p) or ("player" in p) or ("Media Player" in p) or ("Player" in p):
             pyttsx3.speak("Please wait I am Opening Window Media Player")
             os.system("wmplayer")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("firefox" in p) or ("firefox browser" in p) or ("Firefox" in p) or ("Firefox Browser" in p):
             pyttsx3.speak("Please wait I am Opening Firefox Browser")
             os.system("firefox")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("Edge" in p) or ("Microsoft edge" in p) or ("edge" in p) or ("Microsoft Edge" in p):
             pyttsx3.speak("Please wait I am Opening Microsoft Edge")
             os.system("msedge")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("visual studio code" in p) or ("vscode" in p) or ("code" in p) or ("Visual Studio Code" in p) or ("VSCode" in p) or ("Code" in p):
             pyttsx3.speak("Please wait I am Opening Visual Studio Code")
             os.system("code")
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("Microsoft Teams" in p) or ("Teams" in p) or ("Microsoft teams" in p) or ("teams" in p):
             pyttsx3.speak("Please wait I am Opening Microsoft Teams App")
             os.system("Teams")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("slack" in p) or ("slack" in p):
             pyttsx3.speak("Please wait I am Opening Slack")
             os.system("slack")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("Virtual Box" in p) or ("virtual box" in p):
             pyttsx3.speak("Please wait I am Opening VirtualBox")
             os.system("virtualbox")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("paint" in p) or ("Paint" in p):
             pyttsx3.speak("Please wait I am Opening Paint")
             os.system("mspaint")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("wordpad" in p) or ("Wordpad" in p):
             pyttsx3.speak("Please wait I am Opening Wordpad")
             os.system("wordpad")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("run" in p or "execute" in p or "open" in p or "launch" in p or "launching" in p or "want" in p) and ("do not"  not in p) and ("don't"  not in p) and ("file explorer" in p) or ("File Explorer" in p):
             pyttsx3.speak("Please wait I am Opening File Explorer")
             os.system("start ..")
             time.sleep(2)
             pyttsx3.speak("Please choose next option")
             
     elif ("exit" in p) or ("quit" in p):
             break

     else:
             pyttsx3.speak("Do Nothing")
             print("Do Nothing")
