# 🏋️ agile-coach Plugin

Agile Coach ذكي — يقيّم الفريق، يبني خطط تطوير شخصية، وينظم جلسات تعليمية.

---

## الأوامر

| الأمر | الوصف |
|-------|-------|
| `/assess-team` | تقييم عضو أو الفريق كله حسب الدور |
| `/assess-workflow` | تقييم على workflow: BRD→Figma→Code→QA→Release |
| `/assess-framework` | تقييم على Kanban/Scrumban + الالتزام بالمواعيد |
| `/growth-plan` | خطة تطوير شخصية مبنية على بيانات Jira |
| `/learning-session` | تصميم جلسة تعليمية تفاعلية |
| `/team-challenge` | إطلاق تحدي أو مسابقة للفريق |
| `/team-progress` | تقرير تقدم شهري متكامل |

---

## التكاملات

```
agile-coach
    ├── Jira MCP          → Velocity, Cycle Time, Bugs لكل عضو
    ├── delivery-kpi      → Defect Rate, UAT Pass Rate
    ├── knowledge-base    → BRD linking كمؤشر فهم المتطلبات
    └── Google Drive      → حفظ التقييمات والخطط والتقارير
```

**يعمل بدون تكاملات** — لكن مع الربط يعطي نتائج مدعومة بالبيانات.

---

## Workflow مقترح للـ Agile Coach

```
الأسبوع 1:
/assess-team الفريق كله    ← تشخيص شامل

الأسبوع 2:
/growth-plan [كل عضو]      ← خطة شخصية لكل واحد

أسبوعياً:
/learning-session [موضوع]  ← جلسة تعليمية
/team-challenge جودة       ← تحدي تحفيزي

شهرياً:
/team-progress شهر X       ← تقرير التحسن بالأرقام
```

---

## مجلد Google Drive المقترح

```
📁 agile-coach/
├── 📁 assessments/      ← تقييمات الأفراد
├── 📁 growth-plans/     ← خطط التطوير الشخصية
└── 📁 progress-reports/ ← التقارير الشهرية
```
