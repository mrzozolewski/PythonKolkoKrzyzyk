import random
#Puste pola w planszy, ktore beda podmieniane na znaki
plansza = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

aktualny_gracz = "X"
Wygrany = None
gra_trwa = True

#Rysowanie planszy

#┌───┬───┬───┐
#│ - │ - │ - │
#├───┼───┼───┤	
#│ - │ - │ - │ 
#├───┼───┼───┤	
#│ - │ - │ - │ 
#└───┴───┴───┘ 

def rysujplansze(plansza):
    print("┌───┬───┬───┐")
    print("│ " + plansza[0] + " │ " + plansza[1] + " │ " + plansza[2] + " │")
    print("├───┼───┼───┤")
    print("│ " + plansza[3] + " │ " + plansza[4] + " │ " + plansza[5] + " │")
    print("├───┼───┼───┤")
    print("│ " + plansza[6] + " │ " + plansza[7] + " │ " + plansza[8] + " │")
    print("└───┴───┴───┘")

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
    global gra_trwa
    #wygrana w 1 rzedzie poziom ---
    if plansza[0] == plansza[1] == plansza[2]and plansza[0] != "-":
        wygrany = plansza[1] # nie ma to znaczenia jaki indeks z tablicy bedzie miala zmienna wygrany bo musza byc one rowne (chodzi oczywiscie o 0,1,2 i w innych przykladach inne liczby)
        rysujplansze(plansza)
        print("Wygrał "+wygrany) 
        gra_trwa = False 
    
    elif plansza[3] == plansza[4] == plansza[5]and plansza[3] != "-":
        wygrany = plansza[4]
        rysujplansze(plansza)
        print("Wygrał "+wygrany) 
        gra_trwa = False 
    
    elif plansza[6] == plansza[7] == plansza[8]and plansza[6] != "-":
        wygrany = plansza[7]
        rysujplansze(plansza)
        print("Wygrał "+wygrany) 
        gra_trwa = False 
    
    
def wygrana_pion(plansza):
    global wygrany
    global gra_trwa
    if plansza[0] == plansza[3] == plansza[6]and plansza[0] != "-":
        wygrany = plansza[0]
        rysujplansze(plansza)
        print("Wygrał "+wygrany) 
        gra_trwa = False 
    
    elif plansza[1] == plansza[4] == plansza[7]and plansza[1] != "-":
        wygrany = plansza[4]
        rysujplansze(plansza)
        print("Wygrał "+wygrany) 
        gra_trwa = False 
    
    elif plansza[2] == plansza[5] == plansza[8]and plansza[2] != "-":
        wygrany = plansza[2]
        rysujplansze(plansza)
        print("Wygrał "+wygrany)
        gra_trwa = False 
    
           
    
def wygrana_na_ukos(plansza):
    global wygrany
    global gra_trwa
    if plansza[0] == plansza[4] == plansza[8] and plansza[0] != "-":
        wygrany = plansza[0]
        rysujplansze(plansza)
        print("Wygrał "+wygrany)
        gra_trwa = False    
    elif plansza[2] == plansza[4] == plansza[6] and plansza[2] != "-":
        wygrany = plansza[4]
        rysujplansze(plansza)
        print("Wygrał "+wygrany)
        gra_trwa = False 

def remis(plansza):
    global gra_trwa
    if "-" not in plansza:
        rysujplansze(plansza)
        print("Remis")
        gra_trwa = False

        
def zmiana_gracza():
    global aktualny_gracz 
    if aktualny_gracz== "X":
        aktualny_gracz = "O"
    else:
        aktualny_gracz = "X"

    
def bot(plansza):
    while aktualny_gracz == "O":
        pozycja = random.randint(0, 8)
        if plansza[pozycja] == "-":
            plansza[pozycja] = "O"
            zmiana_gracza()

while gra_trwa == True:
    rysujplansze(plansza)
    pozycja(plansza)
    wygrana_na_ukos(plansza)
    wygrana_pion(plansza)    
    wygrana_poziom(plansza)
    remis(plansza)
    zmiana_gracza()
    bot(plansza)
    wygrana_na_ukos(plansza)
    wygrana_pion(plansza)    
    wygrana_poziom(plansza)
    remis(plansza)