def sirakayit():
    isim = input("İsim:")
    soyad = input("Soyad:")
    import random
    sira = print("Sıranız :{}.".format(random.randint(1, 100)))

ürünlistesi = {"yiyecekler":{}, "içecekler":{}, "temizlik":{}, "teknolojik":{}}

def ürünkayıt():
    ürünlistesi = {"yemekler": {}, "içecekler": {}, "aburcuburlar": {}, "dondurmalar": {}}
    durum = 1
    while  durum == 1:
        kategori = input("Hangi kategoride ürün ekleyeceksiniz?(Yemek(y),İçecek(i), Aburcubur(a), Dondurma(d)")
        if kategori == "y":
            ürünlistesi["yemekler"].setdefault(input("Ürün ismini giriniz:"), input("Fiyatını giriniz:"))
        elif kategori == "i":
            ürünlistesi["içecekler"].setdefault(input("Ürün ismini giriniz:"), input("Fiyatını giriniz:"))
        elif kategori == "a":
            ürünlistesi["aburcuburlar"].setdefault(input("Ürün ismini giriniz:"), input("Fiyatını giriniz:"))
        elif kategori == "d":
            ürünlistesi["dondurmalar"].setdefault(input("Ürün ismini giriniz:"), input("Fiyatını giriniz:"))
        durum = int(input("Başka ürün girecekseniz 1'e girmeyecekseniz 2'ye basın:"))
    print(ürünlistesi)

def ürünsatış():
    sepet = 0
    durum = 1
    while durum == 1:
        ürün = input("Almak istediğiniz ürünün adı:")
        adet = int(input("Almak istediğiniz adet:"))
        if ürün in ürünlistesi:
            sepet =+ ürün*adet
        else:
            print("Girdiğiniz ürün kantinimizde bulunmamaktadır.")
        durum = input("Alişverişe devam(1), Sepete git(2)")
    öğrenci = input("Öğrenci miyiz?:Evet(e), Hayır(h)")
    if öğrenci == 'e' and sepet > 100:
        sepet = sepet-sepet*35/100
    elif öğrenci == 'e':
        sepet = sepet-sepet*25/100
    elif sepet > 100:
        sepet = sepet-sepet*10/100

    print("Toplam sepet tutarı:{}tl".format(sepet))

    ciro =+ sepet







