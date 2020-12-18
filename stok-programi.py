"""
prgramın işeyişi
! 1- program başlayınca bize bir menü gelecek, bu menüde aşağıdaki şekilde bir liste olacak:
* ürünleri listele
* ürün ekle 
* ürün sil
 ! 2- ürünleri listeleyi seçersen o ana kadar eklenen ürünleri, kullanıcıya göster
 ! 3- ürün ekleyi seçersem, program benden , ürün adı, fiyatı, ve kaç adet bulunduğunu bana sormalı ve bu bilgileri kaydetmeli
4- ürün sili seçersem, program yine ürünleri listeleyerek ve yanında hangi sayı bulunan ürünü silmek istiyorsak o numarayı yazmamızı isteyecek
"""

# program artık başlıyor...

# kalıcı değşkenler burada tanımlama nedenim programın her yeniden bu değşkenlere ulaşmam içinmdir.

urunAdilistesi = []  
urunFiyatiListesi= [] 
urunStoguListesi = []
uygulamaCalisiyor = True



print("******************\npython ile yazılmış basit stok programına hoşgeldiniz...\n******************")
while(uygulamaCalisiyor):
    print("*******************************************")
    print("işlem listesi:\n1-ürünleri listele\n2-ürün ekle\n3-ürün sil\n4- programı kapatmak için q tuşuna basmak yeterlidir")
    islemNo = input("işlem numarasını giriniz : ")

    if islemNo =="1":
        for urun in urunAdilistesi:
            print(" - ",urun)

        print("ürünleri listele seçildi...")
    elif islemNo =="2":
        urunAdi = input("ürünün adı :")
        urunFiyati = input("ürünün fiyatı :")
        urunStogu = input("stok sayisi : ")

        urunAdilistesi.append(urunAdi)
        urunFiyatiListesi.append(urunFiyati)
        urunStoguListesi.append(urunStogu)

        print(urunStogu, urunAdi,"sisteme başarıyla eklendi")

        print("ürünleri ekle seçildi...")
    elif islemNo == "3":

        if len(urunAdilistesi) ==0: # len uzunluktan geliyo yani lenght arrayinn içindeki uzunluğu ölçer
            print("silmek için ürün yok")
        else:
            i = 0
            for urun in urunAdilistesi:
                print(" - ",i,urun)
                i+=1
            urunKodu = input("silmek istediğiniz ürünün kodu : ")
            urunKodu = int(urunKodu)
            
            urunAdilistesi.pop(urunKodu)
            urunFiyatiListesi.pop(urunKodu)
            urunStoguListesi.pop(urunKodu)

            print("ürün silme gerçekleşti")
    elif islemNo =="q":
        print("programdan çıkış yapılıyor")
        uygulamaCalisiyor = False
    else:
        print("hatalı işlem numarası")
                