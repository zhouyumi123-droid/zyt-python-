# 第 2 周手动测试案例

## `material_loader.py`

正常输入：

```powershell
python 脚本_scripts/第02周_week02/material_loader.py --input-dir 测试_tests/测试素材_fixtures/正常资料_materials_normal --output outputs/manual/material_digest.md --manifest outputs/manual/material_manifest.json
```

文件内容为空：

```powershell
python 脚本_scripts/第02周_week02/material_loader.py --input-dir 测试_tests/测试素材_fixtures/资料为空_materials_empty --output outputs/manual/material_empty.md --manifest outputs/manual/material_empty.json
```

JSON 结构错误：

```powershell
python 脚本_scripts/第02周_week02/material_loader.py --input-dir 测试_tests/测试素材_fixtures/资料结构错误_materials_invalid_shape --output outputs/manual/material_invalid.md --manifest outputs/manual/material_invalid.json
```

## `topic_idea_generator.py`

正常输入：

```powershell
python 脚本_scripts/第02周_week02/topic_idea_generator.py --input 测试_tests/测试素材_fixtures/topic_seed_normal.json --output outputs/manual/topic_ideas_normal.json
```

缺少 `keyword` 字段：

```powershell
python 脚本_scripts/第02周_week02/topic_idea_generator.py --input 测试_tests/测试素材_fixtures/topic_seed_missing_keyword.json --output outputs/manual/topic_ideas_missing_keyword.json
```

顶层结构错误：

```powershell
python 脚本_scripts/第02周_week02/topic_idea_generator.py --input 测试_tests/测试素材_fixtures/topic_seed_invalid_shape.json --output outputs/manual/topic_ideas_invalid_shape.json
```
