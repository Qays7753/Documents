/* ═══════════════════════════════════════════════════════════════
   Micro — Direction A «الخلاصة اليومية» / The Daily Brief · app.js
   Large-title collapse · timeline · center capture slot
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const ICONS = {
  search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>',
  plus: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
  x: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  back: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
  chev: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>',
  sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M18.4 5.6L17 7M7 17l-1.4 1.4"/></svg>',
  'sun-fill': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="5"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5 5l1.6 1.6M17.4 17.4L19 19M19 5l-1.6 1.6M6.6 17.4L5 19" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg>',
  ledger: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6.5 4h12v16h-12z"/><path d="M9.5 8.5h6M9.5 12h6M9.5 15.5h3.5"/></svg>',
  'ledger-fill': '<svg viewBox="0 0 24 24"><rect x="6.5" y="3.6" width="12" height="16.8" rx="1" opacity=".16"/><rect x="6.5" y="3.6" width="12" height="16.8" rx="1" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9.5 8.5h6M9.5 12h6M9.5 15.5h3.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg>',
  people: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19c.6-3.4 2.8-5 5.5-5s4.9 1.6 5.5 5"/><circle cx="16.5" cy="9.5" r="2.4"/><path d="M15.8 14.3c2.4.2 4.1 1.7 4.7 4.2"/></svg>',
  'people-fill': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19c.6-3.4 2.8-5 5.5-5s4.9 1.6 5.5 5z"/><circle cx="16.5" cy="9.5" r="2.4" opacity=".55"/><path d="M15.8 14.3c2.4.2 4.1 1.7 4.7 4.2z" opacity=".55"/></svg>',
  tools: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 4.5v2M12 17.5v2M4.5 12h2M17.5 12h2M6.7 6.7l1.4 1.4M15.9 15.9l1.4 1.4M17.3 6.7l-1.4 1.4M8.1 15.9l-1.4 1.4"/></svg>',
  'tools-fill': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="3.4"/><path d="M12 4v2.6M12 17.4V20M4 12h2.6M17.4 12H20M6.4 6.4l1.8 1.8M15.8 15.8l1.8 1.8M17.6 6.4l-1.8 1.8M8.2 15.8l-1.8 1.8" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>',
  check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  'check-fill': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="currentColor" opacity=".18"/><path d="M7.5 12.5l3 3 6-6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  'check-double': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12.5l3.5 3.5L13 9"/><path d="M10.5 15l1.5 1.5L20 8.5"/></svg>',
  clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="8"/><path d="M12 8v4.5l3 2"/></svg>',
  future: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="8" stroke-dasharray="3 3"/></svg>',
  'cloud-off': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18a4.5 4.5 0 0 1-.4-9A5.5 5.5 0 0 1 17.3 8.5 3.9 3.9 0 0 1 17 16.2"/><path d="M4 4l16 16"/></svg>',
  conflict: '<svg viewBox="0 0 24 24"><path d="M12 3l9 16.5H3z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 7v10" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2.5 2.5"/></svg>',
  refresh: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12a7 7 0 1 1-2-4.9"/><path d="M17.5 3.5v3.6h-3.6"/></svg>',
  spark: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4l1.8 4.7L18.5 10.5l-4.7 1.8L12 17l-1.8-4.7L5.5 10.5l4.7-1.8z"/><path d="M18.5 16.5l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/></svg>',
  share: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15V4M8.5 7.5L12 4l3.5 3.5"/><path d="M6 12H4.5v8h15v-8H18"/></svg>',
  backspace: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 5h12v14H8L2.5 12z"/><path d="M11.5 9.5l5 5M16.5 9.5l-5 5"/></svg>',
  alert: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4l9 16H3z"/><path d="M12 10.5v3.5M12 17.2v.3"/></svg>',
  scale: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M7 20h10M5 8h14M5 8l-2.5 5a3 3 0 0 0 5 0zM19 8l2.5 5a3 3 0 0 1-5 0z"/><path d="M12 4.5l7 3.5M12 4.5L5 8"/></svg>',
};
document.querySelectorAll('[data-icon]').forEach(el => { el.innerHTML = ICONS[el.dataset.icon] || ''; });

const $  = (s, c) => (c || document).querySelector(s);
const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
const app = $('#app');
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ═══════════ Navigation stack ═══════════ */
const ROOTS = { brief:'scr-brief', ledger:'scr-ledger', people:'scr-people', tools:'scr-tools' };
const stacks = { brief:['scr-brief'], ledger:['scr-ledger'], people:['scr-people'], tools:['scr-tools'] };
const scrollMemo = {};
let activeTab = 'brief';
let navSource = null;
const screens = {};
const TAB_ICON = { brief:'sun', ledger:'ledger', people:'people', tools:'tools' };
$$('.screen').forEach(s => screens[s.id] = s);

