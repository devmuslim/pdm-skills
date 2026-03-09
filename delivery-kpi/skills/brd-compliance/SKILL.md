# التوافق مع المتطلبات — BRD Compliance KPIs

## المقاييس

### 1. Requirements Coverage
```
Stories مرتبطة بـ BRD / إجمالي متطلبات BRD
الهدف: 100%
```

### 2. Unplanned Work Rate
```
Stories بدون ارتباط بـ BRD / إجمالي Stories
الهدف: < 10%
```

### 3. Requirements Change Rate
```
متطلبات تغيّرت بعد بدء التطوير / إجمالي المتطلبات
الهدف: < 15%
```

### 4. Acceptance Criteria Pass Rate
```
Stories اجتازت UAT من أول مرة / إجمالي Stories
الهدف: > 85%
```

### 5. Business Rules Coverage
```
Business Rules مُختبرة / إجمالي Business Rules في BRD
الهدف: 100%
```

---

## طريقة الحساب

```
من Jira:
- Stories بـ label = BRD-XXX → حساب Coverage
- Stories بدون BRD label → Unplanned Work
- Stories أُعيدت من UAT → Acceptance Criteria issues

من Knowledge Base (Google Drive):
- إجمالي Business Rules في BRD
- قارن مع Test Cases الموجودة
```

---

## ربط مع Knowledge Base

إذا كان `/index-brd` شُغّل مسبقاً:
- اجلب عدد Business Rules لكل BRD في الإصدار
- قارن مع Stories المنجزة
- أظهر gaps في التغطية
