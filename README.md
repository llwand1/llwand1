<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero-light.svg" width="100%" alt="llwan —— AI 应用 &amp; Node 服务端 · 全栈独立开发 · 线上实例 11wand.com">
</picture>

<p align="center">
  <a href="https://11wand.com"><img src="https://img.shields.io/badge/%E7%BA%BF%E4%B8%8A%E5%AE%9E%E4%BE%8B-11wand.com-007AFF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="线上实例 11wand.com"></a>
  <a href="https://github.com/llwand1/studentbuddy-v2"><img src="https://img.shields.io/badge/SOURCE-studentbuddy--v2-181717?style=for-the-badge&logo=github&logoColor=white" alt="源码 studentbuddy-v2"></a>
  <img src="https://komarev.com/ghpvc/?username=llwand1&label=VIEWS&color=007aff&style=for-the-badge" alt="Profile views">
</p>

现在主要写 **AI 应用** 和 **Node 服务端**，习惯**先拿能跑的东西说话**——下面那个站点就是。

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Node.js%2022%2B-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/React%2018-087EA4?style=flat-square&logo=react&logoColor=white" alt="React">
<img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" alt="Express">
<img src="https://img.shields.io/badge/SQLite%20WAL-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">

---

## 先看这个：11wand.com

> **▶ <https://11wand.com>**
> 我做的 AI 学习助手 **StudentBuddy** 的线上实例，2026-09-19 起持续运行，当前部署版本 `v0.2.118`。
> 首页点「**免注册，直接体验**」进完整产品，不用填邮箱。

它不是一个套了学习提示词的聊天框，而是把「学习」做成一条自己转得起来的闭环：

| 环 | 做的事 |
|:---:|---|
| **学** | 流式对话 · 思考链 · 联网检索 · 长文档 BM25 检索 |
| **练** | 自建出题引擎：结构化协议、自动判分、AI 特化 SVG 配图 |
| **析** | 逐题正确率 · 薄弱点定位 · 学习趋势 |
| **忆** | AI 自学词条库 · 艾宾浩斯复习时钟 · 跨会话长期记忆 |
| **反馈** | 事件总线驱动 XP / 连签 / 今日总结，外加 AI 主动督促 |

<img src="assets/app-landing.png" width="100%" alt="StudentBuddy 落地页首屏">

<p align="center"><sub>落地页首屏 · 真机截图</sub></p>

<img src="assets/app-chat.png" width="100%" alt="StudentBuddy 应用壳 · 对话">

<p align="center"><sub>应用壳 · 对话 —— 左侧八视图导航，右下角常驻督促胶囊</sub></p>

数据自持、本地优先：同一套代码既能单机跑（SQLite 单文件 + WAL，默认只绑 `127.0.0.1`），也能自建服务器多用户跑；模型 key 和词条都是你自己的。线上这台也是我自己运维的小规格 VPS（Caddy 反代 + systemd），运行时只依赖 6 个第三方包。

<p>
  <img src="https://img.shields.io/github/v/release/llwand1/studentbuddy-v2?label=release&color=8a63f6&style=flat-square" alt="release">
  <img src="https://img.shields.io/github/last-commit/llwand1/studentbuddy-v2?label=last+commit&color=007aff&style=flat-square" alt="last commit">
  <img src="https://img.shields.io/github/license/llwand1/studentbuddy-v2?label=license&color=0f9d58&style=flat-square" alt="license">
  <img src="https://img.shields.io/github/stars/llwand1/studentbuddy-v2?label=stars&color=f5a623&style=flat-square" alt="stars">
  <img src="https://img.shields.io/github/issues/llwand1/studentbuddy-v2?label=open+issues&color=8a63f6&style=flat-square" alt="issues">
</p>

---

## 我在做的三件事

| 项目 | 是什么 | 现在在哪 |
|---|---|---|
| **StudentBuddy**<br><sub>`studentbuddy-v2`</sub> | 本地优先的 AI 学习助手，单机与多用户共用一份代码 | **[11wand.com](https://11wand.com)**<br>已上线 · 公开仓 · MIT |
| **AI 编排中心**<br><sub>`ai-orchestrator-v2`</sub> | 单人本地用的 AI 协作池，把原生内核和多家外部 AI 编在一起互相派活 | 本地日常在用<br>私有仓 |
| **会打招呼的简历 Agent**<br><sub>`resume`</sub> | 静态简历 + 一个会主动开口的 AI 分身，只按真实信息作答 | 评测完成，待上线<br>私有仓 |

---

## 里程碑

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/milestone-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/milestone-light.svg">
  <img src="assets/milestone-light.svg" width="100%" alt="成长时间线：2026.03 GitHub 起步 → 2026.07 个人博客上线 / StudentBuddy v1 → 2026.09.05 v2 全新重写 → 2026.09.13 AI 编排中心 → 2026.09.19 11wand.com 上线 → 2026.09.24 v0.2.118 发布">
</picture>

个人博客 [llwand1.github.io](https://llwand1.github.io) 一直在更；`studentbuddy` 是 v1，已冻结归档。

---

## 给招聘方

| | |
|---|---|
| **目标岗位** | AI 应用开发 / 全栈（实习） |
| **期望城市** | 长沙 · 株洲 / 远程 |
| **到岗时间** | 随时 |

30 秒：打开 **[11wand.com](https://11wand.com)** 点一次「免注册，直接体验」。

5 分钟：读 [studentbuddy-v2 的「给面试官」一节](https://github.com/llwand1/studentbuddy-v2#给面试官一条-30-秒到-15-分钟的阅读路径)，那里给了 30 秒到 10 分钟四条路径，每条都配可当场复验的机器证据（`npm run check`、`npm run demo:e2e`，零 API key 跑完 9 幕 36 条断言）。

---

## 联系

- **站点** —— <https://11wand.com>
- **GitHub** —— [@llwand1](https://github.com/llwand1)

<sub>I build AI applications and Node backends — currently shipping **[StudentBuddy](https://11wand.com)**, a local-first learning assistant that runs online as a multi-user web service.</sub>
