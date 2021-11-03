# peogram menentukan 3 bilangan terbesar

print(20*"=")

a =int(input("masukan bilangan ke 1 = "))
b =int(input("masukan bilangan ke 2 = "))
c =int(input("masukan bilangan ke 3 = "))


if a > b and a > c :
    print("bilangan ke 1 yang terbesar")
elif b > a and b > c :
    print("bilangan ke 2 yang terbesar")
elif c > a and c > b:
    print ("bilangan ke 3 yang terbesar")
else:
    print("kesalahan")

print(20*"=")