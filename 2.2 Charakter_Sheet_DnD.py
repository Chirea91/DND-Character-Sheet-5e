                    #----importe----

import random

                    #----Menüaufbau----

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
        auswahl = input("Welche Option willst du einsehen?(1-11)\n\n:> ")
        if auswahl == "1":
            allgemeine_daten()
        elif auswahl == "2":
            wuerfel_und_skillchecks()
        elif auswahl == "3":
            attributswerte()
        elif auswahl == "4":
            skillchecks()
        elif auswahl == "5":
            pass
        elif auswahl == "6":
            pass
        elif auswahl == "7":
            inventar()        
        elif auswahl == "8":
            pass        
        elif auswahl == "9":
            pass
        elif auswahl == "10":
            testbereich()
        else:
            print("Beende Charaktermenü")
            break

#----Anzeigen im Menü----

skill_mapping = {"1" : "athletics",
                 
                "2" : "acrobatics",
                "3" : "sleight_of_hand", 
                "4" : "stealth",
                
                "5" : "arcana",
                "6" : "history",
                "7" : "investigation",
                "8" : "nature",
                "9" : "religion",

                "10" : "animal_handling",
                "11" : "insight",
                "12" : "medicine",
                "13" : "perception",
                "14" : "survival",

                "15" : "deception",
                "16" : "intimidation",
                "17" : "performance",
                "18" : "persuasion"}

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
        auswahl = input(":> ").lower()
        if auswahl == "j":
            print("welches Attribut möchtest du ändern? (str, dex, con, int, wis, cha)\n\n: >")
            attribut = input(":> ").lower()
            if attribut in charakter["attribute"]:
                print(f"Wie viel Punkte möchtest du {attribut.upper()} hinzufügen? (negativ möglich)\n\n:> ")
                punkte = int(input(":> "))
                charakter["attribute"][attribut]["wert"] += punkte
                print(f"{attribut.upper()} hat sich um {punkte} erhöht! Neuer Wert: {charakter['attribute'][attribut]['wert']}\n\n")
                print("möchtest du noch ein Attribut ändern? (j/n)\n\n:> ")
                nochmal = input(":> ").lower()
                if nochmal == "j":
                    continue
                else:                    
                    print("zurück zum Hauptmenü")
                    break
        else:
            print("zurück zum Hauptmenü")
            break
                            #zurück zum hauptmenü

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
                skill_nummer = input("Welchen check willst du machen? (1-19)\n\n:> ")
                if skill_nummer == "19":
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
                nochmal = input(":> ").lower()
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
        auswahl = input("Welche Option willst du einsehen?(1-4)\n\n:> ")
        if auswahl == "1":
            anzahl = int(input("Wie viele Würfel? "))
            seiten = int(input("Wie viele Seiten? "))
            bonus = int(input("Welcher Bonus? "))

            würfelwurf(anzahl, seiten, bonus)
        elif auswahl == "2":
            skillchecks()
        elif auswahl == "3":
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
    auswahl = input("Wähle Option(1, 2)\n\nAuswahl:> ")

    if auswahl == "1":
            #daten ändern
        print("\t----Allgemeine Daten----\n\n")
        print("\t1. Subklasse\n")
        print("\t2. Alignment\n")
        print("\t3. Level\n")
        print("\t4. Xp\n")
        print("\t5. Zurück\n")
        print("\t(1-5)\n\n")
        auswahl = input("Auswahl:> ")

        if auswahl == "1":
            #subklasse ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Subklassen----\n")
            print("\t1. Schule des Wissens\n")
            print("\t2. Schule des Wagemuts\n")
            print("\t3. Zurück\n\n")

            auswahl = input("Wähle\n:> ")
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
            auswahl = input(":> ")
            if auswahl == "1":
                charakter["allgemein"]["alignment"] = "Rechtschaffend-Gut"
                print("Dein Alignment hat sich auf Rechtschaffend-Gut verändert!")
            elif auswahl == "2":
                charakter["allgemein"]["alignment"] = "Rechtschaffend-Neutral"
                print("Dein Alignment hat sich auf Rechtschaffend-Neutral verändert!")
            elif auswahl == "3":
                charakter["allgemein"]["alignment"] = "Rechtschaffend-Böse"
                print("Dein Alignment hat sich auf Rechtschaffend-Böse verändert!")
            elif auswahl == "4":
                charakter["allgemein"]["alignment"] = "Neutral-Gut"
                print("Dein Alignment hat sich auf Neutral-Gut verändert!")
            elif auswahl == "5":
                charakter["allgemein"]["alignment"] = "Neutral"
                print("Dein Alignment hat sich auf Neutral verändert!")
            elif auswahl == "6":
                charakter["allgemein"]["alignment"] = "Neutral-Böse"
                print("Dein Alignment hat sich auf Neutral-Böse verändert!")
            elif auswahl == "7":
                charakter["allgemein"]["alignment"] = "Chaotisch-Gut"
                print("Dein Alignment hat sich auf Chaotisch-Gut verändert!")
            elif auswahl == "8":
                charakter["allgemein"]["alignment"] = "Chaotisch-Neutral"
                print("Dein Alignment hat sich auf Chaotisch-Neutral verändert!")
            elif auswahl == "9":
                charakter["allgemein"]["alignment"] = "Chaotisch-Böse"
                print("Dein Alignment hat sich auf Chaotisch-Böse verändert!")
            else:
                print("kehre zurück zum Hauptmenü")
                return
            
        elif auswahl == "3":
            #level ändern
            print("\t----Allgemeine Daten----\n\n")
            print("\t----Level----\n")
            print("\tWelches neue Level hat dein Charakter?\n\n")
            lvl = int(input(":> "))
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
            erfahrung = int(input(":> "))
            charakter["allgemein"]["xp"] += erfahrung
            return
        
        else:
            #zum hauptmenü
            print("kehre zurück zum Hauptmenü")
    else:
        print("Kehre zum Hauptmenü zurück")
        


   #zurück



