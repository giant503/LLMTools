# LLMTools

<div align="center">
  <a href="README.md">English</a> |
  <a href="README_zh.md">中文</a>
</div>

## 概述
LLMTools 是一个为大型语言模型（LLM）服务设计的工具集合。该项目提供各种实用工具，帮助开发者管理和使用不同的 LLM 平台。

## 可用工具

### 1. API 密钥管理工具
- **SiliconFlow API 密钥余额检查工具** 🔑💰
  - 验证 SiliconFlow API 密钥并检查其余额信息
  - [使用文档](api/check/siliconflow/README_zh.md)

## 项目结构
```angular2html
LLMTools/
├── api/
│   └── check/
│       └── siliconflow/
│           ├── test_siliconflow_api.py
│           ├── README.md
│           └── README_zh.md
├── README.md
├── README_zh.md
└── .gitignore
```
## 安装
每个工具都有其自己的安装要求。请参阅特定工具的文档了解详情。

## 未来计划
该项目旨在扩展更多工具，以支持各种 LLM 提供商和 API。模块化结构允许轻松添加新的工具。

计划添加的功能包括：
- 支持更多 LLM 提供商
- Token 计数工具
- 成本估算工具
- 提示词管理系统

## 贡献
欢迎贡献！请随时提交拉取请求，添加新工具或改进现有工具。

## 许可证
[MIT 许可证](LICENSE)