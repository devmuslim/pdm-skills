# دليل إعداد Jira — لجميع الـ Plugins

## الخطوة 1 — حدد نوع Jira عندك

```
❓ ما رابط Jira عندك؟

yourcompany.atlassian.net   →  ☁️  Jira Cloud
jira.yourcompany.com        →  🏢  Jira Data Center
```

---

## ☁️ Jira Cloud

### إنشاء الـ API Token
```
1. اذهب: https://id.atlassian.com/manage-profile/security/api-tokens
2. اضغط: Create API Token
3. سمّه: claude-pdm-skills
4. انسخ التوكن واحفظه
```

### إعداد .mcp.json
```json
{
  "mcpServers": {
    "jira": {
      "type": "sse",
      "url": "https://mcp.atlassian.com/sse",
      "env": {
        "JIRA_URL": "https://YOUR-COMPANY.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "YOUR_TOKEN_HERE"
      }
    }
  }
}
```

### تحقق من الاتصال
```bash
# في Claude Code اكتب:
"اجلب لي قائمة المشاريع من Jira"
```

---

## 🏢 Jira Data Center

### إنشاء الـ Personal Access Token (PAT)
```
1. افتح Jira الداخلي على متصفحك
2. اضغط على صورتك (أعلى اليمين)
3. اختر: Profile
4. من القائمة الجانبية: Personal Access Tokens
5. اضغط: Create Token
6. سمّه: claude-pdm-skills
7. حدد تاريخ انتهاء (مثلاً سنة)
8. اضغط Create
9. ⚠️ انسخ التوكن فوراً — لن يظهر مرة ثانية!
```

### تثبيت المتطلبات
```bash
# macOS / Linux
pip install uv
# أو
brew install uv

# Windows
pip install uv
```

### إعداد .mcp.json
```json
{
  "mcpServers": {
    "jira": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://jira.YOUR-COMPANY.com",
        "JIRA_PERSONAL_TOKEN": "YOUR_PAT_HERE"
      }
    }
  }
}
```

### تحقق من الاتصال
```bash
# في Claude Code اكتب:
"اجلب لي قائمة المشاريع من Jira"
```

---

## الـ Plugins التي تستخدم Jira

| Plugin | الأوامر التي تحتاج Jira |
|--------|------------------------|
| `delivery-kpi` | `/release-kpi`، `/compare-releases` |
| `agile-coach` | `/assess-team`، `/growth-plan`، `/team-progress` |

---

## مشاكل شائعة

### "Unauthorized" أو 401
```
Cloud: تحقق من صحة JIRA_USERNAME وJIRA_API_TOKEN
DC:    تحقق من صحة JIRA_PERSONAL_TOKEN وأنه لم ينته
```

### "Connection refused"
```
DC: تحقق أن JIRA_URL يشير للسيرفر الداخلي الصحيح
    وأن جهازك متصل بالشبكة الداخلية أو VPN
```

### "uv not found"
```
شغّل: pip install uv
ثم أعد تشغيل Claude Code
```

### الـ Token ينتهي بسرعة
```
Cloud: API Tokens لا تنتهي (يمكن حذفها يدوياً)
DC:    عند الإنشاء اختر تاريخ انتهاء بعيد (سنة أو أكثر)
```
