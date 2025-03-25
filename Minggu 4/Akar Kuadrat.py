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

hitung_akar_kuadrat()
