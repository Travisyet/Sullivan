import os
import sys
from datetime import datetime
import speech_recognition as sr
from pynput.keyboard import Key, Controller
import pyttsx3
import pygame
import pyautogui



keyboard = Controller()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Vitesse de parole (défaut ~200)
engine.say("")


pygame.init()
pygame.mixer.init()

startS = pygame.mixer.Sound("Start.wav")
#startS.set_volume(0.5)
endS = pygame.mixer.Sound("Start.wav")
#endS.set_volume(0.5)

def listen_mic():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parle .. ")
        audio = r.listen(source)
    try:
        os.system("cls")
        texte = r.recognize_google(audio, language="fr-FR")
        print("tu as dit : " + texte)
        return texte.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Erreur requête API Google Speech; {0}".format(e))
        return None



def record_video():
    print("enregistre la video")
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.f10)
        keyboard.release(Key.f10)

def play_song(son):
    canal = son.play()
    if canal:
        pygame.time.wait(int(son.get_length() * 1000))

def execute_action(commande):
    if "quelle heure est t'il" in commande or "quelle heure il est" in commande or "il est quelle heure" in commande:
        from datetime import datetime
        print("Il est", datetime.now().strftime("%H:%M"))
        engine.say("Il est" + datetime.now().strftime("%H:%M"))
        engine.runAndWait()
    elif "bonjour" in commande:
        engine.say("bonjour a toi.")
        engine.runAndWait()
    elif "mets pause" in commande or "pause" in commande or "enlève pause" in commande or "relance" in commande or "musique" in commande:
        pyautogui.press('playpause')
    elif "enregistre la vidéo" in commande:
        record_video()
    elif "lance spotify" in commande:
        os.system("start Spotify")
    elif "lance un terminal" in commande:
        os.system("start cmd")
    elif "lance powershell" in commande:
        os.system("start powershell")
    elif "lance opéra" in commande or "lance opera" in commande:
        os.system("start Opera")
    elif "lance google" in commande:
        os.system("start chrome")
    elif "lance firefox" in commande:
        os.system("start firefox")
    elif "lance un éditeur de code" in commande:
        os.system("start code")
    elif "lance l'explorateur de fichiers" in commande or "lance l'explorateur" in commande:
        os.system('explorer')
    elif "lance la calculatrice" in commande or "calculatrice" in commande:
        os.system("start calc")
    elif "lance steam" in commande:
        steam_path = r'"C:\Program Files (x86)\Steam\Steam.exe"'
        os.system(f'start "" {steam_path}')
    elif "lance epic" in commande or "lance EPIC" in commande or "lance epic game" in commande:
        epic_path = r'"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe"'
        os.system(f'start "" {epic_path}')
    elif "créer dossier" in commande or "nouveau dossier" in commande or "créer moi un dossier" in commande:
        chemin_dossier = os.path.join(os.path.expanduser("~"), "Desktop", "DossierParSullivan")
        if not os.path.exists(chemin_dossier):
            os.mkdir(chemin_dossier)
            engine.say("Le dossier a été créé sur le bureau.")
        else:
            engine.say("Le dossier existe déjà sur le bureau.")
            engine.runAndWait()
    elif "lance paint" in commande or "lance dessin" in commande:
        os.system("start mspaint")
    elif "au revoir" in commande:
        engine.say("à plus tard.")
        engine.runAndWait()
        sys.exit()
    else:
        engine.say("je n'est pas compris la commande.")
        engine.runAndWait()
        pass


def main_while():
    os.system("cls")
    print("Démarrage de la reconnaissance vocale ....")
    while True:
        texte = listen_mic()
        if texte and "ok sullivan" in texte:
            print("j'écoute ta commande..")
            play_song(startS)
            commande = listen_mic()
            if commande:
                execute_action(commande)
                play_song(endS)
            print("Retour à l'écoute de 'OK-Sullivan'..")


if __name__ == "__main__":
    main_while()
