# SiliconFlow API Key Balance Checker 🔑💰

<div align="center">
  <a href="README.md">English</a> |
  <a href="README_zh.md">中文</a>
</div>

## Overview
This tool allows you to check the balance information of SiliconFlow API keys from a text file and outputs sorted results in CSV format and a list of valid keys.

## Features
- ✅ Load API keys from text file
- 🔄 Remove duplicate keys
- 💲 Check account balance for each key
- 📊 Generate sorted CSV report
- ✨ Extract valid keys with positive balance

## Requirements
- Python 3.x
- Required packages:
  - requests
  - tqdm

## Installation

```sh
pip install requests tqdm
```

## Usage

Run the script with the following command:

```bash
python test_siliconflow_api.py [-f API_KEYS_FILE_PATH]
```

### Arguments

- `-f`, `--file`: API keys file path (default: `./api_keys.txt`)

## Input Format

Create a text file with one API key per line:

```
sk-xxxxxxxxxxxxxxxxxxxxxxxx
sk-yyyyyyyyyyyyyyyyyyyyyyyy
```

## Output Files

1. `api_keys_balance.csv` 📄 - Contains detailed information about each key:
   - API key
   - Remaining balance
   - Total balance
   - User ID
   - Name
   - Email

2. `valid_api_keys.txt` ✅ - Contains only keys with positive balance

## Example

```bash
python test_siliconflow_api.py -f my_keys.txt
```

## Notes

- 🕒 The script adds a 0.5-second delay between queries to avoid API rate limits
- 📉 Results are sorted by remaining balance in descending order