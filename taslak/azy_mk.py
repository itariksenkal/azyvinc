# -*- coding: utf-8 -*-
"""Generate an azyvinc blog page from structured content, reusing the existing
page chrome (head scripts, header, footer, CTA band) byte-for-byte."""
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
