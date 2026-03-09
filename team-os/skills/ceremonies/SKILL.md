# Ceremonies — الاجتماعات لكل Framework

---

## 🔵 Scrum Ceremonies

### 1. Sprint Planning
```
متى:      أول يوم Sprint
المدة:    ساعتان لكل أسبوع (Sprint أسبوعين = 4 ساعات)
من يحضر: PO + SM + الفريق كله
الهدف:   الاتفاق على Sprint Goal وما سيُنجز

الأجندة:
├── [15 دق] PO يعرض أولويات Backlog
├── [15 دق] الفريق يسأل ويوضح
├── [60 دق] الفريق يختار Stories ويقدّر
├── [20 دق] تقسيم Stories لـ Tasks
└── [10 دق] تأكيد Sprint Goal

Anti-patterns:
❌ PO يملي على الفريق ما سيأخذه
❌ لا يوجد Sprint Goal واضح
❌ الفريق يأخذ أكثر من طاقته
❌ Stories غير مكتملة الـ DoR
```

### 2. Daily Standup
```
متى:      كل يوم — نفس الوقت
المدة:    15 دقيقة بالضبط
من يحضر: الفريق (SM يسهل — PO اختياري)
الهدف:   مزامنة + اكتشاف العوائق

3 أسئلة:
1. ماذا أنجزت أمس؟
2. ماذا سأنجز اليوم؟
3. هل هناك عائق؟

النموذج المتقدم (Walk the Board):
← ابدأ من Done باتجاه To Do
← ركّز على المهام لا الأشخاص
← أي نقاش يُكمل بعد الـ Standup

Anti-patterns:
❌ تقرير للمدير لا تنسيق الفريق
❌ نقاشات تقنية مطولة
❌ أشخاص لا يحضرون أو يتأخرون
❌ تجاوز الـ 15 دقيقة
```

### 3. Sprint Review
```
متى:      آخر يوم Sprint
المدة:    ساعة لكل أسبوع Sprint
من يحضر: الفريق + PO + Stakeholders
الهدف:   عرض ما أُنجز + جمع Feedback

الأجندة:
├── [10 دق] Sprint Goal — هل تحقق؟
├── [30 دق] Demo للـ Stories المكتملة
├── [15 دق] Feedback من Stakeholders
└── [5 دق] تحديث Backlog بناءً على Feedback

Anti-patterns:
❌ عرض Slides بدلاً من Demo حقيقي
❌ Stakeholders لا يُدعون
❌ مناقشة ما لم يكتمل فقط
❌ لا يوجد Feedback حقيقي
```

### 4. Sprint Retrospective
```
متى:      آخر يوم Sprint (بعد Review)
المدة:    90 دقيقة
من يحضر: الفريق + SM (بدون PO أو Management)
الهدف:   تحسين طريقة العمل

نماذج الـ Retro:

1. Start / Stop / Continue
   Start:    ماذا نبدأ؟
   Stop:     ماذا نوقف؟
   Continue: ماذا نكمل؟

2. 4Ls
   Liked:    ما أعجبنا
   Learned:  ما تعلمنا
   Lacked:   ما نقص
   Longed for: ما نتمنى

3. Sailboat
   Wind:    ما يسرّعنا
   Anchors: ما يبطئنا
   Rocks:   المخاطر القادمة
   Island:  هدفنا

الأجندة:
├── [5 دق]  Set the Stage — تهيئة الجو الآمن
├── [15 دق] جمع البيانات — كل شخص يكتب
├── [15 دق] تجميع الأفكار المتشابهة
├── [20 دق] تحديد الأولويات بالتصويت
├── [25 دق] Action Items — من يفعل ماذا؟
└── [10 دق] مراجعة Action Items السابقة

Anti-patterns:
❌ لا Action Items محددة
❌ نفس المشاكل تتكرر كل Retro
❌ Management حاضر — الفريق لا يصارح
❌ Retro فرصة للشكوى لا للتحسين
```

