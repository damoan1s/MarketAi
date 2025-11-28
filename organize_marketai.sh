#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# -----------------------
# Organize MarketAI Project
# -----------------------
# Usage: run from project root (where README.md exists)
# Creates MarketAI_V3 structure and moves existing files into new layout.
# Safe-mode: does not delete files; if destination exists, creates .bak.TIMESTAMP copy.
# -----------------------

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ROOT="$(pwd)"
NEWROOT="$ROOT/MarketAI_V3"

log() { echo -e "[date +%H:%M:%S] $*"; }

ensure_dir() {
  if [ ! -d "$1" ]; then
    mkdir -p "$1"
    log "mkdir -> $1"
  fi
}

safe_move() {
  # safe_move <source> <dest_dir>
  local src="$1" destdir="$2"
  if [ -e "$src" ]; then
    ensure_dir "$destdir"
    local base=$(basename "$src")
    local dest="$destdir/$base"
    if [ -e "$dest" ]; then
      local bak="${dest}.bak.${TIMESTAMP}"
      mv "$dest" "$bak"
      log "backup existing -> $dest to $bak"
    fi
    mv "$src" "$destdir/"
    log "moved -> $src  -> $destdir/"
  else
    log "not found (skip): $src"
  fi
}

safe_copy_if_missing() {
  # safe_copy_if_missing <source> <dest>
  local src="$1" dest="$2"
  if [ -e "$src" ] && [ ! -e "$dest" ]; then
    ensure_dir "$(dirname "$dest")"
    cp -r "$src" "$dest"
    log "copied -> $src -> $dest"
  fi
}

# 1) Create final tree directories
log "Creating final directory tree at: $NEWROOT"
declare -a DIRS=( 
  "$NEWROOT/agents/docs"
  "$NEWROOT/agents/runtime"
  "$NEWROOT/agents/tests"
  "$NEWROOT/config"
  "$NEWROOT/docs/design"
  "$NEWROOT/docs/DNA/Phases"
  "$NEWROOT/docs/operations/work_system"
  "$NEWROOT/docs/Notes"
  "$NEWROOT/docs/Progress/days/day4"
  "$NEWROOT/docs/Progress/days/day5"
  "$NEWROOT/docs/Progress/days/day6"
  "$NEWROOT/docs/Progress/days/day7"
  "$NEWROOT/scripts"
  "$NEWROOT/src/structure/block1_sync"
  "$NEWROOT/src/structure/block2_peaks"
  "$NEWROOT/src/structure/block3_angle"
  "$NEWROOT/src/structure/block4_structure_map"
  "$NEWROOT/src/structure/block5_divergence"
  "$NEWROOT/src/microstructure/block6_wicks"
  "$NEWROOT/src/microstructure/block7_absorption"
  "$NEWROOT/src/microstructure/block8_delta"
  "$NEWROOT/src/microstructure/block9_microdiv"
  "$NEWROOT/src/microstructure/block10_release"
  "$NEWROOT/src/intent/block11_dwam"
  "$NEWROOT/src/intent/block12_mx"
  "$NEWROOT/src/intent/block13_dna"
  "$NEWROOT/src/intent/block14_intent_score"
  "$NEWROOT/src/intent/block15_mfi"
  "$NEWROOT/src/execution/block16_backtest"
  "$NEWROOT/src/execution/block17_execution"
  "$NEWROOT/src/data"
  "$NEWROOT/src/mx/models"
  "$NEWROOT/src/mx/rules"
  "$NEWROOT/tests"
  "$NEWROOT/tools"
  "$NEWROOT/ui"
)
for d in "${DIRS[@]}"; do ensure_dir "$d"; done

# 2) Move files from old typical locations into the new tree (safe_move)
# Common file mappings based on the tree you provided:
log "Moving / mapping known files into the new layout (if present)..."

# Agents (move any top-level agent files)
safe_move "$ROOT/agents/intent_agent.py" "$NEWROOT/agents"
safe_move "$ROOT/agents/micro_agent.py" "$NEWROOT/agents"
safe_move "$ROOT/agents/structure_agent.py" "$NEWROOT/agents"

# move README.* for agents if exist
safe_move "$ROOT/agents/README.intent.md" "$NEWROOT/agents/docs"
safe_move "$ROOT/agents/README.micro.md" "$NEWROOT/agents/docs"
safe_move "$ROOT/agents/README.structure.md" "$NEWROOT/agents/docs"

