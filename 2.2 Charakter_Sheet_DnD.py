                    #----importe----

import json
import random

                    #----Menüaufbau----

#Speichern und Laden von Charakteren

def speichern(name):
    name = charakter["allgemein"]["name"]
    with open(f"{name}.json", "w", encoding="utf-8") as file:
        json.dump(charakter, file, indent=4, ensure_ascii=False)

def laden(name):
    with open(f"{name}.json", "r", encoding="utf-8") as file:
        return json.load(file)

#Eingabefunktionen mit Fehlerbehandlung
def eingabe_str(text):
    while True:
        try:
            value = input(text)            
            return value
        except ValueError:
            print("\tIch brauche einen Text. Bitte versuche es erneut.\n")

def eingabe_int(text):
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("\tIch brauche eine Zahl. Bitte versuche es erneut.\n")
        if eingabe_int(text) == 0:
            print("\tNegativzahl nicht erlaubt.\n")


def charaktermenue():
    while True:
        print("\t----Charaktermenü----\n\n"
              "\t1. Allgemeine Daten\n"
              "\t2. Würfel- und Skillchecks\n"
              "\t3. Attributswerte\n"
              "\t4. Skills\n"
              "\t5. Kampf\n"
              "\t6. Zauberbereich\n"
              "\t7. Inventar\n"
              "\t8. Skills & Traits\n"
              "\t9. Other\n"
              "\t10. Testbereich/Debugging\n"
              "\t11. Beenden\n\n")
        
        menü = {1 : "Allgemeine Daten",
                 2 : "Würfel und Skillchecks",
                 3 : "Attributswerte",
                 4 : "Skillchecks",
                 5 : "Kampf",
                 6 : "Zauberbereich",
                 7 : "Inventar",
                 8 : "Skills & Traits",
                 9 : "Other",
                 10 : "Testbereich/Debugging",
                 11 : "Beenden"}
        auswahl = eingabe_int("Welche Option willst du einsehen?(1-11)\n\n:> ")
        if auswahl in menü:
            if auswahl == 1:
                allgemeine_daten()
            elif auswahl == 2:
                wuerfel_und_skillchecks()
            elif auswahl == 3:
                attributswerte()
            elif auswahl == 4:
                skillchecks()
            elif auswahl == 5:
                kampf()
            elif auswahl == 6:
                zauberbereich()
            elif auswahl == 7:
                inventar()
            elif auswahl == 8:
                pass
            elif auswahl == 9:
                pass
            elif auswahl == 10:
                testbereich()
                print(f"Du hast '{menü[auswahl]}' gewählt!\n")
            elif auswahl == 11:
                print("Programm wird beendet. Auf Wiedersehen!")
                break
        else:
            print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 11.\n")  


#----Anzeigen im Menü----

skill_mapping = {1 : "athletics",
                 
                2 : "acrobatics",
                3 : "sleight_of_hand", 
                4 : "stealth",
                
                5 : "arcana",
                6 : "history",
                7 : "investigation",
                8 : "nature",
                9 : "religion",

                10 : "animal_handling",
                11 : "insight",
                12 : "medicine",
                13 : "perception",
                14 : "survival",

                15 : "deception",
                16 : "intimidation",
                17 : "performance",
                18 : "persuasion"}

