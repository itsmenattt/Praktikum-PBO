nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas Praktikum: ")

teks = "Nama: {}\nNIM: {}\nKelas Praktikum: {}".format(nama, nim, kelas)
file = open("Me.txt", "w")

file.write(teks)