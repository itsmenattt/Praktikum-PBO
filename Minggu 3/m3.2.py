class GolonganDarah:
    def __init__(self, alel1, alel2):
        self.alel1 = alel1.upper()
        self.alel2 = alel2.upper()
    
    def get_fenotipe(self):
        if 'A' in (self.alel1, self.alel2) and 'B' in (self.alel1, self.alel2):
            return "AB"
        elif 'A' in (self.alel1, self.alel2):
            return "A"
        elif 'B' in (self.alel1, self.alel2):
            return "B"
        else:
            return "O"

class Keluarga:
    def __init__(self):
        self.ayah = None
        self.ibu = None
        self.anak = None
        self.kemungkinan_anak = []
    
    def set_orang_tua(self, nama_ayah, goldar_ayah, nama_ibu, goldar_ibu):
        self.ayah = {'nama': nama_ayah, 'goldar': goldar_ayah}
        self.ibu = {'nama': nama_ibu, 'goldar': goldar_ibu}
    
    def hitung_kemungkinan_anak(self):
        alel_ayah = [self.ayah['goldar'].alel1, self.ayah['goldar'].alel2]
        alel_ibu = [self.ibu['goldar'].alel1, self.ibu['goldar'].alel2]
        
        for a_ayah in alel_ayah:
            for a_ibu in alel_ibu:
                gd_anak = GolonganDarah(a_ayah, a_ibu)
                if gd_anak.get_fenotipe() not in self.kemungkinan_anak:
                    self.kemungkinan_anak.append(gd_anak.get_fenotipe())
    
    def tampilkan_info(self):
        print("\n=== Informasi Keluarga ===")
        print(f"\nAyah:")
        print(f"Nama: {self.ayah['nama']}")
        print(f"Golongan Darah: {self.ayah['goldar'].get_fenotipe()}")
        print(f"Genotipe: {self.ayah['goldar'].alel1}{self.ayah['goldar'].alel2}")
        
        print(f"\nIbu:")
        print(f"Nama: {self.ibu['nama']}")
        print(f"Golongan Darah: {self.ibu['goldar'].get_fenotipe()}")
        print(f"Genotipe: {self.ibu['goldar'].alel1}{self.ibu['goldar'].alel2}")
        
        print("\nKemungkinan Golongan Darah Anak:")
        print(f"Anak dari {self.ayah['nama']} dan {self.ibu['nama']} bisa memiliki golongan darah: {', '.join(self.kemungkinan_anak)}")

def input_golongan_darah(peran):
    while True:
        print(f"\nMasukkan data {peran}:")
        nama = input(f"Nama {peran}: ")
        print("Masukkan genotipe (pilih dua alel: A, B, atau O)")
        alel1 = input("Alel 1: ").upper()
        alel2 = input("Alel 2: ").upper()
        
        if alel1 in ['A', 'B', 'O'] and alel2 in ['A', 'B', 'O']:
            return nama, GolonganDarah(alel1, alel2)
        else:
            print("Error: Alel harus A, B, atau O. Silakan coba lagi.")

def main():
    print("=== Program Simulasi Pewarisan Golongan Darah ===")
    
    keluarga = Keluarga()
    
    nama_ayah, goldar_ayah = input_golongan_darah("Ayah")
    nama_ibu, goldar_ibu = input_golongan_darah("Ibu")
    
    keluarga.set_orang_tua(nama_ayah, goldar_ayah, nama_ibu, goldar_ibu)
    keluarga.hitung_kemungkinan_anak()
    keluarga.tampilkan_info()

if __name__ == "__main__":
    main()