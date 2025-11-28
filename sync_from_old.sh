#!/usr/bin/env bash
set -e

OLD="../MarketAi"
NEW="."

echo "🔄 بدء مزامنة MarketAi → MarketAi_V3..."
echo "OLD = $OLD"
echo "NEW = $NEW"
echo ""

sync_dir() {
    src="$1"
    dst="$2"
    if [ -d "$OLD/$src" ]; then
        echo "📁 نقل المجلد: $src → $dst"
        mkdir -p "$NEW/$dst"
        cp -r "$OLD/$src/"* "$NEW/$dst/" 2>/dev/null || true
    fi
}

sync_file() {
    src="$1"
    dst="$2"
    if [ -f "$OLD/$src" ]; then
        echo "📄 نقل الملف: $src → $dst"
        mkdir -p "$(dirname "$NEW/$dst")"
        cp "$OLD/$src" "$NEW/$dst"
    fi
}

# -----------------------
# 1) نقل ملفات DNA
# -----------------------
sync_dir "DNA" "docs/DNA"

# -----------------------
# 2) نقل work_system
# -----------------------
sync_dir "work_system" "docs/operations/work_system"

# -----------------------
# 3) نقل progress (days)
# -----------------------
sync_dir "progress/days_progress" "docs/Progress/days"

# -----------------------
# 4) نقل data_collector
# -----------------------
sync_dir "core/data_collector" "src/data_collector"

# -----------------------
# 5) نقل microstructure
# -----------------------
sync_dir "core/absorption" "src/microstructure"

# -----------------------
# 6) نقل divergence / structure engines
# -----------------------
sync_dir "core/divergence" "src/structure"

# -----------------------
# 7) نقل peaks_engine
# -----------------------
sync_dir "core/peaks_engine" "src/structure/peaks_engine"

# -----------------------
# 8) intent engine
# -----------------------
sync_dir "core/intent_engine" "src/intent"

# -----------------------
# 9) MX engine models/rules/utils
# -----------------------
sync_dir "core/mx/models" "src/mx/models"
sync_dir "core/mx/rules" "src/mx/rules"
sync_dir "core/mx/utils" "src/mx/utils"
sync_dir "core/mx/docs" "src/mx/docs"

# -----------------------
# 10) execution (api/engine/risk)
# -----------------------
sync_dir "execution/api" "src/execution/api"
sync_dir "execution/engine" "src/execution/engine"
sync_dir "execution/risk" "src/execution/risk"

# -----------------------
# 11) نسخ READMEs المهمة
# -----------------------
sync_file "FOUNDATIONS.md" "docs/operations/work_system/FOUNDATIONS.md"
sync_file "PHILOSOPHY.md" "PHILOSOPHY.md"
sync_file "README.md" "README_OLD.md"
sync_file "PROJECT_CONFIG.md" "docs/PROJECT_CONFIG.md"
sync_file "docs/PROJECT_SPEC.md" "docs/PROJECT_SPEC.md"

# -----------------------
# 12) نقل data (بدون raw الضخمة)
# -----------------------
sync_dir "data/example_data" "src/data/example_data"

echo ""
echo "✅ تمت عملية المزامنة بنجاح!"
echo "افتح الآن شجرة MarketAi_V3 وستجد الملفات الناقصة قد تمت إضافتها."
