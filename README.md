# AZY Vinç — Şanlıurfa Vinç Kiralama Web Sitesi

Sade, hızlı ve mobil öncelikli **statik web sitesi**. Tek hedef: ziyaretçi **tek dokunuşla arasın** →
*"işiniz hızlıca halolsun."* GitHub Pages'te yayınlanmak ve Squarespace alan adına bağlanmak üzere hazırlandı.

- **İşletme:** AZY Vinç — Şanlıurfa ve çevresinde mobil vinç, sepetli vinç & platform (menlift, eklemli/teleskopik), ağır yük kaldırma, çatı/klima/cam montaj ve endüstriyel vinç hizmetleri
- **Kurucu / Sahibi:** Aziz Yıldırım
- **Telefon:** 0542 488 98 08 · **WhatsApp:** wa.me/905424889808
- **Hizmet bölgesi:** Şanlıurfa merkez + çevre ilçeler

---

## 📁 Klasör yapısı

```
azyvinc/
├── index.html              → Ana sayfa (hero, net cevap, hizmetler, SSS, CTA, schema)
├── hizmetler.html          → Hizmet detayları + "nasıl çalışıyoruz" süreci
├── hakkimizda.html         → İşletme + Kurucu Aziz Yıldırım
├── iletisim.html           → Telefon/WhatsApp/harita/çalışma saatleri
├── blog/
│   └── index.html          → Blog listesi (yazılar eklendikçe büyüyecek)
├── 404.html                → Özel "sayfa bulunamadı" sayfası
├── assets/
│   ├── css/style.css       → Tüm tasarım (tek dosya, renkler/bileşenler)
│   ├── js/main.js          → Mobil menü + yıl güncelleme
│   ├── img/                → 📷 FOTOĞRAFLAR BURAYA (bkz. assets/img/OKU.md)
│   │   ├── logo/  hero/  hizmetler/  galeri/  og/
│   └── icons/              → favicon.svg (+ ileride png ikonlar)
├── CNAME                   → Özel alan adı (yayın için; alanadiniz.com)
├── robots.txt              → Arama motoru yönergesi + sitemap linki
├── sitemap.xml             → Sayfa haritası (Google'a gönderilecek)
├── site.webmanifest        → PWA / ikon tanımı
├── .nojekyll               → GitHub Pages için (Jekyll'i kapatır)
│
├── README.md               → (bu dosya) genel bakış + yol haritası
├── NOTLAR-SEO-GEO.md       → SEO + yapay zekâ (GEO) görünürlük notları
├── ANAHTAR-KELIMELER.md    → Aranan kelime haritası (hizmet + ilçe + uzun kuyruklu)
├── ICERIK-PLANI.md         → Hangi sayfalar/bloglar yayınlanmalı (blog planı)
└── YAYINLAMA-REHBERI.md    → GitHub Pages + Squarespace domain bağlama adımları
```

---

## ✅ Şu an hazır (v1)

- 5 ana sayfa + 404, tutarlı tasarım, **her yerde tıkla-ara** (üst bar, hero, CTA bandı,
  masaüstü yüzen buton, mobil alt sabit çubuk) ve WhatsApp.
- Mobil öncelikli, hızlı (harici font/kütüphane yok), erişilebilir.
- Tam **SEO**: benzersiz title/description, canonical, OG + Twitter, `lang=tr`.
- **GEO/AI** için: hero altında net tek-cümlelik cevap + görünür **SSS** + **FAQPage** ve
  **LocalBusiness** yapılandırılmış verisi (schema.org JSON-LD).
- Teknik dosyalar: `robots.txt`, `sitemap.xml`, `.nojekyll`, `site.webmanifest`, `404.html`, `favicon.svg`.

## 🔜 Sıradaki adımlar (öncelik sırası)

1. **Fotoğrafları ekle** → `assets/img/` (rehber: `assets/img/OKU.md`). Sonra bana dosya adını söyle.
2. **Yayına al** → `YAYINLAMA-REHBERI.md` adımlarını izle (GitHub + Squarespace domain).
3. **Google İşletme Profili** + **Search Console** → `NOTLAR-SEO-GEO.md`.
4. **Blog yazıları** → `ICERIK-PLANI.md` (önce 🔴 yüksek öncelikli 5 yazı).
5. Hizmet detay + ilçe (bölge) sayfaları, iletişim teklif formu.

---

## ✍️ Hâlâ doğrulanması/eklenmesi gereken bilgiler

Aşağıdakiler şu an **makul varsayım / yer tutucu** olarak konuldu; gerçeğine göre güncellenecek:

- **Alan adı:** `www.azyvinc.com` (Squarespace'ten aldığınız gerçek domain ile değişecek)
- **Çalışma saatleri:** 7/24 (acil dahil) — onaylandı
- **Kesin hizmet listesi** (sahip olunan vinç tipleri/tonajlar)
- **Adres / açık konum** (varsa) ve harita
- **Sertifikalar / deneyim yılı** (Hakkımızda'da E-E-A-T için)

> Bu bilgileri ilet, sitede ilgili yerlere işleyeyim.

---

## 🎨 Tasarım notları (marka kimliği — Figma)
- Logo: `assets/img/logo/azy-ikon.svg` (sarı kare + vinç) — favicon de aynı ikon.
- Renkler: koyu `#14171a` + marka sarısı `#ffc107` + krem `#f5f5f2` + gri `#6b7177`.
- Font: **Barlow** (AZY=Black/900, VİNÇ=Light/300, başlıklar 800).
- Tüm stil tek dosyada: `assets/css/style.css` (`:root` içindeki değişkenlerden kolayca değişir).
- Yeni sayfa eklerken mevcut bir `.html`'in header/footer'ını kopyalayın (tasarım tutarlı kalsın).

İletişim için her yerde: **0542 488 98 08**
