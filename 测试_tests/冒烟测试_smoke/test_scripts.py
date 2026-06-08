import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ScriptSmokeTests(unittest.TestCase):
    def run_command(self, args, expect_success=True):
        result = subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if expect_success and result.returncode != 0:
            self.fail(result.stderr or result.stdout)
        if not expect_success and result.returncode == 0:
            self.fail("Command unexpectedly succeeded.")
        return result

    def test_clean_text_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "cleaned.txt"
            self.run_command(
                [
                    "脚本_scripts/第01周_week01/clean_text.py",
                    "--input",
                    "测试_tests/测试素材_fixtures/raw_text_normal.txt",
                    "--output",
                    str(output),
                ]
            )
            text = output.read_text(encoding="utf-8")
            self.assertIn("AI 自动化 确实能节省时间。", text)

    def test_json_to_csv_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "records.csv"
            self.run_command(
                [
                    "脚本_scripts/第01周_week01/json_to_csv.py",
                    "--input",
                    "测试_tests/测试素材_fixtures/records_normal.json",
                    "--output",
                    str(output),
                ]
            )
            text = output.read_text(encoding="utf-8")
            self.assertIn("title,platform,tags,owner", text)

    def test_prompt_rewriter_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "prompts.json"
            self.run_command(
                [
                    "脚本_scripts/第01周_week01/prompt_rewriter.py",
                    "--input",
                    "测试_tests/测试素材_fixtures/prompts_normal.json",
                    "--output",
                    str(output),
                ]
            )
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertIn("rewritten_prompt", payload[0])

    def test_material_loader_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "digest.md"
            manifest = Path(temp_dir) / "manifest.json"
            self.run_command(
                [
                    "脚本_scripts/第02周_week02/material_loader.py",
                    "--input-dir",
                    "测试_tests/测试素材_fixtures/正常资料_materials_normal",
                    "--output",
                    str(output),
                    "--manifest",
                    str(manifest),
                ]
            )
            text = output.read_text(encoding="utf-8")
            self.assertIn("# 资料汇总", text)

    def test_topic_idea_generator_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "ideas.json"
            self.run_command(
                [
                    "脚本_scripts/第02周_week02/topic_idea_generator.py",
                    "--input",
                    "测试_tests/测试素材_fixtures/topic_seed_normal.json",
                    "--output",
                    str(output),
                ]
            )
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(payload), 5)

    def test_invalid_prompt_case_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "bad.json"
            result = self.run_command(
                [
                    "脚本_scripts/第01周_week01/prompt_rewriter.py",
                    "--input",
                    "测试_tests/测试素材_fixtures/prompts_missing_prompt.json",
                    "--output",
                    str(output),
                ],
                expect_success=False,
            )
            self.assertIn("prompt", result.stderr)


if __name__ == "__main__":
    unittest.main()
