# Framework Config — إعداد نظام العمل حسب الـ Framework

## الهدف
عند اختيار Framework، يضبط الـ plugin كل شيء تلقائياً:
Ceremonies، أدوار، إيقاع العمل، ومقاييس النجاح.

---

## 🔵 Scrum

### الأدوار
| الدور | المسؤولية |
|-------|-----------|
| Product Owner | يملك الـ Backlog ويمثل العميل |
| Scrum Master | يحمي الفريق ويزيل العوائق |
| Development Team | يصمم وينفذ ويختبر |

### الإيقاع
```
Sprint Length:     2 أسبوع (مقترح) — قابل للتعديل 1-4
Planning:          أول يوم Sprint — ساعتان لكل أسبوع
Daily Standup:     كل يوم — 15 دقيقة
Review:            آخر يوم Sprint — ساعة
Retrospective:     آخر يوم Sprint — 90 دقيقة
Refinement:        منتصف Sprint — ساعة
```

### مقاييس النجاح
```
Velocity            → Story Points مكتملة لكل Sprint
Sprint Goal Achievement → هل حُقق هدف Sprint؟
Burndown Chart      → هل الفريق في المسار الصحيح؟
Escaped Defects     → Bugs اكتُشفت في Production
```

---

## 🟡 Kanban

### الأدوار
| الدور | المسؤولية |
|-------|-----------|
| Service Request Manager | يدير الـ Backlog والأولويات |
| Service Delivery Manager | يضمن تدفق العمل |
| Team Members | ينجزون المهام بحسب الأولوية |

### الإيقاع
```
Daily Standup:      كل يوم — 15 دقيقة (Walk the Board)
Flow Review:        أسبوعياً — 30 دقيقة
Replenishment:      أسبوعياً — 30 دقيقة (تعبئة الـ Backlog)
Retrospective:      كل أسبوعين — 60 دقيقة
```

### WIP Limits المقترحة
```
To Do:         لا حد
In Progress:   عدد أعضاء الفريق - 1
In Review:     عدد أعضاء الفريق ÷ 2
Done:          لا حد
```

### مقاييس النجاح
```
Lead Time       → من طلب المهمة حتى تسليمها
Cycle Time      → من بدء العمل حتى الانتهاء
Throughput      → مهام مكتملة لكل أسبوع
Flow Efficiency → وقت العمل الفعلي ÷ Lead Time
```

---

## 🟠 Scrumban

### متى تستخدمه؟
```
✅ فريق يريد مرونة Kanban مع هيكل Scrum
✅ مشاريع بها Urgent tasks متكررة
✅ فريق انتقل من Scrum ويريد التطور
```

### الأدوار
```
يحتفظ بـ: Product Owner + Scrum Master + Team
يضيف:    WIP Limits على الـ Board
```

### الإيقاع
```
Daily Standup:     كل يوم — 15 دقيقة
Planning:          عند وصول Backlog لحد معين (Trigger-based)
Retrospective:     كل أسبوعين — 60 دقيقة
Review:            عند اكتمال Features لا بالتاريخ
```

### مقاييس النجاح
```
مزيج من Scrum وKanban:
Throughput + Cycle Time (من Kanban)
Sprint Goal (من Scrum — اختياري)
```

---

## 🔴 SAFe (Scaled Agile Framework)

### متى تستخدمه؟
```
✅ منظمة كبيرة (3+ فرق تعمل على نفس المنتج)
✅ تنسيق عالي بين الفرق مطلوب
✅ PI Planning كل ربع سنة
```

### الأدوار الإضافية
| الدور | المسؤولية |
|-------|-----------|
| Release Train Engineer (RTE) | Scrum Master للـ ART |
| Product Manager | يملك Program Backlog |
| System Architect | القرارات التقنية عبر الفرق |
| Business Owner | يضمن القيمة التجارية |

### الإيقاع
```
PI Planning:        كل 10 Sprints — يومان
ART Sync:           أسبوعياً — 30 دقيقة
System Demo:        كل Sprint — 60 دقيقة
Inspect & Adapt:    نهاية PI — نصف يوم
Innovation Sprint:  Sprint أخير في كل PI
```

### مقاييس النجاح
```
PI Objectives Score  → هل حققنا أهداف الـ PI؟
Program Predictability → نسبة الـ Features المكتملة
Business Value       → تقييم Business Owners
ART Velocity         → مجموع Velocity كل الفرق
```

---

## اختيار الـ Framework المناسب

```
عدد الفريق 3-9    + مشروع محدد النطاق  → Scrum
عدد الفريق 3-9    + طلبات متدفقة       → Kanban
عدد الفريق 5-12   + مزيج من الاثنين    → Scrumban
عدد الفرق 3+      + منتج كبير موحد     → SAFe
```
