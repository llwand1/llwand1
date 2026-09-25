<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero-light.svg" width="100%" alt="llwan —— 储能材料 → 自学转开发 · AI 应用 &amp; Node 服务端 · 线上实例 11wand.com">
</picture>

<p align="center">
  <a href="https://11wand.com"><img src="https://img.shields.io/badge/%E7%BA%BF%E4%B8%8A%E5%AE%9E%E4%BE%8B-11wand.com-007AFF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="线上实例 11wand.com"></a>
  <a href="https://github.com/llwand1/studentbuddy-v2"><img src="https://img.shields.io/badge/SOURCE-studentbuddy--v2-181717?style=for-the-badge&logo=github&logoColor=white" alt="源码 studentbuddy-v2"></a>
  <a href="mailto:3525748705@qq.com"><img src="https://img.shields.io/badge/EMAIL-3525748705%40qq.com-EA4335?style=for-the-badge&logo=minutemailer&logoColor=white" alt="邮箱"></a>
  <img src="https://komarev.com/ghpvc/?username=llwand1&label=VIEWS&color=007aff&style=for-the-badge" alt="Profile views">
</p>

储能材料工程技术专业在读，自学转做开发，现在主要写 **AI 应用** 和 **Node 服务端**。
手上在维护三个项目：一个已经跑在线上的 AI 学习助手、一个把多家 AI 编成协作池的本地控制台、一个会主动打招呼的简历 Agent。
习惯把取舍写进文档，也习惯**先拿能跑的东西说话**——下面那个站点就是。

---

## 先看这个：11wand.com

> ### ▶ <https://11wand.com>
> 我做的 AI 学习助手 **StudentBuddy** 的线上实例，2026-09-19 起持续运行，当前部署版本 `v0.2.118`。
> 打开首页点「**免注册，直接体验**」，不用填邮箱，直接进完整产品。

<img src="assets/app-landing.png" width="100%" alt="StudentBuddy 落地页首屏">

<p align="center"><sub>落地页首屏 · 真机截图（无头 Chrome 直出当前源码，不是设计稿）</sub></p>

**它不是一个套了学习提示词的聊天框。** 它把「学习」做成一条能自己转起来的闭环：

| 环 | 做的事 |
|:---:|---|
| **学** | 流式对话 + 思考链 + 联网检索 + 长文档 BM25 检索 |
| **练** | 自建出题引擎：结构化协议、自动判分、题型配比可配、AI 特化 SVG 配图 |
| **析** | 逐题正确率、薄弱点定位、学习趋势 |
| **忆** | AI 自学词条库 + 艾宾浩斯复习时钟 + 跨会话长期记忆 |
| **反馈** | 事件总线驱动 XP / 连签 / 今日总结，外加 AI 主动督促 |

<img src="assets/app-chat.png" width="100%" alt="StudentBuddy 应用壳 · 对话">

<p align="center"><sub>应用壳 · 对话 —— 左侧八视图导航，右下角常驻督促胶囊</sub></p>

几个我觉得值得单独说的点：

- **数据自持。** 同一套代码两种形态——本地单机跑（SQLite 单文件、WAL，默认只绑 `127.0.0.1`），或自建服务器多用户跑。模型 key 是你自己的，词条是你自己的。
- **线上这台也是我自己运维的。** 一台小规格 VPS：Caddy 反代 + systemd 守护 + SQLite WAL，没有托管平台兜底，出问题就是自己查。
- **本地优先是真做进去了，不是宣传词。** 运行时只依赖 6 个第三方包，其余全部留在 devDependencies；服务端与前端拆成 3 个 workspace 包。

<p>
  <img src="https://img.shields.io/github/v/release/llwand1/studentbuddy-v2?label=release&color=8a63f6&style=flat-square" alt="release">
  <img src="https://img.shields.io/github/last-commit/llwand1/studentbuddy-v2?label=last+commit&color=007aff&style=flat-square" alt="last commit">
  <img src="https://img.shields.io/github/license/llwand1/studentbuddy-v2?label=license&color=0f9d58&style=flat-square" alt="license">
  <img src="https://img.shields.io/github/stars/llwand1/studentbuddy-v2?label=stars&color=f5a623&style=flat-square" alt="stars">
  <img src="https://img.shields.io/github/issues/llwand1/studentbuddy-v2?label=open+issues&color=8a63f6&style=flat-square" alt="issues">
</p>

<p align="center">
  <a href="https://11wand.com"><b>→ 打开 11wand.com 点一次「免注册，直接体验」</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/llwand1/studentbuddy-v2">看源码</a>
  &nbsp;·&nbsp;
  <a href="https://11wand.com/changelog/">看更新记录</a>
</p>

---

## 我在维护的三件事

