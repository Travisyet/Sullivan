# Sullivan
![Description](icon.ico) Sullivan est une assistance vocale intelligente conçue pour Windows. Elle permet de lancer des applications, effectuer des actions système, ou encore contrôler la lecture multimédia grâce à la reconnaissance vocale.


---

## Fonctionnalités principales

- Reconnaissance vocale en français avec Google Speech API
- Lancement d’applications courantes : Spotify, navigateurs, terminal, calculatrice, Steam, Epic Games, etc.
- Contrôle multimédia (pause, lecture)
- Gestion du système : création de dossiers sur le bureau, enregistrement vidéo via raccourci clavier
- Retour vocal adapté via synthèse vocale (`pyttsx3`)
- Sons de démarrage et fin de commande intégrés

---

## Prérequis

- Python 3.x
- Modules Python :  
  - `speech_recognition`  
  - `pynput`  
  - `pyttsx3`  
  - `pygame`  
  - `pyautogui`
- Connexion Internet (pour la reconnaissance vocale via Google)
- Microphone fonctionnel

---

## Installation

1. Clonez ce dépôt :
git clone https://github.com/Travisyet/Sullivan.git

2. Placez les fichiers audio `Start.wav` dans le même dossier que le script principal.

---

## Utilisation

Lancez le script principal :
python sullivan.py

Prononcez "Ok Sullivan" pour activer l’écoute de commande vocale, puis utilisez les commandes supportées comme "lance Spotify", "quelle heure est-il", "créer un dossier", ou "au revoir" pour quitter.

---
## commande active :

quelle heure est t'il / quelle heure il est / il est quelle heure
--
bonjour
-
mets pause / pause / enlève pause / relance / musique -- pour mettre pause ou réactiver un son/video 
-
enregistre la vidéo -- pour enregistrer un video via le raccourcie clavier Nvidia ALT + F10 
-
lance spotify -- pour ourvir spotify
-
lance un terminal -- pour ouvrir un simple CMD
-
lance powershell -- pour ouvrir un terminal shell
-
lance opera -- pour lancer OperaGX
-
lance google -- pour lancer google chrome
-
lance firefox -- pour lancer Firefox
-
lance un éditeur de code -- pour lancer VScode
-
lance l'explorateur de fichiers / lance l'explorateur -- pour lancer l'explorateur de fichier
-
lance la calculatrice / calculatrice -- pour utiliser la calculatrice windows
-
lance steam -- pour lancer le launcher Steam
-
lance epic / lance epic game -- pour lancer le launcher Epic Game
-
créer dossier / nouveau dossier / nouveau dossier -- pour cree un nouveau dossier
-
lance paint / lance dessin -- pour lancer paint
-
au revoir -- pour quitter
-