# src/data files
safe_move "$ROOT/src/data/example_ohlcv.csv" "$NEWROOT/src/data"
safe_move "$ROOT/data/example_ohlcv.csv" "$NEWROOT/src/data"
safe_move "$ROOT/data/ohlcv_sample.csv" "$NEWROOT/src/data"
safe_move "$ROOT/data/ohlcv_sample.csv" "$NEWROOT/src/data"

# Data collectors
safe_move "$ROOT/src/data_collector/spot_collector.py" "$NEWROOT/src/data"
safe_move "$ROOT/src/data_collector/futures_collector.py" "$NEWROOT/src/data"
safe_move "$ROOT/src/data_collector/gold_data.py" "$NEWROOT/src/data"
safe_move "$ROOT/src/data_collector/normalizer.py" "$NEWROOT/src/data"

# structure / peaks / angle files -> map to structure blocks
safe_move "$ROOT/src/structure/angle_detector.py" "$NEWROOT/src/structure/block3_angle"
safe_move "$ROOT/src/structure/slope_analyzer.py" "$NEWROOT/src/structure/block3_angle"
safe_move "$ROOT/src/structure/differential_engine.py" "$NEWROOT/src/structure/block5_divergence"
safe_move "$ROOT/src/structure/peaks_engine/data_layer.py" "$NEWROOT/src/structure/block2_peaks"
safe_move "$ROOT/src/structure/peaks_engine/logic_layer.py" "$NEWROOT/src/structure/block2_peaks"
safe_move "$ROOT/src/structure/peaks_engine/output_layer.py" "$NEWROOT/src/structure/block2_peaks"
safe_move "$ROOT/src/structure/peaks_engine/run_block1.py" "$NEWROOT/scripts"

# microstructure
safe_move "$ROOT/src/microstructure/absorption_zone_map.py" "$NEWROOT/src/microstructure/block7_absorption"
safe_move "$ROOT/src/microstructure/imbalance_scanner.py" "$NEWROOT/src/microstructure/block7_absorption"
safe_move "$ROOT/src/microstructure/liquidity_pressure.py" "$NEWROOT/src/microstructure/block7_absorption"
safe_move "$ROOT/src/intent/microstructure_filters.py" "$NEWROOT/src/microstructure/block9_microdiv"

# mx
safe_move "$ROOT/src/mx/models/dwam_model.py" "$NEWROOT/src/mx/models"
safe_move "$ROOT/src/mx/models/futures_spot_engine.py" "$NEWROOT/src/mx/models"
safe_move "$ROOT/src/mx/rules/angle_rules.md" "$NEWROOT/src/mx/rules"
safe_move "$ROOT/src/mx/utils/calc.py" "$NEWROOT/src/mx"

# intent / dna
safe_move "$ROOT/src/intent/dna_ruleset.py" "$NEWROOT/src/intent/block13_dna"
safe_move "$ROOT/src/intent/futures_spot_delta.py" "$NEWROOT/src/intent/block11_dwam"
safe_move "$ROOT/src/intent/MI_core.py" "$NEWROOT/src/intent/block14_intent_score"

# execution
safe_move "$ROOT/src/execution/engine/executor.py" "$NEWROOT/src/execution/block17_execution"
safe_move "$ROOT/src/execution/risk/risk_manager.py" "$NEWROOT/src/execution/block17_execution"
safe_move "$ROOT/src/execution/api/webhook_api.py" "$NEWROOT/src/execution/block17_execution"

# docs
safe_move "$ROOT/docs/DNA/Phases/Absorption.md" "$NEWROOT/docs/DNA/Phases"
safe_move "$ROOT/docs/DNA/Phases/Discrepancy.md" "$NEWROOT/docs/DNA/Phases"
safe_move "$ROOT/docs/DNA/Phases/Exhausion.md" "$NEWROOT/docs/DNA/Phases"
safe_move "$ROOT/docs/DNA/Phases/Release.md" "$NEWROOT/docs/DNA/Phases"
safe_move "$ROOT/INSTITUTIONAL_CASES_LIBRARY.md" "$NEWROOT/docs/Notes" 2>/dev/null || true
safe_move "$ROOT/docs/Notes/INTITUTIONAL_CASES_LIBRARY.md" "$NEWROOT/docs/Notes"

# operations / work_system files
safe_move "$ROOT/docs/operations/work_system/01_SYSTEM_OVERVIEW.md" "$NEWROOT/docs/operations/work_system"
safe_move "$ROOT/docs/operations/work_system/FOUNDATIONS.md" "$NEWROOT/docs/operations/work_system"
safe_move "$ROOT/docs/operations/work_system/ANIS_PROFILE.md" "$NEWROOT/docs/operations/work_system"
safe_move "$ROOT/docs/operations/work_system/PROJECT_BRIEFING.md" "$NEWROOT/docs/operations/work_system"
safe_move "$ROOT/docs/operations/work_system/WORK_PROTOCOL.md" "$NEWROOT/docs/operations/work_system"

