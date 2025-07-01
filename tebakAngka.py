import random

def tebak_angka():
    angka_rahasia = random.randint(1, 20)
    percobaan = 0
    max_percobaan = 10

    print(" GAME TEBAK ANGKA ")
    print("Aku sudah memilih angka dari 1 sampai 20.")
    print(f"Tebak dalam maksimal {max_percobaan} kali yaa!")

    while percobaan < max_percobaan:
        try:
            tebak = int(input(f"Tebakan ke-{percobaan + 1}: "))
        except ValueError:
            print("Masukkan angka yaa, bukan huruf!")
            continue

        percobaan += 1

        if tebak < angka_rahasia:
            print("Terlalu kecil!")
        elif tebak > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(f"YEAY! Kamu berhasil menebak dalam {percobaan} kali percobaan 🎉")
            break
    else:
        print(f"Sayang banget, kamu kehabisan percobaan. Angkanya adalah {angka_rahasia} 😭")

# Jalankan program
tebak_angka()
