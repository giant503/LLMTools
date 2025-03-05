# LLMTools

<div align="center">
  <a href="README.md">English</a> |
  <a href="README_zh.md">中文</a>
</div>

## Overview
LLMTools is a collection of utility tools designed for working with Large Language Model (LLM) services. The project provides various utilities to help developers manage and interact with different LLM platforms.

## Available Tools

### 1. API Key Management Tools
- **SiliconFlow API Key Balance Checker** 🔑💰
  - Validates SiliconFlow API keys and checks their balance information
  - [Documentation](api/check/siliconflow/README.md)

## Project Structure
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

## Installation
Each tool has its own installation requirements. Please refer to the specific tool's documentation for details.

## Future Plans
This project aims to expand with more tools for working with various LLM providers and APIs. The modular structure allows for easy addition of new utilities as they are developed.

Planned additions include:
- Support for more LLM providers
- Token counting utilities
- Cost estimation tools
- Prompt management systems

## Contributing
Contributions are welcome! Feel free to submit pull requests with new tools or improvements to existing ones.

## License
[MIT License](LICENSE)