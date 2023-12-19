function hitungKurs() {
    var jumlahRupiah = document.getElementById("rupiahInput").value;
  
    fetch('https://api.exchangeratesapi.io/latest?base=USD')
      .then(response => response.json())
      .then(data => {
        var kursDollar = data.rates.IDR;
        var nilaiDollar = jumlahRupiah / kursDollar;
        var hasil = "Jumlah uang dalam Dollar: $" + nilaiDollar.toFixed(2);
        document.getElementById("hasilKurs").innerHTML = hasil;
      })
      .catch(error => {
        console.error('Terjadi kesalahan:', error);
      });
  }
  