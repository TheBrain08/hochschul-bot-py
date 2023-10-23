import requests
from bs4 import BeautifulSoup
from time import sleep
wochentage = ['tab-mon','tab-tue','tab-wed','tab-thu','tab-fri','tab-sat','tab-sun']


def get_page_links(url, tag):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, "html.parser")
    Essensplan = sp.find("div",{"id":tag})
    Essen = Essensplan.find("small", {"class":"extra-text"})
    Tage = Essensplan.find("h3")
    with open(tag + ".txt", 'w') as file:
        file.write(str(Essen.prettify()))
    with open(tag + "-tag.txt", 'w') as file:
        file.write(str(Tage))

def delet_words(tag):
    with open(tag + '.txt', 'r') as file:
        text = file.read()
    new_text = text.replace('<small class="extra-text mb-15px">', ' ').replace('<br/>', ' ').replace('</small>', ' ') \
        .replace('<h3>', ' ').replace('</h3>', ' ').replace(' ','')

    with open(tag + '.txt', 'w') as file:
        file.write(new_text)

    with open(tag + '-tag.txt', 'r') as file:
        text = file.read()
    new_text = text.replace('<h3>', ' ').replace('</h3>', ' ').replace(' ','')

    with open(tag + '-tag.txt', 'w') as file:
        file.write(new_text)

def colletion():
    dateien =  ['tab-mon.txt','tab-tue.txt','tab-wed.txt','tab-thu.txt','tab-fri.txt']

    # Name der Zieldatei, in die Sie die Dateien zusammenführen möchten
    ziel_datei = 'tab-woche.txt'
    with open(ziel_datei, 'w') as ziel_file:
        for datei in dateien:
            with open(datei, 'r') as quelle_file:
                ziel_file.write(quelle_file.read())


for x in wochentage:
    if x != 'tab-sun' and x != 'tab-sat':
        get_page_links("https://www.swfr.de/essen/mensen-cafes-speiseplaene/mensa-offenburg", x)
    print("Scratching: "+x)


for x in wochentage:
    if x !='tab-sun' and x != 'tab-sat':
        delet_words(x)
    print("Deleting useless word: "+x)

colletion()


