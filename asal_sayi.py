
while True:
    a = int(input("Bir sayı seçin: "))
    b = int(input("Başka bir sayı seçin (bu sayı dahil olmayacak): "))
    if a != 1:
        print("İlk sayı 1 olmazsa hesaplama yanlış olur!")
    elif a < b:
        liste = list(range(a, b))
        liste2 = []
        asal_sayilar = []

        for i in liste:
            if (i > 0 and i % 2 == 1) or i == 2:
                liste2.append(i)
        for i in liste2:
            for x in liste2:
                if i < x:
                    break
                elif x != 1 and i % x == 0 and x <= i:
                    asal_sayilar.append(x)
                    break
        asal_sayilar = set(asal_sayilar)
        print(asal_sayilar)
        break
    else:
        print("İlk sayı ikinci sayıdan küçük olmalı!!!")

