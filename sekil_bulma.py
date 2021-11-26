print("""**************************************

Uygulamaya hoş geldiniz!

Lütfen bulmak istediğiniz geometrik şeklin tipini seçiniz.

1-) Dörtgen
2-) Üçgen

**************************************
""")
a = str(input("Şekil tipi: "))

if a == "Dörtgen" or a == "dörtgen":
    print("Lütfen kenar uzunluklarını belirtin.")
    q = int(input("1. kenar uzunluğu: "))
    w = int(input("2. kenar uzunluğu: "))
    e = int(input("3. kenar uzunluğu: "))
    r = int(input("4. kenar uzunluğu: "))
    if q == w and w == e and e == r:
        print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Kare")
    elif q == e and w == r:
        print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Dikdörtgen")
    elif w == e and q == r:
        print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Dikdörtgen")
    elif q == w and e == r:
        print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Dikdörtgen")
    else:
        print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Dörtgen(Yamuk)")
elif a == "Üçgen" or a == "üçgen":
    print("Lütfen kenar uzunluklarını belirtin.")
    q = int(input("1. kenar uzunluğu: "))
    w = int(input("2. kenar uzunluğu: "))
    e = int(input("3. kenar uzunluğu: "))
    x = abs(q + w)
    y = abs(q - w)
    if (x > e) and (e > y):
        if q == w and w == e:
            print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Eşkenar Üçgen")
        elif q == w and w != e:
            print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: İkizkenar Üçgen")
        elif q != w and w == e:
            print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: İkizkenar Üçgen")
        else:
            print("Belirtmiş olduğunuz kenar uzunluklarına göre geometrik şekliniz: Üçgen")
    else:
        print("Belirtmiş olduğunuz kenar uzunlukları bir üçgen belirtmiyor.")
else:
    print("Lütfen belirtilen seçeneklerden birini seçiniz.")
