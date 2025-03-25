import math

def hitung_akar_kuadrat():
    while True:
        try:
            angka = input("Masukkan angka: ")
            angka = float(angka)
            
            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                hasil = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {hasil}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

def todo_list():
    tugas = []
    while True:
        try:
            print("\nMenu:")
            print("1. Tambah Tugas")
            print("2. Hapus Tugas")
            print("3. Tampilkan Daftar Tugas")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                tugas_baru = input("Masukkan tugas: ").strip()
                if not tugas_baru:
                    raise ValueError("Tugas tidak boleh kosong.")
                tugas.append(tugas_baru)
                print(f"Tugas '{tugas_baru}' berhasil ditambahkan.")
            
            elif pilihan == "2":
                if not tugas:
                    print("Daftar tugas kosong.")
                    continue
                tugas_hapus = input("Masukkan tugas yang ingin dihapus: ").strip()
                if tugas_hapus in tugas:
                    tugas.remove(tugas_hapus)
                    print(f"Tugas '{tugas_hapus}' berhasil dihapus.")
                else:
                    raise ValueError("Tugas tidak ditemukan dalam daftar.")
            
            elif pilihan == "3":
                if not tugas:
                    print("Daftar tugas kosong.")
                else:
                    print("Daftar Tugas:")
                    for idx, t in enumerate(tugas, 1):
                        print(f"{idx}. {t}")
            
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
        
        except ValueError as e:
            print(f"Error: {e}")

todo_list()