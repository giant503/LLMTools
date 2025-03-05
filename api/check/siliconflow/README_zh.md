# SiliconFlow API 密钥余额检查工具 🔑💰

<div align="center">
  <a href="README.md">English</a> |
  <a href="README_zh.md">中文</a>
</div>

## 概述
该工具允许您从文本文件中检查 SiliconFlow API 密钥的余额信息，并将排序后的结果输出为 CSV 格式以及有效密钥列表。

## 功能
- ✅ 从文本文件加载 API 密钥
- 🔄 移除重复密钥
- 💲 检查每个密钥的账户余额
- 📊 生成排序后的 CSV 报告
- ✨ 提取具有正余额的有效密钥

## 环境要求
- Python 3.x
- 所需包:
  - requests
  - tqdm

## 安装

```sh
pip install requests tqdm
```

## 使用方法

使用以下命令运行脚本:

```bash
python test_siliconflow_api.py [-f API密钥文件路径]
```

### 参数

- `-f`, `--file`: API 密钥文件路径 (默认: `./api_keys.txt`)

## 输入格式

创建一个文本文件，每行一个 API 密钥:

```
sk-xxxxxxxxxxxxxxxxxxxxxxxx
sk-yyyyyyyyyyyyyyyyyyyyyyyy
```

## 输出文件

1. `api_keys_balance.csv` 📄 - 包含每个密钥的详细信息:
   - API 密钥
   - 剩余余额
   - 总余额
   - 用户 ID
   - 用户名
   - 邮箱

2. `valid_api_keys.txt` ✅ - 仅包含具有正余额的密钥

## 示例

```bash
python test_siliconflow_api.py -f my_keys.txt
```

## 注意事项

- 🕒 脚本在查询间添加 0.5 秒延迟，以避免 API 速率限制
- 📉 结果按剩余余额降序排序