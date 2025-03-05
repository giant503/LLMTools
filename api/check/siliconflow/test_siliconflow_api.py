import requests
import time
import csv
import os
from collections import OrderedDict

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="查询SiliconFlow API密钥余额信息")
    parser.add_argument("-f", "--file", default="./api_keys.txt",
                        help="指定API密钥文件路径 (默认: ./api_keys.txt)")
    return parser.parse_args()
def load_api_keys(file_path='./api_keys.txt'):
    """从文本文件加载API密钥并去重"""
    try:
        with open(file_path, 'r') as file:
            # 读取所有行并去除空行和空白
            keys = [line.strip() for line in file.readlines() if line.strip()]
            # 使用OrderedDict去重但保持顺序
            unique_keys = list(OrderedDict.fromkeys(keys))
            print(f"加载了 {len(keys)} 个API密钥，去重后剩余 {len(unique_keys)} 个")
            return unique_keys
    except FileNotFoundError:
        print(f"警告: API密钥文件 {file_path} 未找到")
        return []


def get_account_info(api_key):
    """查询账户信息"""
    url = "https://api.siliconflow.cn/v1/user/info"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") and data.get("data"):
                user_data = data["data"]
                remaining_balance = float(user_data.get("balance", "0"))
                total_balance = float(user_data.get("totalBalance", "0"))
                return {
                    "key": api_key,
                    "remaining_balance": remaining_balance,
                    "total_balance": total_balance,
                    "user_id": user_data.get("id", ""),
                    "name": user_data.get("name", ""),
                    "email": user_data.get("email", "")
                }
        return {
            "key": api_key,
            "remaining_balance": 0.0,
            "total_balance": 0.0,
            "user_id": "",
            "name": "",
            "email": "",
            "error": response.text
        }
    except Exception as e:
        return {
            "key": api_key,
            "remaining_balance": 0.0,
            "total_balance": 0.0,
            "user_id": "",
            "name": "",
            "email": "",
            "error": str(e)
        }


def main():
    # 解析命令行参数
    args = parse_args()

    # 加载并去重API密钥
    api_keys = load_api_keys(args.file)
    if not api_keys:
        print(f"未找到可用的API密钥，请检查文件: {args.file}")
        return
    from tqdm import tqdm
    # 查询每个密钥的账户信息
    results = []
    # 使用tqdm创建进度条
    for key in tqdm(api_keys, desc="查询API密钥信息", unit="key"):
        result = get_account_info(key)
        results.append(result)
        # 添加短暂延迟避免API限制
        time.sleep(0.5)

    # 按照剩余额度从大到小排序
    sorted_results = sorted(
        results,
        key=lambda x: float(x["remaining_balance"]),
        reverse=True
    )

    # 保存为CSV文件
    csv_filename = "api_keys_balance.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["key", "remaining_balance", "total_balance", "user_id", "name", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in sorted_results:
            # 只写入基本字段
            writer.writerow({field: result.get(field, "") for field in fieldnames})

    print(f"已保存结果到 {csv_filename}")

    # 将余额大于0的密钥保存为文本文件
    valid_keys = [result["key"] for result in sorted_results if float(result["remaining_balance"]) > 0]

    if valid_keys:
        valid_keys_filename = "valid_api_keys.txt"
        with open(valid_keys_filename, 'w', encoding='utf-8') as file:
            for key in valid_keys:
                file.write(f"{key}\n")
        print(f"已将 {len(valid_keys)} 个有效密钥(余额>0)保存到 {valid_keys_filename}")
    else:
        print("没有找到余额大于0的有效密钥")


if __name__ == "__main__":
    main()