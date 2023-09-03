import requests
from bs4 import BeautifulSoup


def spr_istnieje(slowo):
    url = "https://sjp.pl/" + slowo

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    definicja = soup.find_all("p")

    # just checking if the word is in the dictionary
    if "dopuszczalne w grach " in definicja[0]:
        # print("To slowo jest poprawne 2")
        return True
    elif "nie występuje w słowniku" in definicja[0] or "niedopuszczalne w grach " in definicja[0]:
        # print("To slowo jest nieprawidlowe 2")
        return False
    else:
        print("Chyba cos nie dziala")


def spr_pelne(slowo):
    url = "https://sjp.pl/" + slowo

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    definicja = soup.find_all("p")
    pochodzenie = soup.find_all("a")

    # just checking if the word is in the dictionary
    if "dopuszczalne w grach " in definicja[0]:
        print("To slowo jest poprawne 2")
    elif "nie występuje w słowniku" in definicja[0] or "niedopuszczalne w grach " in definicja[0]:
        print("To slowo jest nieprawidlowe 2")
    else:
        print("Chyba cos nie dziala")

    # print(definicja[0])

    """ for item in definicja:
        print(item, "\n\n")

    print("\n\n\n") """

    """ for item in pochodzenie:
        print(item.text, "\n\n")

    print("\n\n\n") """

    # 9, 12, 15

    # 0, 5, 10 always + 3

    i = 0
    j = 9
    while i < len(definicja):
        if "niedopuszczalne w grach" in definicja[i].text:
            print("To slowo pochodzi od slowa " + pochodzenie[j].text)
            print(definicja[i].text + " nie okok")
            cleanSoup = BeautifulSoup(
                str(definicja[i+3]).replace("<br/>", "\n"), "html.parser")
            print("Definicje:\n" + cleanSoup.text)

        elif "dopuszczalne w grach" in definicja[i].text:
            print("To slowo pochodzi od slowa " + pochodzenie[j].text)
            print(definicja[i].text + "okok")
            cleanSoup = BeautifulSoup(
                str(definicja[i+3]).replace("<br/>", "\n"), "html.parser")
            print("Definicje:\n" + cleanSoup.text)

        i += 5
        j += 3


word = str(input("Podaj slowo do sprawdzenia ------------> "))
spr_pelne(word)
