# جودة التسليم — Quality KPIs

## المقاييس المحسوبة من Jira

### 1. Defect Rate
```
عدد Bugs مفتوحة بعد الإصدار / عدد Stories المسلّمة
الهدف: < 5%
```

### 2. Bug Severity Distribution
```
Critical Bugs : Major : Minor
الهدف: 0 Critical في Production
```

### 3. Reopened Issues Rate
```
Issues أُعيد فتحها / إجمالي Issues المغلقة
الهدف: < 3%
```

### 4. Escaped Defects
```
Bugs اكتُشفت في Production / إجمالي Bugs
الهدف: < 2%
```

### 5. Test Coverage (إذا متوفر)
```
Stories عندها Test Cases / إجمالي Stories
الهدف: > 90%
```

---

## طريقة الحساب من Jira

```
اجلب:
- Issues بنوع Bug مرتبطة بالإصدار
- Issues بحالة Reopened
- Issues بـ Priority = Critical/Blocker

احسب النسب مقارنةً بإجمالي Stories
```

---

## تفسير النتائج

| النتيجة | التفسير | التوصية |
|---------|---------|---------|
| Defect Rate > 10% | جودة منخفضة | راجع Definition of Done |
| Critical Bug في Prod | خطر عالٍ | Hotfix فوري + Post-mortem |
| Reopened > 5% | فهم ناقص للمتطلبات | راجع Acceptance Criteria |
