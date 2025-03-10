# Kelas Induk
class Kendaraan:
    def _init_(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")
    
    def bergerak(self):
        print(f"Kendaraan {self.jenis} sedang bergerak")

# Kelas turunan dari Kendaraan
class Mobil(Kendaraan):
    def _init_(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super()._init_(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merk: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")
    
    def bunyikan_klakson(self):
        print(f"Mobil {self.merk} berbunyi: Tuing! Tuing!")

# Kelas turunan dari Mobil dengan enkapsulasi
class MobilSport(Mobil):
    def _init_(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super()._init_(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self._tenaga_kuda = tenaga_kuda
        self._harga = harga
    
    # Getter dan Setter untuk tenaga_kuda
    def get_tenaga_kuda(self):
        return self._tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        self._tenaga_kuda = value
    
    # Getter dan Setter untuk harga
    def get_harga(self):
        return self._harga
    
    def set_harga(self, value):
        self._harga = value
    
    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self._tenaga_kuda} HP")
        print(f"Harga: Rp {self._harga} juta")
    
    def mode_balap(self):
        print(f"Mobil Sport {self.merk} telah masuk mode balap!")


ferrari = MobilSport("Sport", 340, "Ferrari", 2, 670, 8500)

ferrari.info_mobil_sport()
ferrari.bergerak()
ferrari.bunyikan_klakson()
ferrari.mode_balap()
    
ferrari.set_tenaga_kuda(700)
ferrari.set_harga(9000)
print(f"Tenaga Kuda baru: {ferrari.get_tenaga_kuda()} HP")
print(f"Harga baru: Rp {ferrari.get_harga()} juta")
