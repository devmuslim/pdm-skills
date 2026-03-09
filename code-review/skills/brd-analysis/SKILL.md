# تحليل BRD / وثائق المتطلبات

## متى تُفعَّل
عند رفع أي وثيقة متطلبات (BRD، SRS، User Stories، PRD) لاستخدامها كمرجع للمراجعة.

---

## كيفية تحليل الوثيقة

### استخرج تلقائياً:
1. **Business Rules** — كل قاعدة برمجية مطلوبة
2. **Use Cases / User Stories** — التدفقات الوظيفية
3. **الحقول والتحقق** — Mandatory / Optional / Read Only
4. **الأخطاء والاستثناءات** — EXC، Exception Flows
5. **الرسائل** — نصوص الإشعارات والتحذيرات
6. **التكاملات** — APIs وأطراف خارجية
7. **المتطلبات غير الوظيفية** — Performance، Security، Reliability

### أنشئ Checklist تلقائية:
بعد تحليل الوثيقة، أنشئ قائمة تحقق جاهزة للمراجعة:

```
### Checklist من [اسم الوثيقة]
- [ ] [Business Rule 1]
- [ ] [Business Rule 2]
- [ ] [Use Case Flow 1]
- [ ] [Error Handling 1]
...
```

---

## استخدم هذه الـ Checklist في:
- `/review-code` — مراجعة الكود
- `/review-figma` — مراجعة التصميم
