#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""刷新 GitHub 数据源，同时保留人工分类和技术栈字段。

刷新：
- EvanLi/Github-Ranking Top-100（排名、stars、forks、语言、issues、描述、提交时间）
- GitHub Trending daily（当日快照 + 仓库 API 元数据）
- curated 项目的易变 GitHub 字段（stars、主语言、仓库规范名/URL）

人工字段（category / ai_related / tags / 前后端技术栈）不会被 API 自动覆盖。
"""
from __future__ import annotations

import csv
import html
import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
COLLECTED_AT = os.environ.get("COLLECTED_AT", "2026-07-20")

TOP100_URL = "https://raw.githubusercontent.com/EvanLi/Github-Ranking/master/Top100/Top-100-stars.md"
TRENDING_URL = "https://github.com/trending"

# 新进入 Top-100 的仓库需要人工分类；已有仓库沿用 CSV 中的人工字段。
TOP100_OVERRIDES = {
    "immich-app/immich": {
        "category": "E-工具/应用/其他",
        "ai_related": "否",
        "tags": "TypeScript, Svelte, PostgreSQL, Redis, Docker",
    },
    "nextlevelbuilder/ui-ux-pro-max-skill": {
        "category": "A-AI/Agent生态",
        "ai_related": "是",
        "tags": "Claude Code, UI/UX, 设计技能",
    },
}

# Trending 是每日快照，新仓库按产品属性人工标注（每次刷新后需按当日榜单更新）。
TRENDING_OVERRIDES = {
    "permissionlesstech/bitchat": ("否", "Swift, Bluetooth Mesh, 聊天"),
    "citrolabs/ego-lite": ("是", "JavaScript, AI Agent, Web 自动化, 浏览器"),
    "block/buzz": ("否", "Rust, 通信平台"),
    "pingdotgg/t3code": ("否", "TypeScript, 开发工具"),
    "CoreBunch/Instatic": ("否", "TypeScript, React, 网站构建"),
    "yorukot/superfile": ("否", "Go, TUI, 文件管理"),
    "nodejs/node": ("否", "JavaScript, C++, 运行时"),
    "OtterMind/Chat2DB": ("是", "Java, AI, Text-to-SQL, 数据库"),
    "pbakaus/impeccable": ("是", "JavaScript, AI Harness, 设计"),
    "shiyu-coder/Kronos": ("是", "Python, Foundation Model, 金融, 时间序列"),
    "alibaba/open-code-review": ("是", "Go, AI, 代码审查"),
    "andrewyng/aisuite": ("是", "Python, LLM, 多模型接口"),
    "anthropics/claude-cookbooks": ("是", "Jupyter, Python, Claude, 教程"),
    "Pumpkin-MC/Pumpkin": ("否", "Rust, Minecraft, 游戏服务器"),
    "permissionlesstech/bitchat-android": ("否", "Kotlin, Android, Bluetooth Mesh"),
    "jenkinsci/jenkins": ("否", "Java, CI/CD"),
    "amnezia-vpn/amnezia-client": ("否", "C++, VPN, 网络"),
}


def fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-fsSL", "-A", "ai-vibe-pick-refresh", url]).decode("utf-8")


def gh_repo(full_name: str) -> dict:
    output = subprocess.check_output(["gh", "api", f"repos/{full_name}"], stderr=subprocess.DEVNULL)
    return json.loads(output)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def refresh_top100() -> tuple[int, list[str], list[str]]:
    previous = {row["full_name"]: row for row in read_csv(DATA / "top-100-stars.csv")}
    source = fetch(TOP100_URL)
    (DATA / "source-top-100-stars.md").write_text(source, encoding="utf-8")
    pattern = re.compile(
        r"\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|$"
    )
    rows = []
    for line in source.splitlines():
        match = pattern.match(line)
        if not match:
            continue
        rank, name, url, stars, forks, language, issues, description, last_commit = match.groups()
        full_name = url.split("github.com/", 1)[-1]
        old = previous.get(full_name, {})
        manual = TOP100_OVERRIDES.get(full_name, {})
        rows.append({
            "rank": rank,
            "name": name,
            "full_name": full_name,
            "url": url,
            "stars": stars.replace(",", ""),
            "forks": forks.replace(",", ""),
            "language": "未标注" if language == "None" else language,
            "category": old.get("category") or manual.get("category", "E-工具/应用/其他"),
            "issues": issues.replace(",", ""),
            "description": description,
            "last_commit": last_commit,
            "ai_related": old.get("ai_related") or manual.get("ai_related", "否"),
            "tags": old.get("tags") or manual.get("tags", language if language != "None" else "未标注"),
        })
    if len(rows) != 100:
        raise RuntimeError(f"Top-100 解析到 {len(rows)} 行，预期 100")
    fields = ["rank", "name", "full_name", "url", "stars", "forks", "language", "category", "issues", "description", "last_commit", "ai_related", "tags"]
    write_csv(DATA / "top-100-stars.csv", rows, fields)
    current = {row["full_name"] for row in rows}
    old_names = set(previous)
    return sum(row["ai_related"] == "是" for row in rows), sorted(current - old_names), sorted(old_names - current)


def refresh_trending() -> int:
    page = fetch(TRENDING_URL)
    articles = re.findall(r'<article class="Box-row".*?</article>', page, re.S)
    rows = []
    for article in articles:
        repo_match = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^/]+/[^"]+)"', article, re.S)
        if not repo_match:
            continue
        full_name = repo_match.group(1).strip()
        desc_match = re.search(r'<p class="col-9[^"]*"[^>]*>\s*(.*?)\s*</p>', article, re.S)
        description = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", desc_match.group(1)))).strip() if desc_match else ""
        lang_match = re.search(r'itemprop="programmingLanguage"[^>]*>\s*(.*?)\s*<', article, re.S)
        language = lang_match.group(1).strip() if lang_match else "未标注"
        today_match = re.search(r"([\d,]+)\s*stars?\s+today", article)
        api = gh_repo(full_name)
        ai_related, tags = TRENDING_OVERRIDES.get(full_name, ("否", language))
        rows.append({
            "rank": len(rows) + 1,
            "full_name": full_name,
            "name": full_name.split("/", 1)[-1],
            "description": description,
            "language": language,
            "stars_today": today_match.group(1).replace(",", "") if today_match else "",
            "total_stars": api.get("stargazers_count", ""),
            "ai_related": ai_related,
            "tags": tags,
            "license": (api.get("license") or {}).get("spdx_id") or "NOASSERTION",
            "collected_at": COLLECTED_AT,
        })
    fields = ["rank", "full_name", "name", "description", "language", "stars_today", "total_stars", "ai_related", "tags", "license", "collected_at"]
    write_csv(DATA / "trending-daily.csv", rows, fields)
    return sum(row["ai_related"] == "是" for row in rows)


def refresh_curated() -> int:
    rows = read_csv(DATA / "projects.csv")
    changed = 0
    for row in rows:
        try:
            api = gh_repo(row["full_name"])
        except subprocess.CalledProcessError:
            continue
        before = row.get("stars", "")
        canonical = api.get("full_name", row["full_name"])
        row["full_name"] = canonical
        row["url"] = api.get("html_url", row.get("url", ""))
        row["stars"] = str(api.get("stargazers_count", before))
        row["primary_lang"] = api.get("language") or row.get("primary_lang", "")
        row["owner"] = api.get("owner", {}).get("login") or row.get("owner", "")
        if row["stars"] != before:
            changed += 1
    fields = list(rows[0].keys())
    write_csv(DATA / "projects.csv", rows, fields)
    return changed


def main() -> None:
    ai_count, added, removed = refresh_top100()
    trending_ai = refresh_trending()
    curated_changed = refresh_curated()
    with open(DATA / "top100-delta.json", "w", encoding="utf-8") as fh:
        json.dump({"date": COLLECTED_AT, "added": added, "removed": removed}, fh, ensure_ascii=False, indent=2)
    print(f"Top-100: 100 个，AI 相关 {ai_count} 个；新增 {added or '无'}；移出 {removed or '无'}")
    trending_count = len(read_csv(DATA / "trending-daily.csv"))
    print(f"Trending: {trending_count} 个，AI 相关 {trending_ai} 个")
    print(f"Curated: {curated_changed} 个项目 star 有变化")


if __name__ == "__main__":
    main()