def attributswerte():
                #----attributswerte zeigen----
    while True:
        print("\t----Attributswerte----\n\n")
        for attribut, info in charakter["attribute"].items():
            print(f"{attribut.title()} : {info['wert']}\n"
                  f"Modifikator: {(info['wert'] - 10) // 2}\n"
                  f"Saving throw proficient: {info['save_proficient']}\n\n")
                #----attributswerte ändern----
        print("\t----Attributswerte ändern----\n\n")
        print("Möchstest du Attributswerte ändern? (j/n)  \n\n")
        auswahl = eingabe_str(":> ").lower()
        if auswahl == "j":
            print("welches Attribut möchtest du ändern? (str, dex, con, int, wis, cha)\n\n: >")
            attribut = eingabe_str(":> ").lower()
            if attribut in charakter["attribute"]:
                print(f"Wie viel Punkte möchtest du {attribut.upper()} hinzufügen? (negativ möglich)\n\n:> ")
                punkte = eingabe_int(":> ")
                charakter["attribute"][attribut]["wert"] += punkte
                print(f"{attribut.upper()} hat sich um {punkte} erhöht! Neuer Wert: {charakter['attribute'][attribut]['wert']}\n\n")
                print("möchtest du noch ein Attribut ändern? (j/n)\n\n:> ")
                nochmal = eingabe_str(":> ").lower()
                if nochmal == "j":
                    continue
                else:                    
                    print("zurück zum Hauptmenü")
                    break
        else:
            print("zurück zum Hauptmenü")
            break
                            #zurück zum hauptmenü

def inventar():

    while True:

        print("\n---- Geld ----")
        geld_anzeigen()

        print("\n---- Gegenstände ----\n")

        for gegenstand, info in charakter["inventar"]["items"].items():
            print(f"{gegenstand.title()}")
            print(f"Menge: {info['menge']}\n")

        print(
            "\nWas möchtest du tun?\n"
            "1. Gegenstand benutzen\n"
            "2. Gegenstand kaufen\n"
            "3. Gegenstand verkaufen\n"
            "4. Gegenstand entfernen\n"
            "5. Gegenstand hinzufügen\n" \
            "6. Zurück zum Hauptmenü\n\n"
        )

        auswahl = eingabe_str(":> ")

        # ------------------
        # BENUTZEN
        # ------------------
        if auswahl == "1":
           inventar_benutzen()

        # ------------------
        # KAUFEN
        # ------------------
        elif auswahl == "2":
           inventar_kaufen()

        # ------------------
        # VERKAUFEN
        # ------------------
        elif auswahl == "3":
            inventar_verkaufen()

        # ------------------
        # ENTFERNEN
        # ------------------
        elif auswahl == "4":
            inventar_entfernen()
    
        # ------------------
        # HINZUFÜGEN
        # ------------------
        elif auswahl == "5":
            inventar_hinzufuegen()
        else:        
            print("zurück zum Hauptmenü")
        return

def skillchecks():
                #skills aufrufen und checks durchführen
   while True:
                #----Skills anzeigen----
                print("\t----Skills----\n")
                for nummer, skill in skill_mapping.items():
                    print(f"\t{nummer}. {skill.title()} "
                          f"Modifikator: {get_modifier(skill)}\n")
                print("\t19. Zurück zum Hauptmenü\n")
                #----Skillcheck durchführen----
                skill_nummer = eingabe_int("Welchen check willst du machen? (1-19)\n\n:> ")
                if skill_nummer == 19:
                    print("zurück zum Hauptmenü")
                    break
                elif skill_nummer in skill_mapping:
                    skill_name = skill_mapping[skill_nummer]
                    skillcheck(skill_name)
                    print(f"{skill_name.title()} check durchgeführt!"
                          f" {get_modifier(skill_name)} Modifikator angewendet.")
                else:
                    print("Ungültige Eingabe. Zurück zum Hauptmenü.")
                    continue
                #----noch einen Skillcheck machen?----
                print("Möchtest du noch einen Skillcheck machen? (j/n)")
                nochmal = eingabe_str(":> ").lower()
                if nochmal == "j":
                    continue
                else:
                    print("Zurück zum Hauptmenü")
                    break
   #zurück

def wuerfel_und_skillchecks():
    while True:
        print("\t----Würfel- und Skillchecks----\n\n"
              "\t1. Würfelwurf\n"
              "\t2. Skillcheck\n"
              "\t3. Attribut Saving Throw\n"
              "\t4. Zurück zum Hauptmenü\n\n")
        auswahl = eingabe_int("Welche Option möchtest du wählen? (1-4)\n\n:> ")
        if auswahl == 1:
            anzahl = eingabe_int("Wie viele Würfel? ")
            seiten = eingabe_int("Wie viele Seiten? ")
            bonus = eingabe_int("Welcher Bonus? ")

            würfelwurf(anzahl, seiten, bonus)
        elif auswahl == 2:
            skillchecks()
        elif auswahl == 3:
            attribut_saving_throw()
        else:
            print("zurück zum Hauptmenü")
            break

