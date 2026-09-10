# Claude Mobile Visual Research — Source Register

**Artifact:** `claude-mobile-source-register.md`
**Date:** 2026-09-11 · **Coordinator consolidation of Agent 3's register + Agent 4's verification passes**

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. Register covers sources actually inspected during this study (September 2026). Store-listing metadata is volatile. Fetch failures are recorded as limitations, not as evidence of absence.

**Tiers:** T1 official primary · T2 direct observation / official captures · T3 secondary (triangulation only, never primary for exact values).
**Evidence types:** OBSERVED / MEASURED / DOCUMENTED / INFERRED / UNVERIFIED (per finding pulled from the source).

---

## 1. Anthropic / Claude official pages

| Source | URL / identifier | Tier | Date inspected / page date | What it proves | Limitations |
|---|---|---|---|---|---|
| Claude Android app announcement | https://claude.com/blog/android-app | T1 | fetched Sep 2026 (post dated 2024-07-16) | Android launch date; feature set (vision, sync); "works just like Claude on iOS and the web" | no UI visuals |
| Claude Code on the web announcement | https://claude.com/blog/claude-code-on-the-web | T1 | fetched (post dated 2025-10-20) | Code sessions on web + mobile app as client | mobile layout unspecified |
| Claude in EU | https://www.anthropic.com/news/claude-europe | T1 | fetched (dated 2024-05-14) | iOS app EU availability date | — |
| Claude 3.5 Sonnet announcement | https://www.anthropic.com/news/claude-3-5-sonnet | T1 | fetched (dated 2024-06-21) | iOS app as official distribution surface | — |
| Anthropic newsroom index | https://www.anthropic.com/news | T1 | fetched Sep 2026 | current official news hub | 2024 app-launch posts delisted |
| claude.com/download | https://claude.com/download | T1 | fetched | both store links; cross-platform positioning | — |
| Dead official slugs (checked) | anthropic.com/news/{claude-ios-app, claude-android, claude-app, claude-mobile-app, claude-voice-mode, claude-team-plan, new-claude-app, ios, mobile, …} | T1 (404 checks) | Sep 2026 | original launch posts removed → dates anchored via iTunes API + blog mirror | — |

## 2. Help Center (support.claude.com)

Sitemap inspected: 4,464 URLs, ~367 mobile-related, 13 locales. Articles fetched and mined (all T1, undated pages, fetched Sep 2026):

| Article | ID / URL slug | Proves |
|---|---|---|
| Install Claude for iOS | /en/articles/9266462 | iOS 18+/iPadOS 18+ requirement |
| Install Claude for Android | /en/articles/9612887 | Android 8.0+ requirement |
| Use voice mode | /en/articles/11101966 | voice icon (sound wave next to mic); hands-free/push-to-talk; voice settings bottom-left; model selector in voice mode |
| Use dictation on Claude mobile | /en/articles/10065434 | mic on right side of input; initials top-right profile entry; 12 dictation languages |
| Change the model, effort, and thinking settings | /en/articles/8664678 | model menu next to send button; effort levels; thinking toggle + timer indicator + expandable section; "More models" |
| Upload files to Claude | /en/articles/8241126 | "+" attachments; file types/limits; "Uploaded file is too large" |
| Customizing your appearance settings | /en/articles/8887527 | Light / Match System / Dark; font options incl. Dyslexic Friendly |
| Delete or rename a conversation | /en/articles/8230524 | "⋯"/"⋮" top-right; iOS touch-and-hold; Android checklist multi-select |
| Share and unshare chats | /en/articles/10593882 | Share upper-right; visibility dropdown; "No shared content found" empty state |
| Use incognito chats | /en/articles/12260368 | ghost icon upper-right; "Incognito chat" label + black border; "x" close |
| Chat search & memory | /en/articles/11817273 | memory toggles; notice above message box |
| Use Claude Cowork on web, desktop and mobile | /en/articles/15520349 | "Cowork" bottom-left of message box; mobile capability matrix |
| Assign tasks from anywhere (Dispatch) | /en/articles/13947068 | Dispatch persistent thread; push notifications |
| Use interactive connectors | /en/articles/13454812 | inline cards vs fullscreen view; input remains available |
| Use Claude with iOS apps / Android integrations | /en/articles/11869619 + /11869629 | device-action cards in conversation |
| iOS widgets/intents/controls; Android widget | /en/articles/10263469 + /10534883 | widget buttons; spark icon as chat branding |
| Open the Claude mobile app with a link | /en/articles/14898120 | claude://code deep links; Code tab on session list; new-session composer params |
| Release notes | /en/articles/12138966 | feature timeline incl. Cowork mobile, inline visuals, Dispatch |
| Troubleshoot error messages | /en/articles/12466728 | verbatim limit/capacity/login error strings |
| What are artifacts | /en/articles/9487310 | artifact window behaviors; "Try fixing with Claude" |
| Claude Code on the web | /en/articles/12618689 | Code sessions surface description |

