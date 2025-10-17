import random
import re
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

def wortUmwandler(wort):
  underscores = []
  wort = list(wort)
  length = len(wort)
  for i in range(length):
    underscores.append("_")
  return underscores

def eingabeBuchstabe():
  global counter
  nochmals = True
  while(nochmals != False):
    b = input('Raten sie einen Buchstaben ').lower().strip() #Falls noch ein Leerzeichen eingegeben wurde

    if(len(b) != 1):
       print("Nur einen Buchstaben bitte")
       continue
    
    if(not b.isalpha()):
       print("Nur Buchstaben bitte")
       continue
    
    if(b not in buchstaben):
       nochmals = False

  nochmals = False
  buchstaben.append(b)
  print("Geratene Buchstaben: ", buchstaben)
  if(b in geheimWort):
    for i in range(len(geheimWort)):
      if(b == geheimWort[i]):
          geheim[i] = b
    print("Richtig geraten")
  else:
     counter += 1
     print("Falsch geraten")
    


erneutSpielen = True #Standardmässig auf true, so dass das Spiel startet. Kann vom Benutzer am Ende geändert werden
akzeptabel = False #Zum Wort überprüfen ob dies verwendet werden darf

while(erneutSpielen == True):
    buchstaben = []
    counter = 0 
    while(akzeptabel != True):
      geheimWort = input('Geben Sie bitte das Geheimwort ein').lower()
      geheimWort = re.sub(r'[^A-Za-zÄÖÜäöü ]', '', geheimWort) #Bereinigen der Eingabe, sodass ein cleanes Wort übrigbleibt (Umlaute mitinbegriffen)
      if(" " not in geheimWort):
         akzeptabel = True
    
    geheim = wortUmwandler(geheimWort)
    print(geheim)

    while("_" in geheim and counter != 7): #TODO: AND hangman not full oder so hinzufügen
      print(counter)
      eingabeBuchstabe()
      print("Wort: ", geheim)
      print(HANGMANPICS[counter])
    
    if(counter != 7):
       print("Glückwunsch Sie haben gewonnen :)")
    else:
       print("Leider verloren :()")
      
    akzeptabel = False

    entscheidung = input("Nocheinmal spiele? y/n").lower()
    if(entscheidung == "y"):
       erneutSpielen = True
    else:
       erneutSpielen = False
    


    