def allgemeine_daten():
    print("\t----Allgemeine Daten----\n\n")
    for bezeichnung, info in charakter["allgemein"].items():
        print(f"{bezeichnung.title()} : {info}\n\n")
    print("\t1. Daten ändern\n")
    print("\t2. Zurück\n")
    auswahl = eingabe_str("Was möchtest du tun? (1-2)\n\n:> ")
    if auswahl == "1":
            #daten ändern
        print("\t----Allgemeine Daten ändern----\n\n")
        print("\t1. Subklasse\n")
        print("\t2. Alignment\n")
        print("\t3. Level\n")
        print("\t4. Xp\n")
        print("\t5. Zurück\n")
        print("\t(1-5)\n\n")
        auswahl = eingabe_str("Was möchtest du ändern?\nAuswahl:> ")

        if auswahl == "1":
            #subklasse ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Subklassen----\n")
            print("\t1. Schule des Wissens\n")
            print("\t2. Schule des Wagemuts\n")
            print("\t3. Zurück\n\n")

            auswahl = eingabe_str("Wähle\n:> ")
            if auswahl == "1":
                charakter["allgemein"]["subklasse"] = "Schule des Wissens"
                print("Deine Subklasse wurde auf 'Schule des Wissens' geändert!")
            elif auswahl == "2":
                charakter["allgemein"]["subklasse"] = "Schule des Wagemuts"
                print("Deine Subklasse wurde auf 'Schule des Wagemuts' geändert!")
            else:
                print("kehre zurück zum Hauptmenü")
                return
            
        elif auswahl == "2":
            #alignment ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Alignments----\n")
            print("\t1. Rechtschaffend-Gut\n")
            print("\t2. Rechtschaffend-Neutral\n")
            print("\t3. Rechtschaffend-Böse\n")
            print("\t4. Neutral-Gut\n")
            print("\t5. Neutral\n")
            print("\t6. Neutral-Böse\n")
            print("\t7. Chaotisch-Gut\n")
            print("\t8. Chaotisch-Neutral\n")
            print("\t9. Chaotisch-Böse\n")
            print("\t0. Zurück\n\n")

            alignments = {
                "1" : "Rechtschaffend-Gut",
                "2" : "Rechtschaffend-Neutral",
                "3" : "Rechtschaffend-Böse",
                "4" : "Neutral-Gut",
                "5" : "Neutral",
                "6" : "Neutral-Böse",
                "7" : "Chaotisch-Gut",
                "8" : "Chaotisch-Neutral",
                "9" : "Chaotisch-Böse"
            }

            auswahl = eingabe_str(":> ")
            if auswahl in alignments:
                charakter["allgemein"]["alignment"] = alignments[auswahl]
                print(f"Dein Alignment wurde auf '{alignments[auswahl]}' geändert!")
            else:
                print("kehre zurück zum Hauptmenü")
                return
            
        elif auswahl == "3":
            #level ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Level----\n")
            print("\tWelches neue Level hat dein Charakter?\n\n")
            lvl = eingabe_int(":> ")
            if lvl > 1 and lvl < 21:
                charakter["allgemein"]["level"] = lvl
            else:
                print("Dieser Level ist nicht möglich!")
                print("Kehre zurück zum Hauptmenü")
                return
               
        elif auswahl == "4":
            #erfahrung ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Erfahrung----\n\n")
            print("Um wieviel möchtest du deine Erfahrung erhöhen?")
            erfahrung = eingabe_int(":> ")
            charakter["allgemein"]["xp"] += erfahrung
            return
        
        else:
            #zum hauptmenü
            print("kehre zurück zum Hauptmenü")
    else:
        print("Kehre zum Hauptmenü zurück")
        


   #zurück