| 项目 | 是什么 | 现在在哪 |
|---|---|---|
| **StudentBuddy**<br><sub>`studentbuddy-v2`</sub> | 本地优先的 AI 学习助手。学 → 练 → 析 → 忆 → 反馈 五环闭环，单机与多用户两种形态共用一份代码。它同时管住了「模型不听话」这一整类工程问题：解析阶梯、丢图保题、流式超时、上游并发闸门、契约漂移回归锁——**每条对策都对应一次真实故障的根因登记**。 | **[11wand.com](https://11wand.com)**<br>已上线 · 公开仓 · MIT |
| **AI 编排中心**<br><sub>`ai-orchestrator-v2`</sub> | 单人本地用的 AI 协作池：把一个原生 AI 内核（子进程拉起的 `opencode serve`）和多家外部 AI（API 型 / CLI 型 / 桌面 GUI 型）编在一起互相派活。主张是「**适配新的 AI 靠配置，不靠改代码**」——适配器分三种 profile，内核能力再以插件形式注册回内核自己。 | 本地日常在用<br>私有仓 |
| **会打招呼的简历 Agent**<br><sub>`resume`</sub> | 静态简历 + 右上角一个**会主动开口**的 AI 分身。它只按我的真实信息作答，答不上来会说「让我本人回你」，不硬编；另一侧还能粘一段岗位 JD，当场判匹配度、当场写打招呼语。整站零构建、零框架依赖。 | 评测完成，待上线<br>私有仓 |

---

## 技术栈

**语言 / 运行时**
<br>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Node.js%2022%2B-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">

**前端**
<br>
<img src="https://img.shields.io/badge/React%2018-087EA4?style=flat-square&logo=react&logoColor=white" alt="React">
<img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite">
<img src="https://img.shields.io/badge/%E5%8E%9F%E7%94%9F%20JS%20%E9%9B%B6%E4%BE%9D%E8%B5%96-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="vanilla JS">

**服务端 / 存储**
<br>
<img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" alt="Express">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/SQLite%20WAL-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/SSE%20%E6%B5%81%E5%BC%8F-8A63F6?style=flat-square&logoColor=white" alt="SSE">

**部署 / 运维**
<br>
<img src="https://img.shields.io/badge/Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white" alt="Caddy">
<img src="https://img.shields.io/badge/systemd-000000?style=flat-square&logo=systemd&logoColor=white" alt="systemd">
<img src="https://img.shields.io/badge/Cloudflare%20Pages-F38020?style=flat-square&logo=cloudflarepages&logoColor=white" alt="Cloudflare Pages">

**工程化**
<br>
<img src="https://img.shields.io/badge/vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white" alt="vitest">
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">
<img src="https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white" alt="ESLint">
<img src="https://img.shields.io/badge/pnpm-F69220?style=flat-square&logo=pnpm&logoColor=white" alt="pnpm">
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">

---

## 我的几条工程主张

都是拿真实故障换来的，不是抄来的口号：

> **降级要看得见。**
> 内核不可用时界面上必须显式三态。**绝不假装正常**——降级不可见的时候，用户会把故障当成结果。

> **安全闸门宁可显式失败，也不放通配符。**
> Origin 白名单拒绝 `*`，也拒绝 `null` 来源。放行通配符等于这道闸压根不存在。

> **上游的变化要在构建期拦住，不能留到运行期。**
> 锁版本 + OpenAPI 3.1 校验，破坏性变更由 CI 直接拦下。把不确定的上游变化变成一次构建失败，而不是一次线上事故。

> **测试只登记在测试计划里才算数。**
> 自建 CI 门禁：单文件行数上限、禁内联样式、禁 `any`，新增测试文件未在 test-plan 登记就直接红——否则会出现没人认领的孤儿测试。

> **一份掺了水的复核，比没有复核更危险。**
> 安全复核逐条留痕，没达到的判据如实写「部分达成」并标出根因。不装全绿。

> **诚实比显得无所不知更重要。**
> 简历里的 AI 分身答不上来就说「让我本人回你」，不编。

---

## 里程碑

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/milestone-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/milestone-light.svg">
  <img src="assets/milestone-light.svg" width="100%" alt="成长时间线：2026.03 GitHub 起步 → 2026.07 个人博客上线 / StudentBuddy v1 → 2026.09.05 v2 全新重写 → 2026.09.13 AI 编排中心 → 2026.09.19 11wand.com 上线 → 2026.09.24 v0.2.118 发布">
</picture>

另外两个也在跑的：个人博客 [llwand1.github.io](https://llwand1.github.io)（Hexo，一直在更）；
`llwand1/studentbuddy` 是 v1，已冻结归档，只在 [studentbuddy-v2](https://github.com/llwand1/studentbuddy-v2) 上继续。

---

## 给招聘方

| | |
|---|---|
| **目标岗位** | AI 应用开发 / 全栈（实习） |
| **期望城市** | 长沙 · 株洲 / 远程 |
| **到岗时间** | 随时 |

如果只有 30 秒：打开 **[11wand.com](https://11wand.com)** 点一次「免注册，直接体验」。
如果有 5 分钟：读 [studentbuddy-v2 的「给面试官」一节](https://github.com/llwand1/studentbuddy-v2#给面试官一条-30-秒到-15-分钟的阅读路径)——那里按 30 秒 / 2 分钟 / 5 分钟 / 10 分钟给了四条路径，每条都配了**可当场复验**的机器证据（一条 `npm run check`、一条 `npm run demo:e2e`，零 API key 跑完 9 幕 36 条断言）。**不信文档信机器**，这是我在那个仓里写的前提。

---

## 联系

- **线上站点** —— <https://11wand.com>
- **GitHub** —— [@llwand1](https://github.com/llwand1)
- **邮箱** —— [3525748705@qq.com](mailto:3525748705@qq.com)

<sub>Storage-materials major, self-taught developer. I build AI applications and Node backends — currently shipping **[StudentBuddy](https://11wand.com)**, a local-first learning assistant that runs online as a multi-user web service.</sub>
