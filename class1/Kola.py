import math

def odl(p1,p2)->float:
    return math.dist(list(p1), list(p2))


print("Ten program sprawdza, czy podane przez użytkownika koła mają niepuste przecięcie.")
x1 = float(input("Podaj wspolrzedne srodka pierwszego kola (wsp x): "))
y1 = float(input("Podaj wspolrzedne srodka pierwszego kola (wsp y): "))
z1 = float(input("Podaj wspolrzedne srodka pierwszego kola (wsp z): "))
x2 = float(input("Podaj wspolrzedne srodka drugiego kola (wsp x): "))
y2 = float(input("Podaj wspolrzedne srodka drugiego kola (wsp y): "))
z2 = float(input("Podaj wspolrzedne srodka drugiego kola (wsp z): "))
r1 = float(input("Podaj promien pierwszego kola : "))
r2 = float(input("Podaj promien drugiego kola : "))

l = odl((x1, y1), (x2, y2))
if l <= r1 + r2:
    print("Maja niepuste przeciecie")
else:
    print("Nie maja niepustego przeciecia")