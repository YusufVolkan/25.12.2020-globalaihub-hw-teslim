name=input("enter your name:")
surname=input("enter your surname:")

deneme=3
failed=0

while True:

    if deneme==0:
        print("please try again later..")
        break


    if name=="Yusuf" and surname=="Volkan":

        print("Welcome {} {}".format(name,surname))
        deneme-=1
        break


    if name=="Yusuf" and surname!="Volkan":

        print("Soyadınızı doğru giriniz lütfen..")

        deneme-=1


    elif name!="Yusuf" and surname=="Volkan":

        print("İsminiz yanlış, lütfen isminizi doğru giriniz..")

        deneme-=1

    else:
        print("isminiz ve soyadınız yanlış....")
        deneme-=1

"""
DERSLER
1.MAT
2.kimya
3.software
4.biology
5.fizik
"""
ders1=input("ders1 seçiniz:")
ders2=input("ders2 seçiniz:")
ders3=input("ders3 seçiniz:")
ders4=input("ders4 seçiniz:")
ders5=input("ders5 seiçini:")

dersler=[ders1,ders2,ders3,ders4,ders5]
print("seçtiğiniz dersler:",dersler)

midterm=0
final=0
project=0

while True:
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
    print(grades)

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













