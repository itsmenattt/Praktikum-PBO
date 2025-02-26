#TUGAS NO. 1
height = int(input("Masukkan tinggi: "))

for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))

