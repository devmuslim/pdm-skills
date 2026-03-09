# رضا العميل — Stakeholder Satisfaction KPIs

## المقاييس

### 1. UAT Pass Rate
```
Stories اعتمدها العميل من أول مرة / إجمالي Stories في UAT
الهدف: > 85%
```

### 2. Change Requests بعد الإصدار
```
طلبات التغيير المستلمة بعد الإطلاق
الهدف: < 3 طلبات جوهرية
```

### 3. On-Time Delivery
```
هل الإصدار سُلّم في الموعد المتفق عليه؟
الهدف: 100% أو تأخير < 5 أيام
```

### 4. Stakeholder Feedback Score
```
تقييم الـ Stakeholders بعد كل إصدار (1-5)
الهدف: > 4/5
```

### 5. Features Accepted vs Rejected
```
Features قبلها العميل / إجمالي Features المسلّمة
الهدف: > 90%
```

---

## طريقة الجمع

```
من Jira:
- Issues أُعيدت من UAT (status = Rejected in UAT)
- Change Request tickets بعد Release Date
- On-Time: قارن actual release date مع planned date

يدوي (اسأل المستخدم):
- Stakeholder Feedback Score
- ملاحظات العميل النصية
```

---

## قالب جمع الـ Feedback

بعد كل إصدار، أرسل هذا للـ Stakeholders:

```
📋 تقييم إصدار [اسم الإصدار]

1. هل الميزات المسلّمة تلبي احتياجاتك؟ (1-5)
2. هل جودة التسليم كانت مقبولة؟ (1-5)  
3. هل الموعد كان مناسباً؟ (1-5)
4. ما الذي تريد تحسينه في الإصدار القادم؟
```
