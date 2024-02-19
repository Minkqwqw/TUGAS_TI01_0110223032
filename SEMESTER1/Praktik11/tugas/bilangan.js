function hitungJumlah() {
    // Mengambil nilai dari input bilangan pertama dan kedua
    let bil1 = document.getElementById("bil1").valueAsNumber || 0;
    let bil2 = document.getElementById("bil2").valueAsNumber || 0;

    // Menghitung jumlah kedua bilangan
    let jumlah = bil1 + bil2;

    // Menyimpan hasil pada input hasil
    document.getElementById("hasil").value = jumlah;
}