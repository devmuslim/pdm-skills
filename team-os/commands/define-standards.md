---
description: بناء DoD / DoR / AC مخصصة للفريق وحفظها ليقرأها agile-coach
argument-hint: [Framework + أنواع الأدوار في الفريق]
---

## الخطوة 1 — اجمع المعلومات

- "ما الـ Framework؟"
- "ما أدوار الفريق؟ (Dev/QA/BA/Designer)"
- "هل هناك Code Coverage requirement?"
- "كم Approval يحتاج الـ PR؟"
- "ما بيئات الـ Deploy المتاحة؟"

## الخطوة 2 — أنتج المعايير المخصصة

من skills/dod-dor-ac اجلب القوالب وخصّصها.

## الخطوة 3 — احفظ في Google Drive

```
team-os/[الفريق]/
├── dor.md    ← agile-coach يقرأه في assess-team
├── dod.md    ← agile-coach يقرأه في team-progress
└── ac-guide.md
```

## الخطوة 4 — أبلغ agile-coach

اكتب ملاحظة في نهاية الملف:
```
# للـ agile-coach
عند تقييم الفريق، تحقق من هذه المعايير:
DoR: [أهم 3 معايير]
DoD: [أهم 3 معايير]
```
