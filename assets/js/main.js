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
      'Detaylar: <a href="/cerez-politikasi.html">Çerez Politikası</a>.</p>' +
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
})();
