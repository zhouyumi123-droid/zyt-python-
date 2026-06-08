import argparse
import csv
import json
from pathlib import Path


def normalize_value(value):
    if isinstance(value, list):
        return "|".join(str(item) for item in value)
    if value is None:
        return ""
    return value


def json_to_rows(records):
    if not isinstance(records, list):
        raise ValueError("JSON 顶层结构必须是对象列表。")

    headers = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("JSON 列表中的每一项都必须是对象。")
        for key in record.keys():
            if key not in headers:
                headers.append(key)

    rows = []
    for record in records:
        row = {header: normalize_value(record.get(header)) for header in headers}
        rows.append(row)

    return headers, rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="把 JSON 对象列表转换成 CSV 表格。")
    parser.add_argument("--input", required=True, help="输入 JSON 文件路径。")
    parser.add_argument("--output", required=True, help="输出 CSV 文件路径。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"找不到输入文件：{input_path}")

    records = json.loads(input_path.read_text(encoding="utf-8"))
    headers, rows = json_to_rows(records)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"已保存 CSV 文件：{output_path}")


if __name__ == "__main__":
    main()