function renderTab(fade){
  const stack = stacks[activeTab];
  Object.entries(screens).forEach(([id, el]) => {
    const idx = stack.indexOf(id);
    if (idx === -1) { el.hidden = true; el.classList.remove('is-under','is-under-resting','is-enter','is-exiting'); return; }
    if (idx === stack.length - 1) {
      el.hidden = false; el.classList.remove('is-under','is-under-resting','is-enter','is-exiting');
      if (fade) { el.classList.remove('fade-in'); void el.offsetWidth; el.classList.add('fade-in'); }
    } else if (idx === stack.length - 2) { el.hidden = false; el.classList.add('is-under-resting'); }
    else { el.hidden = true; }
  });
  const top = screens[stack[stack.length - 1]];
  const sc = $('[data-scroller]', top); if (sc) sc.scrollTop = scrollMemo[top.id] || 0;
  $$('.tabbtn').forEach(b => {
    const on = b.dataset.tab === activeTab;
    b.classList.toggle('is-active', on);
    b.setAttribute('aria-selected', on);
    const ic = $('.t-ic', b);
    if (ic) ic.innerHTML = ICONS[TAB_ICON[b.dataset.tab] + (on ? '-fill' : '')];
  });
}
function switchTab(tab, viaTap){
  if (tab === activeTab) {
    if (viaTap) {
      const st = stacks[tab];
      while (st.length > 1) { const id = st.pop(); screens[id].hidden = true; }
      const sc = $('[data-scroller]', screens[ROOTS[tab]]); if (sc) sc.scrollTop = 0;
      renderTab(false);
    }
    return;
  }
  const cur = screens[stacks[activeTab][stacks[activeTab].length - 1]];
  const sc = $('[data-scroller]', cur); if (sc) scrollMemo[cur.id] = sc.scrollTop;
  activeTab = tab;
  renderTab(true);
}
function push(id, source){
  const stack = stacks[activeTab];
  if (stack[stack.length - 1] === id) return;
  navSource = source || document.activeElement;
  const from = screens[stack[stack.length - 1]];
  const to = screens[id];
  stack.push(id);
  to.hidden = false;
  to.classList.add('is-enter');
  void to.offsetWidth;
  requestAnimationFrame(() => { to.classList.remove('is-enter'); from.classList.add('is-under'); });
  const title = $('.appbar-title-compact', to) || $('.appbar-title', to) || $('.largetitle h1', to);
  if (title) { title.setAttribute('tabindex','-1'); title.focus({ preventScroll:true }); }
}
function pop(){
  const stack = stacks[activeTab];
  if (stack.length < 2) return;
  const from = screens[stack.pop()];
  const to = screens[stack[stack.length - 1]];
  from.classList.add('is-exiting');
  to.classList.remove('is-under','is-under-resting');
  setTimeout(() => { from.hidden = true; from.classList.remove('is-exiting'); }, REDUCED ? 0 : 280);
  if (navSource && navSource.isConnected) { try { navSource.focus({ preventScroll:true }); } catch(e){} }
}
$$('[data-nav]').forEach(el => el.addEventListener('click', e => {
  if (e.target.closest('.fixlink')) return;
  const target = el.dataset.nav;
  if (target === 'party') openParty(el);
  else push('scr-' + target, el);
}));
$$('[data-back]').forEach(el => el.addEventListener('click', pop));
$$('.tabbtn').forEach(b => b.addEventListener('click', () => switchTab(b.dataset.tab, true)));

/* ═══════════ Large-title collapse — A's signature ═══════════ */
const briefBody = $('#brief-body');
const compactbar = $('#brief-compact');
briefBody.addEventListener('scroll', () => {
  compactbar.classList.toggle('on', briefBody.scrollTop > 132);
}, { passive:true });

