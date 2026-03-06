# طبقة التكامل — Agile Coach + PDM Plugins

## الهدف
ربط agile-coach ببيانات حقيقية من:
- **delivery-kpi** → أداء الفريق الفعلي من Jira
- **knowledge-base** → مستوى فهم الفريق للـ BRD's
- **Jira MCP** → Velocity وSprint data تلقائياً
- **Google Drive** → حفظ التقييمات واسترجاعها

---

## كيف يعمل التكامل

### عند `/assess-team` أو `/assess-workflow`
```
1. اجلب من Jira (إذا متاح):
   - Sprint Velocity آخر 3 Sprints
   - نسبة إغلاق Stories لكل عضو
   - عدد Bugs مرفوعة ضد كل Developer
   - متوسط Cycle Time لكل عضو

2. اجلب من knowledge-base (إذا شُغّل /index-brd):
   - هل يربط الفريق Stories بـ BRD's في Jira

3. استخدم البيانات لتعميق التقييم:
   بدلاً من: "كيف تقدّر وقتك؟"
   قل: "Velocity الخاص بك X pts — هل يعكس تقديراتك؟"
```

### عند `/growth-plan`
```
1. اجلب KPIs الحقيقية من Jira للعضو
2. حدد الفجوة بين الأداء الحالي والهدف
3. ابن الخطة على البيانات لا على التخمين

مثال:
"Cycle Time = 8 أيام (الهدف 5)"
→ الخطة: تحسين تقسيم المهام وإدارة التبعيات
```

### عند `/team-progress`
```
1. اجلب من Jira: مقارنة Velocity شهر بشهر
2. اجلب من delivery-kpi: Defect Rate, UAT Pass Rate
3. اربطها بالتقييمات المحفوظة في Google Drive
4. أظهر التحسن الحقيقي بالأرقام لا بالانطباعات
```

---

## السيناريوهات المتكاملة

### السيناريو 1 — تقييم مطور
```
/assess-team Ahmed — Developer

├── يسأل 5 أسئلة مخصصة (role-assessment)
├── يجلب من Jira: Velocity، Bugs، Cycle Time
├── يجلب من knowledge-base: هل يربط Stories بـ BRD؟
└── ينتج تقييم مدعوم بالبيانات + خطة تطوير
```

### السيناريو 2 — خطة تطوير
```
/growth-plan Sara — QA

├── يجلب KPIs Sara من Jira
├── يحدد الفجوات الحقيقية بالأرقام
└── يبني خطة مخصصة بناءً على البيانات
```

### السيناريو 3 — تقرير تقدم شهري
```
/team-progress شهر 3

├── يجلب Velocity مقارنةً بالأشهر السابقة
├── يجلب Defect Rate من delivery-kpi
├── يقارن بالتقييمات المحفوظة في Drive
└── "الفريق تحسّن X% في جودة الكود — بيانات Jira"
```

---

## قواعد التكامل

### إذا لم تكن البيانات متاحة
```
Jira غير مربوط    → أسئلة فقط + تنبيه
knowledge-base لم يُشغَّل → اسأل عن BRD يدوياً
Google Drive غير مربوط → احفظ في الجلسة الحالية فقط
```

### أولوية البيانات
```
1. بيانات Jira الحقيقية  → أعلى موثوقية
2. تقييمات Drive المحفوظة → موثوقية عالية
3. إجابات المقابلة        → ذاتية — أقل موثوقية
```

---

## هيكل حفظ التقييمات في Google Drive

```
📁 agile-coach/
├── 📁 assessments/
│   ├── ahmed-2026-03.yaml
│   └── team-overview-2026-03.yaml
├── 📁 growth-plans/
│   └── ahmed-growth-plan.yaml
└── 📁 progress-reports/
    ├── month-1-report.yaml
    └── month-3-report.yaml
```

عند كل تقييم جديد:
1. تحقق من تقييم سابق في Drive
2. إذا موجود → أظهر المقارنة والتحسن
3. احفظ التقييم الجديد مع timestamp

---

## إعداد Jira — Cloud vs Data Center

### كيف تعرف أي نوع عندك؟
```
Jira Cloud:       رابطك مثل → yourcompany.atlassian.net
Jira Data Center: رابطك مثل → jira.yourcompany.com (سيرفر داخلي)
```

---

### ☁️ Jira Cloud — الإعداد

**الخطوات:**
```
1. اذهب: https://id.atlassian.com/manage-profile/security/api-tokens
2. Create Token → سمّه "claude-pdm"
3. انسخ التوكن
4. في .mcp.json:
   - غيّر _OPTION_A_JIRA_CLOUD إلى "jira"
   - ضع رابطك وإيميلك والتوكن
```

**المصادقة:** `JIRA_USERNAME` + `JIRA_API_TOKEN`

**الـ MCP Server:** الرسمي من Atlassian عبر SSE
```
"type": "sse",
"url": "https://mcp.atlassian.com/sse"
```

---

### 🏢 Jira Data Center — الإعداد

**الخطوات:**
```
1. افتح Jira الداخلي
2. Profile (أيقونة أعلى اليمين) → Personal Access Tokens
3. Create Token → سمّه "claude-pdm"
4. انسخ الـ PAT (يظهر مرة واحدة فقط!)
5. ثبّت uv: pip install uv
6. في .mcp.json:
   - غيّر _OPTION_B_JIRA_DATA_CENTER إلى "jira"
   - ضع رابط سيرفرك والـ PAT
```

**المصادقة:** `JIRA_PERSONAL_TOKEN` فقط (لا يحتاج username)

**الـ MCP Server:** mcp-atlassian مفتوح المصدر عبر uvx
```
"command": "uvx",
"args": ["mcp-atlassian"]
```

---

### مقارنة سريعة

| | Cloud | Data Center |
|--|-------|-------------|
| نوع التوكن | API Token | Personal Access Token (PAT) |
| مكان إنشاء التوكن | id.atlassian.com | داخل Jira نفسه |
| الـ MCP | SSE رسمي | uvx mcp-atlassian |
| يحتاج تثبيت؟ | لا | نعم (uv) |
| الشبكة | إنترنت | داخلية فقط |
