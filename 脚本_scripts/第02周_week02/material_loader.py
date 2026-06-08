import argparse
import json
from pathlib import Path


SUPPORTED_EXTENSIONS = {".txt", ".md", ".json"}


def read_material(path: Path) -> dict:
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"不支持的文件类型：{path.name}")

    if suffix in {".txt", ".md"}:
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            raise ValueError(f"文件内容为空：{path.name}")
        return {"source": path.name, "content": content}

    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        title = payload.get("title", path.stem)
        body = payload.get("content") or payload.get("summary")
        if not body:
            raise ValueError(f"JSON 文件缺少 `content` 或 `summary`：{path.name}")
        return {"source": title, "content": body}

    raise ValueError(f"JSON 文件内容必须是对象：{path.name}")


def build_markdown(materials: list[dict]) -> str:
    sections = ["# 资料汇总", ""]
    for item in materials:
        sections.append(f"## {item['source']}")
        sections.append(item["content"])
        sections.append("")
    return "\n".join(sections).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="读取一个目录中的资料文件，并合并成一份摘要。"
    )
    parser.add_argument("--input-dir", required=True, help="资料目录路径。")
    parser.add_argument("--output", required=True, help="输出 Markdown 文件路径。")
    parser.add_argument(
        "--manifest",
        required=True,
        help="输出 JSON 清单文件路径。",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_path = Path(args.output)
    manifest_path = Path(args.manifest)

    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"找不到输入目录：{input_dir}")

    materials = []
    for path in sorted(input_dir.iterdir()):
        if path.is_file():
            materials.append(read_material(path))

    if not materials:
        raise ValueError("输入目录中没有找到可处理的资料文件。")

    markdown_output = build_markdown(materials)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(markdown_output, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(materials, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"已保存资料摘要：{output_path}")
    print(f"已保存资料清单：{manifest_path}")


if __name__ == "__main__":
    main()
