# NoteConverterApp

（中文版本在下方 / Chinese Version Below）

## ✨ Features

- **Preserve Timestamps**: Each note keeps its original reading timestamp.
- **Retain User-defined Obsidian Tags**: If you manually added tags like `#感想`, `#行动` while taking notes on your Boox device, these tags will be preserved as standard Obsidian-style tags in the final Markdown output.
- **Merge Notes**: All selected notes are merged into a single, organized Markdown file.
- **Simple GUI**: No command line needed — use a straightforward graphical interface.

## 🚀 How to Use

1. Go to the [Releases](https://github.com/LeaiFish/NoteConverterApp/releases) page.
2. Download the latest `html_to_md_converter.zip`.
3. Unzip it to get `html_to_md_converter.app`.
4. Open the app and select your exported HTML notes file.
5. The cleaned Markdown (`.md`) file will be generated in the same folder with the same base filename.

✅ Example:
> Select `Tiny Experiments.html` → Output `Tiny Experiments.md`

⚠️ **Note:** If you see a warning when opening the app (because it is from an unidentified developer),  
you can right-click the app → Open → Confirm to run it on macOS.

## 🧠 Design Philosophy

Many users (including myself) manually add lightweight tags such as `#感想` and `#行动` when taking notes on Boox devices.  
This tool is specifically designed to **retain and properly format these user-defined tags** into Obsidian-compatible Markdown, ensuring a smooth migration from Boox to Obsidian without losing personal note structures or reading annotations.

## 🛠️ Built With

- [Python 3.11](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — for GUI
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — for HTML parsing
- [PyInstaller](https://pyinstaller.org/) — for packaging into a standalone macOS `.app`

## 📦 Packaging (macOS)

This app is packaged using PyInstaller with GUI mode (`--windowed` option) into a native `.app` format for macOS users.

## 📄 License

This project is licensed under the MIT License — feel free to use and modify it!

## 🙏 Acknowledgement

I do not have a background in computer science.  
This project was made possible with the assistance of ChatGPT, which guided me through the entire development process.

---

# NoteConverterApp （中文说明）

一个轻量级的小工具，能够将Boox导出的HTML格式读书笔记，转换为适合Obsidian使用的干净Markdown文件。

## ✨ 功能特色

- **保留时间戳**：每条笔记都会保留原本记录的阅读时间。
- **保留用户自定义的Obsidian标签**：如果你在Boox设备上记笔记时手动添加了 `#感想`、`#行动` 等标签，本工具会自动保留下来，并转换成标准的Obsidian标签格式。
- **合并所有笔记**：所有选中的笔记会合并成一个有序的Markdown文件。
- **简洁的图形界面**：无需使用命令行，通过简单直观的界面完成操作。

## 🚀 使用方法

1. 前往 [Releases](https://github.com/LeaiFish/NoteConverterApp/releases) 页面。
2. 下载最新的 `html_to_md_converter.zip` 文件。
3. 解压后得到 `html_to_md_converter.app`。
4. 打开应用程序，选择你的Boox导出的HTML笔记文件。
5. 转换后生成的Markdown (`.md`) 文件，会保存到同一目录下，文件名与原HTML一致。

✅ 示例：
> 选择 `Tiny Experiments.html` → 输出 `Tiny Experiments.md`

⚠️ **注意**：由于应用未经过官方认证，首次打开可能会出现安全提示。  
可以右键点击 `.app` → 选择【打开】→ 再点击【打开】以通过验证。

## 🧠 设计理念

许多Boox用户（包括我自己）在记录读书笔记时，会手动添加轻量级标签如 `#感想`、`#行动`。  
本工具特别设计为**保留并正确格式化这些用户自定义标签**，确保从Boox迁移到Obsidian时，不丢失笔记结构和个人标记。

## 🛠️ 技术栈

- [Python 3.11](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — 图形界面
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — 解析HTML
- [PyInstaller](https://pyinstaller.org/) — 打包生成macOS的独立`.app`应用

## 📦 打包说明（macOS）

本应用使用PyInstaller，采用GUI模式（`--windowed`选项）打包成macOS原生`.app`文件，无需安装Python环境即可直接使用。

## 📄 授权许可

本项目使用MIT开源许可证发布，允许自由使用、修改和分发。

## 🙏 致谢

本人没有计算机专业背景。  
本项目在ChatGPT的协助和指导下完成。

---

> Made with ❤️ by [LeaiFish](https://github.com/LeaiFish)
