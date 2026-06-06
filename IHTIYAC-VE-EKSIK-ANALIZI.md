# AZY Vinç — Kullanıcı İhtiyaç & Site Eksik Analizi

> "İnsanlar vinçle ilgili ne arar, özellikle ihtiyaç anında ne yazar?" sorusunu araştırıp siteyi bu
> gerçek ihtiyaçlara göre denetledik. Aşağıda; insanların **ihtiyaç anı niyetleri**, **gerçek kullanım
> senaryoları**, ve siteyi bu ihtiyaçlara göre kıyaslayan **önceliklendirilmiş eksik listesi** var.
> Son güncelleme: 2026-06-06

---

## 1. İnsanlar ihtiyaç anında ne arar? (özet)

Vinç/platform talebi iki ana koldan gelir ve neredeyse her arama **yerel + acil + telefon/WhatsApp** odaklıdır.

**Niyet grupları:**
- **Acil & yerel:** "yakınımda sepetli vinç", "Şanlıurfa acil vinç kiralama", "aynı gün vinç", "7/24 vinç"
- **Fiyat:** "vinç kiralama fiyatları 2026", "saatlik vinç ücreti", "vinç kirası ne kadar"
- **Teknik karar:** "kaç tonluk vinç lazım", "sepetli vinç kaç metre çıkar", "5. kata klima için kaç metre"
- **Uygulama (iş tipi):** "klima dış ünite nasıl çıkarılır", "yüksek ağaç dalı kesimi vinç", "balkondan eşya indirme"
- **Güven/güvenlik:** "operatörlü vinç", "sigortalı vinç firması", "belgeli operatör"
- **Karşılaştırma:** "asansörlü mü vinçli mi taşıma", "sepetli vinç mi manlift mi", "mobil vinç sepetli vinç farkı"
- **İletişim tercihi:** "vinç kiralama whatsapp", "sepetli vinç telefon numarası", "hemen ara"

**İnsanlar aramadan ÖNCE şunları görmek ister:** vincin kaç metreye ulaştığı / kaç ton kaldırdığı,
gerçek iş fotoğrafı, fiyatın nasıl hesaplandığı (her şey dahil mi), aynı gün gelinip gelinmeyeceği, güven (operatör/sigorta).

**En çok aranan gerçek senaryolar:** klima dış ünite montajı (yaz), ağaç budama (yaz), asansöre sığmayan
eşya taşıma, konteyner/prefabrik indirme, cam & cephe montajı, çatı, jeneratör/trafo, çelik konstrüksiyon,
fabrika makine taşıma, tabela/totem montaj-sökme.

---

## 2. Sitenin durumu — kısa değerlendirme

**Sağlam temel:** mobil öncelikli, her yerde tıkla-ara + WhatsApp, sticky alt çubuk, temiz LocalBusiness +
FAQPage schema, 5 blog yazısı, 13 gerçek saha fotoğrafı (galeri + hero + hizmetler + hakkımızda + OG).

**Eksik olan 3 kritik katman:** (1) **karar-anı bilgisi** (kaç metre/ton, fiyat mantığı), (2) **güven kanıtı**
(yorum, sertifika, sigorta, referans), (3) **niyet & yerel eşleşme** (ilçe sayfaları, iş-tipi açılış sayfaları,
hızlı teklif formu, karar-anı SSS).

---

## 3. Önceliklendirilmiş eksik listesi

Durum anahtarı: ✅ bu turda yapıldı · 🟡 sahip bilgisi gerekiyor · ⏳ sıradaki iş (sayfa üretimi)

### 🔴 Yüksek öncelik

| Eksik | Hangi ihtiyaç | Durum / Çözüm |
|---|---|---|
| **Hızlı teklif formu (foto+konum)** | "Form doldurmadan, foto atıp hızlı fiyat" | ⏳ İletişim + ana sayfaya 3-4 alanlı kısa form; statik site olduğu için **WhatsApp'a ön-doldurulmuş mesaj** üretir (sunucu gerekmez). |
| **WhatsApp foto+konum akışı** | İletişim tercihi (en çok dönen mobil kanal) | ✅ Tüm WhatsApp linkleri "fotoğraf + konum gönder, hızlı fiyat al" mesajına çevrildi. |
| **Karar-anı SSS** (KDV, izin, hava, sigorta, min. süre) | Güven + fiyat + B2B | ✅ Kısmen: operatör/nakliye, personeli sepete alma, hava iptali, dar sokak, şehir dışı, ön hazırlık eklendi. 🟡 KDV/fatura, sigorta, MYK belge → sahip onayı bekliyor (aşağıda). |
| **Kapasite / "hangi iş için hangi vinç" tablosu** | Teknik karar: kaç metre/ton/kişi | ✅ Genel rehber tablosu eklendi (hizmetler). 🟡 Gerçek tonaj/metre değerleri için sahip bilgisi. |
| **Gerçek saha fotoğrafları** | Kanıt: "benzer işi yapmışlar mı" | ✅ 13 gerçek foto eklendi (galeri + hizmetler + hakkımızda + hero). |
| **İş-tipi (use-case) açılış sayfaları** | Uygulama aramaları (klima, ağaç, konteyner…) | ⏳ 6-8 sayfa önerildi (aşağıda "Önerilen sayfalar"). |
| **Sertifika / sigorta / operatör belgesi / deneyim** | Güven (özellikle B2B/ihale) | 🟡 Sahip bilgisi gerekiyor — gerçek belge/yıl olmadan yazılmaz (abartı yok). |