def muenzwerte():
    print("\t\t1 Platin = 1000 Kupfer")
    print("\t\t1 Gold = 100 Kupfer")
    print("\t\t1 Silber = 10 Kupfer\n\n")



def kampf():
    pass
   #zeige waffen und Zauber
   #würfelchecks und schadenswürfe

def zauberbereich():
    pass
   #zeige Zauberdaten
   #zeige Zauber
   #zeige slots

def inventar_hinzufuegen():
    name = eingabe_str("Welchen Gegenstand willst du hinzufügen?: ").lower()
    anzahl = eingabe_int("Wie viel/e? \nAnzahl: ")
    items = charakter["inventar"]["items"]
    if name in items:
        items[name]["menge"] += anzahl
    else:
        items[name] = {"menge": anzahl}

    print(f"{name} hinzugefügt: {anzahl} an der Zahl\n")

def inventar_kaufen():
    while True:
        name = eingabe_str("Was willst du kaufen?" \
                "Item Name: ").lower()
        anzahl = eingabe_int("Wie viele Stücke? \nAnzahl: ")
        muenzwerte()
        preis = eingabe_int("Preis pro Stück in Kupfer: \nPreis: ")
        if preis <= 0:
            print("Ungültiger Preis.")
            continue

        kosten = preis * anzahl

        if charakter["inventar"]["geld"]["copper"] < kosten:
                    print("Zu wenig Geld.")
                    continue

        geld_ausgeben(kosten)

        items = charakter["inventar"]["items"]

        if name in items:
            items[name]["menge"] += anzahl
        else:
            items[name] = {"menge": anzahl}

            print(f"{name} gekauft: {anzahl}")
        
        nachfrage = eingabe_str("Möchtest du noch etwas kaufen? (j/n)\n\n:> ").lower()
        if nachfrage == "j":
            continue
        else:
            print("zurück zum Inventar")
            break

def inventar_verkaufen():
    while True:
        name = eingabe_str("Welchen Gegenstand willst du verkaufen?: ").lower()

        items = charakter["inventar"]["items"]

        if name not in items:
            print("Nicht vorhanden.")
            continue
            
        anzahl = eingabe_int("Wie viele willst du verkaufen?: ")
        if anzahl > items[name]["menge"]:
            print("Nicht genügend Gegenstände.")
            continue

        muenzwerte()
        preis = eingabe_int("Preis pro Stück in Kupfer: \nPreis: ")

        erlös = preis * anzahl

        geld_hinzufügen(erlös)

        items[name]["menge"] -= anzahl

        if items[name]["menge"] <= 0:
            del items[name]
        print(f"{name} verkauft: {anzahl}\nErlös: {erlös} Kupfer\n")
        print(f"Neue Anzahl: {items[name]['menge']}\n")
        if items[name]["menge"] <= 0:
            print(f"{name} ist jetzt komplett verkauft und wurde aus dem Inventar entfernt.")

        nachfrage = eingabe_str("\n\nMöchtest du noch etwas verkaufen? (j/n)\n\n:> ").lower()
        if nachfrage == "j":
            continue
        else:
            print("zurück zum Inventar")
            break

def inventar_benutzen():
    while True:
        name = eingabe_str("Welchen Gegenstand? willst du benutzen?\n:> ").lower()

        items = charakter["inventar"]["items"]

        if name not in items:
                print("Nicht im Inventar.")
                continue

        item = items[name]

        print(f"Du benutzt {name.title()}")

        if "effekt" in item:
            print(item["effekt"])


def inventar_entfernen():
    while True:
        name = eingabe_str("Welchen Gegenstand willst du entfernen?: ").lower()
        items = charakter["inventar"]["items"]

        if name not in items:
            print("Nicht vorhanden.")
            continue

        anzahl = eingabe_int("Wie viele willst du entfernen?: ")

        items[name]["menge"] -= anzahl

        if items[name]["menge"] <= 0:
            del items[name]
        print(f"{name} entfernt: {anzahl} Stück")


