# 5W2H Skill for PM：需求定义与对齐（Psychology & UX Edition）

这是一个可共享到 GitHub 的 **Cursor Project Skill**，用于把“模糊想法”梳理为**可评审、可落地**的需求输出：
- 基于 **5W2H** 框架引导提问与结构化沉淀
- 在 **Who / When** 环节自动做**心理学增强**的人群与时机分析
- 自动生成面向 **RD / UI/UX / QA** 的对齐沟通要点

## Skill 位置（仓库内）

`/.cursor/skills/pm-5w2h-requirements/`

- `SKILL.md`：Skill 入口（触发场景、流程、输出约束）
- `prompt.md`：完整 System Prompt（可直接复制为系统提示词）
- `examples.md`：可复用的对话与交付示例

## 使用方式
直接 Clone 下来运行 python3 start_skill.py。

复制仓库里的 5w2h-core-engine.md 投喂给任意 AI 对话

我一般会把本仓库克隆到本地并用 Cursor 打开后，该 Skill 会作为**项目级 Skill**被自动发现与使用。

## 5W2H 核心框架（Psychology & UX 速记）

- **Why（价值定位）**：解决什么心理痛点？成功指标是什么？
- **Who（受众定义）**：人群分层、认知负荷、动机与阻力、权限边界
- **What（功能边界）**：MVP 必须做什么/不做什么；非功能需求（性能/安全/埋点）
- **When（触发时机）**：触发条件、频率、情绪与注意力、关键“真相时刻”、默认与兜底
- **Where（交付平台）**：端与入口、环境约束、跨端联动
- **How（交互逻辑）**：主链路 + 异常分支（断网/空状态/失败）的可逆与心理补偿
- **How much（成本收益）**：资源投入、里程碑、优先级

## 跨岗位对齐（提示）

- **研发（RD）**：逻辑闭环与边界 case、状态一致性、幂等/并发/性能
- **设计（UI/UX）**：认知负荷与信息层级、3 秒可理解、可控/可逆/可追溯
- **测试（QA）**：验收口径、Given-When-Then、极端输入与异常路径覆盖
