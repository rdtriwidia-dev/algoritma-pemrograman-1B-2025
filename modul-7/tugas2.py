def inventaris_gudang():
    gudang = {}
    ID = 1

    while True:
        print("\n=== MENU INVENTARIS ===")
        print("1. Tampilkan semua barang")       # Read
        print("2. Cari barang berdasarkan ID")   # Read
        print("3. Tambah barang baru")           # Create
        print("4. Perbarui stok barang")         # Update
        print("5. Hapus barang")                 # Delete
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            if not gudang:
                print("Inventaris kosong")
            else:
                print("== Daftar Barang ==")
                for id_barang, data in gudang.items():
                    nama, harga, stok = data
                    print(f"ID: {id_barang} | Nama: {nama} | Harga: {harga} | Stok: {stok}")
            print("\n------------------------------------------------")

        elif pilihan == "2":
            cari_id = input("Masukkan ID barang yang dicari: ")
            barang = gudang.get(cari_id)
            if barang:
                nama, harga, stok = barang
                print(f"ID: {cari_id} | Nama: {nama} | Harga: {harga} | Stok: {stok}")
            else:
                print(f"Barang dengan ID {cari_id} tidak ditemukan")
            print("\n------------------------------------------------")

        elif pilihan == "3":
            while True:
                nama = input("Masukkan nama barang: ")
                ada_angka = False
                for karakter in nama:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama barang tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break

            while True:
                harga_input = input("Masukkan harga barang: ")
                try:
                    harga = float(harga_input)
                    if harga < 0:
                        print("Harga tidak boleh negatif")
                    else:
                        break
                except:
                    print("Harga harus berupa angka")

            while True:
                stok_input = input("Masukkan jumlah stok: ")
                try:
                    stok = int(stok_input)
                    if stok < 0:
                        print("Stok tidak boleh negatif")
                    else:
                        break
                except:
                    print("Stok harus berupa angka")

            gudang[str(ID)] = [nama, harga, stok]
            print(f"Barang berhasil ditambahkan dengan ID: {ID}")
            ID += 1
            print("\n------------------------------------------------")

        elif pilihan == "4":
            if not gudang:
                print("Inventaris kosong")
                continue

            print("== Daftar Barang Saat Ini ==")
            for id_barang, data_barang in gudang.items():
                nama, harga, stok = data_barang
                print(f"ID: {id_barang} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

            while True:
                id_update = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
                try:
                    int(id_update)
                except:
                    print("ID harus berupa angka. Silakan coba lagi")
                    continue

                if id_update not in gudang:
                    print(f"Barang dengan ID {id_update} tidak ditemukan. Silakan coba lagi")
                    continue
                else:
                    break

            while True:
                print("1. Tambah stok")
                print("2. Kurangi stok")
                pilihan_stok = input("Pilih pilihan stok (1/2): ")

                if  pilihan_stok not in ["1", "2"]:
                    print("Pilihan tidak valid. Silakan pilih 1 atau 2")
                    continue

                jumlah_input = input("Masukkan jumlah stok yang ingin diubah: ")
                try:
                    jumlah = int(jumlah_input)
                    if jumlah < 0:
                        print("Jumlah tidak boleh negatif. Silakan coba lagi")
                        continue

                    if  pilihan_stok == "1":
                        gudang[id_update][2] += jumlah
                        print("Stok berhasil ditambahkan")
                    else:
                        if jumlah > gudang[id_update][2]:
                            print("Jumlah pengurangan melebihi stok yang tersedia. Silakan coba lagi")
                            continue
                        gudang[id_update][2] -= jumlah
                        print("Stok berhasil dikurangi")
                    break
                except:
                    print("Input jumlah harus berupa angka. Silakan coba lagi")

            print("== Daftar Barang Terbaru ==")
            for id_barang, data_barang in gudang.items():
                nama, harga, stok = data_barang
                print(f"ID: {id_barang} | Nama: {nama} | Harga: {harga} | Stok: {stok}")
            print("\n------------------------------------------------")
    
        elif pilihan == "5":
            if not gudang:
                print("Inventaris kosong")
                continue

            print("== Daftar Barang Saat Ini ==")
            for id_barang, data_barang in gudang.items():
                nama, harga, stok = data_barang
                print(f"ID: {id_barang} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

            while True:
                id_hapus = input("Masukkan ID barang yang ingin dihapus: ")
                try:
                    int(id_hapus)  
                except ValueError:
                    print("ID harus berupa angka. Silakan coba lagi")
                    continue

                if id_hapus not in gudang:
                    print(f"Barang dengan ID {id_hapus} tidak ditemukan. Silakan coba lagi")
                    continue  
                
                del gudang[id_hapus]
                print("Barang berhasil dihapus")
                break
            print("== Daftar Barang Terbaru ==")
            for id_barang, data_barang in gudang.items():
                nama, harga, stok = data_barang
                print(f"ID: {id_barang} | Nama: {nama} | Harga: {harga} | Stok: {stok}")
            print("\n------------------------------------------------")

        elif pilihan == "6":
            print("Program selesai")
            break
        
        else:
            print("Pilihan tidak valid")

inventaris_gudang()