## 3. Claude Code official documentation (code.claude.com / docs.claude.com)

| Page | URL | Page lastmod | Proves |
|---|---|---|---|
| Claude Code on mobile | https://code.claude.com/docs/en/mobile | 2026-08-22 | "Tap Code in the app's navigation"; app as client; mode dropdown contents (cloud: Accept edits/Plan/Auto; RC: Manual/Accept edits/Plan); /mcp, /config behavior; iPad note |
| Remote Control | https://code.claude.com/docs/en/remote-control | 2026-09-10 | computer icon + green status dot; offline within seconds; diff pane; dialog persistence vs ~5-min expiry; push toggles; attachments behavior; Trusted Devices |
| Claude Code on the web | https://code.claude.com/docs/en/claude-code-on-the-web | 2026-09-10 | diff indicator "+42 -18"; session sidebar; mobile auto-fix PR wording |
| What's new 2026-w32 | https://code.claude.com/docs/en/whats-new/2026-w32 | fetched | self-hosted env selection; auto-mode status bar |

## 4. Store listings & metadata

| Source | Identifier | Tier | Proves | Limitations |
|---|---|---|---|---|
| iTunes Lookup API | https://itunes.apple.com/lookup?id=6473753684 | T1 | identity (Anthropic PBC), first release 2024-05-01, minOS 18.0, official screenshot URLs | metadata volatile (verification re-fetch drifted version/ratings/size — cite "as of Sept 2026") |
| App Store listing | https://apps.apple.com/us/app/claude-by-anthropic/id6473753684 | T1 | listing name/developer/OS; 9 iPhone + 9 iPad official captures (T2) | marketing composites, not live screens; 17+/18+ rating conflict |
| Google Play listing | https://play.google.com/store/apps/details?id=com.anthropic.claude | T1 | package id; developer; Android 8.0+; version; tagline; official imagery (T2) | inline-JS data blobs |
| App trailers (Apple CDN) | apptrailers.itunes.apple.com …m3u8 ×2 | T1-hosted | existence of official video creative | not analyzed (video out of scope) |

## 5. Official public CSS (design-token evidence)

| Source | Artifact | Tier | Proves |
|---|---|---|---|
| claude.ai landing CSS | raw/a2-claude-brand.css (`claude-brand.shared.*.min.css`) | T1 (publicly inspectable) | gray-000…1000 ramp; clay #D97757 / clay-interactive #C96442; error #B53333; switch #2C84DB; secondary hues; role mapping (background/foreground/border/button tiers); Anthropic Sans/Serif/Mono variable families |
| anthropic.com CSS | raw/a2-ant-brand.css | T1 (publicly inspectable) | same ramp as ivory/slate/cloud aliases; site accent #C6613F; kraft/manilla; alpha-tint pattern; Tiempos Text |

## 6. Samsung official sources (device-frame harness)

