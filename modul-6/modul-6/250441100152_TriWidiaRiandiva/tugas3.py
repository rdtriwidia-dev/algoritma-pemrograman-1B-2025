def program_dominic():
    data = []

    while True:
        print("\n=== MENU CRUD ===")
        print("1. Tambah angka") #create
        print("2. Tampilkan daftar") #read
        print("3. Ubah angka") #update
        print("4. Hapus angka") #delete
        print("5. Cek pembagian sama besar")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            print("Masukkan angka satu per satu. Ketik 'selesai' untuk berhenti")
            while True:
                angka_input = input("Angka: ")
                if angka_input.lower() == "selesai":
                    break
                try:
                    angka = int(angka_input)
                    data.append(angka)
                    print("Angka ditambahkan")
                except ValueError:
                    print("Input tidak valid. Masukkan angka")

            print("\n------------------------------------------------")

        elif pilihan == "2":
            print("== Daftar angka ==")
            for i in range(len(data)):
                print(f"[{i}] {data[i]}")

            print("\n------------------------------------------------")

        elif pilihan == "3":
            while True:
                try:
                    indeks = int(input(f"Masukkan indeks yang ingin diubah (0-{len(data)-1}):"))
                    if 0 <= indeks < len(data):
                        break
                    else:
                        print(f"Indeks tidak valid. Coba lagi")
                except ValueError:
                    print("Input harus berupa angka")

            angka_baru = int(input("Masukkan angka baru:"))
            data[indeks] = angka_baru
            print("Angka berhasil diubah")
            print("== Daftar angka terbaru ==")
            for i in range(len(data)):
                print(f"[{i}] {data[i]}")

            print("\n------------------------------------------------")

        elif pilihan == "4":
            while True:
                try:
                    indeks = int(input(f"Masukkan indeks yang ingin dihapus (0-{len(data)-1}): "))
                    if 0 <= indeks < len(data):
                        break
                    else:
                        print("Indeks tidak valid. Coba lagi")
                except ValueError:
                        print("Input harus berupa angka")

            del data[indeks]
            print("Angka berhasil dihapus")
            print("== Daftar angka terbaru ==")
            for i in range(len(data)):
                print(f"[{i}] {data[i]}")
                
            print("\n------------------------------------------------")

        elif pilihan == "5":
            total = sum(data)
            if total % 2 != 0:
                hasil = False
            else:
                bagian1 = []
                bagian2 = []
                tengah = len(data) // 2
                hitung = 0
            
                for angka in data:
                    if hitung < tengah:
                        bagian1.append(angka)
                    else:
                        bagian2.append(angka)
                    hitung += 1

                total1 = sum(bagian1)
                total2 = sum(bagian2)

                print(f"Bagian 1: {bagian1}, jumlah = {total1}")
                print(f"Bagian 2: {bagian2}, jumlah = {total2}")

                hasil = total1 == total2
            
                if hasil:
                    print("True (kedua bagian memiliki jumlah yang sama)")
                else:
                    print("False (kedua bagian memiliki jumlah berbeda)")

            print("\n------------------------------------------------")
            
        elif pilihan == "6":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

program_dominic()

