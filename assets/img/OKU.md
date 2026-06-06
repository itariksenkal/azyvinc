# 📷 Fotoğraflar buraya / Görsel klasörü rehberi

> **Güncel durum (2026-06-06):** 13 saha fotoğrafı eklendi, SEO uyumlu isimlendirildi ve dağıtıldı:
> ana sayfa galerisi (13), hizmetler "Sahadan örnekler" (6), hakkımızda (1), hero arka planı ve OG görseli.
> **Yeni foto eklemek için:** dosyayı ilgili klasöre koy → bana dosya adını söyle, sayfaya bağlayayım.
> **Not (OG):** `og/og-kapak.jpg` şu an dikey bir fotoğraftan kopyalandı; ideali 1200×630 yatay bir
> görsel hazırlayıp bununla değiştirmek (WhatsApp/Facebook önizlemesi en iyi böyle görünür).


Fotoğraflarınızı aşağıdaki klasörlere koyun. Dosya adlarını **küçük harf, Türkçe karaktersiz ve tireli** verin
(örn. `sepetli-vinc-cephe.webp`). Bu hem SEO hem de düzen için önemlidir.

## Hangi görsel nereye?

| Klasör | Ne koyulacak | Önerilen boyut / format |
|---|---|---|
| `logo/` | İşletme logosu (varsa) | SVG ya da şeffaf PNG |
| `hero/` | Ana sayfa üst (kapak) fotoğrafı — sahada vinç | Yatay, geniş (1920×1080), WebP |
| `hizmetler/` | Her hizmet için kart görseli (mobil vinç, sepetli vinç vb.) | Kare/4:3, ~800px, WebP |
| `galeri/` | Sahadan iş fotoğrafları (en az 6 adet) | 4:3, ~1000px, WebP |
| `og/` | Sosyal medya paylaşım görseli → **`og-kapak.jpg`** | Tam **1200×630** px |
| `../icons/` | favicon ve uygulama ikonları | SVG var; `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` eklenebilir |

## İpuçları
- **WebP** kullanın: aynı kalitede çok daha küçük dosya = hızlı açılan, SEO'su yüksek site.
  (Telefonla çektiğiniz JPG'leri https://squoosh.app üzerinden ücretsiz WebP'ye çevirebilirsiniz.)
- Her fotoğrafı yüklemeden önce boyutunu küçültün; **500 KB altı** idealdir.
- Gerçek, kendi işlerinize ait fotoğraflar kullanın (internetten alınan stok görseller güven vermez).
- Yatay/dikey karışmasın; galeri için hepsini benzer oranda (4:3) tutmaya çalışın.

## Fotoğrafı siteye nasıl bağlarız?
Fotoğrafları bu klasörlere koyduktan sonra bana **dosya adlarını** söyleyin
(örn. "galeriye `is1.webp`, `is2.webp` koydum, hero'ya `kapak.webp`"),
ben de galeri ve sayfalardaki yer tutucuları gerçek `<img>` etiketleriyle değiştireyim.