# progress days
safe_move "$ROOT/docs/Progress/days/day4/day4_test.py" "$NEWROOT/docs/Progress/days/day4"
safe_move "$ROOT/docs/Progress/days/day5/day5_card.py" "$NEWROOT/docs/Progress/days/day5"
safe_move "$ROOT/docs/Progress/days/day6/day6_card.py" "$NEWROOT/docs/Progress/days/day6"
safe_move "$ROOT/docs/Progress/days/day7/day7_card.py" "$NEWROOT/docs/Progress/days/day7"

# top-level files: README, PHILOSOPHY, etc.
safe_move "$ROOT/README.md" "$NEWROOT"
safe_move "$ROOT/PHILOSOPHY.md" "$NEWROOT"
safe_move "$ROOT/README.structure.md" "$NEWROOT/docs/design" 2>/dev/null || true

# 3) Create placeholder files for Layers & example rules we discussed (Weak_early etc.)
log "Creating placeholder rule files and placeholders for layers..."

cat > "$NEWROOT/docs/design/00_SYSTEM_MAP.md" <<'EOF'
MarketAI final map — autogenerated.
Refer to docs/operations/work_system and src/ for block/layer implementation.
EOF

# example DNA phase placeholders
for phase in Absorption Discrepancy Exhausion Release; do
  if [ ! -f "$NEWROOT/docs/DNA/Phases/${phase}.md" ]; then
    cat > "$NEWROOT/docs/DNA/Phases/${phase}.md" <<EOF
# ${phase}
Placeholder file for ${phase} phase description, indicators, rules, and examples.
- description: ...
- indicators: DWAM, MX, CVD, Volume Profile
- rules: ...
EOF
    log "created placeholder -> docs/DNA/Phases/${phase}.md"
  fi
done

# create some example micro-rules such as "Weak_early" and "Cluster_candle_volume_profile"
RULES_DIR="$NEWROOT/src/mx/rules"
ensure_dir "$RULES_DIR"
cat > "$RULES_DIR/weak_early.md" <<'EOF'
# Weak_early rule
Definition: early weakness in futures with spot lag. Use as bias filter (short).
Signals:
 - futures_angle_decline > 8deg and spot_angle_decline < 4deg
 - delta_shift indicates selling pressure
EOF

cat > "$RULES_DIR/cluster_candle_volume_profile.md" <<'EOF'
# Cluster Candle + Volume Profile confirmation
Rule:
 - large candle closes above high-volume node -> bullish confirmation
 - require multi-timeframe confirmation (e.g., 1H and 4H)
EOF

log "created sample rules: weak_early.md, cluster_candle_volume_profile.md"

# 4) If old top-level folders exist, move them into archive inside NEWROOT for reference
ARCHIVE_DIR="$NEWROOT/_OLD_PROJECT_ARCHIVE_${TIMESTAMP}"
ensure_dir "$ARCHIVE_DIR"
for check in "MarketAi" "MarketAI" "MarketAi_V3" "MarketAI.zip" "MarketAI.zip"; do
  if [ -e "$ROOT/$check" ] && [ "$ROOT/$check" != "$NEWROOT" ]; then
    mv "$ROOT/$check" "$ARCHIVE_DIR/"
    log "archived $ROOT/$check -> $ARCHIVE_DIR/"
  fi
done

# 5) Generate a README summary in the new root if missing
if [ ! -f "$NEWROOT/README.md" ]; then
  cat > "$NEWROOT/README.md" <<EOF
# MarketAI_V3

This folder is the reorganized version of the MarketAI project.
Structure: src/ -> Root Engines (structure, microstructure, intent, execution)
Agents: agents/ (structure_agent.py, micro_agent.py, intent_agent.py)

If you need to restore a moved file, check _OLD_PROJECT_ARCHIVE_${TIMESTAMP}/
EOF
  log "created $NEWROOT/README.md"
fi

# 6) Print final tree (if tree command installed)
log "Organization complete. Final project tree (top 6 levels):"
if command -v tree >/dev/null 2>&1; then
  tree -L 4 "$NEWROOT" || true
else
  find "$NEWROOT" -maxdepth 4 -type d -print | sed 's|'"$NEWROOT"'||g'
fi

log "Done. Check $NEWROOT for the reorganized project."
log "If something moved unexpectedly, look into $ARCHIVE_DIR or restore from backups."