### 5. Backlog Refinement
```
متى:      منتصف Sprint
المدة:    ساعة (لا تزيد عن 10% من Sprint)
من يحضر: PO + SM + الفريق (Three Amigos مهم)
الهدف:   تجهيز Stories للـ Sprint القادم

الأجندة:
├── [10 دق] PO يقدم Stories الأولوية
├── [30 دق] مناقشة وتوضيح كل Story
│           ← هل AC مكتملة؟
│           ← هل التبعيات واضحة؟
│           ← هل DoR محققة؟
├── [15 دق] تقدير Story Points
└── [5 دق]  تأكيد الـ Stories الجاهزة للـ Sprint

Anti-patterns:
❌ Stories تدخل Sprint بدون Refinement
❌ PO يتحدث فقط والفريق صامت
❌ لا يوجد AC واضحة
❌ التقدير بالساعات لا Story Points
```

---

## 🟡 Kanban Ceremonies

### 1. Daily Standup (Walk the Board)
```
متى:      كل يوم — نفس الوقت
المدة:    15 دقيقة
الفرق عن Scrum: نبدأ من Done ونمشي للـ To Do

الأسئلة:
1. هل هناك مهام عالقة؟ (Blocked)
2. هل WIP Limit ممتلئ في أي عمود؟
3. ما المهمة الأقرب للإنجاز؟

التركيز: على الـ Board لا الأشخاص
```

### 2. Flow Review (أسبوعياً)
```
المدة:    30-45 دقيقة
الهدف:   تحليل التدفق وتحسينه

المقاييس المراجعة:
├── Cycle Time — هل تحسّن؟
├── Throughput — كم مهمة أكملنا؟
├── WIP — هل نحترم الحدود؟
├── Blocked Items — ما الأسباب؟
└── Flow Efficiency — كم % وقت عمل فعلي؟
```

### 3. Replenishment Meeting (أسبوعياً)
```
المدة:    30 دقيقة
الهدف:   تعبئة الـ Backlog بأولويات جديدة

الأجندة:
├── مراجعة Backlog الحالي
├── إضافة وترتيب Items الجديدة
└── التأكد من WIP Limits
```

### 4. Kanban Retrospective
```
المدة:    60 دقيقة كل أسبوعين
الفرق:   مبنية على بيانات Flow لا على Sprint

أسئلة خاصة بـ Kanban:
- ما الـ Bottleneck الأكثر تكراراً؟
- هل WIP Limits مناسبة؟
- أي Items أخذت أطول من المتوقع؟
- هل يمكن تحسين أي Step في الـ Flow؟
```

---

## 🟠 Scrumban Ceremonies

```
يحتفظ من Scrum:
✅ Daily Standup (Walk the Board)
✅ Retrospective (كل أسبوعين)
✅ Sprint Review (اختياري — عند اكتمال Features)

يضيف من Kanban:
✅ Flow Review أسبوعياً
✅ Trigger-based Planning (لا Fixed Sprint Planning)
   → يُخطط عندما يصل Backlog لـ X items فقط

يتخلى عن:
❌ Fixed Sprint Commitment
❌ Velocity كمقياس رئيسي
```

---

## 🔴 SAFe Ceremonies

### PI Planning (كل 10 Sprints)
```
المدة:    يومان كاملان
من يحضر: كل الفرق + Management + Stakeholders
الهدف:   تنسيق خطة الـ Program Increment كله

اليوم 1:
├── Business Context (CEO/CPO)
├── Product/Solution Vision
├── Architecture Vision
├── Team Breakouts (دورة 1)
└── Management Review

اليوم 2:
├── Team Breakouts (دورة 2)
├── Risk Identification (ROAM)
│   Resolved / Owned / Accepted / Mitigated
├── Final Plan Review
└── Confidence Vote (1-5 أصابع)
```

### ART Sync (أسبوعياً)
```
المدة:    30 دقيقة
من يحضر: Scrum Masters + RTEs + Tech Leads
الهدف:   تنسيق التبعيات بين الفرق
```

### System Demo (كل Sprint)
```
المدة:    60 دقيقة
الهدف:   Demo متكامل لكل ما أنجزته فرق الـ ART
الفرق:   يجمع كل الفرق — ليس فريقاً واحداً
```

### Inspect & Adapt (نهاية PI)
```
المدة:    نصف يوم
3 أجزاء:
1. PI System Demo
2. Quantitative Measurement (قياس الأداء)
3. Problem-Solving Workshop (حل المشاكل جذرياً)
```
