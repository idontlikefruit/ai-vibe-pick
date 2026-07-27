#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""以 full_name 为主键，把 curated / Top-100 / Trending upsert 为规范元数据。"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
COLLECTED_AT = os.environ.get("COLLECTED_AT", "2026-07-20")

ALIAS = {
    "ggerganov/llama.cpp": "ggml-org/llama.cpp",
    "OpenInterpreter/open-interpreter": "openinterpreter/openinterpreter",
}


def key(full_name):
    return ALIAS.get(full_name, full_name).lower()


PLACEHOLDERS = {"", "—", "—(待补)", "未标注", "null", "None"}
CANON = [
    "full_name", "name", "url", "stars", "rank_top100", "trending_today",
    "trending_stars_today", "category", "ai_related", "platform", "primary_lang",
    "dev_langs", "frontend", "backend", "database", "llm_runtime", "tags",
    "license", "owner", "forks", "open_issues", "description", "sources", "last_updated",
]


def meaningful(value):
    return value is not None and str(value).strip() not in PLACEHOLDERS


def richer(current, new):
    if not meaningful(new):
        return current
    if not meaningful(current):
        return new
    return new if len(str(new)) > len(str(current)) else current


store = {}


def upsert(row, source):
    full_name = row.get("full_name", "")
    if not full_name:
        return
    canonical = ALIAS.get(full_name, full_name)
    k = key(full_name)
    target = store.setdefault(k, {field: "" for field in CANON})
    if not target["full_name"]:
        target["full_name"] = canonical
    sources = [item for item in target["sources"].split(",") if item]
    if source not in sources:
        sources.append(source)
    target["sources"] = ",".join(sources)

    mapped = dict(row)
    mapped["primary_lang"] = row.get("primary_lang") or row.get("language", "")
    mapped["open_issues"] = row.get("open_issues") or row.get("issues", "")
    mapped["rank_top100"] = (row.get("rank_top100") or row.get("rank", "")) if source == "top100" else ""

    # 人工/技术字段保留信息更丰富的值；curated 通常优于自动来源。
    for field in [
        "name", "url", "category", "platform", "primary_lang", "dev_langs", "frontend",
        "backend", "database", "llm_runtime", "tags", "license", "owner", "description",
    ]:
        target[field] = richer(target[field], mapped.get(field, ""))

    # stars 是当前快照，不取历史最大值。来源优先级：curated > top100 > trending。
    if meaningful(mapped.get("stars")):
        if source == "curated" or not meaningful(target["stars"]):
            target["stars"] = str(mapped["stars"]).replace(",", "")
        elif source == "top100" and "curated" not in target["sources"]:
            target["stars"] = str(mapped["stars"]).replace(",", "")
        elif source == "trending" and not any(s in target["sources"] for s in ("curated", "top100")):
            target["stars"] = str(mapped["stars"]).replace(",", "")

    for field in ["rank_top100", "forks", "open_issues"]:
        if meaningful(mapped.get(field)):
            target[field] = mapped[field]

    if row.get("ai_related") == "是" or source == "curated":
        target["ai_related"] = "是"
    elif not meaningful(target["ai_related"]):
        target["ai_related"] = row.get("ai_related", "否")

    if meaningful(row.get("stars_today")):
        target["trending_today"] = "是"
        target["trending_stars_today"] = str(row["stars_today"]).replace(",", "")
    elif not meaningful(target["trending_today"]):
        target["trending_today"] = "否"
    if source == "trending":
        target["trending_today"] = "是"
        if meaningful(row.get("stars_today")):
            target["trending_stars_today"] = str(row["stars_today"]).replace(",", "")
    target["last_updated"] = row.get("collected_at") or COLLECTED_AT


for row in csv.DictReader(open(os.path.join(DATA, "projects.csv"), encoding="utf-8")):
    upsert({**row, "ai_related": "是"}, "curated")
for row in csv.DictReader(open(os.path.join(DATA, "top-100-stars.csv"), encoding="utf-8")):
    upsert(row, "top100")
for row in csv.DictReader(open(os.path.join(DATA, "trending-daily.csv"), encoding="utf-8")):
    upsert({**row, "stars": row.get("total_stars", "")}, "trending")


def numeric_stars(row):
    value = str(row.get("stars", "")).replace(",", "")
    return int(value) if value.isdigit() else 0


rows = sorted(store.values(), key=numeric_stars, reverse=True)
with open(os.path.join(DATA, "projects-metadata.csv"), "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=CANON)
    writer.writeheader()
    writer.writerows(rows)

print(f"upsert 完成: 共 {len(rows)} 个项目 -> data/projects-metadata.csv")
print("AI 相关:", sum(row["ai_related"] == "是" for row in rows), "/", len(rows))
