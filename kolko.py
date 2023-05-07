plansza = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
gracz = "X"
Wygrany = None

def rysujplansze(plansza):
    print(plansza[0] + " | " + plansza[1] + " | " + plansza[2])
    print("----------")
    print(plansza[3] + " | " + plansza[4] + " | " + plansza[5])
    print("----------")
    print(plansza[6] + " | " + plansza[7] + " | " + plansza[8])

rysujplansze(plansza)