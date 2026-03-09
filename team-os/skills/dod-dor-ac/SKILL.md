# DoD / DoR / AC — معايير الجودة والجاهزية

---

## 📥 Definition of Ready (DoR) — متى نبدأ؟

Story جاهزة للـ Sprint عندما تحقق كل هذا:

### المعايير الأساسية
```
✅ العنوان واضح ومفهوم
✅ الوصف يجيب: من؟ ماذا يريد؟ لماذا؟
✅ Acceptance Criteria مكتوبة وواضحة
✅ مقدّرة بـ Story Points (أو T-Shirt Size)
✅ التبعيات محددة (داخلية وخارجية)
✅ Mockup / Figma متاح (إذا كانت UI Story)
✅ لا تعارض مع BRD أو متطلبات أخرى
✅ حجمها قابل للإنجاز في Sprint واحد
```

### DoR حسب الـ Framework
```
Scrum:    Story يجب أن تحقق DoR قبل Sprint Planning
Kanban:   Item يجب أن يحقق DoR قبل دخول "In Progress"
Scrumban: نفس Kanban
SAFe:     Feature تحقق DoR قبل PI — Story قبل Sprint
```

### علامات Story غير جاهزة ❌
```
- "سنوضح التفاصيل مع التطوير"
- لا يوجد AC
- "افعل مثل الشاشة القديمة" بدون Figma
- Story Points = 0 أو غير محددة
- تعتمد على فريق آخر لم يؤكد بعد
```

---

## ✅ Definition of Done (DoD) — متى ننتهي؟

Story مكتملة عندما تحقق كل هذا:

### DoD للـ Developer
```
✅ الكود مكتوب ويعمل بدون أخطاء
✅ Unit Tests مكتوبة وناجحة (Coverage > X%)
✅ Code Review معتمد من [X] أشخاص
✅ لا Code Smells أو Technical Debt جديد
✅ Branch مدمج وـ Conflicts محلولة
✅ لا Hardcoded Values أو Secrets في الكود
✅ Logging مناسب مضاف
```

### DoD للـ QA
```
✅ Test Cases مكتوبة وتمت مراجعتها
✅ جميع AC اختُبرت (Happy Path + Edge Cases)
✅ Regression Testing على المناطق المتأثرة
✅ لا Open Bugs بأولوية P1 أو P2
✅ Performance مقبول (لا تراجع عن Baseline)
✅ اختبار على [Browsers/Devices] المتفق عليها
```

### DoD للـ BA / PO
```
✅ BRD محدّث إذا تغيرت المتطلبات
✅ Stakeholder وافق على الـ Demo
✅ User Documentation محدّثة (إذا لزم)
✅ Release Notes جاهزة
```

### DoD للـ Story (كاملة)
```
✅ Developer DoD محققة
✅ QA DoD محققة
✅ BA/PO DoD محققة
✅ تم Deploy على Test Environment
✅ PO قبل الـ Story في Review
✅ Jira Ticket محدّث ومغلق
```

### DoD للـ Sprint
```
✅ جميع Sprint Stories حققت Story DoD
✅ Sprint Goal تحقق
✅ Demo قُدِّم في Sprint Review
✅ Retro Action Items موثقة
✅ Backlog محدّث للـ Sprint القادم
```

### DoD للـ Release
```
✅ Sprint DoD محققة
✅ Regression Testing كامل
✅ Security Scan نظيف
✅ Performance Tests ناجحة
✅ Rollback Plan جاهز
✅ Stakeholders وافقوا
✅ Support Team مبلّغ
✅ Monitoring جاهز
```

---

## 📋 Acceptance Criteria (AC) — ماذا نبني بالضبط؟

### قالب Given / When / Then

```
Given [السياق — الوضع الأولي]
When  [الإجراء — ما يفعله المستخدم]
Then  [النتيجة المتوقعة]

مثال:
Given المستخدم مسجّل دخول وعنده عقد نشط
When يضغط على "تعديل العقد"
Then تظهر صفحة التعديل مع بيانات العقد الحالية
 And يكون زر "حفظ" معطلاً حتى يتم تعديل حقل واحد على الأقل
 And تظهر رسالة تأكيد قبل الحفظ
```

### AC يجب أن تغطي

```
Happy Path:     السيناريو الطبيعي الناجح
Error Cases:    ماذا لو فشل شيء؟
Edge Cases:     الحالات الحدية (فارغ، الحد الأقصى، etc)
Permissions:    من يملك صلاحية؟ من لا يملكها؟
Performance:    هل هناك متطلب زمن استجابة؟
Accessibility:  هل هناك متطلبات إمكانية الوصول؟
```

### مثال AC كامل
```
Story: كمستخدم أريد تعديل مبلغ العقد

AC-1: Happy Path
Given عقد بحالة "نشط" ومستخدم بصلاحية "مدير عقود"
When يعدّل المبلغ لقيمة صحيحة ويضغط "حفظ"
Then يُحفظ التعديل ويظهر تاريخ التعديل والمعدِّل
 And يُرسل إشعار للطرف الثاني بالتعديل

AC-2: Error — قيمة غير صالحة
When يدخل مبلغ سالب أو صفر
Then تظهر رسالة خطأ "المبلغ يجب أن يكون أكبر من صفر"
 And لا يُحفظ التعديل

AC-3: Permissions
Given مستخدم بصلاحية "موظف عادي"
When يحاول الوصول لصفحة التعديل
Then يُعاد توجيهه لصفحة "غير مصرح" (403)

AC-4: Edge Case — عقد منتهي
Given عقد بحالة "منتهٍ"
When يحاول المستخدم تعديله
Then زر "تعديل" معطّل ويظهر Tooltip "لا يمكن تعديل عقد منتهٍ"
```

---

## مقارنة DoR / DoD / AC

```
DoR  → بوابة الدخول  "هل الـ Story جاهزة للبناء؟"
AC   → مواصفات البناء "ماذا نبني بالضبط؟"
DoD  → بوابة الخروج  "هل الـ Story مكتملة فعلاً؟"
```

---

## تخصيص حسب الـ Framework

### Scrum
```
DoR: يُطبّق في Refinement قبل Sprint
DoD: يُتحقق منه في Sprint Review
AC:  يكتبها PO ويراجعها الفريق في Refinement
```

### Kanban
```
DoR: شرط دخول عمود "In Progress"
DoD: شرط دخول عمود "Done"
AC:  يكتبها قبل سحب Item للعمل
```

### SAFe
```
Feature DoR: قبل PI Planning
Story DoR:   قبل Sprint Planning
Feature DoD: يحقق System Demo
Story DoD:   نفس Scrum
```