def kampf():
    pass
   #zeige waffen und Zauber
   #würfelchecks und schadenswürfe

def zauberbereich():
    pass
   #zeige Zauberdaten
   #zeige Zauber
   #zeige slots

def inventar():

    while True:

        print("\n---- Geld ----")
        geld_anzeigen()

        print("\n---- Gegenstände ----\n")

        for gegenstand, info in charakter["inventar"].items():
            if gegenstand == "geld":
                continue
            print(f"{gegenstand.title()}")
            print(f"Anzahl: {info['menge']}\n")

        print(
            "\nWas möchtest du tun?\n"
            "1. Gegenstand benutzen\n"
            "2. Gegenstand verkaufen\n"
            "3. Gegenstand entfernen\n"
            "4. Zurück zum Hauptmenü\n"
        )

        auswahl = input(":> ")

        # ------------------
        # Gegenstand benutzen
        # ------------------

        if auswahl == "1":
            gegenstand = input("Welchen Gegenstand möchtest du benutzen?\n:> ").lower()

            if gegenstand not in charakter["inventar"]:
                print("Dieser Gegenstand ist nicht im Inventar.")
                continue

            if gegenstand == "geld":
                print("Geld kann nicht benutzt werden.")
                continue
            print(f"\nDu benutzt {gegenstand.title()}!")

            info = charakter["inventar"][gegenstand]
            if "effekt" in info:
                print(f"\nEffekt:\n{info['effekt']}")
            else:
                print("Dieser Gegenstand hat keinen besonderen Effekt.")

        # ------------------
        # Gegenstand verkaufen
        # ------------------

        elif auswahl == "2":

            gegenstand = input("Welchen Gegenstand möchtest du verkaufen?\n:> ").lower()

            if gegenstand not in charakter["inventar"]:
                print("Dieser Gegenstand ist nicht im Inventar.")
                continue

            if gegenstand == "geld":
                print("Geld kann nicht verkauft werden.")
                continue

            preis = int(input("Wie viel Kupfer erhältst du dafür?\n:> "))
            geld_hinzufügen(preis)
            charakter["inventar"][gegenstand]["menge"] -= 1
            if charakter["inventar"][gegenstand]["menge"] <= 0:
                charakter["inventar"].pop(gegenstand)
            print(f"{gegenstand.title()} verkauft."
                  f" Du erhältst {preis} Kupfer.")

        # ------------------
        # Gegenstand entfernen
        # ------------------

        elif auswahl == "3":

            gegenstand = input("Welchen Gegenstand möchtest du entfernen?\n:> ").lower()

            if gegenstand not in charakter["inventar"]:
                print("Dieser Gegenstand ist nicht im Inventar.")
                continue

            if gegenstand == "geld":
                print("Geld kann nicht entfernt werden.")
                continue

            charakter["inventar"][gegenstand]["menge"] -= 1
            if charakter["inventar"][gegenstand]["menge"] <= 0:
                charakter["inventar"].pop(gegenstand)
            print(f"{gegenstand.title()} wurde entfernt.")

        # ------------------
        # Zurück
        # ------------------

        elif auswahl == "4":
            print("Zurück zum Hauptmenü")
            break

        else:
            print("Ungültige Eingabe.")