/* ═══════════ Search + people filters ═══════════ */
function normAr(s){
  return (s||'').replace(/[\u064B-\u0652\u0640]/g,'')
    .replace(/[أإآ]/g,'ا').replace(/ة/g,'ه').replace(/ى/g,'ي').trim();
}
function filterRegister(){
  const q = normAr($('#reg-search').value);
  $$('#reg-list .daysec').forEach(sec => {
    let any = false;
    $$('.row', sec).forEach(r => {
      const show = !q || normAr(r.textContent).includes(q);
      r.style.display = show ? '' : 'none';
      if (show) any = true;
    });
    sec.style.display = any ? '' : 'none';
  });
  const total = $$('#reg-list .row').filter(r => r.style.display !== 'none').length;
  $('#reg-empty').hidden = total !== 0;
  $('#reg-list').style.display = total ? '' : 'none';
}
$('#reg-search').addEventListener('input', filterRegister);
$('[data-act="clear-search"]').addEventListener('click', () => { $('#reg-search').value=''; filterRegister(); $('#reg-search').focus(); });
$('[data-act="clear-people-search"]').addEventListener('click', () => { $('#people-search').value=''; filterPeople(); });

let pseg = 'cust', pchip = 'all';
$$('[data-pseg]').forEach(b => b.addEventListener('click', () => {
  pseg = b.dataset.pseg;
  $$('[data-pseg]').forEach(x => { x.classList.toggle('is-active', x===b); x.setAttribute('aria-selected', x===b); });
  filterPeople();
}));
$$('[data-pchip]').forEach(b => b.addEventListener('click', () => {
  pchip = b.dataset.pchip;
  $$('[data-pchip]').forEach(x => x.classList.toggle('is-active', x===b));
  filterPeople();
}));
$('#people-search').addEventListener('input', filterPeople);
$$('#people-list .ppl-row').forEach(r => r.dataset.week = ['khatib','aman','yasmine'].includes(r.dataset.party) ? '1' : '');
function filterPeople(){
  const q = normAr($('#people-search').value);
  $$('.ppl').forEach(list => list.hidden = !list.classList.contains(pseg));
  let total = 0;
  $$('.ppl-row').forEach(r => {
    const okSeg = r.closest('.ppl').classList.contains(pseg);
    const okChip = pchip === 'all' || (pchip === 'late' && r.dataset.late) || (pchip === 'week' && r.dataset.week);
    const okQ = !q || normAr(r.textContent).includes(q);
    const show = okSeg && okChip && okQ;
    r.style.display = show ? '' : 'none';
    if (show) total++;
  });
  $('#people-empty').hidden = total !== 0;
  $('#people-list').hidden = total === 0;
}

/* party detail */
const PARTIES = {
  khatib:  { title:'محمد الخطيب', sub:'مقاول تركيبات صحية', bal:'940.00', cls:'pos', state:'مستحق منذ <bdi dir="ltr">21/07/2026</bdi> — 48 يومًا', icon:'clock', icls:'st-wait' },
  aman:    { title:'ورشة الأمان', sub:'ورشة صيانة', bal:'540.00', cls:'pos', state:'حالي 260.00 + متأخر 280.00', icon:'clock', icls:'st-wait', rel:true },
  abuziad: { title:'أبو زياد للمقاولات', sub:'مقاولات', bal:'760.00', cls:'pos', state:'مستحق منذ <bdi dir="ltr">27/08</bdi> · تعارض بانتظار المراجعة', icon:'clock', icls:'st-wait' },
  yasmine: { title:'مقهى الياسمين', sub:'مشروع تجديد', bal:'0.00', cls:'', state:'محصّل بالكامل — الأحد <bdi dir="ltr">06/09</bdi>', icon:'check-fill', icls:'st-ok' },
  rashid:  { title:'شركة الرشيد للتوزيع', sub:'مواد صحية بالجملة', bal:'2,350.00', cls:'neg', state:'استحقاق <bdi dir="ltr">15/09/2026</bdi>', icon:'future', icls:'st-future' },
  petra:   { title:'مصنع البتراء للسيراميك والبلاط', sub:'فرع السخنة', bal:'4,300.00', cls:'neg', state:'استحقاق <bdi dir="ltr">30/09/2026</bdi> · طلب اليوم غير محدد', icon:'future', icls:'st-future' },
  sharq:   { title:'مؤسسة الشرق للتجهيزات', sub:'تجهيزات', bal:'0.00', cls:'', state:'مسدّد بالكامل', icon:'check-fill', icls:'st-ok' },
};
function openParty(rowEl){
  const p = PARTIES[rowEl.dataset.party]; if (!p) return;
  $('#party-title').textContent = p.title;
  $('#party-sub').textContent = p.sub;
  $('#party-balance').textContent = p.bal;
  $('#party-balance').parentElement.className = 'eh-amt ' + p.cls;
  $('#party-state').innerHTML = `<span class="st-ic ${p.icls}" data-icon="${p.icon}"></span><span>${p.state}</span>`;
  $('[data-icon]', $('#party-state')).innerHTML = ICONS[p.icon];
  $('#relbar').hidden = !p.rel;
  push('scr-party', rowEl);
}

