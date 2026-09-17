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
    
    time.sleep(1)

    skorna_baklänges = input("Vill du ta på skorna baklänges? ja eller nej: ")

    if skorna_baklänges == "ja":
        print("Det gick inte att ta på skorna baklänges. Du fick bara ont i foten. Varför försökte du ens?")
        time.sleep(3)
        print("Du tog på skorna åt rätt håll istället.")
    
    time.sleep(1)
    print("Då går vi!")


else:
    print("Fegis!")