# This is a Python script to create references with the users input, and then is copied into the clipboard(CTRL + V).

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyperclip3
nn = ""
def addToString(str):
    global nn
    nn +=str

def mainLoop():
    global nn
    inputter = 0
    while inputter != 99:
        print("----------------")
        print("type 1 for 'Bücher oder Monographien'")
        print("type 2 for 'Normen'")
        print("type 3 for 'Publikationen juristischer Personen'")
        print("type 99 for exit")
        print("----------------")
        print("press Enter to confirm your choice")
        inputter = input()

        if inputter == "1":
            pyperclip3.clear()
            nn=""
            print("chose 'Bücher oder Monographien'")
            print("always press Enter to confirm your input")
            print("you can leave input blank if you don't have the infos")
            print("----------------")
            print("type in Nachname d. Verf.")
            addToString(input() + ", ")
            print("type in Vorname d. Verf.")
            addToString(input() + ": ")
            print("type in Sachtitel")
            addToString(input() + ". ")
            print("type in Untertitel or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Untertitel")
            else:
                addToString(ut + ". ")
            print(
                "type in Ggf. Angaben zur Schriftenreihe und Bandangaben (Reihentitel, Nummer, Band, Heft etc.) - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Extras")
            else:
                addToString(ut + ". ")
            print("type in Auflage - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Auflage")
            else:
                addToString(ut + ". ")
            print("type in Ort - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Ort")
            else:
                addToString(ut + ": ")
            print("type in Verlag - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Verlag")
            else:
                addToString("Verlag " + ut + " ")
            print("type in Jahr - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Jahr")
            else:
                addToString(ut + ". ")
            print("type in Seite - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Seite")
            else:
                addToString(ut + ".")

            print("-------------------")
            print("your cite is now in your clipboard (ctrl+v)")
            pyperclip3.copy(nn)

        if inputter == "2":
            pyperclip3.clear()
            nn=""
            print("chose 'Normen'")
            print("always press Enter to confirm your input")
            print("you can leave input blank if you don't have the infos")
            print("----------------")
            print("type in Name d. Hrsg.")
            addToString(input() + ". ")
            print("type in Titel")
            addToString(input() + ". ")
            print("type in Erscheinungsdatum")
            addToString(input() + ". ")
            print("type in § Litera Ziffer etc. - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out § Litera Ziffer etc.")
            else:
                addToString(ut + ".")

            print("-------------------")
            print("your cite is now in your clipboard (ctrl+v)")
            pyperclip3.copy(nn)

        if inputter == "3":
            pyperclip3.clear()
            nn=""
            print("chose 'Publikationen juristischer Personen'")
            print("always press Enter to confirm your input")
            print("you can leave input blank if you don't have the infos")
            print("----------------")
            print("type in Titel d. Publikation")
            addToString(input() + ". ")
            print("type in Hrsg.Juristische Person(z.B.Ministerium, Kammer, Gemeinde, Firma)")
            addToString(input() + " ")
            print("type in Ausgabejahr.")
            addToString(input() + ". ")
            print("type in Seite - or leave blank")
            ut = input()
            if ut == "":
                print("leaving out Seite")
            else:
                addToString(ut + ".")

            print("-------------------")
            print("your cite is now in your clipboard (ctrl+v)")
            pyperclip3.copy(nn)



        if inputter == "99":
            exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