def testbereich():

    while True:

        print("\n----Testbereich----\n")
        print("1. Würfelwurf")
        print("2. Skillcheck")
        print("3. Zurück")

        auswahl = eingabe_str(":> ")

        if auswahl == "1":
            anzahl = eingabe_int("Wie viele Würfel? ")
            seiten = eingabe_int("Wie viele Seiten? ")
            bonus = eingabe_int("Welcher Bonus? ")
            würfelwurf(anzahl, seiten, bonus)

        elif auswahl == "2":
            skillchecks()

        elif auswahl == "3":
            break

        else:
            print("Ungültige Eingabe.")


#----Mechaniken----


#Geldsystem: 1 Platin = 10 Gold = 100 Silber = 1000 Kupfer
def geld_anzeigen():
    kupfer = charakter["inventar"]["geld"]["copper"]

    platin = kupfer // 1000
    kupfer %= 1000

    gold = kupfer // 100
    kupfer %= 100

    silber = kupfer // 10
    kupfer %= 10

    print(f"Platin: {platin}")
    print(f"Gold: {gold}")
    print(f"Silber: {silber}")
    print(f"Kupfer: {kupfer}")

def geld_hinzufügen(kupfer=0):
    charakter["inventar"]["geld"]["copper"] += kupfer

def geld_ausgeben(kupfer=0):
    if charakter["inventar"]["geld"]["copper"] >= kupfer:
        charakter["inventar"]["geld"]["copper"] -= kupfer
    else:
        print("Du hast nicht genug Geld!")

#Proficiency Bonus basierend auf Level

def proficiency_bonus():
      lvl = charakter["allgemein"]["level"]
      if lvl <= 4:
        proficiency_bonus = 2
      elif lvl <= 8:
        proficiency_bonus = 3
      elif lvl <= 12:
        proficiency_bonus = 4
      elif lvl <= 16:
        proficiency_bonus = 5
      else:
        proficiency_bonus = 6
      return proficiency_bonus

#modifikator, würfel, skillcheck, saving throw, passive perception

def get_modifier(skill_name):
    skill = charakter["skills"][skill_name]

    attr_name = skill["attribut"]
    attr = charakter["attribute"][attr_name]["wert"]

    mod = (attr - 10) // 2

    if skill["expertise"]:
        mod += proficiency_bonus() * 2

    elif skill["proficient"]:
        mod += proficiency_bonus()

    return mod

def attribut_modifier(attribut):
    attr = charakter["attribute"][attribut]["wert"]
    mod = (attr - 10) // 2
    return mod

def würfelwurf(anzahl, seiten, bonus=0):
    
    ergebnisse = []
    for _ in range(anzahl):
        wurf = random.randint(1, seiten)
        ergebnisse.append(wurf)
    gesamt = sum(ergebnisse) +(bonus)

    print(f"würfel: {ergebnisse}")

    if bonus != 0:
        print(f"Bonus: {bonus}")

    print(f"Gesamt: {gesamt}")

    return gesamt

def skillcheck(skill_name):
    mod = get_modifier(skill_name)

                    #abfragen advantage/disadvantage/none

    print("\n\tAdvantage ('A')")
    print("\tDisadvantage ('D')")
    print("\toder normal? ('N')\n")
    modus = eingabe_str("Auf was willst du würfeln?\nEntscheidung:> ").lower()

                    #abfertigen modus

    if modus == "a":
        wuerfe = [random.randint(1, 20), random.randint(1, 20)]
        d20 = max(wuerfe)
    elif modus == "d":
        wuerfe = [random.randint(1, 20), random.randint(1, 20)]
        d20 = min(wuerfe)
    else:
        wuerfe = [random.randint(1, 20)]
        d20 = wuerfe[0]

                    #ergebnis skillcheck mit mod
    total = d20 + mod

    print(f"Wurf: {wuerfe}")
    print(f"Modifikator: {mod}")
    print(f"Gesamt(Wurf + Modifikator): {total}")

    return total

