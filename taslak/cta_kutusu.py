# -*- coding: utf-8 -*-
"""Yayindaki blog yazilarina konuya ozel cagri kutusunu ekler veya yeniler.

    python taslak/cta_kutusu.py            -> tum blog/*.html (yonlendirme sayfalari haric)
    python taslak/cta_kutusu.py --liste    -> hicbir sey yazmaz; hangi yaziya hangi kutu
                                              gidecegini listeler

Repo kokunden calistirin. Kutu metinleri ve konu eslesmesi azy_mk.py icindedir
(CTA_KONU / CTA_KUTU); kuyruktan yayinlanan yeni yazilar ayni kutuyu otomatik alir.
Kutu ilk H2 bolumunun sonuna (ikinci H2'den hemen once) konur. Script tekrar
calistirilabilir: varsa eski kutu silinip guncel metin yeniden yazilir.
"""
import glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from azy_mk import read, write, cta_ekle, cta_konu  # noqa: E402

ART = re.compile(r'(<article class="prose">)(.*?)(</article>)', re.S)
liste = "--liste" in sys.argv
sayac, degisen = {}, 0
for p in sorted(glob.glob("blog/*.html")):
    s = read(p)
    if 'http-equiv="refresh"' in s or os.path.basename(p) == "index.html":
        continue
    m = ART.search(s)
    if not m:
        print("  makale bulunamadi: " + p)
        continue
    slug = os.path.basename(p)[:-5]
    konu = cta_konu(slug)
    sayac[konu] = sayac.get(konu, 0) + 1
    if liste:
        print("  %-8s %s" % (konu, slug))
        continue
    yeni = s[:m.start(2)] + cta_ekle(m.group(2), slug) + s[m.end(2):]
    if yeni != s:
        write(p, yeni)
        degisen += 1
print("Konu dagilimi: " + ", ".join("%s=%d" % kv for kv in sorted(sayac.items())))
if not liste:
    print("Guncellenen yazi: %d" % degisen)
