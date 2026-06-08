# 环境配置说明

这份文件只讲“怎么把环境跑起来”。

你现在不用理解太多原理。

先把步骤做通就行。

## 第一步：打开终端

你可以先把终端理解成：

“和电脑直接说话的窗口”

## 第二步：依次输入下面 3 行

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 这 3 行分别是什么意思

### 第 1 行

```powershell
py -m venv .venv
```

创建一个当前项目专用的小环境。

### 第 2 行

```powershell
.\.venv\Scripts\Activate.ps1
```

启用这个小环境。

### 第 3 行

```powershell
pip install -r requirements.txt
```

安装这个项目需要的工具。

## 第三步：试着跑第一个脚本

```powershell
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_normal.txt --output outputs/clean_text/cleaned.txt
```

## 如果成功了

你会在这里看到输出文件：

`outputs/clean_text/cleaned.txt`

## 如果失败了

不要慌。

先做下面这件事：

把终端里最后几行报错完整发给我。

## 你现在不用理解的词

下面这些词现在可以先跳过：

- 虚拟环境原理
- 依赖管理
- requirements

你现在只需要知道：

这些步骤是为了让脚本能正常运行。

