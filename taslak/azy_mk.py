# -*- coding: utf-8 -*-
"""Generate an azyvinc blog page from structured content, reusing the existing
page chrome (head scripts, header, footer, CTA band) byte-for-byte.
Every post also gets a topic-matched CTA box (cta_ekle) at the end of its first
H2 section; taslak/cta_kutusu.py applies the same box to already published posts."""
import re, json, os, html

BASE = "https://www.azyvinc.com"
CRLF, LF = bytes([13, 10]), bytes([10])
DONOR = "blog/kac-tonluk-vinc-gerekir.html"
TR = [None, "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
      "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def read(p):
    return open(p, "rb").read().decode("utf-8").replace(chr(13) + chr(10), chr(10))


def write(p, s):
    open(p, "wb").write(s.encode("utf-8").replace(CRLF, LF))


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ---- Konuya özel çağrı kutusu: ilk H2 bölümünün sonuna (ikinci H2'den önce) ----
# Konu slug'dan bulunur; ilk eşleşen kazanır, hiçbiri tutmazsa "mobil".
WA = ("https://wa.me/905424889808?text=Merhaba%2C%20bir%20is%20icin%20vinc%20lazim.%20Isin%20"
      "fotografini%20ve%20konumumu%20gonderiyorum%3B%20uygun%20fiyat%20ve%20ne%20zaman%20"
      "gelebileceginizi%20ogrenebilir%20miyim%3F")
CTA_KONU = [
    ("hiyap", re.compile(r"hiyap|hiab|hiup")),
    ("fatura", re.compile(r"tevkifat|fatura|kdv|muhasebe|hakedis|birim-fiyat|sozlesme|ihale|"
                          r"sartname|evrak|kurumsal|puantaj|kapora|teklif|ceza|hukuki|sigorta|"
                          r"komsu-mulke|periyodik|satin-alma|gizli-maliyet|risk-degerlendirme|"
                          r"calisma-izni|toolbox")),
    ("sepetli", re.compile(r"manlift|menlift|sepet|platform|makasli|yuksekte|myk|ehliyet|belgesi|"
                           r"cephe|budama|boya|branda|tabela")),
]
CTA_KUTU = {
    "fatura": ("Faturalı, sözleşmeli, operatörlü — İSG dosyası hazır",
               "Kurumsal işlerde yazılı teklif, sözleşme ve faturayla çalışırız; operatör belgeleri "
               "ve İSG evrakları sahaya girmeden önce elinizde olur.",
               None),
    "sepetli": ("Belgeli operatörle manlift ve sepetli platform",
                "Platformu belgeli operatörümüz kullanır, ekibiniz sepette kendi işine odaklanır. "
                "Çalışma yüksekliğini ve zemini söyleyin, uygun aracı birlikte seçelim.",
                ("/hizmetler/sepetli-platform-manlift-kiralama",
                 "Sepetli platform ve manlift kiralama")),
    "hiyap": ("Hiyap ile yükle, taşı, yerine indir",
              "Araç üstü vinç yükü kendi kasasında getirir ve yerine indirir; totem, konteyner, "
              "malzeme ve makine işleri tek araçla biter. Yükü ve adresi söyleyin, uygun aracı "
              "netleştirelim.",
              ("/hizmetler/hiyap-kiralama", "Hiyap (araç üstü vinç) kiralama")),
    "mobil": ("Operatörlü mobil vinç — keşif ve net fiyat",
              "Yükü, yüksekliği ve adresi söyleyin; uygun vinci ve fiyatı baştan netleştirelim. "
              "Şanlıurfa merkez ve ilçelerinde 7/24 ulaşabilirsiniz.",
              ("/hizmetler/mobil-vinc-kiralama", "Mobil vinç kiralama")),
}
CTA_RE = re.compile(r'<aside class="post-cta[ "].*?</aside>\n*', re.S)


def cta_konu(slug):
    return next((k for k, rx in CTA_KONU if rx.search(slug)), "mobil")


def cta_kutu(slug):
    konu = cta_konu(slug)
    baslik, metin, link = CTA_KUTU[konu]
    more = ('\n  <p class="post-cta__more"><a href="%s">%s &rarr;</a></p>' % link) if link else ""
    return ('<aside class="post-cta post-cta--%s" data-cta-location="post_cta">\n'
            '  <p class="post-cta__title">%s</p>\n'
            '  <p class="post-cta__text">%s</p>\n'
            '  <div class="post-cta__actions">\n'
            '    <a class="btn btn--accent" href="tel:+905424889808">Hemen Ara</a>\n'
            '    <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">WhatsApp\'tan yaz</a>\n'
            '  </div>%s\n'
            '</aside>\n' % (konu, baslik, metin, WA, more))


def cta_ekle(article, slug):
    """Makale HTML'ine kutuyu ekler (varsa eskisini yeniler). İkinci <h2>'nin
    satır başına konur; tek H2 varsa makalenin sonuna."""
    article = CTA_RE.sub("", article)
    h2 = [m.start() for m in re.finditer(r"<h2[ >]", article)]
    if not h2:
        return article
    at = article.rfind("\n", 0, h2[1]) + 1 if len(h2) > 1 else len(article)
    return article[:at] + cta_kutu(slug) + "\n" + article[at:]


def render_body(blocks):
    out = []
    for b in blocks:
        t = b["type"]
        if t == "h2":
            out.append("<h2>%s</h2>" % b["text"])
        elif t == "h3":
            out.append("<h3>%s</h3>" % b["text"])
        elif t == "p":
            out.append("<p>%s</p>" % b["text"])
        elif t == "ul":
            out.append("<ul>\n" + "\n".join("  <li>%s</li>" % x for x in b["items"]) + "\n</ul>")
        elif t == "table":
            head = "".join("<th>%s</th>" % c for c in b["head"])
            rows = "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
                           for r in b["rows"])
            out.append('<div style="overflow-x:auto"><table><thead><tr>%s</tr></thead>'
                       "<tbody>%s</tbody></table></div>" % (head, rows))
        else:
            raise ValueError("unknown block: " + t)
    return "\n".join(out)


def build(post, date_iso, words_per_min=190):
    d = __import__("datetime").date.fromisoformat(date_iso)
    tr_date = "%d %s %d" % (d.day, TR[d.month], d.year)
    slug, url = post["slug"], "%s/blog/%s" % (BASE, post["slug"])
    img = "%s/assets/img/galeri/%s" % (BASE, post["image"])

    # word count -> read time
    n = len(post["intro"].split())
    for b in post["body"]:
        n += len(b.get("text", "").split()) if "text" in b else 0
        n += sum(len(x.split()) for x in b.get("items", []))
        for r in b.get("rows", []):
            n += sum(len(str(c).split()) for c in r)
    n += sum(len(f["q"].split()) + len(f["a"].split()) for f in post["faqs"])
    read_min = max(3, round(n / words_per_min))

    s = read(DONOR)

    # ---- head ----
    s = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % esc(post["title"]), s, count=1)
    for name, val in [("description", post["desc"])]:
        s = re.sub(r'<meta name="%s" content="[^"]*"' % name,
                   '<meta name="%s" content="%s"' % (name, esc(val)), s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]*"',
               '<link rel="canonical" href="%s"' % url, s, count=1)
    for prop, val in [("og:title", post["ogTitle"]), ("og:description", post["desc"]),
                      ("og:url", url), ("og:image", img)]:
        s = re.sub(r'<meta property="%s" content="[^"]*"' % re.escape(prop),
                   '<meta property="%s" content="%s"' % (prop, esc(val)), s, count=1)
    for nm, val in [("twitter:title", post["ogTitle"]), ("twitter:description", post["desc"]),
                    ("twitter:image", img)]:
        s = re.sub(r'<meta name="%s" content="[^"]*"' % re.escape(nm),
                   '<meta name="%s" content="%s"' % (nm, esc(val)), s, count=1)

    # ---- structured data: replace every ld+json block with our three ----
    blog = {"@context": "https://schema.org", "@type": "BlogPosting",
            "headline": post["ogTitle"], "description": post["desc"], "image": img,
            "datePublished": date_iso, "dateModified": date_iso, "inLanguage": "tr-TR",
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "author": {"@type": "Person", "name": "Aziz Yıldırım",
                       "jobTitle": "Kurucu & Genel Müdür",
                       "worksFor": {"@type": "LocalBusiness", "@id": BASE + "/#business",
                                    "name": "AZY Vinç"}},
            "publisher": {"@type": "Organization", "name": "AZY Vinç",
                          "logo": {"@type": "ImageObject",
                                   "url": BASE + "/assets/icons/favicon.svg"}}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": f["q"],
                           "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                          for f in post["faqs"]]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": BASE + "/"},
                  {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
                  {"@type": "ListItem", "position": 3, "name": post["h1"]}]}
    new_ld = "\n".join('<script type="application/ld+json">\n%s\n</script>'
                       % json.dumps(x, ensure_ascii=False, indent=2)
                       for x in (blog, faq, crumbs))
    head_end = s.index("</head>")
    head, rest = s[:head_end], s[head_end:]
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    s = head.rstrip() + "\n" + new_ld + "\n" + rest

    # ---- hero ----
    s = re.sub(r"(<section class=\"page-hero\">.*?)<h1>.*?</h1>",
               lambda m: m.group(1) + "<h1>%s</h1>" % post["h1"], s, count=1, flags=re.S)

    # ---- article body ----
    meta_line = ('<p class="post__meta" style="color:var(--muted);font-size:.85rem;'
                 'margin-bottom:18px">Yayın: %s · Güncelleme: %s · ~%d dk okuma</p>'
                 % (tr_date, tr_date, read_min))
    cover = ('<figure class="post-cover"><img src="/assets/img/galeri/%s" alt="%s" '
             'width="1200" height="675" loading="eager" /><figcaption>%s</figcaption></figure>'
             % (post["image"], esc(post["imageAlt"]), post["caption"]))
    faq_html = "<h2>Sık sorulan sorular</h2>\n" + "\n".join(
        "<h3>%s</h3>\n<p>%s</p>" % (f["q"], f["a"]) for f in post["faqs"])
    cta = ('<p style="margin-top:30px"><a class="btn btn--accent" '
           'href="tel:+905424889808">Hemen Ara: 0542 488 98 08</a></p>')
    body = "\n".join([meta_line, cover, "<p>%s</p>" % post["intro"],
                      render_body(post["body"]), faq_html, cta])
    body = cta_ekle(body, slug)  # konuya özel çağrı kutusu (ilk H2 bölümünün sonu)
    s = re.sub(r'(<article class="prose">).*?(</article>)',
               lambda m: m.group(1) + "\n" + body + "\n      " + m.group(2),
               s, count=1, flags=re.S)

    path = "blog/%s.html" % slug
    assert not os.path.exists(path), "exists: " + path
    write(path, s)

    assert len(post["title"]) <= 62, "title %d: %s" % (len(post["title"]), slug)
    assert len(post["desc"]) <= 165, "desc %d: %s" % (len(post["desc"]), slug)
    assert os.path.exists("assets/img/galeri/" + post["image"]), "no image: " + post["image"]
    return n, read_min
