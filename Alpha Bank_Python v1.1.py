

### Giriş Kısmı ###
print("\n\n    *|*  ALPHA BANK TÜRKİYE ŞUBESİNE HOŞGELDİNİZ  *|* ")

ad = input("\n  Adınızı giriniz: ")
soyad = input("\n  Soyadınızı giriniz: ")



### TC Kimlik Numarası Girişi ###
tc = int(input("\n  TC Kimlik Numaranızı giriniz: "))

while True:

    if tc > 99999999999:
        print("\n  TC Kimlik Numaranız 11 haneli olmalıdır!")
        tc = int(input("\n  TC Kimlik Numaranızı tekrar giriniz: "))
        continue

    elif tc < 10000000000:
        print("\n  TC Kimlik Numaranız 11 haneli olmalıdır!")
        tc = int(input("\n  TC Kimlik Numaranızı tekrar giriniz: "))
        continue

    else: break;



### Şifre Girişi ###
sifre = int(input("\n  Lütfen 4 haneli kart şifrenizi giriniz: "))

while True:

    if sifre > 9999:
        print("\n  Şifreniz 4 haneli olmalıdır!")
        sifre = int(input("\n  Lütfen 4 haneli kart şifrenizi giriniz: "))
        continue

    elif sifre < 1000:
        print("\n  Şifreniz 4 haneli olmalıdır!")
        sifre = int(input("\n  Lütfen 4 haneli kart şifrenizi giriniz: "))
        continue

    else: break;


    
### Banka İşlemleri Enterleme ve Şifre Kontrolü ###
bakiye = 0

print("\n\n\n\n  **Banka İşlemleri **")

bos = input("\n\n  Lütfen Kartınızı Yerleştiriniz ve ENTER Tuşuna Basınız...")

while True:

     girilen_sifre = int(input("\n  Lütfen Kart Şifrenizi Giriniz: "))
     
     if sifre == girilen_sifre:
         print("\n  ŞİFRENİZ DOĞRU")
         break;

     else: print("\n  Girdiğiniz şifre hatalı lütfen tekrar deneyiniz!")



     # alt + e = €
     # alt + t = ₺
     # alt + 2 = £
     # alt + 4 = $



### Banka İşlemleri ###
print("\n\n\n\n  Lütfen Yapmak İstediğiniz İşlemin Sayısını Yazarak ENTER Tuşuna basınız... ")
print("\n  1 - Hesap sahibi bilgileri")
print("\n  2 - Hesaptan Para Çekme")
print("\n  3 - Hesaptan Para yatırma")
print("\n  4 - Bakiye Sorgulama")
print("\n  5 - (EUR/TRY) Euro (€) kuru ile bakiye sorgulama")
print("\n  6 - (USD/TRY) Dolar ($) kuru ile bakiye sorgulama")
print("\n  7 - (GBP/TRY) İngiliz Sterlin (£) kuru ile bakiye sorgulama")
print("\n  8 - Şifre Değiştirme")
print("\n  9 - Çıkış Yapmak İstiyorum")



while True:

       islem = int(input("\n\n  Hangi işlemi yapmak istersiniz? : "))
       
       ### Hesap Sahibi Bilgileri sorgulama ###
       if islem == 1:
           print("\n  Bilgileriniz; \n")
           print("\n  Kullanıcı adı: ",ad)
           print("\n  Kullanıcı soyadı: ",soyad)
           print("\n  TC Kimlik Numarası: ",tc)
           print("\n  Hesap bakiyesi: ",bakiye)
           print("\n  Hesap Şifresi: ",sifre)
           continue
       


       ### Para Çekme ###
       elif islem == 2:
           tutar = int(input("\n  Çekmek İstediğiniz Tutarı Giriniz: "))
          
           if tutar <= bakiye:
              print("\n  Hesabınızdan {} ₺ çekilmiştir".format(tutar))          
              bakiye = bakiye - tutar
              print("\n  Kalan bakiyeniz {} ₺ dir...".format(bakiye))

           else:
              print("\n  Hesabınızda yeterli bakiye yok!")
              continue
           


       ### Para Yatırma ###
       elif islem == 3:
           tutar = int(input("\n  Yatırmak İstediğiniz Tutarı Giriniz: "))
           bakiye = bakiye + tutar
           print("\n  Hesabınıza {} ₺ yatırılmıştır".format(tutar))
           print("\n  Toplam Bakiyeniz {} ₺ dir...".format(bakiye))
           continue
       


       ### Bakiye Sorgulama ###
       elif islem == 4:
           print("\n\n  Banka hesabınızda toplam {} ₺ bakiye bulunmaktadır...".format(bakiye))
           continue



       ### Euro Bakiye Sorgulama ###
       elif islem == 5:
           print("\n\n  Şu an ki (EUR/TRY) kuru 17.48 ₺'dir.")
           print("\n  Banka hesabınızda toplam {} € (euro) bakiye bulunmaktadır...".format(bakiye / 17.48))
           continue



       ### Dolar Bakiye Sorgulama ###
       elif islem == 6:
           print("\n\n Şu an ki (USD/TRY) kuru 16.76 ₺'dir.")
           print("\n Banka hesabınızda toplam {} $ (dolar) bakiye bulunmaktadır...".format(bakiye / 14.76))
           continue



       ### Sterlin Bakiye Sorgulama ###
       elif islem == 7:
           print("\n\n Şu an ki (GBP/TRY) kuru 20.29 ₺'dir.")
           print("\n Banka hesabınızda toplam {} £ (sterlin) bakiye bulunmaktadır...".format(bakiye / 20.29))
           continue






       ### Şifre Değiştirme ###
       elif islem == 8:

           msifre = int(input("\n  Lütfen mevcut şifrenizi giriniz: "))

                      
           while True:
                if msifre == sifre:
                    ysifre = int(input("\n  Lütfen yeni şifrenizi giriniz: "))
                

                    if ysifre < 1000 | ysifre > 9999:
                        print("\n  Yeni şifreniz 4 haneli olmalıdır! Lütfen tekrar deneyiniz: ")
               
                    else: 
                        yysifre = int(input("\n  Lütfen yeni şifrenizi tekrar giriniz: "))

                        if yysifre == ysifre:
                            print("\n  Şifreniz değiştirildi... Yeni şifreniz: ", yysifre)
                            break;

                        else: 
                            print("\n  Yanlış veya eksik tuşlama yaptınız... Lütfen tekrar deneyiniz: ")
                       
  
                else: print("\n  Yanlış şifre girişi! Lütfen tekrar deneyiniz: ")
                
               
             
                   
           




       ### Çıkış Yapma ###
       elif islem == 9: 
           print("\n  Çıkış yapılıyor...")
           break;



       ### Yanlış İşlem Tuşlama ###
       else: 
           print("\n  Böyle bir seçim bulunmamaktadır!")
           
           
           
           
           
           
           
           
           
           
           
           