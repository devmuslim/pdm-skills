# أداء الفريق — Team Performance KPIs

## المقاييس المحسوبة من Jira

### 1. Velocity
```
Story Points مكتملة في الإصدار
قارن مع الإصدار السابق
الهدف: ثبات أو نمو تدريجي
```

### 2. Throughput
```
عدد Stories مكتملة في الإصدار
الهدف: مقارنة بالمتوسط التاريخي
```

### 3. Blocked Time Rate
```
مجموع أيام الـ Blocked / مجموع Cycle Time
الهدف: < 10%
```

### 4. توزيع العمل
```
Stories لكل عضو في الفريق
الهدف: توزيع متوازن ± 20%
```

### 5. Technical Debt Ratio
```
Technical Debt tickets مغلقة / إجمالي tickets
الهدف: > 20% من كل إصدار للـ Tech Debt
```

---

## طريقة الحساب من Jira

```
اجلب:
- Story Points per Assignee
- Issues بـ label = blocked
- Issues بنوع = Technical Debt
- Velocity تاريخي (آخر 3 إصدارات)

احسب المتوسطات والمقارنات
```

---

## تفسير النتائج

| النتيجة | التفسير | التوصية |
|---------|---------|---------|
| Velocity انخفض > 20% | مشكلة في الفريق أو نطاق | راجع Retrospective |
| Blocked Time > 20% | تبعيات خارجية كثيرة | راجع خريطة التبعيات |
| توزيع غير متوازن | bottleneck على شخص واحد | أعد توزيع المهام |
