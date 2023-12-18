function hitungKurs() {
    let jumlahRupiah = document.getElementById("rupiahInput").value;
    let kursDollar = 14650;
    let nilaiDollar = jumlahRupiah / kursDollar;
    let hasil = "Jumlah uang dalam Dollar: $" + nilaiDollar.toFixed(2);
    document.getElementById("hasilKurs").innerHTML = hasil;
  }
  