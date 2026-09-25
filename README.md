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
| **学** | 流式对话 · 思考链 · 联网检索 · 长文档 BM25 |
| **练** | 自建出题引擎 · 结构化协议 · 自动判分 · AI 特化配图 |
| **析** | 逐题正确率 · 薄弱点定位 · 学习趋势 |
| **忆** | AI 自学词条库 · 艾宾浩斯复习时钟 · 跨会话记忆 |
| **反馈** | 事件总线驱动 XP / 连签 / 今日总结 · AI 主动督促 |

<img src="assets/app-landing.png" width="100%" alt="StudentBuddy 落地页首屏">

<p align="center"><sub>落地页首屏 · 真机截图</sub></p>

<img src="assets/app-chat.png" width="100%" alt="StudentBuddy 应用壳 · 对话">

<p align="center"><sub>应用壳 · 对话 —— 八视图导航 + 常驻督促胶囊</sub></p>

数据自持、本地优先：同一套代码既能单机跑（SQLite 单文件 + WAL），也能自建服务器多用户跑，模型 key 和词条都是你自己的。线上这台也是我自己运维的——小规格 VPS，Caddy 反代 + systemd，运行时只依赖 6 个第三方包、0 个第三方 UI 库。

<p>
  <img src="https://img.shields.io/github/v/release/llwand1/studentbuddy-v2?label=release&color=8a63f6&style=flat-square" alt="release">
  <img src="https://img.shields.io/github/last-commit/llwand1/studentbuddy-v2?label=last+commit&color=007aff&style=flat-square" alt="last commit">
  <img src="https://img.shields.io/github/license/llwand1/studentbuddy-v2?label=license&color=0f9d58&style=flat-square" alt="license">
  <img src="https://img.shields.io/github/stars/llwand1/studentbuddy-v2?label=stars&color=f5a623&style=flat-square" alt="stars">
  <img src="https://img.shields.io/github/issues/llwand1/studentbuddy-v2?label=open+issues&color=8a63f6&style=flat-square" alt="issues">
</p>

---

## 里程碑

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/milestone-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/milestone-light.svg">
  <img src="assets/milestone-light.svg" width="100%" alt="StudentBuddy 成长时间线：2026.03 GitHub 起步 → 2026.07 v1 → 2026.09.05 v2 重写 → 2026.09.19 11wand.com 上线 → 2026.09.24 v0.2.118 发布">
</picture>

<sub>I build AI applications and Node backends — currently shipping **[StudentBuddy](https://11wand.com)**, a local-first learning assistant that runs online as a multi-user web service.</sub>
