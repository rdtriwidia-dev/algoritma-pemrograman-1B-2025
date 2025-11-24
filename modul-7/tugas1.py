def contact_book():
    kontak = {}

    while True:
        print("\n=== MENU KONTAK ===")
        print("1. Tampilkan semua kontak")       # Read
        print("2. Cari kontak berdasarkan nama") # Read
        print("3. Tambah kontak baru")           # Create
        print("4. Perbarui email kontak")        # Update
        print("5. Hapus kontak")                 # Delete
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6):")

        if pilihan == "1":
            if not kontak:
                print("Kontak kosong")
            else:
                print("== Daftar Kontak ==")
                i = 1
                for nama in kontak:
                    data = kontak[nama]
                    print(f"{i}. {nama}: Telp = {data[0]}, Email = {data[1]}")
                    i += 1
            print("\n------------------------------------------------")

        elif pilihan == "2":
            while True:
                nama = input("Masukkan nama kontak yang dicari: ")
                if nama in kontak:
                    print(f"{nama}: Telp = {kontak[nama][0]}, Email = {kontak[nama][1]}")
                    break
                else:
                    print(f"Kontak dengan nama {nama} tidak ditemukan")
            print("\n------------------------------------------------")

        elif pilihan == "3":
            while True:
                nama = input("Masukkan nama kontak baru: ")
                ada_angka = False
                for karakter in nama:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama kontak tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break

            if nama in kontak:
                print("Kontak sudah ada")
            else:
                while True:
                    telp = input("Masukkan nomor telepon: ")
                    ada_huruf = False
                    for karakter in telp:
                        if karakter not in "0123456789":
                            ada_huruf = True
                            break
                    if ada_huruf or telp == "":
                        print("Nomor telepon harus berupa angka. Silakan coba lagi")
                    else:
                        break

                while True:
                    email = input("Masukkan email: ")
                    if "@" not in email:
                        print("Email tidak valid. Harus mengandung @ Silakan coba lagi")
                    else:
                        break

                kontak[nama] = [telp, email]
                print("Kontak berhasil ditambahkan")
                print("\n------------------------------------------------")

        elif pilihan == "4":
            print("== Daftar Kontak Saat Ini ==")
            i = 1
            for nama_kontak in kontak:
                data = kontak[nama_kontak]
                print(f"{i}. {nama_kontak}: Telp = {data[0]}, Email = {data[1]}")
                i += 1

            while True:
                nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
                if nama in kontak:
                    while True:
                        email_baru = input("Masukkan email baru: ")
                        if "@" not in email_baru:
                            print("Email tidak valid. Harus mengandung @ Silakan coba lagi")
                        else :
                            break
                    kontak[nama][1] = email_baru
                    print("Email berhasil diperbarui")
                    print("== Daftar Kontak Terbaru ==")
                    i = 1
                    for nama_kontak in kontak:
                        data = kontak[nama_kontak]
                        print(f"{i}. {nama_kontak}: Telp = {data[0]}, Email = {data[1]}")
                        i += 1
                    break
                else:
                    print(f"Kontak dengan nama {nama} tidak ditemukan")
            print("\n------------------------------------------------")

        elif pilihan == "5":
            print("== Daftar Kontak Saat Ini ==")
            i = 1
            for nama_kontak in kontak:
                data = kontak[nama_kontak]
                print(f"{i}. {nama_kontak}: Telp = {data[0]}, Email = {data[1]}")
                i += 1

            while True:
                nama = input("Masukkan nama kontak yang ingin dihapus: ")
                if nama in kontak:
                    del kontak[nama]
                    print("Kontak berhasil dihapus")
                    print("== Daftar Kontak Terbaru ==")
                    i = 1
                    for nama_kontak in kontak:
                        data = kontak[nama_kontak]
                        print(f"{i}. {nama_kontak}: Telp = {data[0]}, Email = {data[1]}")
                        i += 1
                    break
                else:
                    print(f"Kontak dengan nama {nama} tidak ditemukan.")
            print("\n------------------------------------------------")

        elif pilihan == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid")
            print("\n------------------------------------------------")

contact_book()