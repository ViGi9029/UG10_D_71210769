a = int(input("Nilai a :"))
b = int(input("Nilai b :"))
c = int(input("Nilai c :"))

d = ((b**2)-(4*a*c))
x = d**0.5
if d < 0 :
    print("Fungsi tersebut tidak memiliki akar riil")
elif d > 0 :
    print("Akar dari persamaan tersebut adalah "+str(d)+" dan "+str(x))
elif d == 0 :
    print("Fungsi tersebut memiliki akar kembar yaitu "+ d)
else :
    print("otak error")