/* ═══════════ Sheets ═══════════ */
const scrim = $('#scrim');
let openSheetId = null;
function openSheet(id){
  if (openSheetId) hideSheet(openSheetId, true);
  openSheetId = id;
  const sh = document.getElementById(id);
  sh.hidden = false;
  scrim.hidden = false; requestAnimationFrame(() => scrim.classList.add('show'));
  requestAnimationFrame(() => sh.classList.add('open'));
  $('#capbtn').classList.add('hidden-cap');
  const t = $('.sheet-title', sh); if (t) { t.setAttribute('tabindex','-1'); t.focus({preventScroll:true}); }
}
function hideSheet(id, instant){
  const sh = document.getElementById(id);
  sh.classList.add('closing');
  scrim.classList.remove('show');
  const done = () => { sh.hidden = true; sh.classList.remove('open','closing'); sh.style.transform = ''; };
  if (instant || REDUCED) done(); else setTimeout(done, 230);
  if (openSheetId === id) openSheetId = null;
  $('#capbtn').classList.remove('hidden-cap');
}
function closeSheet(id){ hideSheet(id); }
$$('[data-close-sheet]').forEach(b => b.addEventListener('click', () => {
  const sh = b.closest('.sheet');
  if (sh.id === 'sheet-capture' && parseAmt() > 0) { openDialog('dlg-discard'); return; }
  hideSheet(sh.id);
  if (sh.id === 'sheet-capture') resetCapture();
}));
$$('.sheet [data-drag]').forEach(zone => {
  const sh = zone.closest('.sheet');
  let y0 = null, dy = 0, t0 = 0;
  zone.addEventListener('pointerdown', e => { y0 = e.clientY; t0 = Date.now(); dy = 0; });
  zone.addEventListener('pointermove', e => {
    if (y0 === null) return;
    dy = Math.max(0, e.clientY - y0);
    sh.style.transition = 'none';
    sh.style.transform = `translateY(${dy}px)`;
  });
  const end = () => {
    if (y0 === null) return;
    const v = dy / Math.max(1, Date.now() - t0);
    sh.style.transition = ''; sh.style.transform = '';
    if (dy > 96 || v > 0.5) {
      if (sh.id === 'sheet-capture' && parseAmt() > 0) { openDialog('dlg-discard'); sh.classList.remove('open'); return; }
      hideSheet(sh.id);
      if (sh.id === 'sheet-capture') resetCapture();
    }
    y0 = null; dy = 0;
  };
  zone.addEventListener('pointerup', end);
  zone.addEventListener('pointercancel', end);
});
scrim.addEventListener('click', () => { if (openSheetId) { const id = openSheetId; hideSheet(id); if (id === 'sheet-capture') resetCapture(); } });
$$('[data-act="open-capture"]').forEach(b => b.addEventListener('click', () => openSheet('sheet-capture')));
$('[data-act="discard-amount"]').addEventListener('click', () => { closeDialog('dlg-discard'); resetCapture(); hideSheet('sheet-capture'); });

/* ═══════════ Keypad ═══════════ */
let amtStr = '';
function fmtLive(s){
  if (!s) return '0';
  const [i, f] = s.split('.');
  const gi = (i||'').replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return s.includes('.') ? gi + '.' + (f||'') : gi;
}
function renderAmt(){ $('#amt-val').textContent = fmtLive(amtStr); $('#col-amt').textContent = fmtLive(amtStr); }
function kpress(k){
  if (k === '⌫') amtStr = amtStr.slice(0, -1);
  else if (k === '.') { if (!amtStr.includes('.')) amtStr += '.'; }
  else if (/^\d$/.test(k)) { if (amtStr.replace('.','').length < 9) amtStr += k; }
  renderAmt();
}
$$('.keypad button').forEach(b => b.addEventListener('click', () => {
  if (b.dataset.k) kpress(b.dataset.k);
  else if (b.dataset.add) { amtStr = String(Math.round((parseAmt() + parseFloat(b.dataset.add)) * 100) / 100); renderAmt(); }
  else if (b.dataset.act === 'amt-clear') { amtStr = ''; renderAmt(); }
}));
function parseAmt(){ const v = parseFloat(amtStr.replace(/,/g,'')); return isNaN(v) ? 0 : v; }
function fmt2(v){ return v.toLocaleString('en-US', { minimumFractionDigits:2, maximumFractionDigits:2 }); }
const SAVE_HTML = $('#cap-save').innerHTML;
function resetCapture(){
  amtStr = ''; renderAmt();
  $('#cap-party').value = ''; $('#cap-note').value = '';
  $('#capture-receipt').hidden = true;
  $('#sheet-capture .sheet-mid').hidden = false;
  $('#sheet-capture .keypad').hidden = false;
  $('#sheet-capture .accessory').hidden = false;
  const sb = $('#cap-save'); sb.innerHTML = SAVE_HTML; sb.disabled = false;
}

