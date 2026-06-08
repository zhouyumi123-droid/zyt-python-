# 从这里开始

这份文件只做一件事：

带你完成第一次最简单的 Python 练习。

你现在不用理解全部内容，只要先把第一步跑通。

## 你现在要做什么

### 目标

运行一个叫 `clean_text.py` 的小脚本。

这个脚本的作用非常简单：

把一段乱糟糟的文字整理干净。

比如：

- 去掉多余空格
- 去掉空行

## 先理解 4 个词

### 1. 终端

终端就是你输入命令的黑框或蓝框窗口。

你可以把它理解成：

“直接跟电脑下命令的地方”

### 2. 命令

命令就是你输入给电脑的一句话。

比如：

```powershell
python --version
```

它的意思是：

“告诉我你这台电脑上的 Python 版本”

### 3. 脚本

脚本就是一个 `.py` 文件。

你可以把它理解成一个小工具。

### 4. 输入 和 输出

你现在先这样理解：

- 输入：给脚本的东西
- 输出：脚本处理完给你的结果

在这次练习里：

- 输入：一份原始文本文件
- 输出：一份整理后的文本文件

## 第一次操作

请按顺序运行下面这些命令。

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_normal.txt --output outputs/lesson01/cleaned.txt
```

## 每一行命令是什么意思

### 第 1 行

```powershell
py -m venv .venv
```

意思是：

创建一个这个项目专用的小环境。

你现在不用深究原理，只要知道：

这样做比较干净，不容易和别的项目打架。

### 第 2 行

```powershell
.\.venv\Scripts\Activate.ps1
```

意思是：

启用刚才那个小环境。

### 第 3 行

```powershell
pip install -r requirements.txt
```

意思是：

把这个项目需要的工具装好。

### 第 4 行

```powershell
python 脚本_scripts/第01周_week01/clean_text.py --input 测试_tests/测试素材_fixtures/raw_text_normal.txt --output outputs/lesson01/cleaned.txt
```

意思是：

用 Python 运行 `clean_text.py`，
让它读取输入文件，
再把结果写到输出文件里。

## 如果成功了，你会得到什么

你会在下面这个位置看到新文件：

`outputs/lesson01/cleaned.txt`

这个文件就是脚本处理后的结果。

## 如果失败了，先别慌

你现在只需要做这 3 件事：

1. 看最后一行报错
2. 复制报错给我
3. 不要自己乱改一堆东西

## 这次练习结束后，你应该会明白什么

哪怕只明白下面这 3 件事，就已经很好：

1. Python 脚本是可以运行起来的
2. 脚本会吃“输入”，吐出“输出”
3. 你已经开始真正进入这个领域了

