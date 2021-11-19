i1 = input("Masukan daftar belanja : ").title().split(",")
print("Daftar belanja :", i1)

i2 = input("Masukan barang yang ingin ditambahkan : ").lower()
if i2.title() in i1:
    print("Barang", i2.upper(), "sudah berada dalam daftar belanja")
else:
    i1.append(i2.upper())
    print("Hasil penambahan pada daftar belanja", i1)