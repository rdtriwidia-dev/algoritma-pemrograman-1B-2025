total_jam_lembur = 0
bonus_shift_malam = 0
gaji_seminggu = 0
jam_lembur = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    while True:
        jam_lembur = int(input("Masukkan jumlah jam lembur (0-8): "))
        if 0 <= jam_lembur <= 8:
            break
        elif jam_lembur > 8:
            print("Lembur melebihi batas, tidak dihitung.")
            break

    while True:
        shift = input("Apakah ini shift malam? (y/n): ").lower()
        if shift in ["y", "n"]:
            break
        else:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    gaji_harian = 100000
    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_harian += 100000
    elif jam_lembur ==5:
        gaji_harian += 125000
    elif jam_lembur == 6:
        gaji_harian += 200000
    elif jam_lembur == 7:
        gaji_harian += 225000
    elif jam_lembur == 8:
        gaji_harian += 300000


    if shift == "y":
        bonus_shift_malam += 50000

    gaji_seminggu += gaji_harian
    total_jam_lembur += jam_lembur

print("\nRekap Mingguan")
print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{bonus_shift_malam:,}")
print(f"Total gaji seminggu: Rp{gaji_seminggu:,}")