def attribut_saving_throw():

    while True:

        print("\t----Attribut Saving Throw----\n")
                #----Saving Throw Attribute holen----
        attribut = eingabe_str(
            "Welchen Saving Throw? (str, dex, con, int, wis, cha, 0 für Hauptmenü)\n:> "
        ).lower()
        if attribut == "0":
            print("zurück zum Hauptmenü")
            break

        if attribut in charakter["attribute"]:

            wert = charakter["attribute"][attribut]["wert"]

            mod = attribut_modifier(attribut)
                #----Proficiency Bonus hinzufügen, falls proficient----
            mod_mit_bonus = mod

            if charakter["attribute"][attribut]["save_proficient"]:

                mod_mit_bonus += proficiency_bonus()

            wurf = random.randint(1, 20)

            gesamt = wurf + mod_mit_bonus
                #----Ergebnis anzeigen----
            print(f"\nWurf: {wurf}")
            print(f"Attributsmodifikator: {mod}")

            if charakter["attribute"][attribut]["save_proficient"]:
                print(f"Proficiency Bonus: +{proficiency_bonus()}")

            print(f"Gesamt: {gesamt}\n")
                #----noch einen Saving Throw machen?----
            nochmal = eingabe_str("Möchtest du noch einen Saving Throw machen? (j/n)\n\n:> ").lower()
            if nochmal == "j":
                continue

        else:
            print("Ungültige Eingabe.")
            break

def passive_perception():
    base = 10
    mod = get_modifier("perception")
    passive_perception = base + mod
    return passive_perception



#----Charakterdaten----


