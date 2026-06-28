/* AZY Vinç — küçük etkileşimler (mobil menü + yıl + çerez onayı) */
(function () {
  "use strict";

  // ---- Mobil menü aç/kapa ----
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("is-open"); });
    });
  }

  // ---- Footer yılını otomatik güncelle ----
  var y = document.querySelector("[data-year]");
  if (y) { y.textContent = new Date().getFullYear(); }

  // ---- Çerez onayı (KVKK / ePrivacy) ----
  var KEY = "azy_cookie_consent";

  function store(val) { try { localStorage.setItem(KEY, val); } catch (e) {} }
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }

  // Onaya bağlı gömülü içerikleri (ör. Google Haritalar) yükle
  function loadConsented() {
    document.querySelectorAll("[data-cookie-src]").forEach(function (el) {
      if (!el.getAttribute("src")) { el.setAttribute("src", el.getAttribute("data-cookie-src")); el.style.display = "block"; }
    });
    document.querySelectorAll(".map-consent").forEach(function (el) { el.style.display = "none"; });
  }

  // "Haritayı göster" tek tıkla yükleme (genel onaydan bağımsız)
  document.querySelectorAll("[data-loadmap]").forEach(function (btn) {
    btn.addEventListener("click", function () { loadConsented(); });
  });

  function removeBanner() {
    var b = document.querySelector(".cookie");
    if (b) { b.parentNode.removeChild(b); }
  }

  function showBanner() {
    var bar = document.createElement("div");
    bar.className = "cookie";
    bar.setAttribute("role", "dialog");
    bar.setAttribute("aria-label", "Çerez bildirimi");
    bar.innerHTML =
      '<p class="cookie__txt">Size daha iyi hizmet sunmak için zorunlu çerezleri ve onay verirseniz harita/ölçüm çerezlerini kullanıyoruz. ' +
      'Detaylar: <a href="/cerez-politikasi">Çerez Politikası</a>.</p>' +
      '<div class="cookie__btns">' +
      '<button class="btn-cookie btn-cookie--ghost" data-cc="reject">Reddet</button>' +
      '<button class="btn-cookie btn-cookie--ok" data-cc="accept">Kabul Et</button>' +
      '</div>';
    document.body.appendChild(bar);
    bar.querySelector('[data-cc="accept"]').addEventListener("click", function () {
      store("accepted"); removeBanner(); loadConsented();
    });
    bar.querySelector('[data-cc="reject"]').addEventListener("click", function () {
      store("rejected"); removeBanner();
    });
  }

  var consent = read();
  if (consent === "accepted") { loadConsented(); }
  else if (consent !== "rejected") { showBanner(); }

  // ---- Foto büyütme (lightbox) ----
  (function () {
    var group = Array.prototype.slice.call(document.querySelectorAll(".gallery img, .post-cover img"));
    if (!group.length) return;
    var idx = 0, scrollY = 0;

    var ov = document.createElement("div");
    ov.className = "lightbox";
    ov.setAttribute("aria-hidden", "true");
    ov.innerHTML =
      '<button class="lb-close" aria-label="Kapat">&times;</button>' +
      '<button class="lb-nav lb-prev" aria-label="Önceki fotoğraf">&#8249;</button>' +
      '<figure class="lb-stage"><img alt="" /><figcaption></figcaption></figure>' +
      '<button class="lb-nav lb-next" aria-label="Sonraki fotoğraf">&#8250;</button>';
    document.body.appendChild(ov);
    var lbImg = ov.querySelector(".lb-stage img");
    var lbCap = ov.querySelector("figcaption");

    function show(i) {
      idx = (i + group.length) % group.length;
      var alt = group[idx].getAttribute("alt") || "";
      lbImg.setAttribute("src", group[idx].currentSrc || group[idx].getAttribute("src"));
      lbImg.setAttribute("alt", alt);
      lbCap.textContent = alt;
      var multi = group.length > 1 ? "" : "none";
      ov.querySelector(".lb-prev").style.display = multi;
      ov.querySelector(".lb-next").style.display = multi;
    }
    function open(i) {
      scrollY = window.scrollY || window.pageYOffset;
      show(i);
      ov.classList.add("is-open");
      ov.setAttribute("aria-hidden", "false");
      document.body.classList.add("lb-lock");
      document.body.style.top = (-scrollY) + "px";
    }
    function close() {
      ov.classList.remove("is-open");
      ov.setAttribute("aria-hidden", "true");
      document.body.classList.remove("lb-lock");
      document.body.style.top = "";
      window.scrollTo(0, scrollY);
    }
    group.forEach(function (im, i) { im.addEventListener("click", function () { open(i); }); });
    ov.querySelector(".lb-close").addEventListener("click", close);
    ov.querySelector(".lb-prev").addEventListener("click", function (e) { e.stopPropagation(); show(idx - 1); });
    ov.querySelector(".lb-next").addEventListener("click", function (e) { e.stopPropagation(); show(idx + 1); });
    ov.addEventListener("click", function (e) { if (e.target === ov || e.target.classList.contains("lb-stage")) close(); });
    document.addEventListener("keydown", function (e) {
      if (!ov.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(idx - 1);
      else if (e.key === "ArrowRight") show(idx + 1);
    });
  })();

  // ---- Blog pagination ----
  (function () {
    var list = document.querySelector(".post-list");
    if (!list) return;
    var posts = Array.prototype.slice.call(list.querySelectorAll(".post"));
    var PER = 9;
    if (posts.length <= PER) return;
    var pages = Math.ceil(posts.length / PER), cur = 1;
    var nav = document.createElement("nav");
    nav.className = "pagination";
    nav.setAttribute("aria-label", "Blog sayfaları");
    list.parentNode.insertBefore(nav, list.nextSibling);
    function render() {
      posts.forEach(function (p, i) { p.style.display = (i >= (cur - 1) * PER && i < cur * PER) ? "" : "none"; });
      var h = '<button class="pg-btn pg-prev"' + (cur === 1 ? " disabled" : "") + ">‹ Önceki</button>";
      for (var n = 1; n <= pages; n++) { h += '<button class="pg-btn pg-num' + (n === cur ? " is-active" : "") + '" data-pg="' + n + '">' + n + "</button>"; }
      h += '<button class="pg-btn pg-next"' + (cur === pages ? " disabled" : "") + ">Sonraki ›</button>";
      nav.innerHTML = h;
    }
    nav.addEventListener("click", function (e) {
      var b = e.target.closest ? e.target.closest(".pg-btn") : null;
      if (!b || b.disabled) return;
      if (b.classList.contains("pg-prev")) cur = Math.max(1, cur - 1);
      else if (b.classList.contains("pg-next")) cur = Math.min(pages, cur + 1);
      else if (b.getAttribute("data-pg")) cur = parseInt(b.getAttribute("data-pg"), 10);
      render();
      var top = list.getBoundingClientRect().top + window.scrollY - 90;
      window.scrollTo({ top: top, behavior: "smooth" });
    });
    render();
  })();

  // ---- Google Ads dönüşüm izleme: arama & WhatsApp tıklamaları ----
  // tel: linkleri çevirici açar (sayfa kapanmaz), wa.me linkleri yeni sekmede
  // açılır; her iki durumda da sayfa kaldığından dönüşüm güvenle gönderilir.
  (function () {
    var CALL_SEND_TO = "AW-18219228365/HLGmCIPZ0bocEM25ze9D"; // Telefon Araması
    var WA_SEND_TO = "AW-18219228365/-PguCNjVqMccEM25ze9D";   // WhatsApp Tıklaması

    function fire(sendTo) {
      if (typeof window.gtag !== "function") return;
      window.gtag("event", "conversion", { send_to: sendTo, value: 1.0, currency: "TRY" });
    }

    document.addEventListener("click", function (e) {
      var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (href.indexOf("tel:") === 0) { fire(CALL_SEND_TO); }
      else if (/wa\.me|api\.whatsapp\.com|whatsapp:/i.test(href)) { fire(WA_SEND_TO); }
    }, true);
  })();
})();
