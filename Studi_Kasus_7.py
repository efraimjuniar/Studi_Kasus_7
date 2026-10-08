import json

path = r"C:\Users\ACER\ddp\Tugas_DDP\Studi_Kasus_7.json"


def baca_data():
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            isi = f.read()
    except FileNotFoundError:
        return []

    if isi.strip() == "":
        return []
    return json.loads(isi)


while True:
    print("\n=== INVENTARIS TOKO ===")
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        data = baca_data()

        if len(data) == 0:
            print("Data masih kosong.")
        for barang in data:
            print(f"{barang['kode']} | {barang['nama']} | Rp{barang['harga']} | stok: {barang['stok']}")

    elif menu == "2":
        kode = input("Kode barang : ")
        nama = input("Nama barang : ")
        try:
            harga = int(input("Harga       : "))
            stok = int(input("Stok        : "))
        except ValueError:
            print("Harga dan stok harus berupa angka!")
            continue

        data = baca_data()
        data_baru = {
            "kode": kode,
            "nama": nama,
            "harga": harga,
            "stok": stok
        }
        data.append(data_baru)

        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Barang berhasil disimpan!")

    elif menu == "3":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid.")
