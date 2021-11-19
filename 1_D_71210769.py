makanan = int(input("Harga makanan sebesar Rp "))
snack = int(input("Harga snack sebesar Rp "))
minuman = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))

total = int(makanan+snack+minuman)

print("Total yang harus anda bayar sebesar Rp "+ str(total))

if uang < total :
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp "+ str(total-uang))
elif total == uang :
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
elif uang > total :
    print("Anda memiliki kembalian sebesar Rp "+ str(uang-total))
else:
    print("error")
