# Här skriver du ditt textäventyr
import time

#PROMENADEN

gå_ut = input("Det är kusligt ute. Vill du gå ut? ja eller nej: ")

if gå_ut == "ja":
    print("Vad kul! Ta på ytterkläder så går vi")
    
    time.sleep(1)

    jacka = input("Vilken jacka vill du ta på? fina eller fula: ")

    if jacka == "fina":
        print("Den där kan du inte ha på! Vi ska ju ut i skogen!")
    else:
        print("Tur att det är mörkt ute så folk slipper se dig med den där jackan")
    
    time.sleep(2)

    skorna_baklänges = input("Vill du ta på skorna baklänges? ja eller nej: ")

    if skorna_baklänges == "ja":
        print("Det gick inte att ta på skorna baklänges. Du fick bara ont i foten.")
        time.sleep(2)
        print("Du tog på skorna åt rätt håll istället.")
        time.sleep(1)
    
    
    print("Då går vi!")

    time.sleep(1)

    print("Det är mörkt ute. Gatlyktorna tänds en efter en.")

    time.sleep(2)

    väg = input("Du kommer till en korsning.  1. Sväng vänster, 2. Sväng höger : ")

    if väg == "1":
        enter = input("du kom till ett hus. Vill du gå in? ja eller nej: ")
        if enter == "ja":
            print("du blev uppäten av en vampyr och dog")
        else:
            print("du gick hem och överlevde")
    else:
        print("du kom till ett stup, föll ner och dog")
else:
    print("Fegis!")