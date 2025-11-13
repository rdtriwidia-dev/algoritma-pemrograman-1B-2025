def menu():
    data_kunjungan = []
    id_counter = 1

    while True:
        print("\n=== Sistem Kunjungan Santri ===")
        print("1. Tambah Pengunjung")
        print("2. Tampilkan Daftar Pengunjung")
        print("3. Hapus Pengunjung")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            while True :
                nama_pengunjung = input("Masukkan nama pengunjung: ")
                ada_angka = False
                for karakter in nama_pengunjung:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama pengunjung tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break

            while True :
                nama_santri = input("Masukkan nama santri yang dijenguk: ")
                ada_angka = False
                for karakter in nama_santri:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama santri tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break
            
            while True:
                daerah = input("Masukkan daerah asal pengunjung (Sumatra/Kalimantan/Jawa):").lower()
                if daerah in ["sumatra", "kalimantan", "jawa"]:
                    break
                else :
                    print("Daerah tidak valid. Silahkan coba lagi")
               

            data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
            print(f"Data berhasil ditambahkan dengan ID antrian: {id_counter}")
            id_counter += 1

        elif pilihan == "2":
            print("\n=== Daftar Pengunjung Berdasarkan Daerah ===")
            for daerah in ["sumatra", "kalimantan", "jawa"]:
                print(f"\nPengunjung dari {daerah}:")
                for data in data_kunjungan:
                    if data[3] == daerah:
                        print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}")

        elif pilihan == "3":
            while True:
                    try:
                        id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi")
                        continue  
                    for data in data_kunjungan:
                        if data[0] == id_hapus:
                            data_kunjungan.remove(data)
                            print(f"Data dengan ID {id_hapus} berhasil dihapus")
                            break
                    else:
                        print("ID tidak ditemukan, silahkan input ID yang tersedia")
                        continue
                    break
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem kunjungan santri")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4")

menu()