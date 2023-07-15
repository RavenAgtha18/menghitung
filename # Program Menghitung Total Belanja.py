# Program Menghitung Total Belanja

# Data Eksternal
daftar_harga = {
    "Apel": 5000,
    "Jeruk": 3000,
    "Mangga": 7000,
    "Pisang": 2000,
    "Semangka": 10000
}

# Variabel
total_belanja = 0

# Looping
print("Daftar Barang:")
for barang in daftar_harga:
    print(barang, ":", daftar_harga[barang])

while True:
    nama_barang = input("Masukkan nama barang (atau selesai untuk mengakhiri): ")
    if nama_barang.lower() == "selesai":
        break

    if nama_barang in daftar_harga:
        jumlah = int(input("Masukkan jumlah barang: "))
        total_harga = daftar_harga[nama_barang] * jumlah
        total_belanja += total_harga
        print("Total harga:", total_harga)
    else:
        print("Barang tidak ditemukan!")

# Boolean
dapat_diskon = total_belanja >= 20000

# Menampilkan Total Belanja dan Diskon
print("Total belanja Anda:", total_belanja)
if dapat_diskon:
    print("Anda mendapatkan diskon 10%!")