/* ═══════════ Capture → quiet completion ═══════════ */
let cash = 3477.50, recv = 2240.00, pay = 6650.00;
const YEST = { cash: 3180.00, recv: 2380.00, pay: 7150.00 };
const TYPE_AR = { sale:'بيع', collect:'قبض', expense:'مصروف', payment:'دفع', adjust:'تسوية' };

$('[data-act="save-entry"]').addEventListener('click', () => {
  const amt = parseAmt();
  if (amt <= 0) { toast('أدخل مبلغًا أولًا'); return; }
  const btn = $('#cap-save');
  btn.disabled = true; btn.setAttribute('aria-busy','true');
  btn.innerHTML = '<span class="mini-arc" aria-hidden="true"></span> جارٍ التسجيل…';
  setTimeout(() => {
    const type = $('.typeseg .is-active').dataset.ctype;
    const party = $('#cap-party').value.trim();
    const credit = type === 'sale' && party !== '';
    if (type === 'collect') { cash += amt; recv -= amt; }
    else if (type === 'sale') { credit ? recv += amt : cash += amt; }
    else if (type === 'payment') { cash -= amt; pay -= amt; }
    else if (type === 'expense') { cash -= amt; }
    else if (type === 'adjust') { cash += -amt; }
    updateBrief();
    insertTimelineRow(type, amt, party, credit);
    $('#sheet-capture .sheet-mid').hidden = true;
    $('#sheet-capture .keypad').hidden = true;
    $('#sheet-capture .accessory').hidden = true;
    const stateNote = offline ? 'بانتظار المزامنة — سيُرسل عند عودة الاتصال.' : 'متزامن الآن.';
    $('#receipt-sentence').innerHTML =
      `سُجّل ${TYPE_AR[type]} <bdi dir="ltr">${fmt2(amt)}</bdi> د.أ — النقد المتاح صار <bdi dir="ltr">${fmt2(Math.max(cash,0))}</bdi> د.أ`;
    $('#receipt-note').textContent = party ? `الجهة: ${party} · ${stateNote}` : stateNote;
    $('#capture-receipt').hidden = false;
  }, REDUCED ? 100 : 800);
});
$('[data-act="done-entry"]').addEventListener('click', () => { hideSheet('sheet-capture'); resetCapture(); });
$('[data-act="undo-entry"]').addEventListener('click', () => {
  const last = $('.timeline .tl-row.new-row');
  const amt = last ? parseFloat((last.querySelector('.amt bdi')||{}).textContent.replace(/,/g,'')) || 0 : 0;
  const type = last ? (last.dataset.ctype || 'sale') : 'sale';
  if (type === 'collect') { cash -= amt; recv += amt; }
  else if (type === 'sale') { /* credit sale: recv -= amt; cash unchanged */ }
  else { cash += amt; }
  if (last) last.remove();
  updateBrief();
  hideSheet('sheet-capture'); resetCapture();
  toast('تم التراجع — أُلغي القيد الأخير');
});
function deltaText(cur, yest){
  const d = Math.round((cur - yest) * 100) / 100;
  if (Math.abs(d) < 0.005) return 'كما هي عن أمس';
  return (d > 0 ? 'أعلى بـ ' : 'أخفض بـ ') + `<bdi dir="ltr">${fmt2(Math.abs(d))}</bdi>`;
}
function updateBrief(){
  $('.pb-hero bdi').textContent = fmt2(cash);
  $('.pb-delta').innerHTML = `${deltaText(cash, YEST.cash)} — قبضت <bdi dir="ltr">${fmt2(Math.max(cash - YEST.cash + 527.50, 0))}</bdi> وصرفت <bdi dir="ltr">527.50</bdi>.`;
  $('.cb-cash').innerHTML = `<bdi dir="ltr">${fmt2(cash)}</bdi> <i>د.أ</i>`;
  $('.pb-rows .pb-r:first-child .pb-v').innerHTML = `<bdi dir="ltr">${fmt2(Math.max(recv,0))}</bdi> <i>د.أ</i>`;
  $('.pb-rows .pb-r:last-child .pb-v').innerHTML = `<bdi dir="ltr">${fmt2(pay)}</bdi> <i>د.أ</i>`;
  const hero = $('.posblock');
  hero.classList.remove('hl'); void hero.offsetWidth; hero.classList.add('hl');
}
function insertTimelineRow(type, amt, party, credit){
  const tl = $('.timeline');
  const neg = (type === 'expense' || type === 'payment');
  const li = document.createElement('li');
  li.className = 'tl-row new-row hl';
  li.tabIndex = 0;
  li.dataset.nav = 'entry';
  li.dataset.ctype = type;
  li.innerHTML =
    `<span class="tl-time">الآن</span>
     <span class="tl-node ${offline ? 'queue' : ''}" aria-hidden="true"></span>
     <span class="tl-body"><span class="tl-t">${TYPE_AR[type]}${party ? ' — ' + party : ''}</span><span class="tl-s">${offline ? 'بانتظار المزامنة' : 'متزامن'}${credit ? ' — آجل' : ''}</span></span>
     <span class="amt ${neg ? 'neg' : 'pos'}"><bdi dir="ltr">${neg ? '−' : '+'}${fmt2(amt)}</bdi><span class="unit">د.أ</span></span>`;
  $$('[data-nav]', li).forEach(el => el.addEventListener('click', () => push('scr-entry', li)));
  tl.prepend(li);
}

