#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 CSV 数据生成 README 中的动态区域和 Markdown 报告。"""
from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
README = ROOT / "README.md"
AS_OF = os.environ.get("COLLECTED_AT", "2026-07-27")
SHIELD_DATE = AS_OF.replace("-", "--")


def write_csv(name, rows, fields):
    with (DATA / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def rebuild_merged_ai():
    """重建 curated + Top-100 AI 子集，同时保留既有人工技术栈 enrichment。"""
    aliases = {"ggerganov/llama.cpp": "ggml-org/llama.cpp", "OpenInterpreter/open-interpreter": "openinterpreter/openinterpreter"}
    canonical = lambda name: aliases.get(name, name).lower()
    old = {canonical(row["full_name"]): row for row in read_csv("merged-ai-projects.csv")}
    curated = read_csv("projects.csv")
    top_ai = [row for row in read_csv("top-100-stars.csv") if row["ai_related"] == "是"]
    top_by = {canonical(row["full_name"]): row for row in top_ai}
    merged = {}
    fields = ["name", "full_name", "url", "stars", "rank_top100", "category", "platform", "primary_lang", "dev_langs", "frontend", "backend", "database", "llm_runtime", "tags", "license", "owner", "description", "source", "last_updated"]
    for row in curated:
        k = canonical(row["full_name"])
        top = top_by.get(k, {})
        previous = old.get(k, {})
        merged[k] = {
            "name": row["name"], "full_name": row["full_name"], "url": row["url"], "stars": row["stars"],
            "rank_top100": top.get("rank", ""), "category": row["category"], "platform": row["platform"],
            "primary_lang": row["primary_lang"], "dev_langs": row["dev_langs"], "frontend": row["frontend"],
            "backend": row["backend"], "database": row["database"], "llm_runtime": row["llm_runtime"],
            "tags": previous.get("tags") or row["primary_lang"], "license": row["license"], "owner": row["owner"],
            "description": row["description"], "source": "curated+top100" if top else "curated", "last_updated": AS_OF,
        }
    for row in top_ai:
        k = canonical(row["full_name"])
        if k in merged:
            continue
        previous = old.get(k, {})
        merged[k] = {
            "name": row["name"], "full_name": row["full_name"], "url": row["url"], "stars": row["stars"],
            "rank_top100": row["rank"], "category": previous.get("category") or "AI/Agent 生态",
            "platform": previous.get("platform") or "—(待补)", "primary_lang": row["language"],
            "dev_langs": previous.get("dev_langs") or row["language"], "frontend": previous.get("frontend") or "—",
            "backend": previous.get("backend") or "—", "database": previous.get("database") or "—",
            "llm_runtime": previous.get("llm_runtime") or "—", "tags": row["tags"],
            "license": previous.get("license") or "—(待补)", "owner": previous.get("owner") or row["full_name"].split("/")[0],
            "description": row["description"], "source": "top100", "last_updated": AS_OF,
        }
    rows = sorted(merged.values(), key=lambda row: -int(row["stars"]))
    write_csv("merged-ai-projects.csv", rows, fields)
    lines = [f"# 合并去重：知名 AI 项目总表（{len(rows)} 个）", "", f"> **采集日期**：{AS_OF} ｜ curated {len(curated)} + Top-100 AI {len(top_ai)}，按 full_name 去重。", "> **结构化数据**：[`data/merged-ai-projects.csv`](../data/merged-ai-projects.csv)（含 tags 技术栈属性）", "", "## 总表（按 Star 排序，含技术栈 tags）", "", "| # | 项目 | ⭐ Stars | 榜号 | 平台 | 主语言 | 技术栈 tags | 来源 |", "|---|------|---------|------|------|--------|------------|------|"]
    for index, row in enumerate(rows, 1):
        lines.append(f'| {index} | [{row["full_name"]}]({row["url"]}) | {int(row["stars"]):,} | {row["rank_top100"] or "—"} | {clip(row["platform"], 18)} | {row["primary_lang"]} | {clip(row["tags"], 42)} | {row["source"]} |')
    (REPORTS / "merged-ai-projects.md").write_text("\n".join(lines), encoding="utf-8")
    return rows


def read_csv(name):
    with (DATA / name).open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def clip(value, size):
    value = str(value or "—").replace("|", "/").replace("\n", " ")
    return value if len(value) <= size else value[: size - 1] + "…"


def replace_section(text, start_heading, end_heading, replacement):
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    return text[:start] + replacement.rstrip() + "\n\n---\n\n" + text[end:]


def load_delta():
    path = DATA / "top100-delta.json"
    if path.exists():
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            pass
    return {"date": AS_OF, "added": [], "removed": []}


def delta_summary(delta):
    added = delta.get("added", [])
    removed = delta.get("removed", [])
    parts = []
    if added:
        parts.append("本次新增 " + "、".join(f"`{x}`" for x in added))
    if removed:
        parts.append("移出 " + "、".join(f"`{x}`" for x in removed))
    return "；".join(parts) + "。" if parts else "本次无新进入或移出。"


def delta_bullets(delta):
    added = delta.get("added", [])
    removed = delta.get("removed", [])
    bullets = []
    if added:
        bullets.append("- **新进入 Top-100**：" + "、".join(f"[`{x}`](https://github.com/{x})" for x in added))
    if removed:
        bullets.append("- **移出 Top-100**：" + "、".join(f"[`{x}`](https://github.com/{x})" for x in removed))
    if not bullets:
        bullets.append("- 本次 Top-100 名单无新进入或移出。")
    return bullets


def top100_section(rows):
    langs = Counter(row["language"] for row in rows)
    cats = Counter(row["category"] for row in rows)
    ai_count = sum(row["ai_related"] == "是" for row in rows)
    delta = load_delta()
    lines = [
        "## 📊 全站历史总榜 Top-100 分析",
        "",
        f"> 来源：[EvanLi/Github-Ranking · Top-100-stars](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md) ｜ 采集：{AS_OF} ｜ 数据：[`data/top-100-stars.csv`](data/top-100-stars.csv) · [`data/source-top-100-stars.md`](data/source-top-100-stars.md)",
        "",
        f"**一句话结论**：GitHub 全站历史 Star 总榜前 100 里，**{ai_count} 个是 AI / Agent 生态项目**。{delta_summary(delta)}",
        "",
        "### 类别分布（人工分类，共 100）",
        "",
        "| 类别 | 数量 | 占比 |",
        "| :--- | ---: | ---: |",
    ]
    labels = [
        ("A-AI/Agent生态", "🤖 AI / Agent 生态"),
        ("B-学习资源/Awesome", "📚 学习资源 / Awesome / 书籍"),
        ("E-工具/应用/其他", "🛠️ 工具 / 应用 / 其他"),
        ("C-前端/UI框架", "🧩 前端 / UI 框架"),
        ("D-系统/运行时/语言", "⚙️ 系统 / 运行时 / 语言 / 基础设施"),
    ]
    for key, label in labels:
        count = cats[key]
        lines.append(f"| {label} | {count} | {count}% |")
    lines += ["", "### 主语言分布（精确）", "", "| 语言 | 数量 | 语言 | 数量 |", "| :--- | ---: | :--- | ---: |"]
    ordered = langs.most_common()
    half = (len(ordered) + 1) // 2
    for i in range(half):
        left = ordered[i]
        right = ordered[i + half] if i + half < len(ordered) else ("", "")
        lines.append(f"| {left[0]} | {left[1]} | {right[0]} | {right[1]} |")
    lines += ["", "<details open>", "<summary><b>📎 展开查看全部 100 个项目（含 AI 相关标注 + 框架 tags）</b></summary>", "", "| 榜号 | 项目 | ⭐ Stars | 主语言 | AI 相关 | 框架 tags | 简介 |", "| :---: | :--- | ---: | :--- | :---: | :--- | :--- |"]
    for row in sorted(rows, key=lambda item: int(item["rank"])):
        lines.append(f'| {row["rank"]} | [{row["full_name"]}]({row["url"]}) | {int(row["stars"]):,} | {row["language"]} | {row["ai_related"]} | {clip(row["tags"], 32)} | {clip(row["description"], 42)} |')
    lines += ["", "</details>", "", "### 本次更新变化", ""] + delta_bullets(delta)
    return "\n".join(lines)


def trending_section(rows):
    ai_count = sum(row["ai_related"] == "是" for row in rows)
    lines = [
        "## 🔥 Trending 今日热榜产品分析",
        "",
        f"> 来源：https://github.com/trending （全语言 daily）｜采集：{AS_OF} ｜ 数据：[`data/trending-daily.csv`](data/trending-daily.csv) · 完整分析：[`reports/trending-analysis.md`](reports/trending-analysis.md)",
        "",
        "| 项目 | ⭐ Stars | 今日 ⭐ | 主语言 | AI 相关 | 框架 tags | 简介 |",
        "| :--- | ---: | ---: | :--- | :---: | :--- | :--- |",
    ]
    for row in rows:
        lines.append(f'| [{row["full_name"]}](https://github.com/{row["full_name"]}) | {int(row["total_stars"]):,} | +{int(row["stars_today"]):,} | {row["language"]} | {row["ai_related"]} | {clip(row["tags"], 34)} | {clip(row["description"], 40)} |')
    lines += ["", f"**产品分析**：今日热榜共 **{len(rows)}** 个项目，其中 AI 相关 **{ai_count} 个（{ai_count/len(rows):.0%}）**。新热点集中在：AI Agent 工程教程、代码知识图谱/MCP、异构 LLM 推理、Voice AI、Coding Agent、Computer Use 与 GenBI。"]
    return "\n".join(lines)


def write_trending_report(rows):
    ai_count = sum(row["ai_related"] == "是" for row in rows)
    lines = ["# GitHub Trending 今日热榜产品分析", "", f"> 采集：{AS_OF} ｜ 项目：{len(rows)} ｜ AI 相关：{ai_count}（{ai_count/len(rows):.0%}）", "", "| # | 项目 | 今日⭐ | 总⭐ | 语言 | AI | tags |", "| :--: | :--- | ---: | ---: | :--- | :--: | :--- |"]
    for row in rows:
        lines.append(f'| {row["rank"]} | [{row["full_name"]}](https://github.com/{row["full_name"]}) | +{int(row["stars_today"]):,} | {int(row["total_stars"]):,} | {row["language"]} | {row["ai_related"]} | {row["tags"]} |')
    lines += ["", "## 新热点", "", "1. **AI Agent 教程与工程实践**：`ai-agent-book`、`ai-engineering-from-scratch`。", "2. **代码智能/MCP**：`code-review-graph`、`wigolo`、`copilot-sdk`。", "3. **推理与多模态**：`ktransformers`、`voicebox`、`airllm`。", "4. **Coding Agent / Computer Use**：`jcode`、`kimi-cli`、`cua`。", "5. **AI 数据产品**：`WrenAI`（Text-to-SQL / GenBI）。"]
    (REPORTS / "trending-analysis.md").write_text("\n".join(lines), encoding="utf-8")


def write_metadata_reports(top100, metadata):
    lines = ["# Top-100 项目完整元数据（100 个）", "", f"> 采集：{AS_OF} ｜ 数据：[`data/top-100-stars.csv`](../data/top-100-stars.csv)", ""]
    for row in top100:
        lines += [f'## #{row["rank"]} {row["name"]}', "", f'> {row["description"]}', "", "| 字段 | 值 |", "| :--- | :--- |", f'| 仓库 | [{row["full_name"]}]({row["url"]}) |', f'| Stars / Forks | {int(row["stars"]):,} / {int(row["forks"]):,} |', f'| 主语言 / AI | {row["language"]} / {row["ai_related"]} |', f'| 类别 | {row["category"]} |', f'| tags | {row["tags"]} |', "", "---", ""]
    (REPORTS / "top-100-metadata.md").write_text("\n".join(lines), encoding="utf-8")

    lines = [f"# 全部项目元数据（{len(metadata)} 个）", "", f"> upsert 规范化存储 ｜ 采集：{AS_OF} ｜ 数据：[`data/projects-metadata.csv`](../data/projects-metadata.csv)", ""]
    for index, row in enumerate(metadata, 1):
        lines += [f'## {index}. {row["name"] or row["full_name"].split("/")[-1]}', "", f'> {row["description"]}', "", "| 字段 | 值 |", "| :--- | :--- |", f'| 仓库 | [{row["full_name"]}]({row["url"]}) |', f'| Stars | {int(row["stars"]):,} |' if row["stars"].isdigit() else '| Stars | — |', f'| Top-100 / Trending | {row["rank_top100"] or "—"} / {row["trending_today"]} |', f'| 类别 / AI | {row["category"] or "—"} / {row["ai_related"]} |', f'| 前端 / 后端 | {row["frontend"] or "—"} / {row["backend"] or "—"} |', f'| 数据库 / LLM | {row["database"] or "—"} / {row["llm_runtime"] or "—"} |', f'| tags | {row["tags"] or "—"} |', f'| 来源 | {row["sources"]} |', "", "---", ""]
    (REPORTS / "all-projects-metadata.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    merged_ai = rebuild_merged_ai()
    top100 = read_csv("top-100-stars.csv")
    trending = read_csv("trending-daily.csv")
    metadata = read_csv("projects-metadata.csv")
    text = README.read_text(encoding="utf-8")
    text = replace_section(text, "## 📊 全站历史总榜 Top-100 分析", "## 🔥 Trending 今日热榜产品分析", top100_section(top100))
    text = replace_section(text, "## 🔥 Trending 今日热榜产品分析", "## 🏷️ 技术栈 tags（新属性）", trending_section(trending))
    n = len(metadata)
    ai = sum(row["ai_related"] == "是" for row in metadata)
    ai100 = sum(row["ai_related"] == "是" for row in top100)
    # 徽章
    text = re.sub(r"data%20as%20of-[\d]+--[\d]+--[\d]+", f"data%20as%20of-{SHIELD_DATE}", text)
    text = re.sub(r"projects-\d+-blue", f"projects-{n}-blue", text)
    text = re.sub(r"Top--100_AI-\d+", f"Top--100_AI-{ai100}", text)
    # 各处计数（幂等：用正则匹配任意旧数字）
    text = re.sub(r"\d+ 个真实 GitHub 项目（其中 AI 相关 \d+ 个）", f"{n} 个真实 GitHub 项目（其中 AI 相关 {ai} 个）", text)
    text = re.sub(r"全部项目元数据（\d+ 个）", f"全部项目元数据（{n} 个）", text)
    text = re.sub(r"全部项目元数据\d+-个", f"全部项目元数据{n}-个", text)
    text = re.sub(r"全部 \d+ 个见 reports/all-projects-metadata\.md", f"全部 {n} 个见 reports/all-projects-metadata.md", text)
    text = re.sub(r"规范化元数据存储\(\d+ 个", f"规范化元数据存储({n} 个", text)
    text = re.sub(r"规范化元数据存储 \d+ 个", f"规范化元数据存储 {n} 个", text)
    text = re.sub(r"\d+ 个项目完整元数据卡片", f"{n} 个项目完整元数据卡片", text)
    text = re.sub(r"全部 \d+ 个项目元数据卡片", f"全部 {n} 个项目元数据卡片", text)
    text = re.sub(r"共 \*\*\d+ 个\*\*，其中 AI 相关 \d+ 个、Top-100 项目 \d+ 个、今日 Trending 项目 \d+ 个", f"共 **{n} 个**，其中 AI 相关 {ai} 个、Top-100 项目 {len(top100)} 个、今日 Trending 项目 {len(trending)} 个", text)
    text = re.sub(r"（\d+ \+ 100）", f"（{n} + 100）", text)
    text = re.sub(r"Trending 今日热榜\(\d+ 个", f"Trending 今日热榜({len(trending)} 个", text)
    text = re.sub(r"Trending 今日热榜 \d+ 个", f"Trending 今日热榜 {len(trending)} 个", text)
    README.write_text(text, encoding="utf-8")
    write_trending_report(trending)
    write_metadata_reports(top100, metadata)
    print(f"生成完成: README + reports，metadata={len(metadata)}, trending={len(trending)}")


if __name__ == "__main__":
    main()
