#!/bin/bash
# 每日数据刷新：Top-100 / Trending / curated → upsert → 生成报告 → 提交并推送。
# 由 launchd 在每天早上 7 点调用（也可手动运行）。
set -uo pipefail

# launchd 的 PATH 很精简，显式补上 Homebrew 路径
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

REPO_DIR="/Users/xukun/PycharmProject/AI选型/ai-github-projects-stats"
cd "$REPO_DIR" || { echo "无法进入仓库目录"; exit 1; }

export COLLECTED_AT="$(date +%Y-%m-%d)"
LOG="$REPO_DIR/scripts/refresh.log"

{
  echo "===== 刷新开始 $(date '+%Y-%m-%d %H:%M:%S') (COLLECTED_AT=$COLLECTED_AT) ====="

  python3 scripts/refresh_sources.py   || { echo "refresh_sources 失败"; exit 1; }
  python3 scripts/upsert_metadata.py   || { echo "upsert_metadata 失败"; exit 1; }
  python3 scripts/generate_reports.py  || { echo "generate_reports 失败"; exit 1; }

  echo "--- 提交并推送 ---"
  # 磁盘保护：可用空间不足 500MB 时只刷新本地、不提交，避免再次写满磁盘
  FREE_MB=$(df -k . | tail -1 | awk '{print int($4/1024)}')
  if [ "$FREE_MB" -lt 500 ]; then
    echo "可用空间仅 ${FREE_MB}MB（<500MB），跳过提交/推送，仅保留本地刷新。"
    echo "===== 刷新结束 $(date '+%Y-%m-%d %H:%M:%S') ====="
    exit 0
  fi

  git add -A
  if git diff --cached --quiet; then
    echo "无变化，跳过提交。"
  else
    git commit -m "chore: 每日数据刷新 $COLLECTED_AT (Top-100/Trending/curated)" \
      && git push origin main \
      && echo "已提交并推送。" \
      || echo "提交/推送失败（数据已在本地刷新）。"
  fi

  echo "===== 刷新结束 $(date '+%Y-%m-%d %H:%M:%S') ====="
} >> "$LOG" 2>&1
