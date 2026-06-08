# 第 1 周手动测试案例

## `clean_text.py`

正常输入：

```powershell
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_normal.txt --output outputs/manual/clean_text_normal.txt
```

空内容输入：

```powershell
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_missing.txt --output outputs/manual/clean_text_missing.txt
```

格式混乱输入：

```powershell
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_noisy.txt --output outputs/manual/clean_text_noisy.txt
```

## `json_to_csv.py`

正常输入：

```powershell
python 脚本_scripts/第01周_week01/json_to_csv.py --input 测试_tests/测试素材_fixtures/records_normal.json --output outputs/manual/records_normal.csv
```

顶层结构错误：

```powershell
python 脚本_scripts/第01周_week01/json_to_csv.py --input 测试_tests/测试素材_fixtures/records_invalid_shape.json --output outputs/manual/records_invalid_shape.csv
```

列表元素结构错误：

```powershell
python 脚本_scripts/第01周_week01/json_to_csv.py --input 测试_tests/测试素材_fixtures/records_bad_item.json --output outputs/manual/records_bad_item.csv
```

## `prompt_rewriter.py`

正常输入：

```powershell
python 脚本_scripts/第01周_week01/prompt_rewriter.py --input 测试_tests/测试素材_fixtures/prompts_normal.json --output outputs/manual/prompts_normal.json
```

缺少 `prompt` 字段：

```powershell
python 脚本_scripts/第01周_week01/prompt_rewriter.py --input 测试_tests/测试素材_fixtures/prompts_missing_prompt.json --output outputs/manual/prompts_missing_prompt.json
```

顶层结构错误：

```powershell
python 脚本_scripts/第01周_week01/prompt_rewriter.py --input 测试_tests/测试素材_fixtures/prompts_invalid_shape.json --output outputs/manual/prompts_invalid_shape.json
```
