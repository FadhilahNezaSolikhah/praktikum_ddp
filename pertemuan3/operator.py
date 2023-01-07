number1 = 5
number2 = 10

# Operator Perbandingan
print(number1 != number2)

if number1 != number2:
    print("Nomor Berbeda !")
else :
    print("Nomor Sama !")

# Operator Logika
if number1 > 99 and number1 < 1000:
    print("Bilangan ratusan !")
else :
    print ("Bukan Bilangan Ratusan !")

# Operator Aritmatika
while True :
    number3 = int(input("Masukkan angka = "))

    if number3 == 00 :
        break
    if number3 % 2 == 0 :
        print("Bilangan Genap")
    else :
        print("Bilangan Ganjil")