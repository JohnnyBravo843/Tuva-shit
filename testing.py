
import datetime





def sjekkeMåned(måned):
    maaneder = {
        "01":"januar",
        "02":"februar",
        "03":"mars",
        "04":"april",
        "05":"mai",
        "06":"juni",
        "07":"july",
        "08":"august",
        "09":"september",
        "10":"oktober",
        "11":"november",
        "12":"desember"
    }
    return maaneder[måned]

def sjekkMåned2(måned):
    if måned == "01":
        return "januar"
    elif måned == "02":
        return "februar"
    elif måned == "03":
        return "mars"
    elif måned == "04":
        return "april"
    elif måned == "05":
        return "mai"
    elif måned == "06":
        return "juni"
    elif måned == "07":
        return "juli"
    elif måned == "08":
        return "august"
    elif måned == "09":
        return "september"
    elif måned == "10":
        return "oktober"
    elif måned == "11":
        return "november"
    elif måned == "12":
        return "desember"

def sjekkÅr(år):
    if int(år) >  int(str(datetime.datetime.now())[2:4]):
        return "19"+ år
    else:
        return "20" + år




def sjekkKjønn(tall):
    if int(tall) % 2 == 0:
        return "Dame"
    else:
        return "Mann"


def oppgave1C():
    foedselsnummer = "01128244456"
    if len(foedselsnummer) != 11:
        print("Ugyldig fødselsnummer, DET SKAL VÆRE 11 SIFFER!")
    else:
        print(f"{foedselsnummer[0:2]}.{foedselsnummer[2:4]}.{foedselsnummer[4:6]}" )

    
    return f"Fødselsdatoen er {int(foedselsnummer[0:2])}. {sjekkMåned2(foedselsnummer[2:4])} {sjekkÅr(foedselsnummer[4:6])} ({sjekkKjønn(foedselsnummer[8])}) "

print(oppgave1C())



varer = {"ASUS Zenbook GH215": {"varenavn":"asus laptop",
                                "pris": 9999,
                                "varelager":10,
                                "produktinfo":"En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD", 
                                "tekniske egenskaper": ["prosessor: Intel Core i5-1135G7",
                                                        "grafikkort: Intel Iris Xe Graphics",
                                                        "batterikapasitet: Opptil 8 timer",
                                                        "vekt: 1.8 kg"],
                                "farger":["blå","grå","svart"]},


        "Samsung Galaxy S22 GH67": {"varenavn":"Samsung mobiltelefon",
                                "pris":6999,
                                "varelager":20,
                                "produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
                                "tekniske egenskaper":["prosessor: Qualcomm Snapdragon 888",
                                                        "grafikkort: Adreno 660",
                                                        "batterikapasitet: 4500 mAh",
                                                        "vekt: 200 g"],
                                "farger":["svart","hvit","grønn"]},
        "Apple Airpods Pro Gen 3 (2023)":{"varenavn":"airpods pro",
                                "pris":2499,
                                "varelager":30,
                                "produktinfo": "Trådløse hodetelefoner med aktiv støydemping",
                                "tekniske egenskaper":["batterikapasitet: Opptil 4.5 timer",
                                                        "vekt: 5.4 g",],
                                "farger":["hvit","gul","spygrønn"]}}



def printUtVare(vareId):
    if vareId not in varer:
        return "Feilmld, varen eksisterer ikke"
    utskrift = f"=====================================\n{vareId}\n"
    for i in varer[vareId]:
        if type(varer[vareId][i]) == int:
            utskrift += f"> {i}: {str(varer[vareId][i])}\n"
        elif type(varer[vareId][i]) == list:
            utskrift += f"> {i}\n"
            for i in varer[vareId][i]:
                utskrift += f"  - {i}\n"
        else:
            utskrift += f"> {i}: {varer[vareId][i]}\n"


    return utskrift


def printUtAlleVarer():
    superutskrift = ""
    for i in varer:
        superutskrift += printUtVare(i)
    return superutskrift


print(printUtAlleVarer())




def byttPris(vareId,nypris):
    varer[vareId]["pris"] = nypris
    return printUtVare(vareId)

print(byttPris("ASUS Zenbook GH215",15))