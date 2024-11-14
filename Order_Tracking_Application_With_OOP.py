class Siparis:
    def __init__(self, urun_adi, miktar, fiyat):
        self.urun_adi = urun_adi
        self.miktar = miktar
        self.fiyat = fiyat

    def toplam_hesapla(self):
        return self.miktar * self.fiyat

class Musteri:
    def __init__(self, isim):
        self.isim = isim
        self.siparisler = []

    def siparis_ekle(self, siparis):
        self.siparisler.append(siparis)

    def siparis_iptal_et(self, urun_adi):
        self.siparisler = [siparis for siparis in self.siparisler if siparis.urun_adi != urun_adi]

    def toplam_fatura_hesapla(self):
        return sum(siparis.toplam_hesapla() for siparis in self.siparisler)

    def siparisleri_goster(self):
        print(f"{self.isim}' in Siparişleri:")
        for siparis in self.siparisler:
            print(f"{siparis.urun_adi} - {siparis.miktar} adet - {siparis.fiyat} TL")

musteri1 = Musteri("Ali")
siparis1 = Siparis("Pizza", 1, 50)
siparis2 = Siparis("Hamburger", 2, 30)
musteri1.siparis_ekle(siparis1)
musteri1.siparis_ekle(siparis2)
musteri1.siparisleri_goster()
