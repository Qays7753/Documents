# Micro Design Direction Brief V1

## 1. Product purpose

Micro is an Arabic financial and operational system for home-based, micro, and small businesses in Jordan. It helps owners record and understand sales, expenses, orders, customers, cash, wallets, collection, debts, suppliers, purchases, products, services, inventory, and business results according to data completeness.

Micro must help a non-accountant move from scattered memory, WhatsApp conversations, cash, notebooks, and delivery follow-up toward a truthful, understandable view of the business.

## 2. Primary user contract

Design first for an owner who:

- Uses a phone as the primary device.
- Understands البيع، المصروف، الكاش، الدين، العربون، الطلب and التحصيل.
- Does not reliably distinguish sales, collected cash, and profit.
- May use WhatsApp and Instagram confidently but distrust financial software.
- Works while interrupted, moving, serving customers, cooking, producing, or delivering.
- Needs large, obvious actions and direct language.
- Wants depth when needed but not on first view.

When beginner and advanced needs conflict, preserve beginner task success and reveal advanced depth progressively.

## 3. Core jobs to be done

1. أعرف وضع مشروعي الآن.
2. أعرف إن كنت ربحانًا أو خسرانًا، أو لماذا لا يمكن حساب النتيجة بعد.
3. أسجل بيعًا أو مصروفًا أو طلبًا بسرعة.
4. أعرف أين الكاش.
5. أعرف من عليه لي وماذا عليّ.
6. أتابع الطلبات والمواعيد والتأخير.
7. أفهم ماذا تغيّر بعد كل عملية.
8. أعرف الإجراء التالي دون أن أكون محاسبًا.

## 4. Psychological contract

Micro should create **agency**, not entertainment. The desired feeling is “أنا مسيطر وفاهم”، not “التطبيق جميل” alone.

| Context | Desired feeling | Target energy |
|---|---|---:|
| Open home | Awareness and control | 7/10 |
| Record an operation | Speed and focus | 8/10 |
| Review finance | Calm analysis | 4/10 |
| Debt or delay | Attention without panic | 6/10 |
| Successful save | Brief accomplishment and trust | 7/10 |
| Error recovery | Clarity and safety | 5/10 |
| Empty state | Encouragement and clear start | 6/10 |

## 5. Brand personality

Micro is:

- **Alert:** notices what matters.
- **Truthful:** never invents certainty.
- **Capable:** feels like a serious operating system.
- **Warm:** speaks to the owner without institutional coldness.
- **Decisive:** turns information into a next action.

Micro is not:

- Childish, gamified, or celebratory.
- A cold bank dashboard.
- A dense ERP.
- A beige digital notebook.
- A generic SaaS template.
- A chatbot personality.
- A collection of equally weighted cards.

## 6. Direction statement

### Bold Modular Micro

A vivid but disciplined financial operating interface. Strong modular color fields create orientation, priority, and momentum. Financial reading surfaces remain controlled. The visual system changes energy according to the task while preserving one coherent product identity.

Direction C leads:

- Stronger color blocking.
- Higher module recognition.
- More expressive status and progress.
- Greater perceived interactivity.
- A clear identity without depending on the logo.

Direction A supports:

- Warmth.
- Human proximity.
- Plain language.
- Comfort for small-business owners.

Direction B supports:

- Numeric discipline.
- Clean financial surfaces.
- Trust and traceability.
- Reduced noise in records and analysis.

## 7. Experience principles

1. Status before features.
2. One dominant answer before supporting figures.
3. Every important number has a meaning, state, source, and period.
4. Every problem ends with one relevant action.
5. Color communicates; it never merely decorates.
6. Strong energy at decision and action points; quiet energy during analysis.
7. A successful operation visibly updates its destination.
8. Incomplete is a first-class state, not an error or zero.
9. Arabic RTL is structural, not translated decoration.
10. Do not make every item a card.

## 8. Signature behavior: Micro Signal

The primary candidate for Micro’s functional signature is a repeated three-part structure:

1. **Status:** What is happening?
2. **Reason:** Why is it happening or what is missing?
3. **Action:** What should the owner do next?

Examples:

> النتيجة غير مكتملة  
> ينقص تسجيل تكلفة عمليتي بيع  
> **أكمل التكلفة**

> عندك 3 طلبات تحتاج انتباهًا  
> أحدها تجاوز موعد التسليم  
> **راجع الطلبات**

The designer must explore a recognizable visual grammar for Micro Signal without turning it into a decorative banner repeated everywhere.

## 9. Financial-result model

Use one stable component family with four explicit states:

- Complete positive result.
- Complete negative result.
- Incomplete result.
- No activity yet.

No state may rely on color alone. “Profit” is used only when the required data is complete. Incomplete results show the missing cause and a completion action.

## 10. Color strategy

Use functional layers:

- Brand Warm: identity and action energy.
- Trust Blue: information, navigation, active context, and system confidence.
- Positive Green: positive financial result only.
- Attention Amber: incomplete data or attention.
- Negative Red: negative result, danger, or error with explicit labels.
- Warm Neutral: comfort and background support.
- Clean Surface: reading and financial detail.
- Dark Ink: primary text, numbers, and high-commitment actions.

Do not finalize hex values until concept screens are reviewed. All proposed pairs must include measured contrast.

## 11. Interaction strategy

- Use a visible, labeled Quick Action Bar for frequent operations.
- Use contextual actions inside Micro Signals and owned screens.
- Avoid duplicating the same persistent action in a FAB and a bar.
- Show press feedback immediately.
- After save, show amount, destination, reference, and changed metric.
- Avoid count-up delays, confetti, bounce, and unnecessary celebration.

## 12. Success criteria

A successful direction lets a target user:

- Identify business status within five seconds.
- Locate the first useful action without instruction.
- Distinguish sales, cash, debt, and result.
- Understand incomplete data without interpreting it as loss or zero.
- Feel that the product is active and modern without feeling noisy.
- Trust the figures and understand what changed after a transaction.

## 13. Scope of the visual exploration

The visual designer produces C1, C2, and C3 using the same content, layouts, viewport, and state fixtures. No direction may improve its content or information architecture to appear stronger than the others.

## 14. Non-goals

- Final production design system.
- Rewriting product scope.
- Adding dashboard metrics without evidence.
- Redesigning the navigation model.
- Designing market or delivery product logic beyond representative visual states.
- Repository implementation.

