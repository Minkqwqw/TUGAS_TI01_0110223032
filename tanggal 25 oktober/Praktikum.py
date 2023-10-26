#list
yamaha = ["R1", "R1", 1000, "Pink", "Michelin"]
yamaha.append("600Juta")
yamaha.append("sport")
yamaha.insert(2, "R1M")
pooped_value = yamaha.pop(1)
print(len(yamaha))
print(yamaha)


#match case
math=input("Ingin menghitung luas bangun datar apa hari ini?")
match math:
    case "persegi":
        s = int(input("masukkan sisi!:"))
        persegi = s * s
        
    case "lingkaran":
        r = int(input("masukkan jari-jari!:"))
        lingkaran = 3.14*r*r
        print("Luas lingkaran", lingkaran)
    case "segitiga":
        alas = int(input("masukkan alas segitiganya!:"))
        tinggi = int(input("masukkan tinggi segitiganya!:"))
        luas = alas * tinggi / 2
        print("luas segitiga", luas)

        
        