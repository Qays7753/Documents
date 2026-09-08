/* component-gallery.js — offline gallery behavior. No dependencies, no network.
   Controls: viewport width, direction, text size, motion. Interactions: chips,
   segmented (pill + underline), select menu, search clear, sheet/dialog/snackbar
   (mounted into the triggering frame), loading/completion buttons, nav switching,
   amount live-grouping. Evidence panel builds ramp swatches (documentation chrome). */
(function () {
  "use strict";
  var root = document.documentElement;
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ---------- controls ---------- */
  function bindSeg(id, attr, apply) {
    var seg = $(id);
    if (!seg) return;
    $$("button", seg).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", seg).forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        apply(b.getAttribute(attr), b);
      });
    });
  }

  var frameLabels = $$("[data-w-label]");
  function setViewport(vp) {
    root.style.setProperty("--frame-w", vp === "auto" ? "100%" : vp + "px");
    frameLabels.forEach(function (el) { el.textContent = vp === "auto" ? "auto" : vp; });
  }

  bindSeg("#ctrl-viewport", "data-vp", setViewport);
  bindSeg("#ctrl-dir", "data-dir", function (v) { root.setAttribute("dir", v); });
  bindSeg("#ctrl-text", "data-text", function (v) { root.setAttribute("data-text-size", v); });
  bindSeg("#ctrl-motion", "data-motion", function (v) { root.setAttribute("data-motion", v); });
  setViewport("auto");

  /* ---------- evidence panel ---------- */
  var evPanel = $("#evidence-panel");
  var evBtn = $("#btn-evidence");
  function toggleEvidence(open) {
    if (!evPanel) return;
    evPanel.hidden = !open;
    if (evBtn) evBtn.setAttribute("aria-expanded", String(open));
  }
  if (evBtn) evBtn.addEventListener("click", function () { toggleEvidence(evPanel.hidden); });
  var evClose = $("#btn-evidence-close");
  if (evClose) evClose.addEventListener("click", function () { toggleEvidence(false); });

  var RAMPS = {
    primary: ["#FBF3EF", "#F4E4DB", "#E8C9B8", "#DBAE91", "#D59172", "#CC785C", "#B4613F", "#964E33", "#783B28", "#5A2C1D"],
    accent: ["#E3F5F5", "#C0EAEA", "#8FD5D6", "#5EC0C1", "#2DABAD", "#079FA0", "#057B7C", "#045E5F", "#034142", "#022425"],
    positive: ["#E4F2EA", "#C9E6D5", "#A7D8BE", "#7FC49E", "#57B07E", "#2E7D57", "#256A48", "#1C5739", "#13442A", "#0A311B"],
    negative: ["#FBE7E6", "#F5C9C7", "#EEA19E", "#E47975", "#DB514C", "#C9322A", "#B42318", "#911C12", "#6E150C", "#4B0E06"],
    operational: ["#E8EEF3", "#D1DDE6", "#B0C3D2", "#8AA5B8", "#68899E", "#5B7C99", "#3E5C76", "#2F485B", "#203340", "#111E25"],
    gold: ["#F6ECCF", "#EFDAA0", "#E2C268", "#D6AB38", "#C99100", "#B08532", "#8A6927", "#644D1C", "#3E3112", "#1F1809"]
  };
  $$("[data-ramp]").forEach(function (holder) {
    var vals = RAMPS[holder.getAttribute("data-ramp")] || [];
    vals.forEach(function (hex, i) {
      var s = document.createElement("span");
      s.style.background = hex;
      s.setAttribute("data-step", String((i + 1) * 50));
      s.title = hex;
      holder.appendChild(s);
    });
  });

  /* ---------- chips (single selection) ---------- */
  $$("[data-chip-group]").forEach(function (group) {
    $$("button.chip", group).forEach(function (chip) {
      chip.addEventListener("click", function () {
        if (chip.disabled) return;
        $$("button.chip", group).forEach(function (c) { c.classList.remove("on"); });
        chip.classList.add("on");
      });
    });
  });

  /* ---------- segmented control (pill) ---------- */
  $$("[data-seg]").forEach(function (seg) {
    var thumb = $(".segctl-thumb", seg);
    var buttons = $$("button", seg);
    function place() {
      var on = seg.querySelector("button.on");
      if (!on || !thumb) return;
      var segRect = seg.getBoundingClientRect();
      var onRect = on.getBoundingClientRect();
      var start = onRect.left - segRect.left;
      if (getComputedStyle(root).direction === "rtl") {
        start = segRect.right - onRect.right;
      }
      thumb.style.width = onRect.width + "px";
      thumb.style.insetInlineStart = start + "px";
      thumb.hidden = false;
    }
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        place();
      });
    });
    window.addEventListener("resize", place);
    window.addEventListener("load", place);
    place();
  });

  /* ---------- segmented control (underline) ---------- */
  $$("[data-seg-lines]").forEach(function (seg) {
    var buttons = $$("button", seg);
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
      });
    });
  });

  /* ---------- search clear ---------- */
  $$("input[type=search]").forEach(function (input) {
    var wrap = input.closest(".search-wrap");
    var clear = wrap ? $(".clear-btn", wrap) : null;
    function refresh() { if (clear) clear.hidden = !input.value; }
    input.addEventListener("input", refresh);
    if (clear) clear.addEventListener("click", function () {
      input.value = ""; refresh(); input.focus();
    });
    refresh();
  });

  /* ---------- amount live grouping ---------- */
  $$("input.input-amount").forEach(function (input) {
    input.addEventListener("input", function () {
      var digits = input.value.replace(/[^\d]/g, "").slice(0, 12);
      input.value = digits ? digits.replace(/\B(?=(\d{3})+(?!\d))/g, ",") : "";
    });
  });

  /* ---------- select menu ---------- */
  $$("[data-menu]").forEach(function (field) {
    var trigger = $(".input-select", field);
    var menu = $(".menu", field);
    if (!trigger || !menu) return;
    trigger.addEventListener("click", function () {
      var open = menu.hidden;
      menu.hidden = !open;
      trigger.setAttribute("aria-expanded", String(open));
    });
    $$("button", menu).forEach(function (opt) {
      opt.addEventListener("click", function () {
        $$("button", menu).forEach(function (o) { o.setAttribute("aria-selected", "false"); o.classList.remove("on"); });
        opt.setAttribute("aria-selected", "true"); opt.classList.add("on");
        $(".sel-value", trigger).textContent = opt.textContent;
        menu.hidden = true;
        trigger.setAttribute("aria-expanded", "false");
      });
    });
  });

  /* ---------- overlays: mount into the triggering frame ---------- */
  var home = $("#overlays .screen");
  var scrim = $("[data-scrim]");
  var sheet = $(".sheet");
  var dialog = $(".dialog");
  var snackbar = $(".snackbar");
  var openTrigger = null;

  function mount(el, screen) {
    if (el && screen && el.parentElement !== screen) screen.appendChild(el);
  }
  function overlayClose() {
    if (sheet) sheet.hidden = true;
    if (dialog) dialog.hidden = true;
    if (scrim) scrim.hidden = true;
    if (openTrigger && openTrigger.focus) { try { openTrigger.focus(); } catch (e) {} }
    openTrigger = null;
  }
  function firstFocusable(el) {
    return el.querySelector("button, input, textarea, select, a[href]");
  }
  function openOverlay(el, screen) {
    overlayClose();
    mount(scrim, screen); mount(el, screen);
    if (scrim) scrim.hidden = false;
    el.hidden = false;
    var f = firstFocusable(el);
    if (f) setTimeout(function () { try { f.focus(); } catch (e) {} }, 60);
  }
  $$("[data-open-sheet]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      openTrigger = btn;
      var screen = btn.closest(".screen") || home;
      if (sheet) openOverlay(sheet, screen);
    });
  });
  $$("[data-open-dialog]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      openTrigger = btn;
      var screen = btn.closest(".screen") || home;
      if (dialog) openOverlay(dialog, screen);
    });
  });
  $$("[data-close-overlay]").forEach(function (btn) {
    btn.addEventListener("click", overlayClose);
  });
  if (scrim) scrim.addEventListener("click", overlayClose);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") overlayClose();
    if (e.key === "Tab") {
      var open = null;
      if (sheet && !sheet.hidden) open = sheet;
      if (dialog && !dialog.hidden) open = dialog;
      if (!open) return;
      var f = $$("button, input, textarea, select, a[href]", open).filter(function (x) { return !x.disabled && x.offsetParent !== null; });
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* ---------- snackbar ---------- */
  var sbTimer = null;
  function fireSnackbar(msg, screen) {
    if (!snackbar) return;
    if (home) mount(snackbar, screen || home);
    var m = $(".snackbar-msg", snackbar);
    if (m) m.textContent = msg;
    snackbar.hidden = false;
    if (sbTimer) clearTimeout(sbTimer);
    sbTimer = setTimeout(function () { snackbar.hidden = true; }, 5000);
  }
  $$("[data-fire-snackbar]").forEach(function (btn) {
    btn.addEventListener("click", function () { fireSnackbar("Record deleted", btn.closest(".screen")); });
  });
  var undo = $("[data-undo]");
  if (undo) undo.addEventListener("click", function () {
    snackbar.hidden = true;
    fireSnackbar("Deletion reversed");
  });

  /* ---------- loading & quiet completion ---------- */
  $$("[data-loading-btn]").forEach(function (btn) {
    var label = $(".btn-label", btn);
    var spinner = $(".spinner", btn);
    var check = $(".ic-check", btn);
    var busy = false;
    btn.addEventListener("click", function () {
      if (busy) return;
      busy = true;
      btn.classList.add("is-loading");
      btn.disabled = true;
      if (label) label.textContent = "Saving";
      if (spinner) spinner.hidden = false;
      setTimeout(function () {
        btn.classList.remove("is-loading");
        if (spinner) spinner.hidden = true;
        btn.classList.add("btn-complete");
        if (label) label.textContent = "Saved";
        if (check) check.hidden = false;
        setTimeout(function () {
          btn.classList.remove("btn-complete");
          if (check) check.hidden = true;
          if (label) label.textContent = "Save";
          btn.disabled = false;
          busy = false;
          fireSnackbar("Record saved", btn.closest(".screen"));
        }, 800);
      }, 1600);
    });
  });
  var completeDemo = $("[data-complete-demo]");
  if (completeDemo) completeDemo.addEventListener("click", function () {
    fireSnackbar("Already saved", completeDemo.closest(".screen"));
  });

  /* ---------- retry ---------- */
  $$("[data-retry]").forEach(function (btn) {
    var busy = false;
    btn.addEventListener("click", function () {
      if (busy) return;
      busy = true;
      var original = btn.textContent;
      btn.textContent = "Retrying";
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = original;
        btn.disabled = false;
        busy = false;
        fireSnackbar("Connection restored — records loaded", btn.closest(".screen"));
      }, 1400);
    });
  });

  /* ---------- clear filters ---------- */
  $$("[data-chip-clear]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var group = $("[data-chip-group]");
      if (group) {
        var chips = $$("button.chip", group);
        chips.forEach(function (c) { c.classList.remove("on"); });
        if (chips[0]) chips[0].classList.add("on");
      }
      fireSnackbar("Filters cleared", btn.closest(".screen"));
    });
  });

  /* ---------- bottom nav switching ---------- */
  $$("[data-nav]").forEach(function (item) {
    item.addEventListener("click", function () {
      var nav = item.closest(".bottomnav");
      if (!nav) return;
      $$("[data-nav]", nav).forEach(function (x) { x.classList.remove("on"); });
      item.classList.add("on");
    });
  });
})();
