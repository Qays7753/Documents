# Screen Architecture and Hierarchy

## Global shell

### Compact top zone

- Right: Micro logo/mark.
- Left: النقل والتوصيل and Ask Micro.
- Logo opens a vertical menu containing account, project information, settings, protection, and related account controls.
- Account settings remain visible even when setup is incomplete.
- No traditional oversized top app bar.

### Bottom navigation

1. مشروعي الآن
2. العمل
3. المالية
4. أدواتي
5. السوق

Active state must be more than a subtle color change. It may use controlled fill, weight, container, or shape while preserving one icon family.

## 1. مشروعي الآن

### Required order

1. Compact top zone.
2. Project context: project name and relevant date/period.
3. Business Status Hero: the answer to “كيف وضعي؟”.
4. Micro Signal: one priority, reason, and next action.
5. Quick Action Bar: بيع، مصروف، طلب، تحصيل، المزيد.
6. Today summary: sales, result state, cash context.
7. Exposure summary: لي عند العملاء، عليّ للموردين، pending commitments.
8. Work attention: delayed order, due collection, missing cost, or “everything under control”.
9. Recent activity: maximum three to five items plus full record link.

### Rules

- Do not create six equal KPI cards.
- One dominant status answer; supporting figures are grouped.
- The primary action must be visible in the initial viewport at 390×844.
- Incomplete result must visually compete with complete profit; it cannot be a faint caption.
- The hero must not claim that sales alone equal business health.

## 2. العمل

### Required order

1. Work context and search/filter entry.
2. Current priority.
3. Active orders.
4. Delayed or blocked orders.
5. Upcoming appointments.
6. Recently completed work.

### Required order-state model

- اتفاق
- تنفيذ
- جاهز
- تم التسليم
- متأخر or blocked as an exception state

The designer may propose a step rail, segmented progress, or another accessible state pattern. Horizontal overflow may not hide essential status or actions.

## 3. المالية

### Required order

1. Financial-result summary with period and completeness.
2. Cash position.
3. Customer amounts due.
4. Supplier amounts due.
5. Owner money and other obligations when relevant.
6. Insights or exceptions.
7. Links to detailed records and period summary.

### Rules

- Finance is calmer than home.
- Use rows and grouped values before grids of decorative cards.
- Every total must open to its source or clearly indicate that drill-down exists.
- Financial positive and system success are different roles.
- Sales, collected cash, and result must never share one ambiguous label.

## 4. أدواتي

Group by user goal, not technical feature name:

- الحماية: PIN, lock, privacy.
- بياناتي: export, import, backup status.
- أدوات المشروع: calculator, references, inventory activation, checks.
- الحساب والمشروع: account, project data, settings.

The screen may use modular color grouping, but must remain less expressive than home and work.

## 5. السوق

The current state is a truthful future-state promise, not a fake marketplace.

Required content:

- What will be possible.
- What is not available now.
- Optional interest/notification action only if product scope supports it.

Market can use the highest visual expression in the future, but current “coming soon” design must not imply operational availability.

## Contextual screen: منتجاتي وخدماتي

- Reachable from home, work, and relevant forms.
- Search and filtering for product/service type.
- Reference data does not silently imply inventory tracking.
- The screen remains contextual and does not alter bottom navigation.

## Forms and sheets

- Bottom sheet or full-screen form according to task length.
- Label remains visible after input.
- Amount is visually dominant.
- Impact preview appears before financial commitment when meaningful.
- Save button stays reachable with keyboard and safe areas.
- Unsaved-data warning appears only when actual unsaved input exists.
- On success: close or transition into a success state; do not retain stale values.

## Responsive checkpoints

- 320px: narrow Android/older device.
- 360px: common Android.
- 390px: primary concept viewport.
- 430px: large phone.
- 200% text resize must preserve tasks without horizontal page scrolling.

