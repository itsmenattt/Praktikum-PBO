data_siswa = {}

jumlah_siswa = int(input("Masukkan jumlah siswa: "))

for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = float(input(f"Masukkan nilai {nama}: "))
    data_siswa[nama] = nilai  # Tambahkan ke dictionary

# Menampilkan hasil
print("\nData Siswa:")
for nama, nilai in data_siswa.items():
    print(f"{nama}: {nilai}")

print(type(data_siswa))