# BRD Registry — فهرس الوثائق

## الهدف
بناء فهرس مركزي لجميع BRD's في Google Drive يربطها بعلاقات التبعية.

---

## هيكل الفهرس

```yaml
documents:
  - id: "brd-001"
    name: "إنشاء عقد وساطة مع مالك"
    drive_id: "GOOGLE_DRIVE_FILE_ID"
    version: "1.0"
    status: "معتمد"
    domain: "contracts"
    depends_on: []
    required_by:
      - "brd-003"  # تعديل العقود يعتمد عليه
      - "brd-005"  # العقود الفرعية تعتمد عليه

  - id: "brd-002"
    name: "إنشاء عقد وساطة مع مستأجر/مشتري"
    drive_id: "GOOGLE_DRIVE_FILE_ID"
    version: "1.0"
    status: "معتمد"
    domain: "contracts"
    depends_on: []
    required_by:
      - "brd-003"

  - id: "brd-003"
    name: "تعديل العقود"
    drive_id: "GOOGLE_DRIVE_FILE_ID"
    version: "1.2"
    status: "معتمد"
    domain: "contracts"
    depends_on:
      - "brd-001"  # إنشاء عقد مالك
      - "brd-002"  # إنشاء عقد مستأجر
      - "brd-004"  # العقود الفرعية
      - "brd-006"  # OTP Service
    required_by: []
```

---

## كيفية استخدام الفهرس

عند تشغيل `/plan-release` أو `/analyze-brd`:
1. ابحث في الفهرس عن الـ BRD المطلوب
2. اجلب جميع `depends_on` تلقائياً من Google Drive
3. أضفها كـ context للمراجعة أو التخطيط
4. نبّه إذا كان أي BRD تبعية غير معتمد أو قديم

---

## تحديث الفهرس

يتم تحديث `registry.yaml` تلقائياً عند:
- تشغيل `/index-brd` 
- رفع BRD جديد
- تغيير إصدار وثيقة موجودة
