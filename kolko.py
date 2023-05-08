plansza = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
aktualny_gracz = "X"
Wygrany = None

gra_trwa = True

#Rysowanie planszy

def rysujplansze(plansza):
    print(plansza[0] + " | " + plansza[1] + " | " + plansza[2])
    print("----------")
    print(plansza[3] + " | " + plansza[4] + " | " + plansza[5])
    print("----------")
    print(plansza[6] + " | " + plansza[7] + " | " + plansza[8])

rysujplansze(plansza)

#Użytkownik wybiera gdzie postawic znak

def pozycja(plansza):
    wybor = int(input("Gdzie chcesz postawic znak, wybierz liczbe 1-9: "))
    if wybor >= 1 and wybor <= 9 and plansza[wybor-1] == "-":
        plansza[wybor-1] = aktualny_gracz
    else:
        print("Pozycja zajeta")


def wygrana(plansza):
    global wygrany
    #wygrana w 1 rzedzie poziom ---
    if plansza[0] == plansza[1] == plansza[2]:
        wygrany = plansza[1]
        return True
    
    
while gra_trwa == True:
    rysujplansze(plansza)
    pozycja(plansza)
