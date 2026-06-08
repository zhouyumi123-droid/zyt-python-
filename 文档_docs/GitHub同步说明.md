# GitHub 同步说明

这份说明只解决一件事：

怎么把你的学习进度同步到 GitHub，
这样你换一台电脑也能继续学。

## 你的仓库

- 账户：`zhouyumi123-droid`
- 仓库：`zyt-python-`
- 地址：[GitHub 仓库](https://github.com/zhouyumi123-droid/zyt-python-)

## 以后每次学习的最简单流程

### 开始学习前

先拉最新进度：

```powershell
git pull
```

### 学完一个节点后

提交并推送：

```powershell
git add .
git commit -m "学习节点：这里写今天学了什么"
git push
```

## 什么时候算一个“学习节点”

你可以先这样理解：

- 跑通了一个脚本
- 看懂了一个概念
- 改好了一个报错
- 完成了一次小练习

做到这些，就值得提交一次。

## 以后我会怎么帮你同步

从现在开始，只要我们完成了一个明确的小阶段，我都会帮你：

1. 整理这次学了什么
2. 更新进度日志
3. 提交到 Git
4. 推送到 GitHub

## 你换电脑时怎么继续

如果另一台电脑还没有这个项目：

```powershell
git clone https://github.com/zhouyumi123-droid/zyt-python-.git
```

如果另一台电脑已经有这个项目：

```powershell
git pull
```

## 一句话版本

你以后不需要担心“学到哪了”。

因为每一个学习节点，都会被同步到 GitHub。

