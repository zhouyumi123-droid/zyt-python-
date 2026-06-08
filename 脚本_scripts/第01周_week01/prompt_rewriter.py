import argparse
import json
from pathlib import Path


def rewrite_prompt(record: dict) -> dict:
    prompt = record.get("prompt")
    if not prompt:
        raise ValueError("每条记录都必须包含非空的 `prompt` 字段。")

    tone = record.get("tone", "清晰、务实")
    audience = record.get("audience", "通用业务场景用户")
    goal = record.get("goal", "产出一版可直接修改的一稿")

    rewritten_prompt = (
        f"你正在帮助{audience}。"
        f"请使用{tone}的表达风格。"
        f"核心目标：{goal}。"
        f"原始需求：{prompt}"
    )

    updated = dict(record)
    updated["rewritten_prompt"] = rewritten_prompt
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="把提示词改写成更结构化、更适合交付的格式。"
    )
    parser.add_argument("--input", required=True, help="输入 JSON 文件路径。")
    parser.add_argument("--output", required=True, help="输出 JSON 文件路径。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"找不到输入文件：{input_path}")

    records = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("输入 JSON 顶层必须是提示词记录列表。")

    rewritten_records = [rewrite_prompt(record) for record in records]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(rewritten_records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"已保存改写后的提示词：{output_path}")


if __name__ == "__main__":
    main()
