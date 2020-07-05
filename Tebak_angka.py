import random

gusTaken= 0
cobaTebak= int(input("Mencoba tebak berakali: "))
NamaSaya= input("Masaukan nama: ")
AngkaAwal = int(input("Masukan angka awal yang mau di tebak:"))
AngkaAkhhir=  int(input("Masukan angka awal yang mau di tebak: "))
number= random.randint(AngkaAwal,AngkaAkhhir)
print("oke",NamaSaya,"Coba pikirkan angka Awal dan Akhir yang anda tulis dan coba tebak!")

while gusTaken < cobaTebak:
    gues = int(input("Coba tebak: "))
    gusTaken +=1

    if gues < number:
        print("Tebakan anda terlalu kecil " )
    elif gues > number:
        print("Tebakan anda terlalu besar " )
    elif gues == number:
        gusTaken = str(gusTaken)
        print("Bagus sekali ",NamaSaya," Kamu bisa menebak angka sebanyak",gusTaken,"kali")
        break
    elif gues != number:
        number = str(number)
        print("Tebakan yang benar: ",number)
    else:
        print("tidak tepat")
print("Tebakan benar ",number)
