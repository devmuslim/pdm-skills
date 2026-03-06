# Command: /analyze-situation
## Usage: `/analyze-situation [صف الموقف الصعب]`
## Workflow: system-thinking skill → Iceberg Model → 5 Whys → Leverage Point → خطة تدخل

## Description
يحلل موقفاً صعباً باستخدام System Thinking ليكشف الجذر الحقيقي — لا العَرَض السطحي.

## Steps
1. اجلب skills/system-thinking/SKILL.md
2. طبّق Iceberg Model على الموقف:
   - الحدث: ما الذي يحدث ظاهرياً؟
   - الأنماط: متى يتكرر؟ مع من؟
   - الهياكل: ما العملية التي تنتج هذا؟
   - المعتقدات: ماذا يؤمن الناس المتورطون؟
3. طبّق 5 Whys للوصول للجذر
4. حدد Leverage Point — أين التدخل الأذكى؟
5. حذّر من Unintended Consequences
6. أنتج خطة تدخل محددة بخطوات

## Output Format
```
🔍 تحليل الموقف — System Thinking
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 الحدث (ما يُرى): ...
📉 الأنماط: ...
⚙️ الهياكل التي تنتجه: ...
🧠 المعتقدات الجذرية: ...

🎯 5 Whys:
Why 1 → Why 2 → Why 3 → Why 4 → Why 5 (الجذر)

⚡ Leverage Point: ...
⚠️ عواقب غير متوقعة محتملة: ...

📋 خطة التدخل:
الخطوة 1: ...
الخطوة 2: ...
الخطوة 3: ...
```

## Integration
- إذا كان الموقف صراعاً → يقترح /handle-conflict
- إذا احتاج محادثة → يقترح /difficult-conversation
