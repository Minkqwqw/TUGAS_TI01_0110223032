function hitungparkir(){
    // dapatkan nilai input-an user
    let masuk = document.getElementById('masuk').value
    let keluar = document.getElementById('keluar').value


// dapatkan elemen untuk menampilkan hasil
let hasilDurasi = document.querySelector("#HasilDurasi")
let hasilBiaya = document.querySelector("#HasilBiaya")

// hitung durasi
let durasi = keluar - masuk

// hitung biaya
let biaya = 3000

// setelah 2 jam pertama, tambahkan biaya perjamnya sebesar 1000
if(durasi > 2){
    biaya += (durasi - 2) * 1000
}

console.log(biaya);

hasilBiaya.innerHTML = biaya
hasilDurasi.innerHTML = durasi

}