/* collect sheet */
let collectCtx = { name:'محمد الخطيب' };
$$('[data-act="collect-sheet"]').forEach(b => b.addEventListener('click', () => {
  collectCtx = { name: $('#party-title') ? $('#party-title').textContent : 'محمد الخطيب' };
  $('#col-party').textContent = collectCtx.name;
  $('#col-hint').textContent = 'أدخل المبلغ المحصّل نقدًا';
  amtStr = ''; $('#col-amt').textContent = '0';
  openSheet('sheet-collect');
}));
$('[data-act="save-collect"]').addEventListener('click', () => {
  const amt = parseAmt();
  if (amt <= 0) { toast('أدخل مبلغ التحصيل'); return; }
  hideSheet('sheet-collect');
  cash += amt; recv = Math.max(0, recv - amt);
  updateBrief();
  insertTimelineRow('collect', amt, collectCtx.name, false);
  toast(`سُجّل تحصيل ${fmt2(amt)} د.أ من ${collectCtx.name} — النقد صار ${fmt2(cash)} د.أ`);
  amtStr = '';
});

/* ═══════════ Dialogs ═══════════ */
let openDlg = null;
function openDialog(id){
  openDlg = id;
  const w = document.getElementById(id);
  w.hidden = false;
  requestAnimationFrame(() => w.classList.add('show'));
}
function closeDialog(id){
  const w = document.getElementById(id);
  w.classList.remove('show');
  setTimeout(() => { w.hidden = true; }, REDUCED ? 0 : 200);
  if (openDlg === id) openDlg = null;
}
$$('[data-close-dialog]').forEach(b => b.addEventListener('click', () => closeDialog(b.closest('.dialog-wrap').id)));
$('[data-act="open-conflict"]').addEventListener('click', () => openDialog('dlg-conflict'));
function resolveConflict(which){
  closeDialog('dlg-conflict');
  const row = $('.atten .attn-row');
  if (row && row.dataset.act === 'open-conflict') {
    const val = which === 'local' ? '150.00' : '180.00';
    row.innerHTML = `<span class="st-ic st-synced" data-icon="check-fill"></span>
      <span class="subj"><span class="subj-t">تم حل التعارض — اعتُمد تحصيل أبو زياد <bdi dir="ltr">${val}</bdi> د.أ</span></span>
      <span class="st-word ok">متزامن</span>`;
    $('[data-icon]', row).innerHTML = ICONS['check-fill'];
    row.style.borderInlineStartColor = 'var(--brand-text)';
    row.style.background = 'var(--canvas)';
  }
  toast('تم حل التعارض وحُدّث السجل');
}
$('[data-act="resolve-local"]').addEventListener('click', () => resolveConflict('local'));
$('[data-act="resolve-remote"]').addEventListener('click', () => resolveConflict('remote'));

