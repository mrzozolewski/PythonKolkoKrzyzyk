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


#- 0 - 3 - 6
#- 1 - 4 - 7
#- 2 - 5 - 8


#na ukos
# 0 1 2   0 4 8
# 3 4 5   2 4 6
# 6 7 8   

def wygrana_poziom(plansza):
    global wygrany
    #wygrana w 1 rzedzie poziom ---
    if plansza[0] == plansza[1] == plansza[2]:
        wygrany = plansza[1] # nie ma to znaczenia jaki indeks z tablicy bedzie miala zmienna wygrany bo musza byc one rowne (chodzi oczywiscie o 0,1,2 i w innych przykladach inne liczby)
        return True
    elif plansza[3] == plansza[4] == plansza[5]:
        wygrany = plansza[4]
        return True
    elif plansza[6] == plansza[7] == plansza[8]:
        wygrany = plansza[7]
        return True
    
def wygrana_pion(plansza):
    global wygrany
  
    if plansza[0] == plansza[3] == plansza[6]:
        wygrany = plansza[0]
        return True
    elif plansza[1] == plansza[4] == plansza[7]:
        wygrany = plansza[4]
        return True
    elif plansza[2] == plansza[5] == plansza[8]:
        wygrany = plansza[2] 
        return True    
    
def wygrana_na_ukos(plansza):
    global wygrany
    
    if plansza[0] == plansza[4] == plansza[8]:
        wygrany = plansza[0]
        return True
    elif plansza[2] == plansza[4] == plansza[6]:
        wygrany = plansza[4]
        return True     
    
while gra_trwa == True:
    rysujplansze(plansza)
    pozycja(plansza)
