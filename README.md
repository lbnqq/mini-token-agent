# Mini Token Agent

一个面向学生 Agent 学习场景的最小可运行智能体，用于演示：

- 用户任务输入
- Agent 自动拆解计划
- 分步骤调用大模型执行
- 记录每一步 token 消耗
- 输出成本反思报告

## 项目目标

本项目用于降低学习 Agent 开发时的无效 token 消耗。它不是复杂生产级 Agent，而是一个可展示、可复用、可扩展的最小原型。

## 项目结构

```text
mini-token-agent/
├── main.py
├── agent.py
├── llm_client.py
├── token_logger.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
├── logs/
└── outputs/
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置环境变量

复制示例配置：

```bash
cp .env.example .env
```

然后在 `.env` 中填写自己的 API Key：

```env
ZHIPU_API_KEY=your_api_key_here
ZHIPU_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
ZHIPU_MODEL=glm-5.1
```

## 运行

```bash
python main.py
```

输入示例：

```text
帮我学习 Agent 的基本结构
```

运行后会生成：

```text
logs/token_log.csv
outputs/report.md
```

## Agent 流程

```text
用户输入任务
    ↓
Planner：拆解任务
    ↓
Executor：逐步执行
    ↓
Logger：记录 token
    ↓
Reflector：分析浪费点
    ↓
输出报告
```

## 适用场景

- Agent 学习演示
- prompt 调试流程记录
- token 消耗分析
- 免费 token 申请材料中的项目原型展示
