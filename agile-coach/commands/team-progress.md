---
description: تقرير تقدم الفريق الشهري — يجمع Jira + delivery-kpi + تقييمات Drive
argument-hint: [شهر 1 / شهر 2 / شهر 3]
---

## الخطوة 0 — اجلب البيانات من المصادر الثلاثة

### من Jira:
```
- Team Velocity هذا الشهر vs الشهر الماضي
- Sprint Completion Rate
- Cycle Time متوسط الفريق
- Total Bugs هذا الشهر
- Blocked Time إجمالي
```

### من delivery-kpi (إذا شُغّل /release-kpi):
```
- Defect Rate آخر إصدار
- UAT Pass Rate
- On-Time Delivery
- BRD Coverage
```

### من Google Drive:
```
- تقييمات الشهر الماضي في agile-coach/assessments/
- خطط التطوير الشخصية في agile-coach/growth-plans/
- تقارير الأشهر السابقة في agile-coach/progress-reports/
```

---

## أنتج التقرير المتكامل

```
══════════════════════════════════════════════
📈 تقرير تقدم الفريق — [الشهر]
══════════════════════════════════════════════

🌡️ مستوى الفريق العام
الشهر الماضي: X/50 → هذا الشهر: Y/50 | +Z نقطة

📊 مؤشرات Jira الحقيقية
├── Velocity:        X pts (+/- Y% عن الشهر الماضي)
├── Completion Rate: X% (الهدف > 85%)
├── Cycle Time:      X أيام (الهدف < 5)
└── Bug Rate:        X% (الهدف < 5%)

🎯 مؤشرات delivery-kpi (آخر إصدار)
├── UAT Pass Rate:   X%
├── On-Time:         ✅/❌
└── BRD Coverage:    X%

👥 تقدم الأفراد
[اسم] | كان X/25 → صار Y/25 | +Z | [أبرز تحسن]
[اسم] | كان X/25 → صار Y/25 | ثابت | [يحتاج دعم]

🏆 نجم الشهر
[الاسم] — [سبب محدد مدعوم بالأرقام]

⚠️ تحتاج تدخل
[الاسم أو المحور] — [المؤشر + الخطة]

🎯 هدف الشهر القادم (رقم واحد محدد)
[مثال: رفع Completion Rate من 75% إلى 85%]

💡 توصية الـ Coach
[رسالة تحفيزية + خطوة عملية واحدة]
══════════════════════════════════════════════
```

## الخطوة الأخيرة — احفظ في Google Drive
احفظ في: `agile-coach/progress-reports/month-[X]-report.yaml`
