#esimene ülesanne
nimi=input("Teie nimi on? ")
print("Tere,", nimi)

#teine ülesanne
tulemus_sulgudega = 3 + (8 / (4 - 2) * 4)
print("Tulemus sulgudega: ", tulemus_sulgudega)

#2.1
import math

ringi_raadius = float(input("Sisesta ringi raadius: "))

ruudu_pindala = ringi_raadius**2
ruudu_ümbermõõt = 4 * ringi_raadius

ringi_pindala = math.pi * ringi_raadius**2
ringi_ümbermõõt = 2 * math.pi * ringi_raadius

print(f"Ruudu pindala: {ruudu_pindala}, Ruudu ümbermõõt: {ruudu_ümbermõõt}")
print(f"Ringi pindala: {ringi_pindala}, Ringi ümbermõõt: {ringi_ümbermõõt}")

#2.2
maa_raadius_km = 6378
mündi_läbimõõt_cm = 2.52 
pi_vaartus = 3.14159265359

ümbermõõt_km = 2 * pi_vaartus * maa_raadius_km
müntide_arv = ümbermõõt_km * 100000 / mündi_läbimõõt_cm  # 1 km = 100000 cm

print(f"ümbermõõt Maa ekvaatori kohal: {ümbermõõt_km} km")
print(f"2-euroste müntide arv ümber Maa ekvaatori: {int(müntide_arv)} münti")


#kolmas ülesanne
esimene= "kill-koll"
teine= "killadi-koll"
kolmas= "killkoll"

print("{0} {0} {1} {0} {0} {1} {0} {0} {2} {0}".format(esimene,teine,kolmas))

#neljas ülesanne
def laulusonad():
    print("Rong see sõitis tsuhh tsuhh tsuhh,")
    print("piilupart oli rongijuht.")
    print("Rattad tegid rat tat taa,")
    print("rat tat taa ja tat tat taa.")
    print("Aga seal rongi peal,")
    print("kas sa tead, kes olid seal?")


laulusonad()

jatkamine = input("Kas soovid kuulda järgmist laulu? (jah/ei): ")

if jatkamine.lower() == "jah":
    print("\nUus laul:\n")
    def laulusonad():
        print("Rong see s?itis tuut tuut tuut,")
        print("piilupart oli rongijuht.")
        print("Rattad tegid kill koll koll,")
        print("kill koll koll ja kill koll kill.")
    laulusonad()
else:
    print("Programm lõpetab töö.")
    
#viies ülesanne
pikkus = float(input("Sisesta ristküliku pikkus: "))
laius = float(input("Sisesta ristküliku laius: "))

ümbermõõt = 2 * (pikkus + laius)
pindala = pikkus * laius

print("Ristküliku ümbermõõt on:", ümbermõõt)
print("Ristküliku pindala on:", pindala)

#kuues ülesanne
tangitud_kütuse_liitrid = float(input("Sisesta tangitud kütuse kogus liitrites: "))
läbitud_kilomeetrid = float(input("Sisesta läbitud kilomeetrite arv: "))

kütusekulu_100_km = (tangitud_kütuse_liitrid / läbitud_kilomeetrid) * 100

print("Keskmine kütusekulu 100 km kohta on:", kütusekulu_100_km, "liitrit")

#seitsmes ülesanne
kiirus=29.9

M=float(input("sisestage aeg minutites: "))

aeg= M / 60

za_skolko=kiirus * aeg

print("Rulluisutaja jõuab {1} minutiga {3} kilomeetri kaugusele".format(kiirus,M,aeg,za_skolko))

#kahehsas ülesane
aeg_minutites = int(input("Sisesta aeg minutites: "))

tunnid = aeg_minutites // 60
minutid = aeg_minutites % 60

print(f"{aeg_minutites} minutit on {tunnid} tundi ja {minutid} minutit.")




