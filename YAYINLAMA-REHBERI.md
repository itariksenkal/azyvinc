# AZY Vinç — Yayınlama Rehberi (GitHub Pages + Squarespace Domain)

> Bu site **statik** (HTML/CSS/JS) olduğu için **GitHub Pages**'te **ücretsiz** yayınlanabilir.
> Aşağıda; siteyi GitHub'a yükleme, yayına alma ve **Squarespace'ten aldığınız alan adını (domain)**
> bağlama adımları sade şekilde anlatılmıştır.
> Son güncelleme: 2026-06-06

---

## ⚠️ ÖNCE: Alan adınızı belirleyin

Şu an site dosyalarında örnek alan adı olarak **`www.azyvinc.com`** kullanıldı.
Sizin gerçek alan adınız farklıysa (ör. `azizvinc.com`, `urfavinc.com`...), yayından önce
değiştirilmesi gereken yerler:

- `CNAME` (içinde tek satır: alan adınız — örn. `www.alanadiniz.com`)
- `robots.txt` → `Sitemap:` satırı
- `sitemap.xml` → tüm `<loc>` adresleri
- Tüm `.html` dosyalarındaki `canonical`, `og:url`, `og:image`, `twitter:image` ve JSON-LD `url` alanları

> İsterseniz domaini söyleyin, ben tüm dosyalarda **otomatik** değiştireyim — tek tek uğraşmayın.

---

## 1) GitHub hesabı ve depo (repository) açın

1. https://github.com adresinden ücretsiz hesap açın (yoksa).
2. Sağ üstte **+ → New repository**.
3. **Repository name:** `azyvinc` (ya da istediğiniz ad).
4. **Public** seçin (GitHub Pages ücretsiz planda public ister).
5. **Create repository**.

---

## 2) Dosyaları yükleyin (iki yol var — birini seçin)

### Yol A — Sürükle-bırak (kolay, teknik bilgi gerektirmez)
1. Yeni depoda **Add file → Upload files**.
2. `azyvinc` klasörünün **içindeki tüm dosya ve klasörleri** (index.html, assets/, blog/, CNAME,
   robots.txt, sitemap.xml, .nojekyll ... hepsini) sürükleyip bırakın.
   - ⚠️ `azyvinc` klasörünün **kendisini** değil, **içindekileri** yükleyin (index.html en üstte olmalı).
   - ⚠️ Gizli dosya `.nojekyll`'ı da yüklediğinizden emin olun (yoksa bazı dosyalar görünmeyebilir).
3. Altta **Commit changes**.

### Yol B — Git ile (geliştirici yöntemi)
```bash
cd "c:\Users\Lenovo\Desktop\azyvinc"
git init
git add -A
git commit -m "AZY Vinç sitesi - ilk yayın"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/azyvinc.git
git push -u origin main
```

---

## 3) GitHub Pages'i açın

1. Depoda **Settings → Pages**.
2. **Build and deployment → Source:** `Deploy from a branch`.
3. **Branch:** `main` ve klasör `/ (root)` → **Save**.
4. 1–2 dakika sonra site şu adreste yayında olur: `https://KULLANICI_ADINIZ.github.io/azyvinc/`
   - (Alan adınızı bağlayınca asıl adresiniz kendi domaininiz olacak.)

---

## 4) Squarespace alan adını (domain) bağlayın

> Amaç: `alanadiniz.com` ve `www.alanadiniz.com` → GitHub Pages'e yönlensin.

### 4.1 — GitHub tarafında özel alan adını gir
1. **Settings → Pages → Custom domain** kutusuna alan adınızı yazın: `www.alanadiniz.com` → **Save**.
   (Bu, depodaki `CNAME` dosyasını otomatik günceller.)

### 4.2 — Squarespace tarafında DNS kayıtlarını ekle
Squarespace **Domains** panelinde alan adınızı seçin → **DNS / DNS Settings** (Özel kayıtlar / Custom Records).

**a) `www` için (CNAME):**
| Host / Name | Type | Data / Value |
|---|---|---|
| `www` | `CNAME` | `KULLANICI_ADINIZ.github.io` |

**b) Kök (apex) alan adı için (A kayıtları) — `alanadiniz.com`:**
| Host | Type | Value |
|---|---|---|
| `@` | `A` | `185.199.108.153` |
| `@` | `A` | `185.199.109.153` |
| `@` | `A` | `185.199.110.153` |
| `@` | `A` | `185.199.111.153` |

**(İsteğe bağlı, IPv6 için AAAA):**
```
@  AAAA  2606:50c0:8000::153
@  AAAA  2606:50c0:8001::153
@  AAAA  2606:50c0:8002::153
@  AAAA  2606:50c0:8003::153
```

> ⚠️ Squarespace'te alan adıyla gelen **çakışan/önceden tanımlı A veya yönlendirme (forwarding/parking)
> kayıtları** varsa silin; aksi halde GitHub'a yönlenmez.
> ⚠️ DNS değişikliği yayılması **birkaç saat** (bazen 24 saate kadar) sürebilir, sabırlı olun.

### 4.3 — HTTPS'i zorla
DNS yayıldıktan sonra **Settings → Pages → "Enforce HTTPS"** kutusunu işaretleyin
(seçenek aktif hâle gelmesi 24 saati bulabilir). Böylece site `https://` ile güvenli açılır.

---

## 5) Yayın sonrası kontrol listesi

- [ ] `https://www.alanadiniz.com` açılıyor mu? `alanadiniz.com` de `www`'ye yönleniyor mu?
- [ ] HTTPS (kilit simgesi) çalışıyor mu? "Enforce HTTPS" işaretli mi?
- [ ] Telefonda menü, "Hemen Ara" ve WhatsApp butonları çalışıyor mu?
- [ ] **Google Search Console** (https://search.google.com/search-console) → siteyi ekle/doğrula →
      `sitemap.xml`'i gönder.
- [ ] **Google İşletme Profili** oluştur/doldur (bkz. `NOTLAR-SEO-GEO.md`).
- [ ] Paylaşım görseli (`assets/img/og/og-kapak.jpg`, 1200×630) eklendi mi? (WhatsApp/Facebook önizlemesi için)

---

## 6) Sonradan güncelleme nasıl yapılır?

- **Yol A:** GitHub'da ilgili dosyayı aç → kalem (✏️) ikonu → düzenle → **Commit changes**.
  Değişiklik 1–2 dakikada canlıya yansır.
- **Yol B (git):** dosyaları düzenle → `git add -A && git commit -m "güncelleme" && git push`.
- Yeni fotoğraf eklemek için: `assets/img/...` klasörüne yükle, sonra bana dosya adını söyle —
  galeri/sayfa bağlantılarını ben güncelleyeyim.

---

## Kısa özet (akış)
```
GitHub repo aç → dosyaları yükle → Pages'i aç (main /root)
→ Custom domain gir → Squarespace DNS (www=CNAME, @=A kayıtları)
→ bekle (DNS) → Enforce HTTPS → Search Console + İşletme Profili
```
