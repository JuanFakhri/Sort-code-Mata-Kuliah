class Durian:
    # Class attribute
    species = "King of fruit"

    def __init__(self, NamaDurian, Rasa, Bentuk):
        self.namaDurian = NamaDurian
        self.raasa = Rasa
        self.bentuk = Bentuk

# Child class(inherits from Durian class
class Bowor(Durian):
    # instance method
    # fungsi berat untuk memberikan harga pada durian
    def berat(self):
        self.beerat = int(input("Harga 1 kg durian: "))
        return ("Harga 1 kg Bowor : ", self.beerat)
    # instance method
    # fungsi harga untuk memberikan total yang harus di bayar
    def harga(self):
        kg = int(input("Beli berapa kg: "))
        total = self.beerat * kg
        print("Harga Bowor: ", total)
        return "Yanng harus di bayar sebesar = ", total


class MusangKing(Durian):
    def berat(self):
        self.beerat = int(input("Harga 1 kg durian: "))
        return ("Harga 1 kg MusangKing : ", self.beerat)

    # instance method
    # fungsi harga untuk memberikan total yang harus di bayar
    def harga(self):
        kg = int(input("Beli berapa kg: "))
        total = self.beerat * kg
        print("Harga Musang king: ", total)
        return "Yanng harus di bayar sebesar = ", total


# Child class(inherits from Durian class
class Montong(Durian):
    # instance method
    # fungsi berat untuk memberikan harga pada durian
    def berat(self):
        self.beerat = int(input("Harga 1 kg durian: "))
        return ("Harga 1 kg Montong : ", self.beerat)

    # instance method
    # fungsi harga untuk memberikan total yang harus di bayar
    def harga(self):
        kg = int(input("Beli berapa kg: "))
        total = self.beerat * kg
        print("Harga Montong: ", total)
        return "Yanng harus di bayar sebesar = ", total


b = Bowor("Bowor", "Manis", "Lonjong")
c = MusangKing("Musang King", "Manis dan legit", "Oval")
d = Montong("Montong", "Legit", "Oval")

lop = 0
while lop < 3:
    print("+", "-" * 11, "+", "-" * 11, "+")
    print("| Nama Durian yang tersedia |")
    print("| Bowor\t\t\t\t\t\t|")
    print("| Musang king\t\t\t\t|")
    print("| Montong\t\t\t\t\t|")
    print("+", "-" * 11, "+", "-" * 11, "+")
    durian = input("\tPilih durian : ")
    if durian == "Bowor":
        print("+", "-" * 10, "+", "-" * 10, "+")
        print("\tNama Durian", b.namaDurian)
        print("\tRasa Durian", b.raasa)
        print("\tBentuk durian", b.bentuk)
        print("\t", b.berat())
        print("\t", b.harga())
    elif durian == "Musang king":
        print("+", "-" * 10, "+", "-" * 10, "+")
        print("\tNama Durian", c.namaDurian)
        print("\tRasa Durian", c.raasa)
        print("\tBentuk durian", c.bentuk)
        print("\t", c.berat())
        print("\t", c.harga())
    elif durian == "Montong":
        print("\tNama Durian", d.namaDurian)
        print("\tRasa Durian", d.raasa)
        print("\tBentuk durian", d.bentuk)
        print("\t", d.berat())
        print("\t", d.harga())
        break
    else:
        print("Masukan nama durian dengan benar")
