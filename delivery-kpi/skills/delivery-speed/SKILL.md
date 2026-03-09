# سرعة التسليم — Delivery Speed KPIs

## المقاييس المحسوبة من Jira

### 1. Lead Time
```
من: تاريخ إنشاء الـ ticket
إلى: تاريخ Deploy للـ Production
الهدف: < 14 يوم
```

### 2. Cycle Time
```
من: تاريخ بدء العمل الفعلي (In Progress)
إلى: تاريخ الإغلاق (Done)
الهدف: < 5 أيام للـ Story العادية
```

### 3. Deployment Frequency
```
عدد الإصدارات في الشهر
الهدف: إصدار واحد على الأقل كل أسبوعين
```

### 4. نسبة الـ Stories المكتملة في الوقت
```
Stories أُغلقت قبل أو في موعد Sprint / إجمالي Stories
الهدف: > 80%
```

### 5. Scope Creep
```
Stories أُضيفت بعد بدء الإصدار / Stories الأصلية
الهدف: < 10%
```

---

## طريقة الحساب من Jira

```
اجلب جميع Issues للإصدار:
- Fix Version = [اسم الإصدار]
- Status = Done

احسب لكل Issue:
- Lead Time = resolutiondate - created
- Cycle Time = resolutiondate - statusChangedTo("In Progress")

احسب المتوسطات والنسب
```

---

## تفسير النتائج

| النتيجة | التفسير | التوصية |
|---------|---------|---------|
| Lead Time > 21 يوم | عملية طويلة جداً | راجع bottlenecks |
| Cycle Time > 10 أيام | Stories كبيرة جداً | قسّم إلى tasks أصغر |
| Scope Creep > 20% | تغيير متطلبات متكرر | راجع عملية التحليل |