def testbereich():

    while True:

        print("\n----Testbereich----\n")
        print("1. Würfelwurf")
        print("2. Skillcheck")
        print("3. Zurück")

        auswahl = input(":> ")

        if auswahl == "1":
            anzahl = int(input("Wie viele Würfel? "))
            seiten = int(input("Wie viele Seiten? "))
            bonus = int(input("Welcher Bonus? "))
            würfelwurf(anzahl, seiten, bonus)

        elif auswahl == "2":

            while True:
                #----Skills anzeigen----
                print("\t----Skills----\n")
                for nummer, skill in skill_mapping.items():
                    print(f"\t{nummer} {skill.title()}\n"
                          f"\tModifikator: {get_modifier(skill)}\n")
                print("\t19. Zurück zum Hauptmenü\n")
                #----Skillcheck durchführen----
                skill_nummer = input("Welchen check willst du machen? (1-19)\n\n:> ")
                if skill_nummer == "19":
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
                nochmal = input(":> ").lower()
                if nochmal == "j":
                    continue
                else:
                    print("Zurück zum Hauptmenü")
                    break

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
        proficiency_bonus = +2
      elif lvl <= 8:
        proficiency_bonus = +3
      elif lvl <= 12:
        proficiency_bonus = +4
      elif lvl <= 16:
        proficiency_bonus = +5
      else:
        proficiency_bonus = +6
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
    modus = input("Auf was willst du würfeln?\nEntscheidung:> ").lower()

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
        attribut = input(
            "Welchen Saving Throw? (str, dex, con, int, wis, cha, 0 für Hauptmenü)\n:> "
        ).lower()
        if attribut == "0":
            print("zurück zum Hauptmenü")
            break

        if attribut in charakter["attribute"]:

            wert = charakter["attribute"][attribut]["wert"]

            mod = (wert - 10) // 2
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
            nochmal = input("Möchtest du noch einen Saving Throw machen? (j/n)\n\n:> ").lower()
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
        "rapier" : {"menge" : 1,
                    "schaden" : "1W8 + {dex_mod} stichschaden"},
        "diplomatenpack" : {"menge" : 1,
                            "inhalt" : {"Parfüm" : 1, 
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
                                "inhalt" : ["Werkzeug zum Fälschen von Dokumenten\n",
                                            "Werkzeug zum Fälschen von Siegeln\n",
                                            "Werkzeug zum Fälschen von Unterschriften\n"]},
        "verkleidungsausrüstung" : {"menge" : 1,
                                    "inhalt" : ["Kostüm\n",
                                                "Perücke\n",
                                                "Make-up\n"]},
        "flöte" : {"menge" : 1,
                   "effekt" : "\tEine einfache Flöte, die du spielen kannst, um \n"
                              "\tdeine musikalischen Fähigkeiten zu zeigen."},
        "dolch" : {"menge" : 1,
                   "schaden" : "1W4 + Stichschaden"},
        "lederrüstung" : {"menge" : 1,
                          "rüstungswert" : 11,
                          "effekt" : "\tEine leichte Lederrüstung"},
        "geld" : {"copper" : 1_500}
        },




}

charaktermenue()

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

