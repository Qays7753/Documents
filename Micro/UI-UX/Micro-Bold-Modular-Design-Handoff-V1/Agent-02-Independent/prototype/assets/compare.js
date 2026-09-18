/* compare.js — مزامنة الأطر الثلاثة في وضع المقارنة */
(function () {
  "use strict";
  var ids = ["f-c1", "f-c2", "f-c3"];
  var frames = ids.map(function (id) { return document.getElementById(id); }).filter(Boolean);
  if (!frames.length) return;

  function currentUrl(f) {
    try { return new URL(f.src, location.href); } catch (e) { return null; }
  }

  function syncAll() {
    var state = {
      screen: document.getElementById("c-screen").value,
      finance: document.getElementById("c-finance").value,
      orders: document.getElementById("c-orders").value,
      theme: document.getElementById("c-theme").value
    };
    var vp = document.getElementById("c-vp").value;
    frames.forEach(function (f) {
      // أعد التحميل بعنوان محدث لضمان تطابق كامل (أسهل وأصدق من التصحيح الجزئي)
      var u = currentUrl(f);
      if (!u) return;
      ["screen", "finance", "orders", "theme"].forEach(function (k) {
        u.searchParams.set(k, state[k]);
      });
      var target = u.toString();
      if (f.src !== target) f.src = target;
      else {
        try { f.contentWindow.postMessage({ type: "micro-sync", state: state }, "*"); } catch (e) {}
      }
      f.style.blockSize = (vp === "320") ? "700px" : (vp === "430" ? "840px" : "780px");
    });
  }

  ["c-screen", "c-finance", "c-orders", "c-theme", "c-vp"].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) el.addEventListener("change", syncAll);
  });
  syncAll();
})();