### 🟡 Orta öncelik

| Eksik | Hangi ihtiyaç | Durum / Çözüm |
|---|---|---|
| **İlçe açılış sayfaları** (Karaköprü/Haliliye/Eyyübiye + Siverek/Viranşehir/Birecik) | "Yakınımda", yerel | ⏳ Sıradaki büyük iş. ✅ Schema areaServed 12 ilçeyle hizalandı. |
| **Fiyat / Koşullar sayfası** (fiyat mantığı, saatlik/günlük, min. süre) | Fiyat | 🟡 Başlangıç aralığı için sahip bilgisi; mantık zaten blogda var. |
| **Müşteri yorumu / Google puanı / referans** | Güven (sosyal kanıt) | 🟡 Önce Google İşletme Profili kurulmalı, sonra yorum/puan rozeti eklenir. |
| **Gerçek adres / konum / Google İşletme Profili** | Yakınımda + güven | 🟡 Sahip bilgisi + GBP kurulumu. ✅ İletişimdeki dev-not kaldırıldı. |

### 🟢 Düşük öncelik

| Eksik | Durum / Çözüm |
|---|---|
| Yanıt/varış süresi + "gizli ücret yok" vurgusu | 🟡 Gerçekçi süre için sahip bilgisi; "3 adım" sürecine eklenir. |
| OG görseli + favicon dosyaları | ✅ OG (`og-kapak.jpg`) ve `favicon.svg` eklendi. 🟡 favicon `.ico`/`.png` ve ideal 1200×630 OG → görsel aracı olan ortamda üretilecek. |

---

## 4. Bu turda yapılan iyileştirmeler (özet)

- ✅ Tüm WhatsApp linkleri **foto + konum ile hızlı teklif** mesajına çevrildi (42 link).
- ✅ Ana sayfa SSS'ine **6 karar-anı sorusu** eklendi (görünür + FAQPage schema).
- ✅ `hizmetler.html`'e **"hangi iş için hangi vinç" rehber tablosu** (mobil responsive) eklendi.
- ✅ LocalBusiness **areaServed** 12 ilçeyle hizalandı.
- ✅ Canlı sayfalardan **geliştirici notları** kaldırıldı (blog listesi, iletişim harita notu).
- ✅ (Önceki turda) 13 gerçek saha fotoğrafı galeri/hizmetler/hakkımızda/hero/OG'ye dağıtıldı.

---

## 5. Eksik kalan SSS soruları (sahip onayı sonrası eklenecek)

- Fiyata **KDV dahil mi, fatura** kesiyor musunuz? (kurumsal faturalı seçenek)
- **Sigortalı mısınız?** Kaza/hasarda (3. şahıs + müşteri malı) sorumluluk kimde?
- Operatörünüzün **MYK / G-sınıfı belgesi** var mı?
- **Minimum kiralama süresi** (yarım gün/saatlik) ve süre aşımı ücreti?
- **Keşif ücretsiz mi**, ne kadar önceden haber verilmeli?
- Yol/kaldırım **kapatma iznini** kim alır?

---

## 6. Önerilen yeni sayfalar (sıradaki iş)

**İş-tipi (use-case) sayfaları** — yüksek niyetli SEO:
- Klima dış ünite montajı için vinç (yaz önceliği) · Yüksek/tehlikeli ağaç budama (yaz önceliği)
- Asansöre sığmayan eşya/mobilya taşıma · Konteyner/prefabrik indirme-bindirme (B2B)
- Cam & cephe (vantuzlu) montaj · Çelik konstrüksiyon montajı · Fabrika makine taşıma · Tabela/totem montaj-sökme

**Diğer sayfalar:**
- İlçe sayfaları: Karaköprü, Haliliye, Eyyübiye, Siverek, Viranşehir, Birecik
- Fiyatlar & Koşullar · Kapasite & filo (gerçek tonaj/metre ile)

---

## 7. Sahipten gereken bilgiler (bunlar gelince yukarıdaki 🟡'ler tamamlanır)

1. **Sigorta:** İş makinesi ve 3. şahıs sigortanız var mı? (varsa "sigortalı hizmet" yazabiliriz)
2. **Operatör belgesi:** MYK / G-sınıfı operatör belgesi var mı?
3. **Fatura/KDV:** Kurumsal fatura kesiyor musunuz? Fiyatlar KDV dahil mi?
4. **Kapasite/filo:** Sahip olunan/çalışılan vinçlerin tonaj ve erişim metre değerleri (örn. … ton mobil vinç, … m sepetli).
5. **Deneyim:** Kaç yıldır bu işi yapıyorsunuz?
6. **Adres/konum:** Tabela/depo/ofis adresi var mı? (Google İşletme Profili ve harita için)
7. **Varış süresi:** Şanlıurfa merkeze ortalama ne kadar sürede ulaşıyorsunuz?
8. **Minimum süre / keşif:** En kısa kiralama (yarım gün?) ve keşif ücretsiz mi?

> Bu 8 maddeyi yanıtlayın; siteyi gerçek, doğrulanabilir bilgilerle güçlendireyim (abartı yapmadan).