$('[data-act="open-correction"]').addEventListener('click', () => openDialog('dlg-correction'));
$('[data-act="do-correction"]').addEventListener('click', () => {
  closeDialog('dlg-correction');
  const sundayRows = $$('#reg-list .daysec')[1];
  if (sundayRows && !$('.reversed-row', sundayRows)) {
    const src = Array.from($$('.row', sundayRows)).find(r => r.textContent.includes('صيانة المولدة'));
    const li = document.createElement('li');
    li.className = 'row money-row reversed-row hl';
    li.tabIndex = 0;
    li.innerHTML = `<span class="time"><bdi dir="ltr">14:05</bdi></span>
      <span class="subj"><span class="subj-t">معكوس — عكس مصروف صيانة المولدة</span><span class="subj-s">تصحيح مرتبط بقيد <bdi dir="ltr">14:00</bdi> · متزامن</span></span>
      <span class="amt pos"><bdi dir="ltr">+60.00</bdi><span class="unit">د.أ</span></span>`;
    if (src) src.after(li);
    cash += 60; updateBrief();
  }
  toast('تم التصحيح — أُنشئ القيد المعكوس وربطه بالأصل');
});

/* ═══════════ Cash closing ═══════════ */
const EXPECTED = 3477.50;
$('#counted').addEventListener('input', () => {
  const v = parseFloat($('#counted').value.replace(/,/g,''));
  const el = $('#variance');
  if (isNaN(v)) { el.textContent = ''; el.className = 'variance'; return; }
  const d = Math.round((v - EXPECTED) * 100) / 100;
  if (Math.abs(d) < 0.005) { el.textContent = 'مطابق تمامًا'; el.className = 'variance v-zero'; }
  else if (d < 0) { el.innerHTML = `عجز <bdi dir="ltr">${fmt2(Math.abs(d))}</bdi> د.أ`; el.className = 'variance v-neg'; }
  else { el.innerHTML = `فائض <bdi dir="ltr">${fmt2(d)}</bdi> د.أ`; el.className = 'variance v-pos'; }
});
$('[data-act="confirm-closing"]').addEventListener('click', () => {
  const v = parseFloat($('#counted').value.replace(/,/g,''));
  if (isNaN(v)) { toast('أدخل النقد المعدود أولًا'); return; }
  const d = Math.round((v - EXPECTED) * 100) / 100;
  $('#dlgc-b').innerHTML = Math.abs(d) < 0.005
    ? 'الفرق مطابق تمامًا. لن تستطيع إضافة حركات لهذا اليوم بعد الإغلاق.'
    : `الفرق ${d < 0 ? 'عجز' : 'فائض'} <bdi dir="ltr">${fmt2(Math.abs(d))}</bdi> د.أ — سيُسجّل كتسوية. لن تستطيع إضافة حركات لهذا اليوم بعد الإغلاق.`;
  openDialog('dlg-close');
});
$('[data-act="do-closing"]').addEventListener('click', () => {
  closeDialog('dlg-close');
  $('#closing-open').hidden = true;
  $('#closing-done').hidden = false;
  toast('أُغلق صندوق اليوم — سُجّل الفرق كتسوية');
});
$('[data-act="correction-entry"]').addEventListener('click', () => {
  $$('.typeseg .segbtn').forEach(x => x.classList.toggle('is-active', x.dataset.ctype === 'adjust'));
  $('#cap-note').value = 'تصحيح إغلاق 07/09';
  openSheet('sheet-capture');
});

/* ═══════════ Sync states ═══════════ */
let offline = false;
const syncGlyph = $('#sync-glyph');
function setOffline(on){
  offline = on;
  $('#offline-banner').hidden = !on;
  $('#qbadge').hidden = !on;
  $('.iconbtn', syncGlyph).innerHTML = ICONS[on ? 'cloud-off' : 'check-double'];
  syncGlyph.style.color = on ? 'var(--ink3)' : '';
}
function runSync(){
  if (offline) { toast('لا مزامنة بدون اتصال — سجلّاتك محفوظة على الجهاز'); return; }
  syncGlyph.style.color = 'var(--accent-text)';
  $('.iconbtn', syncGlyph).innerHTML = ICONS.refresh;
  const svg = $('svg', syncGlyph); if (svg && !REDUCED) svg.style.animation = 'spin 1200ms linear infinite';
  setTimeout(() => {
    if (svg) svg.style.animation = '';
    setOffline(false);
    $('#error-banner').hidden = true;
    syncGlyph.style.color = '';
    toast('تمت المزامنة — كل السجلّات محفوظة');
  }, 1400);
}
syncGlyph.addEventListener('click', runSync);
$('[data-act="retry-sync"]').addEventListener('click', runSync);
$('[data-act="force-sync"]').addEventListener('click', runSync);

