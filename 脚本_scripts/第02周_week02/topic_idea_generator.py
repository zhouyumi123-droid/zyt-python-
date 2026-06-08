import argparse
import json
from pathlib import Path


IDEA_PATTERNS = [
    "{audience} 在做 {keyword} 时最容易犯的 3 个错误",
    "如何用 AI 做出一套关于 {keyword} 的实用工作流",
    "今年 {audience} 做 {keyword} 有哪些新变化",
    "想提升 {keyword}，团队必须先有的检查清单",
    "幕后拆解：怎么把 {keyword} 做成可复用系统",
]


def score_idea(text: str, keyword: str) -> int:
    score = 50
    if keyword.lower() in text.lower():
        score += 20
    if any(token in text.lower() for token in ["检查清单", "工作流", "错误"]):
        score += 15
    if len(text) <= 80:
        score += 15
    return min(score, 100)


def generate_ideas(seed: dict) -> list[dict]:
    keyword = seed.get("keyword")
    if not keyword:
        raise ValueError("输入 JSON 必须包含非空的 `keyword` 字段。")

    audience = seed.get("audience", "内容运营人员")
    platform = seed.get("platform", "内容平台")

    ideas = []
    for pattern in IDEA_PATTERNS:
        title = pattern.format(keyword=keyword, audience=audience)
        ideas.append(
            {
                "title": title,
                "platform": platform,
                "audience": audience,
                "score": score_idea(title, keyword),
            }
        )
    ideas.sort(key=lambda item: item["score"], reverse=True)
    return ideas


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="根据一个简单的种子 JSON 生成内容选题建议。"
    )
    parser.add_argument("--input", required=True, help="输入种子 JSON 文件路径。")
    parser.add_argument("--output", required=True, help="输出 JSON 文件路径。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"找不到输入文件：{input_path}")

    seed = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(seed, dict):
        raise ValueError("输入 JSON 顶层必须是对象。")

    ideas = generate_ideas(seed)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(ideas, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"已保存选题建议：{output_path}")


if __name__ == "__main__":
    main()
