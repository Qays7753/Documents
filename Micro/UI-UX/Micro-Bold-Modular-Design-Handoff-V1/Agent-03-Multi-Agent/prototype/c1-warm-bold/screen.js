/* Micro Bold Modular — Agent-03 · screen behavior (vanilla, no dependencies)
   Round-2 fixes applied: theme switch scoped to #settings, choice toggles,
   order stage advancement, submit validation intercept, focus-safe sheets.
   - URL params: ?state= &theme= &sheet= &zoom= &motion= */
(function () {
  "use strict";
  var params = new URLSearchParams(location.search);

  /* ---------- theme / zoom / motion ---------- */
  function applyTheme(theme) {
    if (theme === "dark" || theme === "light") document.documentElement.setAttribute("data-theme", theme);
  }
  applyTheme(params.get("theme"));
  if (params.get("zoom") === "200") { document.documentElement.style.fontSize = "32px"; document.documentElement.classList.add("zoom-200"); }
  if (params.get("motion") === "reduce") document.documentElement.classList.add("reduce-motion");

  /* ---------- screen state ---------- */
  var state = params.get("state");
  var states = document.querySelectorAll("[data-screen-state]");
  if (states.length) {
    var found = false;
    states.forEach(function (el) { if (el.getAttribute("data-screen-state") === state) found = true; });
    if (!found) state = states[0].getAttribute("data-screen-state");
    states.forEach(function (el) {
      el.classList.toggle("is-active", el.getAttribute("data-screen-state") === state);
    });
  }

  /* keep theme/motion/zoom on internal navigation (D-114 + D-211) */
  var keep = [];
  var urlTheme = params.get("theme");
  var storedTheme = null;
  try { storedTheme = localStorage.getItem("micro-theme"); } catch (err) { /* file:// private mode */ }
  var activeTheme = urlTheme || storedTheme;
  if (activeTheme) applyTheme(activeTheme);
  if (urlTheme) keep.push("theme=" + urlTheme);
  if (params.get("zoom")) keep.push("zoom=" + params.get("zoom"));
  if (params.get("motion")) keep.push("motion=" + params.get("motion"));
  function rewriteKeep() {
    document.querySelectorAll("a[data-keep]").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href || href.indexOf(".html") === -1 || href.indexOf("javascript") === 0) return;
      var qIdx = href.indexOf("?");
      var base = qIdx === -1 ? href : href.slice(0, qIdx);
      var existing = new URLSearchParams(qIdx === -1 ? "" : href.slice(qIdx + 1));
      ["theme", "zoom", "motion"].forEach(function (k) { existing.delete(k); });
      var parts = [];
      if (urlTheme) parts.push("theme=" + urlTheme);
      else if (storedTheme) parts.push("theme=" + storedTheme);
      if (params.get("zoom")) parts.push("zoom=" + params.get("zoom"));
      if (params.get("motion")) parts.push("motion=" + params.get("motion"));
      var kept = existing.toString();
      var add = parts.join("&");
      var final = base;
      if (kept) final += "?" + kept;
      if (add) final += (kept ? "&" : "?") + add;
      a.setAttribute("href", final);
    });
  }
  rewriteKeep();
  window.__rewriteKeep = function () { storedTheme = document.documentElement.getAttribute("data-theme"); try { localStorage.setItem("micro-theme", storedTheme); } catch (err) {} rewriteKeep(); };

  /* ---------- sheets: open/close + focus trap + Esc + focus return ---------- */
  var backdrop = document.querySelector(".backdrop");
  var lastFocus = null;
  function openSheet(id) {
    var sheet = document.getElementById("sheet-" + id);
    if (!sheet) return;
    lastFocus = document.activeElement;
    sheet.classList.add("sheet--open");
    if (backdrop) backdrop.classList.add("backdrop--open");
    var first = sheet.querySelector(".sheet__close, .menu-row, .btn, [href], button");
    if (first) first.focus();
    sheet.__opener = lastFocus;
  }
  function closeSheets() {
    document.querySelectorAll(".sheet--open").forEach(function (sheet) {
      sheet.classList.remove("sheet--open");
      if (sheet.__opener && sheet.__opener.focus) sheet.__opener.focus();
    });
    if (backdrop) backdrop.classList.remove("backdrop--open");
  }
  document.addEventListener("click", function (e) {
    var opener = e.target.closest("[data-sheet]");
    if (opener) { e.preventDefault(); openSheet(opener.getAttribute("data-sheet")); return; }
    var closer = e.target.closest("[data-close]");
    if (closer) { e.preventDefault(); closeSheets(); return; }
    if (e.target === backdrop) { closeSheets(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeSheets();
    if (e.key === "Tab") {
      var open = document.querySelector(".sheet--open");
      if (!open) return;
      var focusables = open.querySelectorAll("button, [href], input, select, textarea, [tabindex]:not([tabindex='-1'])");
      if (!focusables.length) return;
      var first = focusables[0], last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* open sheet from ?sheet= */
  var sheetParam = params.get("sheet");
  if (sheetParam) openSheet(sheetParam);

  /* ---------- choice chips (payment etc.) — local toggle (D-113) ---------- */
  document.querySelectorAll(".choice-row").forEach(function (group) {
    group.addEventListener("click", function (e) {
      var chip = e.target.closest(".choice");
      if (!chip || !group.contains(chip)) return;
      group.querySelectorAll(".choice").forEach(function (c) {
        c.classList.remove("choice--on");
        c.setAttribute("aria-pressed", "false");
      });
      chip.classList.add("choice--on");
      chip.setAttribute("aria-pressed", "true");
    });
  });

  /* ---------- sale form: live validation (fixture I) + submit intercept (D-102) ---------- */
  var form = document.getElementById("sale-form");
  if (form) {
    var amount = form.querySelector("[name=amount]");
    var field = form.querySelector(".amount-field");
    var err = document.getElementById("amount-error");
    var submit = form.querySelector("#submit-sale, button[type=submit]");
    function validate() {
      var v = amount ? parseFloat(amount.value.replace(",", ".")) : NaN;
      var bad = isNaN(v) || v <= 0;
      if (field) field.classList.toggle("field--error", bad);
      if (err) err.classList.toggle("is-hidden", !bad);
      return !bad;
    }
    if (amount) amount.addEventListener("input", function () {
      if (field && field.classList.contains("field--error")) validate();
      var v = parseFloat(amount.value.replace(",", "."));
      var previews = document.querySelectorAll(".preview-amount");
      if (!isNaN(v) && v > 0) previews.forEach(function (el) { el.textContent = amount.value.trim(); });
    });
    if (submit) submit.addEventListener("click", function (e) {
      if (!validate()) { e.preventDefault(); e.stopPropagation(); if (amount) amount.focus(); }
    });
    if (params.get("state") === "validation") {
      if (amount) amount.value = "0";
      validate();
      if (amount) setTimeout(function () { amount.focus(); }, 60);
    }
  }

  /* ---------- switches: only the settings row toggles the theme (D-113) ---------- */
  document.querySelectorAll(".switch").forEach(function (sw) {
    var isThemeSwitch = !!sw.closest("#settings");
    if (isThemeSwitch) {
      var isDark = document.documentElement.getAttribute("data-theme") === "dark";
      sw.setAttribute("role", "switch");
      sw.setAttribute("aria-checked", isDark ? "true" : "false");
      sw.setAttribute("aria-label", "تبديل الوضع الليلي");
      if (isDark) sw.classList.add("switch--on");
      sw.addEventListener("click", function () {
        var nowDark = document.documentElement.getAttribute("data-theme") === "dark";
        applyTheme(nowDark ? "light" : "dark");
        sw.classList.toggle("switch--on", !nowDark);
        sw.setAttribute("aria-checked", !nowDark ? "true" : "false");
        if (window.__rewriteKeep) window.__rewriteKeep();
      });
    } else {
      sw.setAttribute("role", "switch");
      sw.setAttribute("aria-checked", "false");
      sw.addEventListener("click", function () {
        var on = sw.classList.toggle("switch--on");
        sw.setAttribute("aria-checked", on ? "true" : "false");
      });
    }
  });

  /* ---------- order screen: advance stage rail (D-113) ---------- */
  var advance = document.getElementById("advance-stage");
  if (advance) {
    var STAGES = ["اتفاق", "تنفيذ", "جاهز", "تم التسليم"];
    var steps = document.querySelectorAll(".ostep");
    advance.addEventListener("click", function () {
      var cur = -1;
      steps.forEach(function (el, i) { if (el.classList.contains("ostep--current")) cur = i; });
      if (cur === -1 || cur >= STAGES.length - 1) { advance.setAttribute("disabled", "disabled"); return; }
      steps[cur].classList.remove("ostep--current", "ostep--late");
      steps[cur].classList.add("ostep--done");
      var next = steps[cur + 1];
      next.classList.add("ostep--current");
      next.classList.remove("ostep--late");
      var chip = document.querySelector(".project-context .late-chip");
      if (chip) {
        if (STAGES[cur + 1] === "تم التسليم") { chip.innerHTML = next.querySelector(".ostep__label").innerHTML ? "تم التسليم" : "تم التسليم"; chip.style.color = "var(--pos)"; chip.style.background = "var(--pos-tint)"; chip.style.borderColor = "var(--pos)"; }
        else if (STAGES[cur + 1] === "جاهز") { chip.textContent = "جاهز للتسليم"; chip.style.color = "var(--att)"; chip.style.background = "var(--att-tint)"; chip.style.borderColor = "var(--att)"; }
      }
      if (cur + 1 >= STAGES.length - 1) advance.setAttribute("disabled", "disabled");
    });
  }

  /* ---------- market: notify toggle (honest local demo state) ---------- */
  var notify = document.getElementById("notify-btn");
  if (notify) {
    notify.addEventListener("click", function () {
      notify.textContent = "تم تسجيل اهتمامك — بنبلغك لما يجهز";
      notify.classList.remove("btn--secondary");
      notify.classList.add("btn--ink");
      notify.setAttribute("aria-pressed", "true");
    });
  }

  /* ---------- success impact flash (Success Impact) ---------- */
  var impact = document.querySelector(".success-impact");
  if (impact && !document.documentElement.classList.contains("reduce-motion")) {
    impact.classList.add("success-impact--flash");
  }
})();
