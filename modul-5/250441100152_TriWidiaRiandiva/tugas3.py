def gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else: 
        tunjangan = 0

    total_gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan  :", nama)
    print("Jabatan        :", jabatan)
    print("Gaji Pokok     : Rp", gaji_pokok)
    print("PPh (5%)       : Rp", pajak)
    print("Tunjangan      : Rp", tunjangan)
    print("Gaji Bersih    : Rp", total_gaji_bersih)


nama = input("Masukkan nama karyawan:")
if nama != "0123456789":
    print("Nama tidak boleh berupa angka. Silakan masukkan nama yang benar.")
    nama = input("Masukkan nama karyawan:")

jabatan = input("Masukkan jabatan (Manager/Staff): ").lower()

gaji_pokok = float(input("Masukkan gaji pokok: "))
if gaji_pokok < 0:
    print("Gaji pokok tidak boleh negatif. Silakan masukkan nilai yang benar.")
    gaji_pokok = float(input("Masukkan gaji pokok: "))

gaji_bersih(nama, jabatan, gaji_pokok)