#!/usr/bin/env python3
"""
validate_plugins.py — PDM Skills Marketplace
يتحقق من صحة بنية الـ plugins وجودة المحتوى.
"""

import os
import json
import sys
from pathlib import Path

# ألوان للطرفية
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

REQUIRED_SKILL_SECTIONS = ["## Purpose", "## When to Use", "## Output Format"]
REQUIRED_COMMAND_SECTIONS = ["## Description", "## Usage", "## Workflow"]
MIN_SKILL_LINES = 20
MIN_COMMAND_LINES = 15

errors = []
warnings = []
passed = []


def check(condition, success_msg, fail_msg, is_warning=False):
    if condition:
        passed.append(f"  {GREEN}✓{RESET} {success_msg}")
    else:
        msg = f"  {YELLOW if is_warning else RED}{'⚠' if is_warning else '✗'}{RESET} {fail_msg}"
        if is_warning:
            warnings.append(msg)
        else:
            errors.append(msg)


def validate_plugin_json(plugin_dir: Path):
    print(f"\n{BLUE}{BOLD}[{plugin_dir.name}]{RESET}")

    plugin_json = plugin_dir / "plugin.json"
    check(plugin_json.exists(), "plugin.json موجود", "plugin.json مفقود ❌")

    if not plugin_json.exists():
        return

    try:
        with open(plugin_json) as f:
            data = json.load(f)

        check("name" in data, "حقل name موجود", "حقل name مفقود")
        check("description" in data, "حقل description موجود", "حقل description مفقود")
        check("skills" in data and len(data.get("skills", [])) > 0,
              f"skills معرّفة ({len(data.get('skills', []))} مهارة)",
              "لا توجد skills معرّفة")
        check("commands" in data and len(data.get("commands", [])) > 0,
              f"commands معرّفة ({len(data.get('commands', []))} أمر)",
              "لا توجد commands معرّفة", is_warning=True)

        # تحقق من وجود ملفات المهارات المعرّفة
        skills_dir = plugin_dir / "skills"
        if skills_dir.exists():
            for skill in data.get("skills", []):
                skill_file = skills_dir / f"{skill}.md"
                check(skill_file.exists(),
                      f"ملف المهارة {skill}.md موجود",
                      f"ملف المهارة {skill}.md مفقود")
        else:
            errors.append(f"  {RED}✗{RESET} مجلد skills/ مفقود")

        # تحقق من وجود ملفات الأوامر المعرّفة
        commands_dir = plugin_dir / "commands"
        if commands_dir.exists():
            for cmd in data.get("commands", []):
                cmd_file = commands_dir / f"{cmd}.md"
                check(cmd_file.exists(),
                      f"ملف الأمر {cmd}.md موجود",
                      f"ملف الأمر {cmd}.md مفقود", is_warning=True)

    except json.JSONDecodeError as e:
        errors.append(f"  {RED}✗{RESET} plugin.json غير صالح: {e}")


def validate_skill_file(skill_file: Path):
    content = skill_file.read_text(encoding="utf-8")
    lines = content.strip().split("\n")

    check(len(lines) >= MIN_SKILL_LINES,
          f"{skill_file.name}: طول كافٍ ({len(lines)} سطر)",
          f"{skill_file.name}: قصير جداً ({len(lines)} سطر < {MIN_SKILL_LINES})",
          is_warning=True)

    for section in REQUIRED_SKILL_SECTIONS:
        check(section in content,
              f"{skill_file.name}: قسم '{section}' موجود",
              f"{skill_file.name}: قسم '{section}' مفقود",
              is_warning=True)


def validate_command_file(cmd_file: Path):
    content = cmd_file.read_text(encoding="utf-8")
    lines = content.strip().split("\n")

    check(len(lines) >= MIN_COMMAND_LINES,
          f"{cmd_file.name}: طول كافٍ ({len(lines)} سطر)",
          f"{cmd_file.name}: قصير جداً ({len(lines)} سطر < {MIN_COMMAND_LINES})",
          is_warning=True)

    for section in REQUIRED_COMMAND_SECTIONS:
        check(section in content,
              f"{cmd_file.name}: قسم '{section}' موجود",
              f"{cmd_file.name}: قسم '{section}' مفقود",
              is_warning=True)


