---
description: مراجعة تصميم Figma مقابل المتطلبات — ارفع BRD أولاً ثم رابط Figma
argument-hint: [رابط Figma]
---

## طريقة الاستخدام

**الخطوة 1 — ارفع المتطلبات (اختياري لكن مستحسن):**
```
/analyze-brd
[ارفع ملف BRD]
```

**الخطوة 2 — راجع التصميم:**
```
/review-figma https://figma.com/design/XXXXX/Project-Name
```

---

## عند استلام رابط Figma:

1. اقرأ الملف عبر Figma MCP
2. إذا تم تحليل BRD → قارن كل شاشة مع المتطلبات
3. إذا لم يوجد BRD → راجع UX وجودة التصميم عموماً
4. أنتج التقرير بالصيغة المحددة في skills/figma-review

---

## إذا لم يوجد FIGMA_API_KEY:
أخبر المستخدم:
"يرجى إضافة Figma API Token: `export FIGMA_API_KEY=your_token`"