/* ═══════════ Toast ═══════════ */
let toastT = null;
function toast(msg){
  const t = $('#toast');
  t.textContent = msg;
  t.hidden = false;
  requestAnimationFrame(() => t.classList.add('show'));
  clearTimeout(toastT);
  toastT = setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.hidden = true, 250); }, 2600);
}

/* ═══════════ Simulated keyboard ═══════════ */
const kbd = $('#kbd-sim');
$$('input[type="text"], input[type="search"]').forEach(inp => {
  inp.addEventListener('focus', () => { if (inp.closest('.sheet')) { app.classList.add('kbd-on'); kbd.hidden = false; } });
  inp.addEventListener('blur', () => setTimeout(() => { if (!document.activeElement || !document.activeElement.closest('.sheet')) { app.classList.remove('kbd-on'); setTimeout(() => kbd.hidden = true, 240); } }, 80));
});
$('[data-act="kbd-done"]').addEventListener('click', () => {
  const f = document.activeElement; if (f && f.blur) f.blur();
  app.classList.remove('kbd-on'); setTimeout(() => kbd.hidden = true, 240);
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    if (openDlg) closeDialog(openDlg);
    else if (openSheetId) { const id = openSheetId; hideSheet(id); if (id === 'sheet-capture') resetCapture(); }
    else pop();
  }
});

/* ═══════════ Theme / dir ═══════════ */
function setTheme(mode){
  const dark = mode === 'dark' || (mode === 'auto' && matchMedia('(prefers-color-scheme: dark)').matches);
  app.dataset.theme = dark ? 'dark' : 'light';
  $$('.seg-block [data-theme-set]').forEach(b => b.classList.toggle('is-active', b.dataset.themeSet === mode));
}
$$('[data-theme-set]').forEach(b => b.addEventListener('click', () => setTheme(b.dataset.themeSet)));

/* ═══════════ Skeletons ═══════════ */
function skeletonOnce(tab){
  const sk = $('#' + tab + '-skeleton'), list = $('#' + tab + '-list');
  if (!sk || sk.dataset.done) return;
  sk.dataset.done = '1';
  list.hidden = true; sk.hidden = false;
  setTimeout(() => { sk.hidden = true; list.hidden = false; if (tab === 'people') filterPeople(); }, 450);
}
['people'].forEach(tab => {
  document.querySelector(`.tabbtn[data-tab="${tab}"]`).addEventListener('click', () => skeletonOnce(tab), { once:true });
});

/* misc */
$('[data-act="noop-endcap"]').addEventListener('click', () => toast('الأيام الأقدم — بيانات تجريبية فقط في هذه النسخة'));
$('[data-act="share-entry"]').addEventListener('click', () => toast('جهة المشاركة جاهزة في النسخة الكاملة'));
$('[data-act="assistant"]').addEventListener('click', () => toast('مساعد مايكرو قيد التطوير — سيفسّر تغيّرات النقد لاحقًا'));
$('[data-act="goto-people"]').addEventListener('click', () => switchTab('people'));
$('[data-act="goto-people-recv"]').addEventListener('click', () => { switchTab('people'); pseg='cust'; filterPeople(); });
$('[data-act="goto-people-pay"]').addEventListener('click', () => { switchTab('people'); pseg='supp'; $$('[data-pseg]').forEach(x => x.classList.toggle('is-active', x.dataset.pseg === 'supp')); filterPeople(); });

/* ═══════════ URL params ═══════════ */
const q = new URLSearchParams(location.search);
setTheme(q.get('theme') || 'auto');
if (q.get('width')) app.style.setProperty('--app-w', parseInt(q.get('width')) + 'px');
if (q.get('dir') === 'ltr') document.documentElement.dir = 'ltr';
if (q.get('demo') === 'offline') setOffline(true);
if (q.get('demo') === 'error') $('#error-banner').hidden = false;
if (q.get('demo') === 'collapsed') { briefBody.scrollTop = 200; compactbar.classList.add('on'); }
if (q.get('demo') === 'closed') { $('#closing-open').hidden = true; $('#closing-done').hidden = false; }
const deep = q.get('screen');
if (deep) {
  const id = screens['scr-' + deep] ? 'scr-' + deep : null;
  if (id) {
    const tabOf = Object.keys(ROOTS).find(t => ROOTS[t] === id);
    if (tabOf) { switchTab(tabOf); if (tabOf === 'people') skeletonOnce(tabOf); }
    else push(id);
  }
}

/* init */
renderTab(false);
