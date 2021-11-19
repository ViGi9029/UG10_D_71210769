b1 = int(input("Masukkan bilangan 1 : "))
b2 = int(input("Masukkan bilangan 2 : "))
b3 = int(input("Masukkan bilangan 3 : "))

if b1>b2 and b2>b3 :
    print("Urutan bilangan dari yang terbesar adalah", b1,b2,b3)
elif b1<b2 and b2<b3 :
    print("Urutan bilangan dari yang terbesar adalah", b3,b2,b1)
elif b1<b2 and b1>b3  :
    print("Urutan bilangan dari yang terbesar adalah", b2,b1,b3)
elif b3<b2 and b1<b3 :
    print("Urutan bilangan dari yang terbesar adalah", b2,b3,b1)
elif b1<b3 and b2<b1 :
    print("Urutan bilangan dari yang terbesar adalah", b3,b1,b2)
elif b1>b3 and b3>b2 :
    print("Urutan bilangan dari yang terbesar adalah", b1,b3,b2)
elif b1==b3 and b2>b3 :
    print("Urutan bilangan dari yang terbesar adalah", b2,b1,b3)
elif b2==b3 and b1>b3 :
    print("Urutan bilangan dari yang terbesar adalah", b1,b2,b3)
elif b1==b2 and b3>b1 :
    print("Urutan bilangan dari yang terbesar adalah", b3,b1,b2)
elif b1==b3 and b2<b3 :
    print("Urutan bilangan dari yang terbesar adalah", b3,b1,b2)
elif b2==b3 and b1<b3 :
    print("Urutan bilangan dari yang terbesar adalah", b3,b2,b1)
elif b1==b2 and b2>b3 :
    print("Urutan bilangan dari yang terbesar adalah", b2,b1,b3)
elif b1==b3 and b2==b3 :
    print("Urutan bilangan dari yang terbesar adalah", b1,b2,b3)
else :
    print("error otakku")