charakter = {
                #----Charakterbogen allgemein----
                    #Name
                    #Klasse
                    #Subklasse
                    #Hintergrund
                    #Glauben
                    #Level
                    #XP
                    #Rasse
                    #Grösse
    "allgemein" : {"name" : "chiro",
                          "klasse" : "barde",
                          "subklasse" : "keine",
                          "hintergrund" : "scharlatan", 
                          "alignment" : "chaotisch neutral", 
                          "level" : 1, 
                          "xp" : 0, 
                          "rasse" : "halbling (leichtfuß)",
                          "grösse" : 75},
                #----Attributes----
                    #Strength
                    #Dexterity
                    #Constitution
                    #Intelligence
                    #Wisdom
                    #Charisma

#Attributswerte

    "attribute" : {
                    "str" : {"wert" : 8, 
                            "save_proficient" : False},
                    "dex" : {"wert" : 16, 
                            "save_proficient" : True},
                    "con" : {"wert" : 13, 
                            "save_proficient" : False},                            
                            "int" : {"wert" : 11,
                            "save_proficient" : False},
                    "wis" : {"wert" : 11, 
                             "save_proficient" : False},
                    "cha" : {"wert" : 17,
                             "save_proficient" : True}},

#----Skills----

    "skills" : {"athletics" : 
                    {"attribut" : "str",
                    "proficient" : False,
                    "expertise" : False},

                "acrobatics" : 
                    {"attribut" : "dex",
                    "proficient" : False,
                    "expertise" : False},
                "sleight_of_hand" : 
                    {"attribut" : "dex",
                    "proficient" : True,
                    "expertise" : False},
                "stealth" : 
                    {"attribut" : "dex",
                    "proficient" : False,
                    "expertise" : False},

                "arcana" : 
                    {"attribut" : "int",
                     "proficient" : False,
                     "expertise" : False},
                "history" :
                    {"attribut" : "int",
                     "proficient" : False,
                     "expertise" : False},
                "investigation" :
                    {"attribut" : "int",
                     "proficient" : False,
                     "expertise" : False},
                "nature" :
                    {"attribut" : "int",
                     "proficient" : False,
                     "expertise" : False},
                "religion" : 
                    {"attribut" : "int",
                     "proficient" : False,
                     "expertise" : False},

                "animal_handling" :
                    {"attribut" : "wis",
                     "proficient" : False,
                     "expertise" : False},
                "insight" :
                    {"attribut" : "wis",
                     "proficient" : False,
                     "expertise" : False},
                "medicine" :
                    {"attribut" : "wis",
                     "proficient" : False,
                     "expertise" : False},
                "perception" : 
                    {"attribut" : "wis",
                     "proficient" : True,
                     "expertise" : False},
                "survival" : 
                    {"attribut" : "wis",
                     "proficient" : False,
                     "expertise" : False},

                "deception" :
                    {"attribut" : "cha",
                     "proficient" : True,
                     "expertise" : False},
                "intimidation" : 
                    {"attribut" : "cha",
                     "proficient" : False,
                     "expertise" : False},
                "performance" : 
                    {"attribut" : "cha",
                     "proficient" : True,
                     "expertise" : True},
                "persuasion" : 
                    {"attribut" : "cha",
                     "proficient" : True,
                     "expertise" : True}},


#-Inventar-
    "inventar" : {
        "items": {
            "rapier" : {"menge" : 1,
                        "Typ" : "Waffe",
                        "schaden" : {"anzahl" : 1, 
                                     "seiten" : 8},
                        "attribut" : "dex",
                        "Schadenstyp" : "Stich",},
            "diplomatenpack" : {"menge" : 1,
                                "Typ" : "Container",
                                "inhalt" : 
                                    {"Parfüm" : 1, 
                                    "Truhe" : 1,
                                    "Schriftrollenbehäler" : 2,   
                                    "Feine Kleidung" : 1,
                                    "Tintenfass" : 1,
                                    "Feder" : 1,
                                    "Lampe" : 1,
                                    "Ölflasche" : 1,
                                    "Blatt Papier" : 1,
                                    "Siegelwachs" : 1,
                                    "Seife" : 1}},

            "fälscherausrüstung" : {"menge" : 1,
                                    "Typ" : "Container",
                                    "inhalt" : 
                                        {"Werkzeug zum Fälschen von Dokumenten\n" : 1,
                                         "Werkzeug zum Fälschen von Siegeln\n" : 1,
                                         "Werkzeug zum Fälschen von Unterschriften\n" : 1}},
            "verkleidungsausrüstung" : {"menge" : 1,
                                        "Typ" : "Container",
                                        "inhalt" : 
                                            {"Kostüm\n" : 1,
                                             "Perücke\n" : 1,
                                             "Make-up\n" : 1}},
            "flöte" :   {"menge" : 1,
                        "Typ" : "Instrument",
                        "effekt" : "\tEine einfache Flöte, die du spielen kannst, um \n"
                        "\tdeine musikalischen Fähigkeiten zu zeigen."},
            "dolch" :   {"menge" : 1,
                        "Typ" : "Waffe",
                        "schaden" : {"anzahl" : 1, 
                                     "seiten" : 4},
                        "attribut" : "dex",
                        "Schadenstyp" : "Stich",},
            "lederrüstung" : {"menge" : 1,
                              "Typ" : "Rüstung",
                              "rüstungswert" : 11,
                              "effekt" : "\tEine leichte Lederrüstung"},},
        "geld" : {"copper" : 1_500},}
}




if __name__ == "__main__":
    charaktermenue()


speichern(charakter["allgemein"]["name"])


#-Kampf-

#Max-Hp
#Hp Aktuell
#Death Saves
#Armor Class
#Initiative
#Speed

#Angriffe

#Zauber
#Kampfzauber
#Zauber



#-Zauberteil-
#Spellmod:
#SpellsaveDC:
#Spellattackbonus:
#Max Spells pro Grad
#I
#II
#III
#IV
#V
#VI
#VII
#VIII
#XIX

#{Zauber : {Schaden : zahl,
#          Reichweite : zahl,
#          Dauer : zahl
#          Casttime : "str",
#          Komponenten : {V : True/False,
#                         G : True/False,
#                         M : True/False},
#          Effekt : Str}}

#-Skills und Traits-

#Skills
#Traits



#-Other-
#passive perception

