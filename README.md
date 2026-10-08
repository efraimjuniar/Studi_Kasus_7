# Studi_Kasus_7-Sistem Manajemen Inventaris Barang

Nama  : Efraim Juniar Tonda Kala'<br>
Nim   : 2609116064<br>
Kelas : B

------------------------------------------------------------------------------------------------------------------------------------
Program Python untuk mencatat dan melihat stok barang di toko kelontong. Data disimpan di file JSON, jadi tidak hilang saat program ditutup.

### Fitur
1. Lihat barang — menampilkan semua barang dari file JSON<br>
2. Tambah barang — menambah barang baru dan menyimpannya ke file JSON<br>
3. Keluar — menghentikan program

Menu berjalan terus dengan ```while True``` sampai user memilih keluar.

### File
* ```Studi_Kasus_7.py``` — program utama
* ```Studi_Kasus_7.json``` — tempat data barang disimpan

### Format Data
Setiap barang disimpan sebagai object di dalam array JSON:

```
[
    {
        "kode": "B001",
        "nama": "Gula Pasir 1kg",
        "harga": 16000,
        "stok": 50
    }
]
```
--------------------------------------------
### Cara Menjalankan
Simpan kedua file di satu folder.
Ubah baris path di ```Studi_Kasus_7.py``` sesuai lokasi file JSON kamu.
Jalankan:

```
python Studi_Kasus_7.py
```
---------------------------------------------
### Cara Kerja
* ```baca_data()``` membaca isi file JSON. Kalau file belum ada atau kosong, hasilnya list kosong.
* Lihat barang: data dibaca lalu dicetak satu per satu dengan perulangan ```for```.
* Tambah barang: input diminta (harga dan stok harus angka), data lama dibaca, barang baru ditambahkan dengan ```append()```, lalu seluruh data ditulis ulang ke file dengan ```json.dump()```. Karena data lama dibaca dulu, barang yang sudah ada tidak hilang.
