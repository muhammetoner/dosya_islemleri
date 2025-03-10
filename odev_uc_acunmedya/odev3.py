import codecs



dosya_olustur=input("Lütfen dosya adını giriniz: ")
dosya_NEW=dosya_olustur+".txt"
veri_gir= input(f"Lütfen {dosya_NEW}  dosyasına veri ekleyin :")


with open(dosya_NEW, "w", encoding="utf-8") as dosya:
    dosya.write(veri_gir)
    soru_sor=input("Dosya Üzeerine ekleme yapmak ister misiniz? E/H :").lower()
    if soru_sor=="e":
        open(dosya_NEW,"a")
        yeni_veri=input("Lütfen eklemek istediğiniz veriyi yazınız: ")
        yeni_veri= "\n"+yeni_veri
        dosya.write(yeni_veri)
        print("Verileriniz Güncellendi :)")
    else:
        print("çıkış yapılıyor")

            

info =codecs.open(dosya_NEW,"r",encoding="utf-8")
 
a=info.read()
print("-"*45)
print(a)
print("-"*45)