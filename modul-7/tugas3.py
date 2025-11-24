def tampilkan_kupon(kupon):
        print("== Kupon Tersedia ==")
        for kode, diskon in kupon.items():
            print(f"- {kode}: {diskon}%")

        print("\n------------------------------------------------")

def proses_transaksi(kupon):
    try:
        barang = input("Masukkan nama barang yang dibeli: ")

        while True:  
            total_input = input(f"Masukkan total belanja untuk {barang}: ")
            try:
                total = float(total_input)
                if total <= 0:
                    print("Total belanja harus lebih dari 0. Silakan coba lagi")
                else:
                    break
            except:
                print("Input tidak valid. Masukkan angka total belanja yang benar")

        while True:
            kode = input("Masukkan kode kupon: ").upper()
            if kode in kupon:
                persen = kupon[kode]
                potongan = total * persen / 100
                total_bayar = total - potongan
                print(f"Kupon valid: {persen}% diskon")
                print(f"Barang: {barang}")
                print(f"Potongan: Rp{potongan:,}")
                print(f"Total yang harus dibayar: Rp{total_bayar:,}")
                del kupon[kode]
                print("Transaksi selesai. Kupon telah digunakan dan tidak bisa dipakai lagi")
                break
            else:
                print("Kupon tidak valid atau sudah digunakan. Silakan masukkan kode kupon yang tersedia berikut:")
                print("== Kupon Tersedia ==")
                for kode, diskon in kupon.items():
                    print(f"- {kode}: {diskon}%")
                if not kupon:
                    print("Tidak ada kupon tersisa. Transaksi tanpa diskon")
                    print(f"Barang: {barang}")
                    print(f"Total yang harus dibayar: Rp{total:,}")
                    break
    except:
        print("Input total belanja tidak valid")

    print("\n------------------------------------------------")

def sistem_kupon_diskon():
    kupon = {
        "HEMAT10": 10,
        "DISKON20": 20,
        "PROMO30": 30
    }

    while True:
        print("\n=== MENU KUPON DISKON ===")
        print("1. Tampilkan semua kupon tersedia")
        print("2. Proses transaksi dengan kupon")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_kupon(kupon)
        elif pilihan == "2":
            proses_transaksi(kupon)
        elif pilihan == "3":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")
            print("\n------------------------------------------------")


sistem_kupon_diskon()


