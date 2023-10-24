import requests
from bs4 import BeautifulSoup
from time import sleep
wochentage = ['tab-mon','tab-tue','tab-wed','tab-thu','tab-fri','tab-sat','tab-sun']


def get_page_links(url, tag):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, "html.parser")
    Essensplan = sp.find("div",{"id":tag})
    Essen = Essensplan.find_all("small", {"class":"extra-text"})
    Tage = Essensplan.find("h3")
    Titel = Essensplan.find_all("h5")
    for i in range(3):
        with open("./Essen/" + tag + str(i) + ".txt", 'w') as file:
            file.write(str(Essen[i]))
    with open("./Essen/" + tag + "-tag.txt", 'w') as file:
        file.write(str(Tage))

def delet_words(tag):
    for i in range(3):
        with open("./Essen/" + tag + str(i) + '.txt', 'r') as file:
            text = file.read()
        new_text = text.replace('<small class="extra-text mb-15px">', ' ').replace('<br/>', ' ').replace('</small>', ' ') \
            .replace('<h5>', ' ').replace('</h5>', ' ').replace('<span class="sr-only">', ' ').replace('</span>', ' ')

        with open("./Essen/" + tag + str(i) + '.txt', 'w') as file:
            file.write(new_text)

    with open("./Essen/" + tag + '-tag.txt', 'r') as file:
        text = file.read()
    new_text = text.replace('<h3>', ' ').replace('</h3>', ' ')

    with open("./Essen/" + tag + '-tag.txt', 'w') as file:
        file.write(new_text)




def start():
    for x in wochentage:
        if x != 'tab-sun' and x != 'tab-sat':
            get_page_links("https://www.swfr.de/essen/mensen-cafes-speiseplaene/mensa-offenburg", x)
        print("Scratching: "+x)


    for x in wochentage:
        if x !='tab-sun' and x != 'tab-sat':
            delet_words(x)
        print("Deleting useless word: "+x)

start()


