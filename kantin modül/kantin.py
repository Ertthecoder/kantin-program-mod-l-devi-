import modulekantin

print("Kantine hoş geldiniz!\n")
işlem = input("Alışveriş yapmak için 'a'ya, kayıt olup sıra almak için 'k'ye, personel girişi için 'p'ye basın:\n")

if işlem == 'a':
    modulekantin.ürünsatış()
elif işlem == 'k':
    modulekantin.sirakayit()
elif işlem == 'p':
    modulekantin.ürünkayıt()




