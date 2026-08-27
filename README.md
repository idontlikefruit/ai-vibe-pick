<div align="center">

# 🤖 AI GitHub 知名项目技术选型统计

**统计 GitHub 知名 AI 项目的技术选型：类型 · 前后端 · 数据库 · LLM · 技术栈 tags**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Projects](https://img.shields.io/badge/projects-142-blue.svg)
![Top100](https://img.shields.io/badge/Top--100_AI-33-orange.svg)
![Stars](https://img.shields.io/github/stars/idontlikefruit/ai-vibe-pick?style=social)
![Last Commit](https://img.shields.io/github/last-commit/idontlikefruit/ai-vibe-pick)
![Data](https://img.shields.io/badge/data%20as%20of-2026--08--28-brightgreen)

</div>

---

## 🧭 AI 技术选型助手（Skill）

> 告诉我你要做什么项目，我基于本仓库 **142 个真实 GitHub 项目（其中 AI 相关 71 个）** 的技术栈数据，给你一套有据可依的选型推荐（不凭空编造，每个推荐都引用真实项目）。

### 怎么用

**方式一（推荐）**：直接描述你的项目，例如：

> 我要做一个企业内部知识库问答平台，需要 RAG + 工作流编排，自托管，团队熟 Python，预计支持多租户。帮我选型。

我会自动调用 `tech-selection` skill，从 `data/projects-metadata.csv` 里筛同类项目（dify / langflow / FastGPT / Quivr …），给出「主语言 / 前端 / 后端 / 数据库 / LLM / 部署」推荐表 + 参考项目 + 替代方案 + 风险提示。

**方式二**：显式触发 `/tech-selection`，再补充项目描述。

### Skill 位置

- 定义文件：[`.claude/skills/tech-selection/SKILL.md`](.claude/skills/tech-selection/SKILL.md)
- 依赖数据：`data/projects-metadata.csv`（若不存在，先 `python3 scripts/upsert_metadata.py` 生成）
- 默认经验基线（数据验证过）：
  - LLM 应用平台 → `Next.js+React` / `Python(FastAPI/Flask)` / `PostgreSQL+Redis+向量库` / 多模型兼容 OpenAI（参考 dify、langflow、FastGPT、Flowise）
  - AI 聊天前端 → `Next.js+React`(LobeHub) 或 `SvelteKit`(Open WebUI)
  - 编程助手 → IDE 插件用 TypeScript(Continue)；自托管推理用 Rust(Tabby)；CLI 用 Python(Aider)
  - 高性能/基础设施 → Rust/Go/C++（ollama / vLLM / llama.cpp / Qdrant）

---

## 📑 目录

- [🧭 AI 技术选型助手（Skill）](#-ai-技术选型助手skill)
- [📊 全站历史总榜 Top-100 分析](#-全站历史总榜-top-100-分析)
- [🔥 Trending 今日热榜产品分析](#-trending-今日热榜产品分析)
- [🏷️ 技术栈 tags（新属性）](#️-技术栈-tags新属性)
- [📋 全部项目元数据（142 个）](#-全部项目元数据142-个)
- [📁 目录结构](#-目录结构)
- [📦 数据文件](#-数据文件)
- [🗺️ 采集字段](#️-采集字段)
- [📈 统计维度](#-统计维度)
- [🔧 采集流程](#-采集流程)

---

## 📊 全站历史总榜 Top-100 分析

> 来源：[EvanLi/Github-Ranking · Top-100-stars](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md) ｜ 采集：2026-08-28 ｜ 数据：[`data/top-100-stars.csv`](data/top-100-stars.csv) · [`data/source-top-100-stars.md`](data/source-top-100-stars.md)

**一句话结论**：GitHub 全站历史 Star 总榜前 100 里，**33 个是 AI / Agent 生态项目**。本次无新进入或移出。

### 类别分布（人工分类，共 100）

| 类别 | 数量 | 占比 |
| :--- | ---: | ---: |
| 🤖 AI / Agent 生态 | 33 | 33% |
| 📚 学习资源 / Awesome / 书籍 | 25 | 25% |
| 🛠️ 工具 / 应用 / 其他 | 21 | 21% |
| 🧩 前端 / UI 框架 | 12 | 12% |
| ⚙️ 系统 / 运行时 / 语言 / 基础设施 | 9 | 9% |

### 主语言分布（精确）

| 语言 | 数量 | 语言 | 数量 |
| :--- | ---: | :--- | ---: |
| Python | 24 | C | 3 |
| TypeScript | 17 | HTML | 3 |
| 未标注 | 13 | Jupyter Notebook | 2 |
| JavaScript | 10 | Batchfile | 1 |
| Shell | 5 | Dart | 1 |
| C++ | 5 | MDX | 1 |
| Rust | 5 | Java | 1 |
| Go | 4 | C# | 1 |
| Markdown | 3 | Swift | 1 |

<details open>
<summary><b>📎 展开查看全部 100 个项目（含 AI 相关标注 + 框架 tags）</b></summary>

| 榜号 | 项目 | ⭐ Stars | 主语言 | AI 相关 | 框架 tags | 简介 |
| :---: | :--- | ---: | :--- | :---: | :--- | :--- |
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 543,243 | Markdown | 否 | 教程 | Master programming by recreating your fav… |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 500,281 | 未标注 | 否 | Awesome 清单 | 😎 Awesome lists about all kinds of intere… |
| 3 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 471,147 | Python | 否 | API 清单 | A collective list of free APIs |
| 4 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 454,643 | TypeScript | 否 | React, Node.js | freeCodeCamp.org's open-source codebase a… |
| 5 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 395,282 | Python | 否 | 书籍 | :books: Freely available programming books |
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 387,740 | TypeScript | 是 | TypeScript | Your own personal AI assistant. Any OS. A… |
| 7 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 366,268 | Python | 否 | 教程 | Learn how to design large-scale systems. … |
| 8 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 365,532 | TypeScript | 否 | Next.js, React | Interactive roadmaps, guides and other ed… |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 359,813 | 未标注 | 否 | 教程 | A complete computer science study plan to… |
| 10 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 316,299 | Python | 否 | Awesome 清单 | The definitive list that answers "I want … |
| 11 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 315,447 | 未标注 | 否 | Awesome 清单 | A list of Free Software network services … |
| 12 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 281,006 | Python | 否 | 教程 | Curated list of project-based tutorials |
| 13 | [obra/superpowers](https://github.com/obra/superpowers) | 278,190 | Shell | 是 | Shell, Claude Code | An agentic skills framework & software de… |
| 14 | [996icu/996.ICU](https://github.com/996icu/996.ICU) | 276,784 | 未标注 | 否 | 社会议题 | Repo for counting stars and contributing.… |
| 15 | [react/react](https://github.com/react/react) | 247,909 | JavaScript | 否 | React | The library for web and native user inter… |
| 16 | [torvalds/linux](https://github.com/torvalds/linux) | 244,514 | C | 否 | C, Linux 内核 | Linux kernel source tree |
| 17 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 243,557 | JavaScript | 是 | JavaScript, Claude Code, Codex | The agent harness performance optimizatio… |
| 18 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 240,554 | 未标注 | 否 | 清单 | A collection of inspiring lists, manuals,… |
| 19 | [mattpocock/skills](https://github.com/mattpocock/skills) | 238,116 | Shell | 是 | Shell, Claude Code | Skills for Real Engineers. Straight from … |
| 20 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 236,958 | Python | 是 | Python | The agent that grows with you |
| 21 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,050 | Python | 否 | Python, 算法 | All Algorithms implemented in Python |
| 22 | [vuejs/vue](https://github.com/vuejs/vue) | 210,691 | TypeScript | 否 | Vue 2 | This is the repo for Vue 2. For Vue 3, go… |
| 23 | [ossu/computer-science](https://github.com/ossu/computer-science) | 208,440 | HTML | 否 | 教程 | 🎓 Path to a free self-taught education in… |
| 24 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 207,767 | 未标注 | 是 | 未标注, Claude Code | A single CLAUDE.md file to improve Claude… |
| 25 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 202,540 | TypeScript | 是 | TypeScript, Vue 3, Vue Flow, Pr… | Fair-code workflow automation platform wi… |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 201,755 | TypeScript | 是 | TypeScript, Node.js | The open source coding agent. |
| 27 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 198,416 | TypeScript | 否 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| 28 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 197,641 | C++ | 是 | C, Python | An Open Source Machine Learning Framework… |
| 29 | [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 196,567 | JavaScript | 否 | JavaScript, 算法 | 📝 Algorithms and data structures implemen… |
| 30 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | 195,890 | Markdown | 否 | HTML | Free domain registration and practical DN… |
| 31 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 195,116 | Rust | 是 | Rust | An agent-managed museum exhibit, built in… |
| 32 | [microsoft/vscode](https://github.com/microsoft/vscode) | 189,634 | TypeScript | 否 | TypeScript, Electron | Visual Studio Code |
| 33 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,398 | Shell | 否 | Shell, Zsh | 🙃   A delightful community-driven (with 2… |
| 34 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 188,395 | Batchfile | 否 | Batchfile | Open-source Windows and Office activator … |
| 35 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 187,205 | Python | 否 | Python | A feature-rich command-line audio/video d… |
| 36 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 186,910 | Python | 是 | Python, Next.js, React, FastAPI… | AutoGPT is the vision of accessible AI fo… |
| 37 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 185,677 | 未标注 | 否 | 面试 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络… |
| 38 | [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 185,647 | Jupyter Notebook | 否 | Jupyter, Python | Python - 100天从新手到大师 |
| 39 | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | 184,742 | 未标注 | 否 | 书籍 | A book series (2 published editions) on t… |
| 40 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 182,372 | Go | 否 | Awesome 清单 | A curated list of awesome Go frameworks, … |
| 41 | [ollama/ollama](https://github.com/ollama/ollama) | 179,525 | Go | 是 | Go, CLI, llama.cpp | Get up and running with Kimi-K2.6, GLM-5.… |
| 42 | [flutter/flutter](https://github.com/flutter/flutter) | 178,665 | Dart | 否 | Dart, Flutter | Flutter makes it easy and fast to build b… |
| 43 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 176,514 | Python | 是 | Python | Python tool for converting files and offi… |
| 44 | [github/gitignore](https://github.com/github/gitignore) | 175,467 | 未标注 | 否 | 模板 | A collection of useful .gitignore templat… |
| 45 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,658 | MDX | 否 | Bootstrap, JavaScript | The most popular HTML, CSS, and JavaScrip… |
| 46 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 173,160 | Python | 否 | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share in… |
| 47 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 172,877 | TypeScript | 是 | TypeScript, Next.js, Node.js | The context API to search, scrape, and in… |
| 48 | [anthropics/skills](https://github.com/anthropics/skills) | 171,881 | Python | 是 | Python, Claude | Public repository for Agent Skills |
| 49 | [f/prompts.chat](https://github.com/f/prompts.chat) | 168,009 | HTML | 是 | HTML, ChatGPT | f.k.a. Awesome ChatGPT Prompts. Share, di… |
| 50 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,676 | Python | 是 | Python, Gradio, FastAPI, 本地文件, … | Stable Diffusion web UI |
| 51 | [huggingface/transformers](https://github.com/huggingface/transformers) | 164,481 | Python | 是 | Python | 🤗 Transformers: the model-definition fram… |
| 52 | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | 162,177 | 未标注 | 否 | 清单 | Master the command line, in one page |
| 53 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 158,050 | JavaScript | 否 | Java, 面试 | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统… |
| 54 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 153,722 | Python | 是 | Python, React, FastAPI, SQLite,… | Langflow is a powerful tool for building … |
| 55 | [langgenius/dify](https://github.com/langgenius/dify) | 153,611 | TypeScript | 是 | TypeScript, Next.js, React, Tai… | Build Agentic workflows, RAG pipelines, w… |
| 56 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 150,052 | Python | 是 | Python, SvelteKit, FastAPI, SQL… | User-friendly AI Interface (Supports Olla… |
| 57 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 148,339 | C | 否 | C, Android | Display and control your Android device |
| 58 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 148,262 | Shell | 是 | Shell | A complete AI agency at your fingertips -… |
| 59 | [airbnb/javascript](https://github.com/airbnb/javascript) | 148,136 | JavaScript | 否 | JavaScript, 风格指南 | JavaScript Style Guide |
| 60 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 145,088 | Python | 是 | Python | The agent engineering platform. |
| 61 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 143,163 | 未标注 | 是 | 未标注 | FULL Augment Code, Claude Code, Cluely, C… |
| 62 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 143,107 | Python | 是 | Python, Claude | Claude Code is an agentic coding tool tha… |
| 63 | [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 142,193 | TypeScript | 否 | React, TypeScript | Curated coding interview preparation mate… |
| 64 | [vercel/next.js](https://github.com/vercel/next.js) | 141,952 | JavaScript | 否 | Next.js, React, JavaScript | The React Framework |
| 65 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141,039 | Python | 否 | Python | Command-line program to download videos f… |
| 66 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 140,368 | TypeScript | 否 | Tauri, TypeScript | A modern GUI client based on Tauri, desig… |
| 67 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 138,143 | C | 否 | C++, C# | Microsoft PowerToys is a collection of ut… |
| 68 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 136,804 | TypeScript | 否 | TypeScript | Collection of publicly available IPTV cha… |
| 69 | [golang/go](https://github.com/golang/go) | 136,470 | Go | 否 | Go | The Go programming language |
| 70 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | 135,470 | Markdown | 否 | 算法 | Crack LeetCode, not only how, but also wh… |
| 71 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 135,434 | HTML | 否 | 清单 | A list of SaaS, PaaS and IaaS offerings t… |
| 72 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 134,624 | Python | 是 | Python | 100+ AI Agents, Agent Skills and RAG Apps… |
| 73 | [github/spec-kit](https://github.com/github/spec-kit) | 131,723 | Python | 是 | Python | 💫 Toolkit to help you get started with Sp… |
| 74 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 130,598 | TypeScript | 否 | React, TypeScript, Canvas | Virtual whiteboard for sketching hand-dra… |
| 75 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 130,178 | Python | 是 | Python, TypeScript, 自定义节点编辑器, a… | The most powerful and modular diffusion m… |
| 76 | [garrytan/gstack](https://github.com/garrytan/gstack) | 129,899 | TypeScript | 是 | TypeScript, Claude Code | Use Garry Tan's exact Claude Code setup: … |
| 77 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 129,623 | Java | 否 | Java, 算法 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、En… |
| 78 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 129,608 | Rust | 是 | Rust, Web, Tauri, Claude, Codex… | A cross-platform desktop All-in-One assis… |
| 79 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 128,837 | JavaScript | 否 | JavaScript | Coding articles to level up your developm… |
| 80 | [react/react-native](https://github.com/react/react-native) | 126,422 | C++ | 否 | React Native, C++ | A framework for building native applicati… |
| 81 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 125,827 | C++ | 是 | C, C++, ggml | LLM inference in C/C++ |
| 82 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 125,211 | Go | 否 | Go | Production-Grade Container Scheduling and… |
| 83 | [electron/electron](https://github.com/electron/electron) | 122,736 | C++ | 否 | C++, JavaScript, Electron | :electron: Build cross-platform desktop a… |
| 84 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 122,227 | TypeScript | 否 | React, Radix UI, Tailwind | A set of beautifully-designed, accessible… |
| 85 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 121,918 | Rust | 否 | Rust, Flutter | An open-source remote desktop application… |
| 86 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 121,454 | Python | 是 | Claude Code, UI/UX, 设计技能 | An AI skill that provides design intellig… |
| 87 | [nodejs/node](https://github.com/nodejs/node) | 119,571 | JavaScript | 否 | JavaScript, C++, V8 | Node.js JavaScript runtime ✨🐢🚀✨ |
| 88 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 119,115 | 未标注 | 否 | Awesome 清单 | A collection of various awesome lists for… |
| 89 | [openai/codex](https://github.com/openai/codex) | 118,877 | Rust | 否 | Rust | Lightweight coding agent that runs in you… |
| 90 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 118,620 | Jupyter Notebook | 是 | Jupyter Notebook, Jupyter, Azur… | 21 Lessons, Get Started Building with Gen… |
| 91 | [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) | 118,523 | 未标注 | 否 | 书籍 | :books: 免费的计算机编程类中文书籍，欢迎投稿 |
| 92 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 116,964 | Python | 否 | Python | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Genera… |
| 93 | [godotengine/godot](https://github.com/godotengine/godot) | 116,191 | C++ | 否 | C++, Godot | Godot Engine – Multi-platform 2D and 3D g… |
| 94 | [rust-lang/rust](https://github.com/rust-lang/rust) | 116,190 | Rust | 否 | Rust | Empowering everyone to build reliable and… |
| 95 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 114,828 | JavaScript | 否 | WebGL, JavaScript | JavaScript 3D Library. |
| 96 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 114,751 | C# | 否 | C# | A GUI client for Windows, Linux and macOS… |
| 97 | [d3/d3](https://github.com/d3/d3) | 113,563 | Shell | 否 | JavaScript, D3 | Bring data to life with SVG, Canvas and H… |
| 98 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 112,821 | JavaScript | 否 | JavaScript | Makes your AI agent think like the lazies… |
| 99 | [immich-app/immich](https://github.com/immich-app/immich) | 112,746 | TypeScript | 否 | TypeScript, Svelte, PostgreSQL,… | High performance self-hosted photo and vi… |
| 100 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 111,860 | Swift | 否 | Awesome 清单 |  This project is dedicated to collecting… |

</details>

### 本次更新变化

- 本次 Top-100 名单无新进入或移出。

---

## 🔥 Trending 今日热榜产品分析

> 来源：https://github.com/trending （全语言 daily）｜采集：2026-08-28 ｜ 数据：[`data/trending-daily.csv`](data/trending-daily.csv) · 完整分析：[`reports/trending-analysis.md`](reports/trending-analysis.md)

| 项目 | ⭐ Stars | 今日 ⭐ | 主语言 | AI 相关 | 框架 tags | 简介 |
| :--- | ---: | ---: | :--- | :---: | :--- | :--- |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 7,886 | +1,984 | JavaScript | 否 | JavaScript, 3d-globe, cesium, fli… | A spy satellite simulator in your brows… |
| [zedeus/nitter](https://github.com/zedeus/nitter) | 13,859 | +279 | Nim | 否 | Nim, privacy, self-hosted, twitte… | Alternative Twitter front-end |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | 22,971 | +2,093 | JavaScript | 是 | JavaScript, agents, ai-image-gene… | Prompt as Code / GPT-Image2 工业级提示词引擎与模板… |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 23,041 | +4,260 | JavaScript | 是 | JavaScript, agent-skills, archite… | Agent skill for beautiful, verifiable a… |
| [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | 2,058 | +314 | Go | 是 | Go, ai-agents, coding-agent, deve… | Help AI coding agents write modern Go |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 34,673 | +290 | Python | 是 | Python, claude-code, mcp, skills | Official, Anthropic-managed directory o… |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 35,292 | +494 | Python | 是 | Python, agent-skills, ai-scientis… | Turn any AI agent into an AI Scientist.… |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 114,001 | +1,610 | JavaScript | 是 | JavaScript, agent-skills, ai-agen… | Makes your AI agent think like the lazi… |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 52,331 | +1,284 | Python | 是 | Python, agent, agentic-ai, ai, cl… | World's first open-source, agentic vide… |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 50,150 | +547 | Python | 是 | Python, agents, ai, ai-agents, ai… | Learn it. Build it. Ship it for others. |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | 11,310 | +413 | CSS | 是 | CSS, agent, claude, gpt-image-2, … | ConardLi's open-source Skills collectio… |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 92,259 | +260 | JavaScript | 是 | JavaScript, ai, ai-agents, ai-mem… | Persistent Context Across Sessions for … |
| [google/googletest](https://github.com/google/googletest) | 39,037 | +4 | C++ | 否 | C++ | GoogleTest - Google Testing and Mocking… |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 13,981 | +631 | Python | 是 | Python, agent-skills, ai-note-tak… | Self-organizing AI second brain for Obs… |
| [marin-community/marin](https://github.com/marin-community/marin) | 2,691 | +255 | Python | 是 | Python | Open-source framework for the research … |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 73,598 | +125 | Python | 是 | Python, agent-skills, ai-agents, … | A curated list of awesome Claude Skills… |
| [actions/checkout](https://github.com/actions/checkout) | 8,718 | +4 | TypeScript | 否 | TypeScript | Action for checking out a repo |
| [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 87,411 | +460 | TypeScript | 否 | TypeScript, editor, oss, videoedi… | The open-source CapCut alternative |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 101,191 | +323 | Python | 是 | Python, agent, finance, llm, mult… | TradingAgents: Multi-Agents LLM Financi… |

**产品分析**：今日热榜共 **19** 个项目，其中 AI 相关 **14 个（74%）**。新热点集中在：AI Agent 工程教程、代码知识图谱/MCP、异构 LLM 推理、Voice AI、Coding Agent、Computer Use 与 GenBI。

---

## 🏷️ 技术栈 tags（新属性）

每个项目新增 **`tags`** 字段，由 `primary_lang / frontend / backend / database / llm_runtime` 提炼归一，作为可筛选/可作徽章展示的属性。例：

> **Dify** → `Next.js` `React` `Tailwind` `Python` `Flask` `PostgreSQL`
> **n8n** → `TypeScript` `Vue 3` `Vue Flow` `PrimeVue` `Node.js` `PostgreSQL`

完整 tags 见 [`data/merged-ai-projects.csv`](data/merged-ai-projects.csv) 的 `tags` 列，卡片式展示见 [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md)。

---

## 📋 全部项目元数据（142 个）

> 以 `full_name` 为主键 **upsert（更新或插入）** 合并三个来源：`projects.csv`(curated) + `top-100-stars.csv` + `trending-daily.csv` → 共 **142 个**，其中 AI 相关 71 个、Top-100 项目 100 个、今日 Trending 项目 19 个。
> 生成脚本：`python3 scripts/refresh_sources.py && python3 scripts/upsert_metadata.py && python3 scripts/generate_reports.py`（幂等，保留人工技术栈字段）。
> 每个项目一张完整元数据卡片见 [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md)；Top-100 单独的完整卡片见 [`reports/top-100-metadata.md`](reports/top-100-metadata.md)。

<details>
<summary><b>📎 展开查看 56 个 AI 项目完整元数据宽表（含前后端/数据库/LLM，按 Star 降序）｜全部 142 个见 reports/all-projects-metadata.md</b></summary>

| # | 项目 | ⭐ | 榜号 | 平台 | 主语言 | 前端 | 后端 | 数据库 | LLM | License | 技术栈 tags | 来源 |
| :---: | :--- | ---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 384,132 | 6 | AI 助手(跨平台) | TypeScri… | — | — | — | 多模型 | —(待补) | TypeScript | top100 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | 261,160 | 14 | Agent Skill… | Shell | — | Shell | — | Claude Co… | —(待补) | Shell, Claude Code | top100 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 233,368 | 18 | Agent Skill… | JavaScri… | — | JavaScript | — | Claude Co… | —(待补) | JavaScript, Claude Code, Codex | top100 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 220,534 | 20 | Agent | Python | — | Python | — | 多模型 | —(待补) | Python | top100 |
| 5 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 198,132 | 23 | Web(自托管/云) | TypeScri… | Vue 3 + V… | Node.js | SQLite/Post… | OpenAI/An… | NOASSER… | TypeScript, Vue 3, Vue Flow, … | curated+top100 |
| 6 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 196,535 | 24 | Library | C++ | — | C++/Python(… | — | — | —(待补) | C, Python | top100 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 196,327 | 26 | Agent Skill… | 未标注 | — | — | — | Claude Co… | —(待补) | 未标注, Claude Code | top100 |
| 8 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,912 | 27 | Agent(实验) | Rust | — | Rust | — | — | —(待补) | Rust | top100 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 189,708 | 28 | CLI/TUI | TypeScri… | — | TypeScript(… | — | 多模型 | —(待补) | TypeScript, Node.js | top100 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | 188,444 | 31 | Agent Skill… | Shell | — | Shell | — | Claude Co… | —(待补) | Shell, Claude Code | top100 |
| 11 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 185,700 | 33 | Web + CLI | Python | Next.js(R… | Python(Fast… | PostgreSQL | 多模型 | NOASSER… | Python, Next.js, React, FastA… | curated+top100 |
| 12 | [ollama/ollama](https://github.com/ollama/ollama) | 176,951 | 41 | CLI/桌面/API | Go | —(CLI/原生桌… | Go | — | llama.cpp | MIT | Go, CLI, llama.cpp | curated+top100 |
| 13 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 169,026 | 44 | CLI/Library | Python | — | Python(库) | — | — | —(待补) | Python | top100 |
| 14 | [f/prompts.chat](https://github.com/f/prompts.chat) | 166,364 | 46 | 网站(可自托管) | HTML | HTML | — | — | ChatGPT | —(待补) | HTML, ChatGPT | top100 |
| 15 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,278 | 47 | Web(自托管) | Python | Gradio | Python(Grad… | —(本地文件) | 本地推理 | AGPL-3.0 | Python, Gradio, FastAPI, 本地文件… | curated+top100 |
| 16 | [anthropics/skills](https://github.com/anthropics/skills) | 164,178 | 48 | Agent Skill… | Python | — | Python | — | Claude | —(待补) | Python, Claude | top100 |
| 17 | [huggingface/transformers](https://github.com/huggingface/transformers) | 163,010 | 49 | Library | Python | — | Python(库) | — | — | Apache-… | Python | curated+top100 |
| 18 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 156,506 | 52 | API/云/自托管 | TypeScri… | Next.js | Node.js | — | 多模型 | AGPL-3.0 | TypeScript, Next.js, Node.js | curated+top100 |
| 19 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 152,449 | 53 | Web(自托管/云) | Python | React | Python(Fast… | SQLite/Post… | 多模型 | MIT | Python, React, FastAPI, SQLit… | curated+top100 |
| 20 | [langgenius/dify](https://github.com/langgenius/dify) | 150,339 | 54 | Web(自托管/云) | TypeScri… | Next.js +… | Python(Flas… | PostgreSQL … | 多模型/兼容 Op… | NOASSER… | TypeScript, Next.js, React, T… | curated+top100 |
| 21 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 146,839 | 56 | Web(自托管/Doc… | Python | Svelte(Sv… | Python(Fast… | SQLite/Chro… | Ollama/Op… | NOASSER… | Python, SvelteKit, FastAPI, S… | curated+top100 |
| 22 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 142,636 | 58 | Library | Python | — | Python(库 含 … | — | 多模型/兼容 Op… | MIT | Python | curated+top100 |
| 23 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 142,286 | 59 | 文档/合集 | 未标注 | — | — | — | — | —(待补) | 未标注 | top100 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 139,098 | 63 | CLI | Python | — | Python | — | Claude | —(待补) | Python, Claude | top100 |
| 25 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 136,683 | 65 | Agent Skill… | Shell | — | Shell | — | 多模型 | —(待补) | Shell | top100 |
| 26 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 127,686 | 74 | 示例库 | Python | — | Python | — | 多模型 | —(待补) | Python | top100 |
| 27 | [garrytan/gstack](https://github.com/garrytan/gstack) | 124,363 | 76 | Agent Skill… | TypeScri… | — | TypeScript | — | Claude Co… | —(待补) | TypeScript, Claude Code | top100 |
| 28 | [github/spec-kit](https://github.com/github/spec-kit) | 123,820 | 78 | CLI/Library | Python | — | Python(库) | — | 多模型 | —(待补) | Python | top100 |
| 29 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 122,396 | 79 | Web(自托管) | Python | TypeScrip… | Python(aioh… | — | 本地推理 | GPL-3.0 | Python, TypeScript, 自定义节点编辑器,… | curated+top100 |
| 30 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 121,691 | 81 | CLI/Library… | C++ | — | C/C++(内置 HT… | — | 自研 ggml | MIT | C, 内置 HTTP server, 自研 ggml | curated+top100 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 121,187 | 82 | 桌面(Tauri) | Rust | Web(Tauri) | Rust | — | Claude/Co… | —(待补) | Rust, Web, Tauri, Claude, Cod… | top100 |
| 32 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 113,498 | 91 | 教程 | Jupyter … | — | Jupyter | — | Azure Ope… | —(待补) | Jupyter Notebook, Jupyter, Az… | top100 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 110,134 | 94 | —(待补) | Python | — | — | — | — | —(待补) | Claude Code, UI/UX, 设计技能 | top100 |
| 34 | [openai/whisper](https://github.com/openai/whisper) | 105,689 | — | Library/CLI | Python | — | Python(库) | — | — | MIT | Python | curated |
| 35 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 87,249 | — | Library/Ser… | Python | — | Python(Fast… | — | 多模型 | Apache-… | Python, FastAPI OpenAI | curated |
| 36 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 82,207 | — | Web/CLI | Python | React | Python(运行时) | — | 多模型 | NOASSER… | Python | curated |
| 37 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 80,834 | — | Web(自托管) | TypeScri… | Next.js +… | Next.js Ser… | IndexedDB/服… | OpenAI/An… | NOASSER… | TypeScript | curated |
| 38 | [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 73,530 | — | Web/CLI | Python | Gradio | Python | — | 本地 | Apache-… | Python | curated |
| 39 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71,140 | — | Web(自托管) | Python | Gradio | Python | — | 多模型 | GPL-3.0 | Python, Gradio | curated |
| 40 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 67,318 | — | CLI | Rust | — | Rust | — | 多模型 | Apache-… | Rust | curated |
| 41 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 61,779 | — | Library/云 | TypeScri… | — | Python + TS… | PostgreSQL/… | 多模型 | Apache-… | TypeScript, Python, TS, Postg… | curated |
| 42 | [microsoft/autogen](https://github.com/microsoft/autogen) | 60,008 | — | Library | Python | —(AutoGen… | Python | — | 多模型 | CC-BY-4… | Python | curated |
| 43 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 56,185 | — | Library | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 44 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 54,949 | — | Web(自托管) | TypeScri… | React + M… | Node.js(Exp… | SQLite/Post… | LangChain… | NOASSER… | TypeScript, React, MUI, Node.… | curated |
| 45 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 51,130 | — | Library | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 46 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | 47,715 | — | CLI | Python | — | Python(库) | — | 多模型 | Apache-… | Python | curated |
| 47 | [oobabooga/textgen](https://github.com/oobabooga/textgen) | 47,497 | — | Web/桌面 | Python | Gradio | Python | — | 本地 | AGPL-3.0 | Python | curated |
| 48 | [milvus-io/milvus](https://github.com/milvus-io/milvus) | 45,387 | — | Server/云 | Go | — | Go | — | — | Apache-… | Go | curated |
| 49 | [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | 42,813 | — | Library | Python | — | Python(库) | — | — | Apache-… | Python | curated |
| 50 | [QuivrHQ/quivr](https://github.com/QuivrHQ/quivr) | 39,361 | — | Web(自托管/云) | Python | Next.js(R… | Python(Fast… | PostgreSQL … | 多模型 | NOASSER… | Python, Next.js, React, Verce… | curated |
| 51 | [continuedev/continue](https://github.com/continuedev/continue) | 35,125 | — | IDE 插件(VSCo… | TypeScri… | React(Web… | TypeScript(… | — | 多模型/本地 | Apache-… | TypeScript, React, WebView, N… | curated |
| 52 | [TabbyML/tabby](https://github.com/TabbyML/tabby) | 33,790 | — | Web/IDE 插件 | Rust | React | Rust | SQLite/Post… | 自托管模型 | NOASSER… | Rust, React, SQLite, PostgreS… | curated |
| 53 | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 33,601 | — | Server/云 | Rust | — | Rust | — | — | Apache-… | Rust | curated |
| 54 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | 31,181 | — | Web(自托管) | JavaScri… | 原生 JS/jQu… | Node.js(Exp… | — | OpenAI/本地 | AGPL-3.0 | JavaScript, 原生 JS, jQuery, No… | curated |
| 55 | [stanford-oval/storm](https://github.com/stanford-oval/storm) | 30,336 | — | Library/CLI | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 56 | [labring/FastGPT](https://github.com/labring/FastGPT) | 29,137 | — | Web(自托管/云) | TypeScri… | Next.js(R… | Node.js(Nex… | MongoDB + P… | 多模型 | NOASSER… | TypeScript, Next.js, React, M… | curated |
| 57 | [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,885 | — | Library/Ser… | Rust | — | Rust + Pyth… | — | — | Apache-… | Rust, Python | curated |

</details>

> ⚠️ top100 独有的 20 个项目（#1–4, #6–9, #12–14, #17, #22, #24–28, #31–32）部分技术栈字段为「—(待补)」，待逐个深度拆解。

---

## 📁 目录结构

```
ai-vibe-pick/
├── README.md                       # 本文件（GitHub 风格：徽章/TOC/折叠/全量元数据/Skill）
├── .claude/skills/tech-selection/  # AI 技术选型 Skill
│   └── SKILL.md
├── scripts/
│   └── upsert_metadata.py          # upsert 脚本(以 full_name 为主键更新或插入)
├── data/
│   ├── source-top-100-stars.md     # Top-100 原始榜单存档
│   ├── top-100-stars.csv           # Top-100 结构化(含 category/ai_related/tags)
│   ├── projects.csv                # 36 个 AI 项目技术选型
│   ├── merged-ai-projects.csv      # 合并去重 56 个(含 tags/source/rank_top100)
│   ├── trending-daily.csv         # Trending 今日热榜(19 个,含 ai_related/tags)
│   └── projects-metadata.csv      # ✅ 规范化元数据存储(142 个,upsert 生成)
└── reports/
    ├── summary.md                 # 36 个 AI 项目技术选型统计
    ├── merged-ai-projects.md      # 合并 56 个总表(含 tags 列)
    ├── trending-analysis.md       # Trending 今日热榜产品分析
    ├── top-100-metadata.md        # Top-100 完整元数据卡片(100 张)
    └── all-projects-metadata.md   # 全部 142 个项目元数据卡片
```

## 📦 数据文件

| 文件 | 说明 |
| :--- | :--- |
| [`data/projects-metadata.csv`](data/projects-metadata.csv) | ✅ **规范化元数据存储 142 个**，24 字段，upsert 生成（含 `tags`/`ai_related`/`rank_top100`/`trending_today`/`sources`） |
| [`scripts/refresh_sources.py`](scripts/refresh_sources.py) | 刷新 Top-100 / Trending / curated GitHub 易变字段，保留人工分类与技术栈 |
| [`scripts/upsert_metadata.py`](scripts/upsert_metadata.py) | upsert 三来源为 `projects-metadata.csv`（按 `full_name` 去重） |
| [`scripts/generate_reports.py`](scripts/generate_reports.py) | 根据数据重建 README 动态章节和元数据/Trending 报告 |
| [`.claude/skills/tech-selection/SKILL.md`](.claude/skills/tech-selection/SKILL.md) | 🧭 **AI 技术选型 Skill**：按项目描述 + 数据推荐栈 |
| [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md) | **142 个项目完整元数据卡片**，每项一张 |
| [`reports/top-100-metadata.md`](reports/top-100-metadata.md) | Top-100 完整元数据卡片（100 张） |
| [`reports/merged-ai-projects.md`](reports/merged-ai-projects.md) | 合并 56 个总表（含技术栈 tags 列） |
| [`data/trending-daily.csv`](data/trending-daily.csv) | Trending 今日热榜 19 个（今日新增/总 star/语言/AI相关/tags） |
| [`reports/trending-analysis.md`](reports/trending-analysis.md) | Trending 产品分析（AI 浓度/Skills 生态/垂直 Agent） |
| [`reports/summary.md`](reports/summary.md) | 36 个 AI 项目选型统计 + 分布图表 + 选型建议 |
| [`data/top-100-stars.csv`](data/top-100-stars.csv) | 全站历史总榜 Top-100（rank/stars/forks/language/category/ai_related/tags） |
| [`data/merged-ai-projects.csv`](data/merged-ai-projects.csv) | 合并去重 56 个，19 字段 |
| [`data/projects.csv`](data/projects.csv) | 36 个 AI 项目 14 字段技术选型表 |

## 🗺️ 采集字段

| 字段 | 说明 |
| :--- | :--- |
| name | 项目名称 |
| repo / url | GitHub 仓库地址 |
| stars | Star 数（采集日期） |
| rank_top100 | 历史总榜榜号（未进总榜为空） |
| category | 类型（LLM 应用 / Agent 框架 / RAG / 编程助手 / 模型推理 等） |
| platform | 平台形态（Web / CLI / IDE 插件 / Library / Server / 桌面 …） |
| primary_lang / dev_langs | 主语言 / 开发语言 |
| frontend | 前端技术栈 |
| backend | 后端技术栈 |
| database | 数据库 / 存储 |
| llm_runtime | LLM / 推理后端 |
| **tags** | **技术栈标签（新增，可作徽章/筛选）** |
| license | 开源协议 |
| owner / company | 维护方 |
| source | 来源（curated / top100 / curated+top100） |
| description | 简介 |
| last_updated | 采集日期 |

## 📈 统计维度

- 项目类型分布 · 前端选型分布（React / Vue / Next.js / Svelte）· 后端语言分布（Python / Node / Go / Rust）
- 后端框架分布（FastAPI / Express / Flask）· 数据库选型 · LLM/推理后端 · **技术栈 tags Top-N**

## 🔧 采集流程

1. 拉取 GitHub API（star/语言/协议/描述）与 Trending 页面 HTML
2. 各来源打 `tags` 与 `ai_related` 标注
3. **upsert**：`python3 scripts/upsert_metadata.py` 以 `full_name` 为主键把三来源（projects/top-100/trending）更新或插入到 `data/projects-metadata.csv`（llama.cpp 别名处理；幂等不清空已有字段）
4. 在 `reports/` 输出统计报告与全量元数据卡片（142 + 100）
5. README GitHub 风格展示（徽章 / TOC / 折叠 / 对齐表格 / Skill 使用入口）