def validate_marketplace():
    marketplace_file = Path(".claude-plugin/marketplace.json")
    print(f"\n{BLUE}{BOLD}[.claude-plugin/marketplace.json]{RESET}")

    check(marketplace_file.exists(),
          "marketplace.json موجود",
          "marketplace.json مفقود")

    if marketplace_file.exists():
        try:
            data = json.load(open(marketplace_file))
            check("name" in data, "حقل name موجود", "حقل name مفقود")
            check("plugins" in data and len(data["plugins"]) > 0,
                  f"plugins معرّفة ({len(data.get('plugins', []))} plugin)",
                  "لا توجد plugins في marketplace.json")
        except json.JSONDecodeError as e:
            errors.append(f"  {RED}✗{RESET} marketplace.json غير صالح: {e}")


def main():
    repo_root = Path(".")

    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}  PDM Skills — فحص صحة الريبو{RESET}")
    print(f"{BOLD}{'='*50}{RESET}")

    # تحقق من الملفات الجذرية
    print(f"\n{BLUE}{BOLD}[الملفات الجذرية]{RESET}")
    check((repo_root / "README.md").exists(), "README.md موجود", "README.md مفقود")
    check((repo_root / "LICENSE").exists(), "LICENSE موجود", "LICENSE مفقود")

    # تحقق من marketplace
    validate_marketplace()

    # تحقق من كل plugin
    plugin_dirs = sorted([d for d in repo_root.iterdir()
                          if d.is_dir() and d.name.startswith("pdm-")])

    if not plugin_dirs:
        errors.append(f"  {RED}✗{RESET} لا توجد مجلدات plugins تبدأ بـ pdm-")
    else:
        for plugin_dir in plugin_dirs:
            validate_plugin_json(plugin_dir)

            # فحص ملفات المهارات
            skills_dir = plugin_dir / "skills"
            if skills_dir.exists():
                for skill_file in sorted(skills_dir.glob("*.md")):
                    validate_skill_file(skill_file)

            # فحص ملفات الأوامر
            commands_dir = plugin_dir / "commands"
            if commands_dir.exists():
                for cmd_file in sorted(commands_dir.glob("*.md")):
                    validate_command_file(cmd_file)

    # طباعة النتائج
    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}  النتائج{RESET}")
    print(f"{BOLD}{'='*50}{RESET}")

    for msg in passed:
        print(msg)
    for msg in warnings:
        print(msg)
    for msg in errors:
        print(msg)

    # ملخص
    total_plugins = len(plugin_dirs)
    total_skills = sum(1 for d in plugin_dirs
                       for _ in (d / "skills").glob("*.md")
                       if (d / "skills").exists())
    total_commands = sum(1 for d in plugin_dirs
                         for _ in (d / "commands").glob("*.md")
                         if (d / "commands").exists())

    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"  📦 Plugins:  {total_plugins}")
    print(f"  🧠 مهارات:   {total_skills}")
    print(f"  ⚡ أوامر:    {total_commands}")
    print(f"  {GREEN}✓ نجح:      {len(passed)}{RESET}")
    print(f"  {YELLOW}⚠ تحذيرات:  {len(warnings)}{RESET}")
    print(f"  {RED}✗ أخطاء:    {len(errors)}{RESET}")
    print(f"{BOLD}{'='*50}{RESET}")

    if errors:
        print(f"\n{RED}{BOLD}❌ الفحص فشل — يرجى إصلاح الأخطاء أعلاه{RESET}\n")
        sys.exit(1)
    elif warnings:
        print(f"\n{YELLOW}{BOLD}⚠ الفحص نجح مع تحذيرات{RESET}\n")
        sys.exit(0)
    else:
        print(f"\n{GREEN}{BOLD}✅ الفحص نجح بالكامل!{RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
