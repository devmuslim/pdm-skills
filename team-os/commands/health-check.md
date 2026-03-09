---
description: فحص صحة الفريق — Spotify Squad Health Check + مؤشرات Jira
argument-hint: [اسم الفريق]
---

## الخطوة 1 — اجمع التقييمات

اسأل كل عضو أن يقيّم الـ 8 محاور: 🔴 / 🟡 / 🟢
من skills/team-health اجلب المحاور الكاملة.

## الخطوة 2 — اجلب مؤشرات Jira (إذا متاح)

- Velocity آخر 3 Sprints
- Bug Rate
- After-hours activity
- Completion Rate

## الخطوة 3 — أنتج تقرير الصحة

```
══════════════════════════════════════
🌡️ Team Health Check — [الفريق]
التاريخ: [X]
══════════════════════════════════════

المحور              | النتيجة | التغيير
Easy to Release    |  🟢/🟡/🔴 | ⬆️/⬇️/=
Suitable Process   |  🟢/🟡/🔴 |
Tech Quality       |  🟢/🟡/🔴 |
Value              |  🟢/🟡/🔴 |
Speed              |  🟢/🟡/🔴 |
Mission            |  🟢/🟡/🔴 |
Fun                |  🟢/🟡/🔴 |
Learning           |  🟢/🟡/🔴 |

🔴 يحتاج تدخل فوري:
[المحاور الحمراء + خطة محددة]

💡 توصية الـ Coach:
[خطوة واحدة هذا الأسبوع]
══════════════════════════════════════
```

احفظ في: `team-os/[الفريق]/health-checks/[تاريخ].md`
