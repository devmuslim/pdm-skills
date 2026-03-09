# Drive Indexer — قراءة BRD's من Google Drive

## الهدف
قراءة جميع BRD's من Google Drive تلقائياً وبناء الفهرس.

---

## خطوات الفهرسة

### 1. ابحث عن مجلد الـ BRD's
```
ابحث في Google Drive عن مجلد باسم:
- "BRD" أو "Business Requirements" أو "متطلبات"
- أو اسأل المستخدم عن مسار المجلد
```

### 2. لكل ملف في المجلد، استخرج:
- اسم الملف
- تاريخ آخر تعديل
- معرّف الملف (Drive ID)
- محتوى الوثيقة (للتحليل)

### 3. حلل كل BRD واستخرج:
- **اسم الخدمة/الميزة**
- **الإصدار والتاريخ**
- **حالة الاعتماد**
- **التبعيات المذكورة** — ابحث عن عبارات مثل:
  - "AS IS" + اسم وثيقة
  - "يعتمد على"
  - "depends on"
  - "نفس العملية المستخدمة في"
  - "وفقاً لـ"

### 4. أنشئ `registry.yaml` بالهيكل المحدد في skills/brd-registry

---

## مثال على اكتشاف التبعية تلقائياً

إذا وجدت في BRD نص:
```
"Adding or editing deeds follows the same process used when creating a contract. 
AS IS Create BC with owner"
```

→ أضف تبعية على: `create-brokerage-contract-with-owner`

---

## تحديث تلقائي

إذا وجدت ملفات جديدة أو محدّثة في Drive:
- أضفها للفهرس
- نبّه المستخدم بالتغييرات
