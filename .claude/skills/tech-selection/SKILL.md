---
name: tech-selection
description: 根据"用户将要建立的项目 + 项目描述"，结合本仓库已有的 140 个 GitHub 项目元数据（其中 AI 相关 64 个，data/projects-metadata.csv），推荐前后端/数据库/LLM/部署等技术选型。当用户描述要新建的 AI 项目并询问"用什么技术/怎么选型"时使用。
---

# AI 技术选型助手

当用户给出"我要做一个 X 项目"并希望得到技术选型建议时，按本流程执行。核心原则：**所有推荐都引用本仓库里真实项目的栈，不凭空编造。**

## 数据来源（必读）

- `data/projects-metadata.csv` —— 规范化元数据存储（140 个项目，其中 AI 相关 64 个；upsert 生成），字段含：
  `full_name, stars, rank_top100, trending_today, category, ai_related, platform, primary_lang, dev_langs, frontend, backend, database, llm_runtime, tags, license, owner, sources`
- `reports/summary.md` —— 已有的主语言/前端/后端/数据库分布统计与选型要点
- `reports/trending-analysis.md` —— 当前风口（Claude Code Skills、垂直 Agent）

## 执行步骤

### 1. 澄清项目画像（若用户未给出则主动问，最多 3-4 个关键问题）

- **项目类型**：LLM 应用平台 / 聊天界面 / 编程助手 / Agent 框架 / RAG 知识库 / 模型推理 / 向量库 / 其他
- **部署形态**：自托管 / 云 SaaS / 桌面 / IDE 插件 / CLI / 纯库
- **规模与团队**：个人 / 小团队；团队熟悉的语言（Python / TS / Go / Rust）
- **关键能力**：是否需 RAG、工作流编排、多模型接入、本地推理、多租户

### 2. 从数据里找"同类参考项目"

用脚本/工具在 `data/projects-metadata.csv` 中按 `ai_related=是` + 类型/平台关键词筛选，挑出 **3-5 个最相似** 的真实项目，记录它们的 `frontend / backend / database / llm_runtime / tags`。

示例筛选（用 shell）：
```bash
# 找"LLM 应用平台"类
awk -F, 'NR==1{for(i=1;i<=NF;i++)h[$i]=i} NR>1 && $h["ai_related"]=="是"' data/projects-metadata.csv | grep -iE "平台|workflow|RAG"
```

### 3. 给出推荐选型表

输出一个 Markdown 表，每个维度给出 **推荐项 + 理由 + 参考项目**：

| 维度 | 推荐 | 理由（引用真实项目） |
|------|------|----------------------|
| 主语言 | … | …（例：n8n/dify 用 TS 做前端 + …） |
| 前端框架 | … | … |
| 后端框架 | … | … |
| 数据库 | … | … |
| LLM/推理 | … | … |
| 部署 | … | … |

### 4. 默认经验基线（数据验证过的主流组合，可直接套用）

- **LLM 应用平台**：Next.js+React / Python(FastAPI 或 Flask) / PostgreSQL+Redis+向量库 / 多模型兼容 OpenAI —— 参考 dify、langflow、FastGPT、Flowise
- **AI 聊天前端**：Next.js+React（LobeHub 风格）或 SvelteKit（Open WebUI 风格）
- **编程助手**：IDE 插件用 TypeScript（Continue）；自托管推理用 Rust（Tabby）；CLI 用 Python（Aider）
- **高性能/基础设施**：Rust/Go/C++ —— 参考 ollama、vLLM、llama.cpp、Qdrant
- **多 Agent 编排**：用 LangChain / CrewAI / AutoGen 作后端库，前端另搭

### 5. 给替代方案 + 风险提示

- 列 1-2 个备选栈（如团队不熟 Python 时的 Node 全栈方案：Next.js API + MongoDB，参考 FastGPT）
- 提示数据中观察到的坑：部分高 star 仓库（openclaw/claw-code/ECC 等）为 Agent Skills 配置类，star 受热度影响，**不应作为工程选型依据**，选型优先看工程级项目（dify/langchain/ollama/vLLM 等）

## 输出格式

最终回复用中文，结构：
1. **项目画像**（复述确认）
2. **推荐选型表**
3. **参考项目**（带 GitHub 链接 + 其栈摘要）
4. **替代方案与风险提示**

> 注：本 skill 依赖 `data/projects-metadata.csv` 存在；若不存在，先运行 `python3 scripts/upsert_metadata.py` 生成。
