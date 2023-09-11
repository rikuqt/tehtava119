"""Tee ohjelma (esimerkiksi tiedostoon T54_kyselija.py), jossa on funktiot main() ja 
kysy_luku_valilta(alaraja, ylaraja). Funktiossa main on vakiot ALA, jonka arvo on 1 ja YLA,
jonka arvo on 5 sekä kokonaislukumuuttuja luku, joka on aluksi 0 ja jonka arvoksi
sijoitetaan funktion kysy_luku_valilta palauttama arvo. Funktiossa main tulostetaan
lopuksi muuttujan luku arvo.

Funktio kysy_luku_valilta kysyy käyttäjältä lukua alarajan ja ylarajan väliltä ja
saatuaan kelvollisen luvun, palauttaa sen arvonaan (vrt. Tehtävä 29). Jos käyttäjä
antaa epäkelvon syötteen, eli alle alarajan, yli ylärajan tai kirjaimia, tulostetaan
virheilmoitus ja kysytään uudelleen. Varaudu funktiossa alle alarajan ja yli ylärajan
oleviin syötteisiin sopivalla ehdolla while-toistossa ja kirjaimia sisältäviin
syötteisiin try-except -rakenteella
(voit käyttää tässä except-osaa ilman nimettyä poikkeusta)."""

def kysy_luku_valilta(ALA, YLA):
    while int or str:
        try:
            kysy = int(input("Anna luku väliltä 1-5: "))
            while not (ALA <= kysy <= YLA):
                try:
                    if not (ALA <= kysy <= YLA):
                        print("Annoit väärän luvun.")
                        kysy = int(input("Anna luku väliltä 1-5: "))
                    else:
                        return kysy
                except:
                    print("Annoit kirjaimen!")
                    kysy = int(input("Anna luku väliltä 1-5: "))
        except:
            print("Annoit kirjaimen!")
        else:
            return kysy

def main():
    ALA = 1
    YLA = 5
    luku = 0
    luku = kysy_luku_valilta(ALA, YLA)
    print(f"Luvun jonka annoit oli {luku}.")

    print (f"hello world")

main()