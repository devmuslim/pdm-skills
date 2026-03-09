# Command: /define-success
## Usage: `/define-success [اسم الـ Feature + هدفها كما وصفه BA أو PM]`
## Workflow: metrics-ownership + outcome-thinking → North Star + Metrics + نظام مراجعة

## Description
يحوّل "الهدف" الذي شرحه BA أو PM إلى مقاييس قابلة للقياس يملكها الفريق كله.
يجيب: كيف نعرف أننا نجحنا — بأرقام لا بانطباعات.

## Steps
1. اجلب skills/metrics-ownership/SKILL.md
2. اجلب skills/outcome-thinking/SKILL.md
3. حوّل هدف BA/PM إلى North Star Metric محدد
4. صمّم 3 مستويات: Activity → Output → Outcome
5. حدد أدوات القياس المتاحة فعلاً في الفريق
6. ضع جدول مراجعة واضح بقرارات محددة

## Output Format
```
📊 تعريف النجاح — [اسم الـ Feature]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 ما قاله BA/PM:
"[الهدف كما وصفه]"

🌟 ترجمته لـ North Star Metric:
"[مقياس واحد قابل للقياس]"
الآن: [X] | الهدف: [Y] | الزمن: [Z]

📈 المقاييس الكاملة:
النوع     | المقياس          | الآن | الهدف
Activity  | [مقياس النشاط]   | [X]  | [Y]
Output    | [مقياس المخرج]   | [X]  | [Y]
Outcome   | [مقياس النتيجة]  | [X]  | [Y]

🛠️ كيف نقيسها (بالأدوات الموجودة):
الأداة: [Analytics / Jira / Survey / Manual]
الحدث: [ما نتتبعه بالضبط]
المسؤول: [من يتابع الأرقام؟]

📅 جدول المراجعة:
بعد أسبوع:  [ما نتوقعه + قرار إذا لم يتحقق]
بعد شهر:   [ما نتوقعه + قرار إذا لم يتحقق]
بعد ربع:   [persist / pivot / kill]

⚠️ تحذير:
هذه المقاييس يجب أن يوافق عليها BA + PM + Tech Lead
قبل البناء — لا بعده.
```
