import argparse
from pathlib import Path


def clean_text(text: str) -> str:
    cleaned_lines = []
    for line in text.splitlines():
        stripped = " ".join(line.strip().split())
        if stripped:
            cleaned_lines.append(stripped)
    return "\n".join(cleaned_lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="清洗文本中的多余空格，并移除空行。"
    )
    parser.add_argument("--input", required=True, help="原始文本文件路径。")
    parser.add_argument("--output", required=True, help="清洗后输出文件路径。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"找不到输入文件：{input_path}")

    raw_text = input_path.read_text(encoding="utf-8")
    cleaned_text = clean_text(raw_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(cleaned_text, encoding="utf-8")
    print(f"已保存清洗后的文本：{output_path}")


if __name__ == "__main__":
    main()
