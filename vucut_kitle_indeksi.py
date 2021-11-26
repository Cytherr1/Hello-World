print("""***************************************************

Uygulamaya hoş geldiniz!

Bu program sizden boy ve kilonuzu alarak vücut
kitle endeksinizi hesaplayarak sağlık durumunuz hakkında bilgi verir.

***************************************************
""")
isim = str(input("Adınızı öğrenmekle başlayalım: "))
boy = float(input("Lütfen metre cinsinden boyunuzu giriniz: "))
kilo = float(input("Lütfen kilonuzu giriniz: "))
print("""*********

Hesaplanıyor......

*********""")

bki = kilo/(boy**2)

if bki < 18.5:
    print("""Vücut kitle indeksinize göre zayıfsınız {}.
    Kilonuzu sağlığınız açısında normal aralığa çekmeniz sizin yararınıza olacaktır""".format(isim))
elif bki < 25 and bki >= 18.5:
    print("""Kilonuz gayet normal {}.
    Sakın formunuzu bozmayın, aynen devam!""".format(isim))
elif bki < 30 and bki >= 25:
    print("""Vücut kitle indeksinize göre fazla kilolusunuz ancak obez değilsiniz {}.
    Lütfen yediklerinize dikkat edin.""".format(isim))
elif bki >= 30:
    print("""Vücut kitle indeksinize göre obez olarak nitelendirilmektesiniz {}.
    Lütfen bir diyet programına kaydolun.""".format(isim))



