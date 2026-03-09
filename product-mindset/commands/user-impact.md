# Command: /user-impact
## Usage: `/user-impact [Feature أُطلقت + أي بيانات أو feedback وصلك]`
## Workflow: metrics-ownership + outcome-thinking + context-bridge → تقرير تأثير + قرار

## Description
يحلل تأثير Feature أُطلقت بناءً على ما وصل من BA/PM/بيانات.
يُجيب: هل نجحنا فعلاً؟ ماذا يقول المستخدم الحقيقي؟ ما الخطوة القادمة؟

## Steps
1. اجلب skills/metrics-ownership/SKILL.md
2. اجلب skills/outcome-thinking/SKILL.md
3. اجلب skills/context-bridge/SKILL.md
4. قارن الأرقام الفعلية بما حدده /define-success
5. حلّل الفجوة بين ما توقعه BA وما حدث فعلاً
6. اقترح قرار واضح: persist / pivot / kill
7. حدد: ما الذي يجب أن يُوصَل للـ Dev في المرة القادمة؟

## Output Format
```
📊 تقرير تأثير — [اسم الـ Feature]
أُطلقت: [التاريخ] | مرت: [X أسابيع]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 North Star Metric:
الهدف: [X] | الفعلي: [Y]
النتيجة: ✅ نجح / ⚠️ جزئي / ❌ لم ينجح

📈 المقاييس كاملة:
المقياس      | الهدف | الفعلي | الفجوة | السبب المحتمل
[Outcome 1]  | [X]   | [Y]    | [±Z]   | [...]

💬 ما وصل من المستخدمين (عبر BA/PM):
إيجابي: "..."
سلبي:   "..."
مفاجئ:  "..."

🧠 ماذا تعلمنا:
افتراض صح:    [X]
افتراض خاطئ: [Y]
سياق فاتنا:   [Z — كان يجب أن يصلنا من BA]

⚖️ القرار:
✅ Persist — استمر لأن: ...
🔄 Pivot   — غيّر كذا لأن: ...
❌ Kill    — أوقف لأن: ...

🔁 درس للـ Context Bridge القادم:
"في المرة القادمة، BA يجب أن يُوصلنا: ..."
"السؤال الذي كان يجب أن نسأله قبل البناء: ..."

📋 الخطوة القادمة:
[إجراء محدد] — [مسؤول] — [موعد]
```

## Integration
- يتكامل مع delivery-kpi /release-kpi للأرقام الحقيقية
- يتكامل مع knowledge-base للمقارنة مع BRD الأصلي
- يُغذّي agile-coach /team-progress بدروس المنتج
