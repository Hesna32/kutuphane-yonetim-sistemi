from abc import ABC, abstractmethod


# ---------------- KAYNAK SINIFI ----------------

class Kaynak(ABC):

    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value


# ---------------- KITAP SINIFI ----------------

class Kitap(Kaynak):

    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)

        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"Başlık: {self.baslik} | Kayıt No: {self.kayitNo} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"


# ---------------- DERGI SINIFI ----------------

class Dergi(Kaynak):

    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)

        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"Başlık: {self.baslik} | Kayıt No: {self.kayitNo} | Yayın Dönemi: {self.yayin_donemi} | Sayı No: {self.sayi_no}"


# ---------------- ISLEM SOYUT SINIFI ----------------

class Islem(ABC):

    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


# ---------------- KITAP ISLEM ----------------

class KitapIslem(Islem):

    def __init__(self):
        self.kitaplar = []

    def ekle(self):

        baslik = input("Kitap başlığı: ")
        kayitNo = input("Kayıt No: ")

        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                print("Bu kayıt numarası zaten var.")
                return

        yazar = input("Yazar: ")
        sayfa = int(input("Sayfa Sayısı: "))

        kitap = Kitap(baslik, kayitNo, yazar, sayfa)

        self.kitaplar.append(kitap)

        print("Kitap eklendi.")
        print("Toplam kitap:", len(self.kitaplar))

    def sil(self):

        kayitNo = input("Silinecek kayıt no: ")

        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)
                print("Kitap silindi.")
                return

        print("Kitap bulunamadı.")

    def guncelle(self):

        kayitNo = input("Güncellenecek kayıt no: ")

        for kitap in self.kitaplar:

            if kitap.kayitNo == kayitNo:

                yeni_baslik = input("Yeni başlık: ")
                yeni_yazar = input("Yeni yazar: ")

                kitap.baslik = yeni_baslik
                kitap.yazar = yeni_yazar

                print("Kitap güncellendi.")
                return

        print("Kitap bulunamadı.")

    def listele(self):

        if len(self.kitaplar) == 0:
            print("Kayıt bulunamadı.")
            return

        for kitap in self.kitaplar:
            print(kitap)


# ---------------- DERGI ISLEM ----------------

class DergiIslem(Islem):

    def __init__(self):
        self.dergiler = []

    def ekle(self):

        baslik = input("Dergi başlığı: ")
        kayitNo = input("Kayıt No: ")

        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                print("Bu kayıt numarası zaten var.")
                return

        yayin = input("Yayın dönemi: ")
        sayi = input("Sayı no: ")

        dergi = Dergi(baslik, kayitNo, yayin, sayi)

        self.dergiler.append(dergi)

        print("Dergi eklendi.")
        print("Toplam dergi:", len(self.dergiler))

    def sil(self):

        kayitNo = input("Silinecek kayıt no: ")

        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)
                print("Dergi silindi.")
                return

        print("Dergi bulunamadı.")

    def guncelle(self):

        kayitNo = input("Güncellenecek kayıt no: ")

        for dergi in self.dergiler:

            if dergi.kayitNo == kayitNo:

                yeni_baslik = input("Yeni başlık: ")
                dergi.baslik = yeni_baslik

                print("Dergi güncellendi.")
                return

        print("Dergi bulunamadı.")

    def listele(self):

        if len(self.dergiler) == 0:
            print("Kayıt bulunamadı.")
            return

        for dergi in self.dergiler:
            print(dergi)


# ---------------- MENU ----------------

class Menu:

    def menu_goster(self):

        print("\n--- KÜTÜPHANE YÖNETİM SİSTEMİ ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")


# ---------------- ANA PROGRAM ----------------

kitap_islem = KitapIslem()
dergi_islem = DergiIslem()

menu = Menu()

while True:

    menu.menu_goster()

    secim = input("Seçiminiz: ")

    if secim == "1":
        kitap_islem.ekle()

    elif secim == "2":
        kitap_islem.sil()

    elif secim == "3":
        kitap_islem.guncelle()

    elif secim == "4":
        kitap_islem.listele()

    elif secim == "5":
        dergi_islem.ekle()

    elif secim == "6":
        dergi_islem.sil()

    elif secim == "7":
        dergi_islem.guncelle()

    elif secim == "8":
        dergi_islem.listele()

    elif secim == "9":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")
