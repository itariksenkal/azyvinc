# -*- coding: utf-8 -*-
"""Kuyruktaki blog taslaklarini yayina alir.

    python taslak/yayinla.py          -> siradaki 1 taslagi yayinlar
    python taslak/yayinla.py 2        -> siradaki 2 taslagi yayinlar
    python taslak/yayinla.py --list   -> bekleyenleri listeler

Repo kokunden calistirin. Tarih her zaman bugundur; ileri tarihli yazi olusmaz.
Her yazi: blog/<slug>.html uretilir, blog listesine, sitemap.xml'e ve
llms.txt'e eklenir, taslak dosyasi silinir. Sonra commit + push yeterli.
Taslaklar numara sirasiyla yayinlanir; sonraki taslaklar yalnizca daha
onceki numaralara link verir, bu yuzden sirayi degistirmeyin.
"""
import datetime, glob, html, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from azy_mk import build, read, write, BASE, TR  # noqa: E402

KUYRUK = "taslak/kuyruk"

arg = sys.argv[1] if len(sys.argv) > 1 else "1"
files = sorted(glob.glob(KUYRUK + "/*.json"))

if arg == "--list":
    print("Bekleyen %d taslak:" % len(files))
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        print("  %s  (hedef: %s)" % (os.path.basename(f)[:-5], d.get("_hedef", "")))
    sys.exit(0)

n = int(arg)
if not files:
    print("Bekleyen taslak yok."); sys.exit(0)

today = datetime.date.today()
iso = today.isoformat()
trd = "%d %s %d" % (today.day, TR[today.month], today.year)

bi, sm, lt = read("blog/index.html"), read("sitemap.xml"), read("llms.txt")
anchor = '<div class="post-list">\n\n        '
assert bi.count(anchor) == 1, "blog listesi isareti bulunamadi"

for f in files[:n]:
    p = json.load(open(f, encoding="utf-8"))
    s = p["slug"]
    words, mins = build(p, iso)
    card = ('<article class="post">\n'
            '          <a class="post__thumb" href="/blog/%s">\n'
            '            <img src="/assets/img/galeri/%s" alt="%s" loading="lazy" width="640" height="360" />\n'
            '          </a>\n'
            '          <div class="post__body">\n'
            '            <div class="post__meta">Rehber · %s</div>\n'
            '            <h3><a href="/blog/%s">%s</a></h3>\n'
            '            <p>%s</p>\n'
            '            <a class="more" href="/blog/%s">Devamını oku &rarr;</a>\n'
            '          </div>\n'
            '        </article>' % (s, p["image"], html.escape(p["imageAlt"], quote=True), trd, s,
                                    html.escape(p["h1"]), html.escape(p["desc"]), s))
    bi = bi.replace(anchor, anchor + card + "\n\n        ", 1)
    if "/blog/%s<" % s not in sm:
        sm = sm.replace("</urlset>", "  <url>\n    <loc>%s/blog/%s</loc>\n    <lastmod>%s</lastmod>\n"
                        "    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n</urlset>"
                        % (BASE, s, iso), 1)
    lt = lt.rstrip() + "\n- [%s](%s/blog/%s): %s\n" % (p["h1"], BASE, s, p["desc"])
    os.remove(f)
    print("  yayinlandi  %s  (%s, %d kelime)" % (s, iso, words))

write("blog/index.html", bi); write("sitemap.xml", sm); write("llms.txt", lt)
print("\nKalan taslak: %d" % (len(files) - min(n, len(files))))
print("Simdi: git add -A && git commit -m \"Blog: yeni yazi\" && git push")
