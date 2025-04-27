import tkinter as tk
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup
import os
import re

# 主转换函数
def convert_html_to_md(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    output = []
    current_chapter = None

    for elem in soup.body.children:
        if elem.name == 'div' and elem.span and elem.span.get('style', '').find('color: #48b4c1') != -1:
            # 章节标题
            current_chapter = elem.get_text(strip=True)
            output.append(f"\n## {current_chapter}\n")
        elif elem.name == 'div' and 'border-top' in elem.get('style', ''):
            # 摘录 + 时间戳
            timestamp = elem.find('div').get_text(strip=True)
            quote = elem.find_all('div')[1].get_text(strip=True)
            output.append(f"> {quote}\n\n{timestamp}\n")
        elif elem.name == 'div' and elem.find('span') and elem.find('span').get_text(strip=True).startswith('注 |'):
            # 注释内容
            note_full = elem.get_text(strip=True)
            note_full = re.sub(r"注 \|#", "注 | #", note_full)
            note_match = re.match(r"注 \| (#[^\s]+) (.+)", note_full)
            if note_match:
                tag = note_match.group(1)
                note_text = note_match.group(2)
                output.append(f"{tag} {note_text}\n\n---\n")
            else:
                output.append(f"{note_full}\n\n---\n")

    final_output = "# Tiny Experiments: How to Live (Anne-Laure Le Cunff)\n" + "\n".join(output)

    # 生成Markdown文件
    output_path = os.path.splitext(html_path)[0] + '.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

    return output_path

# GUI主程序
def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    messagebox.showinfo("选择文件", "请选择要转换的HTML笔记文件。")
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])

    if not file_path:
        messagebox.showinfo("取消", "没有选择任何文件。程序结束。")
        return

    try:
        output_file = convert_html_to_md(file_path)
        messagebox.showinfo("完成", f"转换完成！\n生成文件：\n{output_file}")
    except Exception as e:
        messagebox.showerror("错误", f"转换过程中发生错误：{str(e)}")

if __name__ == "__main__":
    main()
