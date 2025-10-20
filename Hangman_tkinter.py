import tkinter as tk
from tkinter import messagebox
import random

HANGMANPICS = [''' ''',''' 

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


with open("woerter.txt", "r", encoding="utf-8") as f:
    woerter = [w.strip().lower() for w in f if w.strip()]
geheimWort = random.choice(woerter)
geheim = ["_"] * len(geheimWort)
buchstaben = []
counter = 0


def eingabeBuchstaben():
    global counter
    nochmals = True
    while(nochmals != False):
        b = eingabe.get().lower().strip() #Falls noch ein Leerzeichen eingegeben wurde
        eingabe.delete(0, tk.END)

        if(len(b) != 1):
            messagebox.showerror("Fehler", "Nur einen Buchstaben bitte")
            return

        if(not b.isalpha()):
            messagebox.showerror("Fehler", "Nur Buchstaben bitte")
            return
    
        if(b not in buchstaben):
            nochmals = False

    nochmals = False
    buchstaben.append(b)
    if(b in geheimWort):
        for i in range(len(geheimWort)):
         if(b == geheimWort[i]):
             geheim[i] = b
        messagebox.showinfo("","Richtig geraten")
    else:
        counter += 1
        messagebox.showinfo("","Falsch geraten")

    geheimLabel.config(text=" ".join(geheim))
    buchstabenLabel.config(text="Geratene Buchstaben : " + ", ".join(buchstaben))
    hangmanLabel.config(text=HANGMANPICS[min(counter, len(HANGMANPICS) - 1)])

    if "_" not in geheim:
        messagebox.showwarning("GEWONNEN", "Du hast ewonnen :)")
        root.destroy()
    elif counter >= len(HANGMANPICS) - 1:
        messagebox.showwarning("VERLOREN", f"Du hast verloren, das Wort war: {''.join(geheimWort)}")
        root.destroy()


root = tk.Tk()
#Window
root.geometry("1000x800")
root.config(bg="#000000")
root.title("Hangman")

#Eingabe
eingabe = tk.Entry(root, text="Buchstaben Eingeben", font=("Arial", 20))
eingabe.pack()

#Geheim
geheimLabel = tk.Label(root, text=" ".join(geheim), font=("Arial", 20))
geheimLabel.pack()

#Geraten
buchstabenLabel = tk.Label(root, text="Geratene Buchstaben: ", font=("Arial", 20))
buchstabenLabel.pack()

#Hangman
hangmanLabel = tk.Label(root, text=HANGMANPICS[counter], font=("Arial",20), bg="#ffffff")
hangmanLabel.pack()

#Button
button = tk.Button(root, text="Prüfen", command=eingabeBuchstaben, font=("Arial", 50))
button.pack(pady=70)

#Start
root.mainloop()




