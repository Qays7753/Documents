/* ============================================================
   app.js — منطق النموذج المشترك (سلوك متطابق 100% عبر C1/C2/C3)
   يشمل: التنقل، الأوراق، تدفق البيع، حالات Fixtures،
   التحكم بالمعاينة، إدارة التركيز، ومزامنة المقارنة.
   ============================================================ */
(function () {
  "use strict";
  var D = window.MICRO_DATA;
  var app = document.getElementById("app");
  var phone = document.querySelector(".phone");
  var lastFocus = null;
  var state = {
    screen: "home",
    finance: "positive",
    orders: "normal",
    theme: "light",
    motion: "full",
    text: "100",
    savefail: "off",
    saleDone: false
  };

  /* ---------- أدوات مساعدة ---------- */
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function fmt(n) { return Number(n).toFixed(2); }
  function num(v) { var x = parseFloat(String(v).replace(/[^\d.\-]/g, "")); return isNaN(x) ? null : x; }

  function toast(msg) {
    var region = $(".toast-region");
    if (!region) return;
    var t = document.createElement("div");
    t.className = "toast";
    t.setAttribute("role", "status");
    t.textContent = msg;
    region.appendChild(t);
    setTimeout(function () { t.remove(); }, 2600);
  }

  function flash(el) {
    if (!el) return;
    el.classList.remove("is-flashed");
    void el.offsetWidth;
    el.classList.add("is-flashed");
  }

  /* ---------- تطبيق الحالة على الواجهة ---------- */
  function applyTheme(v) {
    state.theme = v;
    app.setAttribute("data-theme", v);
    $all('.cbtn[data-action="theme"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
    var sw = $('.switch[data-action="theme-toggle"]');
    if (sw) sw.setAttribute("aria-checked", String(v === "dark"));
  }

  function applyMotion(v) {
    state.motion = v;
    document.documentElement.setAttribute("data-motion", v);
    $all('.cbtn[data-action="motion"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
    var sw = $('.switch[data-action="motion-toggle"]');
    if (sw) sw.setAttribute("aria-checked", String(v === "reduced"));
  }

  function applyText(v) {
    state.text = v;
    document.documentElement.setAttribute("data-text", v);
    $all('.cbtn[data-action="text"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
    var sw = $('.switch[data-action="text-toggle"]');
    if (sw) sw.setAttribute("aria-checked", String(v === "200"));
  }

  function applyViewport(v) {
    phone.setAttribute("data-vp", v);
    $all('.cbtn[data-action="viewport"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
  }

  function applySavefail(v) {
    state.savefail = v;
    $all('.cbtn[data-action="savefail"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
  }

  function renderRecent(items) {
    var ul = $('[data-live="recent"]');
    if (!ul) return;
    ul.innerHTML = "";
    items.forEach(function (it) {
      var li = document.createElement("li");
      li.className = "op";
      var icon = it.type === "sale" ? "i-tag" : (it.type === "expense" ? "i-receipt" : "i-handcoins");
      li.innerHTML =
        '<span class="op-badge op-' + it.type + '"><svg class="icon" aria-hidden="true"><use href="#' + icon + '"/></svg></span>' +
        '<span class="op-body"><span class="op-t">' + it.t + '</span><span class="op-s">' + it.s + '</span></span>' +
        '<span class="op-v"><span class="num">' + it.v + '</span> <span class="cur">' + D.currency + '</span></span>';
      ul.appendChild(li);
    });
  }

  function setLive(key, value) {
    $all('[data-live="' + key + '"]').forEach(function (el) { el.textContent = value; });
  }

  function applyFinance(v, opts) {
    opts = opts || {};
    state.finance = v;
    document.body.setAttribute("data-finance", v);
    $all('.cbtn[data-action="finance"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });

    var sc = D.scenarios[v] || D.scenarios.positive;
    var hero = $(".hero");
    if (hero) hero.setAttribute("data-hstate", v);
    $all(".hero-inner").forEach(function (h) {
      h.hidden = (h.dataset.hero !== v);
    });

    // شاشة المالية
    var chip = $('[data-live="statechip"]');
    var chipIcons = { positive: "i-trendup", negative: "i-trenddown", incomplete: "i-dash", empty: "i-dash" };
    if (chip) {
      chip.innerHTML = '<svg class="icon" aria-hidden="true"><use href="#' + (chipIcons[v] || "i-dash") + '"/></svg>' + (sc.stateChip || "");
      chip.dataset.state = v;
    }
    setLive("finnote", sc.finNote || "");

    // ملخص اليوم
    var todayCard = $(".today");
    if (todayCard) todayCard.hidden = !sc.today;
    if (sc.today) {
      var rows = $all(".today .row");
      sc.today.forEach(function (tr, i) {
        if (!rows[i]) return;
        var k = rows[i].querySelector(".row-k");
        var labelSpan = k.querySelector("[data-live='todaystate']") || k;
        labelSpan.childNodes[labelSpan.childNodes.length - 1].textContent = tr.k;
        var val = rows[i].querySelector(".row-v");
        if (tr.v === null) {
          val.innerHTML = '<span class="dash-text">غير محسوبة بعد</span>';
        } else {
          val.innerHTML = '<span class="num">' + tr.v + '</span> <span class="cur">' + D.currency + '</span>';
        }
      });
    }

    // الانكشاف
    var expCard = $(".exposure");
    if (expCard) expCard.hidden = !sc.exposure;
    if (sc.exposure) {
      var erows = $all(".exposure .row");
      sc.exposure.forEach(function (tr, i) {
        if (!erows[i]) return;
        var k = erows[i].querySelector(".row-k");
        k.childNodes[k.childNodes.length - 1].textContent = tr.k;
        erows[i].querySelector(".row-v").innerHTML = '<span class="num">' + tr.v + '</span> <span class="cur">' + D.currency + '</span>';
      });
    }

    // آخر الحركة
    var recentCard = $(".recent");
    if (recentCard) recentCard.hidden = (v === "empty");
    if (v !== "empty" && !state.saleDone) renderRecent(D.recentDefault);

    // بطاقة نتيجة المالية: القيمة
    var finAmt = $('[data-live="result"]');
    if (finAmt) finAmt.textContent = sc.result || "—";
  }

  function applyOrders(v) {
    state.orders = v;
    document.body.setAttribute("data-orders", v);
    $all('.cbtn[data-action="orders"]').forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.val === v));
    });
    var late = v === "late";
    $all("[data-attention]").forEach(function (el) {
      var isLate = el.dataset.attention === "late";
      el.hidden = (isLate !== late);
    });
    $all(".order-late").forEach(function (el) { el.hidden = !late; });
    var sigCollect = $('[data-signal="collect"]');
    var sigOrders = $('[data-signal="orders"]');
    if (sigCollect && sigOrders) {
      sigCollect.hidden = late;
      sigOrders.hidden = !late;
    }
  }

  function gotoScreen(name) {
    state.screen = name;
    $all(".screen").forEach(function (s) {
      var on = s.dataset.screen === name;
      s.classList.toggle("is-active", on);
    });
    $all(".tab").forEach(function (t) {
      var on = t.dataset.tab === name;
      t.classList.toggle("is-active", on);
      if (on) t.setAttribute("aria-current", "page"); else t.removeAttribute("aria-current");
    });
    // شريط الإجراءات السريعة يظهر في «مشروعي الآن» فقط (ملف 03)
    var qab = $(".qab");
    if (qab) qab.hidden = (name !== "home");
    var screens = $(".screens");
    if (screens) screens.scrollTop = 0;
    var active = $('.screen[data-screen="' + name + '"]');
    if (active) active.focus({ preventScroll: true });
  }

  /* ---------- الأوراق والحوار: فتح/إغلاق + إدارة تركيز ---------- */
  var FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';

  function openSheet(name) {
    var sheet = $('[data-sheet="' + name + '"]');
    if (!sheet) return;
    closeSheet(true);
    lastFocus = document.activeElement;
    var scrim = $(".scrim");
    sheet.hidden = false;
    scrim.hidden = false;
    requestAnimationFrame(function () { sheet.classList.add("is-open"); });
    var first = sheet.querySelector(FOCUSABLE);
    if (name === "sale") first = $("#sale-amount") || first;
    setTimeout(function () { if (first) first.focus(); }, 60);
    if (name === "sale") {
      var amount = $("#sale-amount");
      if (amount && !amount.value) amount.value = D.sale.amount;
      updateImpact();
    }
    document.addEventListener("keydown", trapFocus, true);
  }

  function closeSheet(silent) {
    var sheet = $(".sheet.is-open");
    var dlg = $(".syserr:not([hidden])");
    document.removeEventListener("keydown", trapFocus, true);
    if (sheet) {
      sheet.classList.remove("is-open");
      var s = sheet;
      setTimeout(function () { s.hidden = true; }, 180);
    }
    if (dlg) dlg.hidden = true;
    var scrim = $(".scrim");
    if (scrim) scrim.hidden = true;
    if (lastFocus && !silent) { try { lastFocus.focus(); } catch (e) {} }
  }

  function trapFocus(e) {
    if (e.key !== "Tab") return;
    var sheet = $(".sheet.is-open") || $(".syserr:not([hidden])");
    if (!sheet) return;
    var f = $all(FOCUSABLE, sheet).filter(function (el) { return el.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  /* ---------- تدفق تسجيل البيع (Fixtures F / G / I / J) ---------- */
  function setAmountError(input, msg) {
    var wrap = input.closest(".amount-wrap");
    var err = document.getElementById(input.id + "-error") || wrap.parentElement.querySelector("[data-error]");
    input.setAttribute("aria-invalid", "true");
    if (wrap) wrap.setAttribute("data-invalid", "on");
    if (err) { err.textContent = msg; err.hidden = false; }
    input.focus();
  }

  function clearAmountError(input) {
    var wrap = input.closest(".amount-wrap");
    var err = document.getElementById(input.id + "-error") || wrap.parentElement.querySelector("[data-error]");
    input.removeAttribute("aria-invalid");
    if (wrap) wrap.setAttribute("data-invalid", "off");
    if (err) { err.hidden = true; err.textContent = ""; }
  }

  function updateImpact() {
    var input = $("#sale-amount");
    var el = $("#sale-impact");
    if (!input || !el) return;
    var v = num(input.value);
    var shown = (v && v > 0) ? fmt(v) : "0.00";
    el.innerHTML = "رح تزيد المبيعات <span class=\"num\">" + shown + "</span> <span class=\"cur\">" + D.currency + "</span>، وينضاف المبلغ إلى درج المحل.";
  }

  function validateAmount(input) {
    var v = num(input.value);
    if (v === null || v <= 0) {
      setAmountError(input, D.validationMsg);
      return null;
    }
    clearAmountError(input);
    return v;
  }

  function submitSale() {
    var input = $("#sale-amount");
    var v = validateAmount(input);
    if (v === null) return;
    var btn = $('[data-submit-sale]');
    var label = btn.querySelector(".btn-label");
    var spin = btn.querySelector("[data-loading]");
    btn.disabled = true;
    if (label) label.textContent = "جارٍ التسجيل…";
    if (spin) spin.hidden = false;
    setTimeout(function () {
      btn.disabled = false;
      if (label) label.textContent = "سجّل البيع";
      if (spin) spin.hidden = true;
      if (state.savefail === "on") {
        // Fixture J: خطأ نظام مع إعادة محاولة — المدخلات محفوظة
        var dlg = $("#dialog-syserror");
        var scrim = $(".scrim");
        dlg.hidden = false;
        scrim.hidden = false;
        var retry = dlg.querySelector("[data-retry]");
        if (retry) retry.focus();
        return;
      }
      completeSale(v);
    }, 900);
  }

  function completeSale(v) {
    state.saleDone = true;
    var sc = D.scenarios[state.finance];
    var oldSales = num(sc.sales) || 0;
    var oldCash = num(sc.cash);
    var newSales = oldSales + v;
    var newCash = (oldCash === null ? v : oldCash + v);

    // تحديث بطاقة النجاح
    var success = $('[data-sheet="success"]');
    success.querySelector(".success-amount .num").textContent = fmt(v);
    var rows = success.querySelectorAll(".impact-row");
    if (oldCash !== null) {
      rows[0].querySelector("s").textContent = fmt(oldCash);
      rows[0].querySelector("b").textContent = fmt(newCash);
    } else {
      rows[0].querySelector("s").hidden = true;
      rows[0].querySelector("b").textContent = fmt(newCash);
    }
    rows[1].querySelector("s").textContent = fmt(oldSales || v);
    rows[1].querySelector("b").textContent = fmt(newSales);
    success.querySelector(".success-ref .num").textContent = D.sale.ref;

    openSheet("success");
    var sc2 = D.scenarios[state.finance];
    sc2.sales = fmt(newSales);
    if (sc2.cash !== null) sc2.cash = fmt(newCash);
    setLive("sales", fmt(newSales));
    setLive("cash", fmt(newCash));
    renderRecent([{ type: "sale", t: "بيع — صينية كنافة", s: "الآن", v: fmt(v) }].concat(D.recentDefault.slice(0, 2)));

    if (state.finance === "empty") {
      // الانتقال الصادق بعد أول بيع: النتيجة غير مكتملة حتى تسجيل التكاليف
      applyFinance("incomplete");
      D.scenarios.incomplete.sales = fmt(v);
      D.scenarios.incomplete.cash = fmt(v);
      var hs = $('[data-hero="incomplete"]');
      if (hs) {
        hs.querySelector(".hero-sub-v .num").textContent = fmt(v);
        hs.querySelector(".hero-note").textContent = "سجّل مصاريفك وتكاليفك لنتيجة دقيقة";
        var pk = hs.querySelector(".hero-progress-k");
        if (pk) pk.textContent = "1 من 1 عمليات مكتملة التكلفة";
        var pb = hs.querySelector(".hero-progress-fill");
        if (pb) pb.style.inlineSize = "0%";
      }
    }
  }

  function undoSale() {
    if (!state.saleDone) { closeSheet(); return; }
    state.saleDone = false;
    var sc = D.scenarios[state.finance];
    var v = num(D.sale.amount);
    if (sc.sales) sc.sales = fmt(Math.max(0, (num(sc.sales) || 0) - v));
    if (sc.cash) sc.cash = fmt(Math.max(0, (num(sc.cash) || 0) - v));
    setLive("sales", sc.sales || "—");
    setLive("cash", sc.cash || "—");
    renderRecent(D.recentDefault);
    closeSheet();
    toast("تم التراجع عن العملية — رجعت الأرقام مثل ما كانت.");
  }

  /* ---------- أحداث عامة ---------- */
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-tab], [data-open], [data-close], [data-goto], [data-toast], [data-action], [data-submit-sale], [data-submit-concept], [data-undo], [data-retry], [data-back], .scrim, .seg-btn, .chip");
    if (!t) return;

    if (t.matches("[data-tab]")) { gotoScreen(t.dataset.tab); return; }

    if (t.matches("[data-goto]")) {
      closeSheet(true);
      gotoScreen(t.dataset.goto);
      return;
    }

    if (t.matches("[data-open]")) {
      if (t.classList.contains("logo-btn")) t.setAttribute("aria-expanded", "true");
      openSheet(t.dataset.open);
      return;
    }

    if (t.matches("[data-close]") || t.matches(".scrim")) {
      if (t.matches("[data-close]") && t.closest(".sheet") === $('[data-sheet="success"]')) {
        // إغلاق النجاح: أبرز القيم المتأثرة في الرئيسية (Success Impact)
        closeSheet();
        gotoScreen("home");
        setTimeout(function () {
          flash($(".today"));
          $all('[data-live="cash"], [data-live="sales"]').forEach(flash);
        }, 220);
        return;
      }
      var lb = $(".logo-btn");
      if (lb) lb.setAttribute("aria-expanded", "false");
      closeSheet();
      return;
    }

    if (t.matches("[data-toast]")) { toast(t.dataset.toast); return; }

    if (t.matches("[data-submit-sale]")) { submitSale(); return; }

    if (t.matches("[data-submit-concept]")) {
      var sheet = t.closest(".sheet");
      var input = sheet.querySelector(".amount-input");
      var v = input ? validateAmount(input) : 1;
      if (v === null) return;
      closeSheet();
      toast(t.dataset.submitConcept);
      return;
    }

    if (t.matches("[data-undo]")) { undoSale(); return; }

    if (t.matches("[data-retry]")) {
      // إعادة المحاولة تنجح (المحاكاة)
      var dlg = $("#dialog-syserror");
      if (dlg) dlg.hidden = true;
      var v2 = num($("#sale-amount").value) || num(D.sale.amount);
      completeSale(v2);
      return;
    }

    if (t.matches("[data-back]")) {
      var d = $("#dialog-syserror");
      if (d) d.hidden = true;
      var a = $("#sale-amount");
      if (a) a.focus();
      return;
    }

    if (t.matches(".seg-btn")) {
      $all(".seg-btn").forEach(function (b) {
        b.classList.toggle("is-active", b === t);
        b.setAttribute("aria-checked", String(b === t));
      });
      return;
    }

    if (t.matches(".chips-row .chip")) {
      $all(".chips-row .chip").forEach(function (c) {
        c.classList.toggle("is-active", c === t);
        c.setAttribute("aria-pressed", String(c === t));
      });
      return;
    }

    if (t.matches("[data-action]")) {
      var act = t.dataset.action;
      var val = t.dataset.val;
      if (act === "theme") applyTheme(val);
      else if (act === "motion") applyMotion(val);
      else if (act === "text") applyText(val);
      else if (act === "viewport") applyViewport(val);
      else if (act === "finance") { state.saleDone = false; applyFinance(val); }
      else if (act === "orders") applyOrders(val);
      else if (act === "savefail") applySavefail(val);
      else if (act === "panel") {
        var panel = $("#chrome-panel");
        var open = panel.hasAttribute("hidden");
        panel.hidden = !open;
        t.setAttribute("aria-expanded", String(open));
      }
      else if (act === "theme-toggle") applyTheme(state.theme === "dark" ? "light" : "dark");
      else if (act === "motion-toggle") applyMotion(state.motion === "reduced" ? "full" : "reduced");
      else if (act === "text-toggle") applyText(state.text === "200" ? "100" : "200");
      return;
    }
  });

  // إدخال حي لمعاينة الأثر + إزالة الخطأ عند الكتابة
  document.addEventListener("input", function (e) {
    if (e.target.classList && e.target.classList.contains("amount-input")) {
      clearAmountError(e.target);
      if (e.target.id === "sale-amount") updateImpact();
    }
  });

  // Escape يغلق أعلى طبقة
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if ($(".syserr:not([hidden])")) {
        var d = $("#dialog-syserror");
        if (d) d.hidden = true;
        var a = $("#sale-amount"); if (a) a.focus();
      } else if ($(".sheet.is-open")) {
        closeSheet();
      }
    }
  });

  /* ---------- تهيئة من URL + مزامنة المقارنة ---------- */
  function applyExternalState(s) {
    if (!s) return;
    if (s.screen) gotoScreen(s.screen);
    if (s.finance) { state.saleDone = false; applyFinance(s.finance); }
    if (s.orders) applyOrders(s.orders);
    if (s.theme) applyTheme(s.theme);
    if (s.motion) applyMotion(s.motion);
    if (s.text) applyText(s.text);
    if (s.savefail) applySavefail(s.savefail);
    if (s.sheet === "sale") openSheet("sale");
    if (s.sheet === "order") openSheet("order");
  }

  function init() {
    var q = {};
    new URLSearchParams(location.search).forEach(function (v, k) { q[k] = v; });
    applyFinance(q.finance || "positive");
    applyOrders(q.orders || "normal");
    applyTheme(q.theme || "light");
    applyMotion(q.motion || "full");
    applyText(q.text || "100");
    if (q.viewport) applyViewport(q.viewport);
    applySavefail(q.savefail || "off");
    gotoScreen(q.screen || "home");
    if (q.sheet === "sale") openSheet("sale");
    if (q.sheet === "order") openSheet("order");

    // روابط التنقل بين الاتجاهات: مرّر الحالة الحالية
    $all(".chrome-links a").forEach(function (a) {
      a.addEventListener("click", function (ev) {
        var url;
        try { url = new URL(a.href); } catch (e) { return; }
        ["finance", "orders", "theme", "motion", "text", "viewport", "savefail"].forEach(function (k) {
          if (state[k] && state[k] !== "off" && !(k === "finance" && state.finance === "positive") &&
              !(k === "orders" && state.orders === "normal") && !(k === "theme" && state.theme === "light") &&
              !(k === "motion" && state.motion === "full") && !(k === "text" && state.text === "100") &&
              !(k === "viewport" && phone.getAttribute("data-vp") === "390")) {
            url.searchParams.set(k, state[k]);
          }
        });
        a.href = url.toString();
      });
    });

    // استقبال أوامر صفحة المقارنة
    window.addEventListener("message", function (ev) {
      if (ev.data && ev.data.type === "micro-sync") applyExternalState(ev.data.state);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