| Source | URL | Tier | Proves |
|---|---|---|---|
| Samsung UK S25 specs | samsung.com/uk/smartphones/galaxy-s25/specs/ | T1 | S25: 6.2"/6.0" display, 2340×1080, 146.9×70.5×7.2 mm, 162 g, Dynamic AMOLED 2X 120 Hz, 12MP F2.2 front |
| Samsung FR S25 specs | samsung.com/fr/smartphones/galaxy-s25/specs/ | T1 | independent regional cross-check (identical) |
| Samsung UK S25 Ultra specs | samsung.com/uk/smartphones/galaxy-s25-ultra/specs/ | T1 | Ultra: 6.9"/6.8", 3120×1440 QHD+, 162.8×77.6×8.2 mm, 218 g |
| Samsung FR S25 Ultra specs | samsung.com/fr/smartphones/galaxy-s25-ultra/specs/ | T1 | cross-check (identical) |
| Samsung Global Newsroom press release | news.samsung.com/global/samsung-galaxy-s25-series-sets-the-standard-of-ai-phone-as-a-true-ai-companion | T1 | full 3-model table (dated 2025-01-23 KST / Jan 22 US); S25+ values (158.4×75.8×7.3 mm, 190 g, 6.7"); punch-hole footnote; launch OS |
| Samsung Mobile Press S25+ specs | samsungmobilepress.com/media-assets/galaxy-s25-plus?tab=specs | T1 (search snippet) | S25+ "6.7-inch QHD+ Dynamic AMOLED 2X, 120Hz"; "75.8 x 158.4 x 7.3mm, 190g" |
| Samsung Mobile Press worldwide-arrival release | (slug unresolved; snippet only) | T1-snippet + T3 | Feb 7, 2025 retail release (with PhoneArena corroboration) |

Known gaps: S25+ exact px (3120×1440) exists only in T3 sources (GSMArena/PhoneArena agree) — official pages print only "QHD+" class; standalone S25+ regional spec pages are retired (404/error shells globally).

## 7. Official captures used for measurement (T2)

Nine iPhone App Store screenshots 392×696 (mzstatic URLs registered in Agent 1 notes §8; files in `evidence-notes/raw/shots/`): Useful_answers, Voice_Mode (photographic — excluded from tokens), Tools (photographic — excluded), Build_App, Ideas_&_Files, Dispatch (photographic — excluded), Code_Review, Write, End_Card; plus the Play hero tile (brand mark). Analysis artifacts: VLM JSONs vlm-01…10; pixel samples `raw/shots/pixel-samples.txt`; sampling scripts in `scripts/`.

## 8. Verification record (Agent 4, phase 1)

Re-fetched and byte-compared during verification: code.claude.com/docs/en/mobile (Code tab + mode dropdown contents — identical), support article 8664678 (model menu wording — identical), iTunes API (identity stable; volatile fields drifted), staged CSS tokens (all reproduced), pixel measurements (all reproduced: `#d9795a`, bubbles `#d5d5d1–#d7d6cf`, composer `#fafafa`, dark surfaces, `#6e6b96`, blue dots). Samsung live re-fetch failed during verification (page_reader 502/504-degraded) — Samsung values rely on the staged dual-region + newsroom fetches (acceptable per protocol; noted as limitation). Rejected during verification: "user bubbles LEFT-aligned" (near-symmetric margins 52/63 and 54/59 px; independent VLM read right-aligned) → alignment UNVERIFIED.

## 9. Rejected / downgraded sources (not primary evidence)

1. GSMArena / PhoneArena — T3 device databases; used only to triangulate S25+ px and the Feb 7 release date; never for app visuals.
2. techradar.com — aggregator; not used for values.
3. galaxys25ultramanual.com — fan site with demonstrable errors (wrong SoC generation, wrong display size) — rejected outright.
4. Wikipedia (Samsung Galaxy S25) — tertiary; label drift ("Dynamic LTPO AMOLED 2X" vs official "Dynamic AMOLED 2X").
5. Samsung community forums, third-party retailer listings — user-generated / non-official.
6. Mashable hands-on and similar press coverage — consulted only to locate official sources; no visual values taken.
7. Unsourced color galleries / social posts — none encountered that claimed token authority; category rejected by policy.

## 10. Access limitations summary

No direct app observation (no authorized device/session in this environment) — T2 limited to official marketing captures. Samsung US spec pages retired; samsungmobilepress product pages render client-side only; news.samsung.com old slug 404/Akamai-blocked; page_reader intermittently 502/504 on heavy Samsung pages. Original May 2024 iOS announcement post removed (date anchored via iTunes API + mirrors). Store metadata volatile. These are environment limitations, not negative evidence.
