#deklarasi dan inisialisasi variabel
pelanggan = 'Budi Santoso'
totalBelanja = 150000

#struktur kendali if
if(totalBelanja > 100000):
    keterangan = "Selamat Anda mendapatkan hadiah"

else:
    keterangan = "Terima kasih sudah berbelanja"

#cetak data
print("Pelanggan",pelanggan,"\nTotal Belanja Anda Rp.",totalBelanja,"\n,keterangan")


#siswa dinyatakan lulus minimal 60 nilainya
nama ="Budi Santoso"
matpel = "Matematika"
nilai = 59.99
#ternary
keterangan = "Lulus" if nilai >=60 else "Gagal"

nama ="Budi Santoso"
matpel = "Matematika"
nilai = 59.99
#uji grade dengan if Multi kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >=75 and nilai <85):
    grade = "B"
elif(nilai >=60 and nilai <75):
    grade = "C"
elif(nilai >=30 and nilai <60):
    grade = "D"
else:
    grade = "E"
    #cetak data
print("Nama Siswa \t:",nama,
    "\nMata Pelajaran \t:",matpel,
    "\nNilai \t\t:",nilai,
    "\nKeterangan \t:",keterangan,
    "\ngrade \t\t:",grade)
