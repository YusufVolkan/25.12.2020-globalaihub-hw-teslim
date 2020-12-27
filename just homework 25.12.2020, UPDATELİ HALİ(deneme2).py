

isim=input("enter your name:")

soyisim=input("enter your surname:")

name="Yusuf"

surname="Volkan"

deneme=3

failed=0

while deneme>=0:

    if name==isim and surname==soyisim:
        print("Welcome {} {}".format(name, surname))
        break



    elif name==isim and surname!=soyisim:
        deneme = deneme - 1

        print("yanlış soyad girdiniz. İsminiz doğru..., Soyadınızı doğru giriniz")

        x=input("soyadınızı tekrardan giriniz:")
        if x==surname:
            print("teşekkürler doğru girdiniz.")
            break

        else:
            print("yine yanlış girdiniz...")
            deneme=deneme-1




    elif name!=isim and surname==soyisim:
        deneme-=1

        print("İsminizi doğru giriniz.")





        y=input("isminizi tekrardan giriniz:")
        if name==y:
            print("teşekkürler doğru girdiniz..")
            break

        else:
            print("isminizi yanlış girdiniz...")
            deneme-=1




    else:
        print("isminiz ve soyadınız yanlış....")
        deneme-=1

        z=input("isminizi giriniz:")
        d=input("soyadınızı giriniz:")

        if z==name and d==soyisim:
            print("doğru girdiniz")
            break

        else:
            print("yanlış bilgi girdiniz..")
            print("işleminiz iptal edildi...")
            deneme-=1

            break

"""
DERSLER
1.MAT
2.kimya
3.software
4.biology
5.fizik
"""

lesson1="mat"
lesson2="kimya"
lesson3="software"
lesson4="biology"
lesson5="fizik"


ders1=input("ders1 seçiniz:")
ders2=input("ders2 seçiniz:")
ders3=input("ders3 seçiniz:")
ders4=input("ders4 seçiniz:")
ders5=input("ders5 seiçini:")

dersler=[ders1,ders2,ders3,ders4,ders5]
print("seçtiğiniz dersler:",dersler)

minimum_ders_sayısı=3
toplam_ders=len(dersler)

z_soru=int(input("Kaç tane ders almak istiyorsun?:"))

if 3<=z_soru<=5:
    print("sınavlara girme şansınız bulunuyor...")
elif z_soru<3:
    print("en az 3 ders almanız lazımdı. O yüzden sınıfta kaldınızz..")

elif z_soru>5:
    print("en fazla 5 ders alabilirsiniz..")

else:
    print("geçersiz işlem yaptınız...")




midterm=0
final=0
project=0

while True:

    sınava_gireceğin_ders=input("hangi dersten sınava girmek istiyorsun?:....")
    midterm_grade=int(input("midterm notunuzu giriniz:"))
    midterm=midterm_grade*0.3

    print("midterm orlamanız is:",midterm)

    final_grade=int(input("final notunuz:"))

    final=final_grade*0.5
    print("final ortalamanız:",final)

    project_grade=int(input("proje puanınınz:"))

    project=project_grade*0.2
    print("proje ortalamanız:",project)

    notlar={"midterm":midterm_grade,"final":final_grade,"proje":project_grade}
    print(notlar)

    grades=midterm+final+project
    print("toplam not ortalamanız:{}".format(grades))

    if grades>=90:
        print("AA")
    elif 90>grades>70:
        print("bb")

    elif 70>grades>50:
        print("cc")

    elif 30<grades<50:
        print("dd")

    else:
        print(" YOU FAILED!!   'FF' ")
        break













