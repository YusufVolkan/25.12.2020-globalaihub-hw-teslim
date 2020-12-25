import random #random modülünü girdik. Kütüphaneyi çağırdık

name=input("İsminizi giriniz:") #ismini girmesini istedik
print("Welcome {} and Good luck!...".format(name))

kelimeler=["python","asansör","merdiven","kitap","futbol","voleybol"]

kelime=random.choice(kelimeler) # random.choice(kelimeler) , kelimeler listesinden rastgele bir tane kelime seçmesini istedim.

print("Kelimeyi tahmin ediniz...")

tahminler=''

turns=12 # 11 kere deneme hakkı

while turns>0:
    failed=0 #kaç kere başarısız olucak diye 0 dan başlattım.


    for char in kelime:

        if char in tahminler:
            print(char)

        else:
            print("_")
            failed +=1

    if failed==0:
        print("Kazandın")

        print("Gizli kelimemiz:",kelime)
        break



    guess=input("harfi tahmin ediniz, harf giriniz:")

    tahminler +=guess

    if guess not in kelime:
        turns-=1
        print("Yanlış harf.")

        print("Bu kadar deneme hakkınız {} tane kalmıştır.".format(turns),"more guesses")

    if turns==0:
        print("kaybettiniz...")

