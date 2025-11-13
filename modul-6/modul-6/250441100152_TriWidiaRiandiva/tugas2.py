input_t1 = input("Masukkan angka untuk tuple pertama (pisahkan dengan spasi):")
input_t2 = input("Masukkan angka untuk tuple kedua (pisahkan dengan spasi):")

t1 = tuple(int(x) for x in input_t1.split()) 
t2 = tuple(int(x) for x in input_t2.split())

def gabungan_urut(t1, t2):
    gabung = list (t1 + t2)

    angka_tanpa_duplikat = []
    for angka in gabung:
        if angka not in angka_tanpa_duplikat:
            angka_tanpa_duplikat.append(angka)

    for i in range(len(angka_tanpa_duplikat)):
        for j in range(i + 1, len(angka_tanpa_duplikat)):
            if angka_tanpa_duplikat[j] > angka_tanpa_duplikat[i]:
                angka_tanpa_duplikat[i], angka_tanpa_duplikat[j] = angka_tanpa_duplikat[j], angka_tanpa_duplikat[i]

    return tuple(angka_tanpa_duplikat)

print("Hasil gabungan urut:", gabungan_urut(t1,t2))
