# -*- coding: utf-8 -*-
"""Kuyruktaki taslaklari yayinlamadan once dogrular.

    python taslak/kontrol.py

Repo kokunden calistirin. Hata varsa cikis kodu 1 olur ve otomatik
yayin durur; boylece bozuk bir taslak siteye hic girmez.
"""
import glob, json, os, re, sys

KUYRUK = "taslak/kuyruk"
DOSYA = re.compile(r"(\d{2,3})-([a-z0-9]+(?:-[a-z0-9]+)*)\.json\Z")
ALANLAR = ("slug", "title", "ogTitle", "h1", "desc", "image", "imageAlt", "caption",
           "intro", "body", "faqs", "_hedef")
BLOKLAR = {"h2": "text", "h3": "text", "p": "text", "ul": "items", "table": "rows"}
LINK = re.compile(r'href="(/[^"#?]*)')


def sayfa_var(yol):
    yol = yol.rstrip("/")
    if not yol:
        return True
    return any(os.path.exists(p) for p in (yol[1:] + ".html", yol[1:] + "/index.html"))


def metinler(p):
    yield p["intro"]
    for b in p["body"]:
        if "text" in b:
            yield b["text"]
        for x in b.get("items", []):
            yield x
        for r in b.get("rows", []):
            for c in r:
                yield str(c)
    for f in p["faqs"]:
        yield f["q"]
        yield f["a"]


def kontrol():
    hatalar, onceki = [], set()
    for f in sorted(glob.glob(KUYRUK + "/*.json")):
        ad = os.path.basename(f)
        m = DOSYA.fullmatch(ad)
        if not m:
            hatalar.append("%s: dosya adi NN-slug.json olmali" % ad)
            continue
        try:
            p = json.load(open(f, encoding="utf-8"))
        except ValueError as e:
            hatalar.append("%s: JSON okunamadi (%s)" % (ad, e))
            continue
        eksik = [k for k in ALANLAR if not p.get(k)]
        if eksik:
            hatalar.append("%s: eksik alan %s" % (ad, ", ".join(eksik)))
            continue
        s = p["slug"]
        if s != m.group(2):
            hatalar.append("%s: slug dosya adiyla ayni olmali" % ad)
        if s in onceki or os.path.exists("blog/%s.html" % s):
            hatalar.append("%s: bu slug zaten var" % ad)
        if len(p["title"]) > 62:
            hatalar.append("%s: title %d karakter (en fazla 62)" % (ad, len(p["title"])))
        if len(p["desc"]) > 165:
            hatalar.append("%s: desc %d karakter (en fazla 165)" % (ad, len(p["desc"])))
        if not os.path.exists("assets/img/galeri/" + p["image"]):
            hatalar.append("%s: gorsel yok: %s" % (ad, p["image"]))
        for b in p["body"]:
            alan = BLOKLAR.get(b.get("type"))
            if not alan or not b.get(alan) or (b["type"] == "table" and not b.get("head")):
                hatalar.append("%s: gecersiz blok %r" % (ad, b.get("type")))
        if len(p["faqs"]) < 3 or any(not x.get("q") or not x.get("a") for x in p["faqs"]):
            hatalar.append("%s: en az 3 eksiksiz SSS gerekli" % ad)
        kelime = sum(len(re.sub(r"<[^>]+>", " ", t).split()) for t in metinler(p))
        if kelime < 350:
            hatalar.append("%s: %d kelime (en az 350)" % (ad, kelime))
        for t in metinler(p):
            if "<script" in t.lower():
                hatalar.append("%s: metinde script olamaz" % ad)
            for yol in LINK.findall(t):
                hedef = yol.rstrip("/")
                if hedef.startswith("/blog/") and hedef[6:] in onceki:
                    continue  # daha once yayinlanacak taslak
                if not sayfa_var(yol):
                    hatalar.append("%s: kirik ic baglanti %s" % (ad, yol))
        onceki.add(s)
    return hatalar, len(onceki)


if __name__ == "__main__":
    hatalar, adet = kontrol()
    for h in hatalar:
        print("HATA  " + h)
    if hatalar:
        sys.exit(1)
    print("Kuyruk gecerli: %d taslak" % adet)
