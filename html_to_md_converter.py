import tkinter as tk
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup
import os
import re

def convert_html_to_md(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    output = []
    current_chapter = None

    for elem in soup.body.children:
        if elem.name == 'div' and elem.span and 'color: #48b4c1' in elem.span.get('style', ''):
            current_chapter = elem.get_text(strip=True)
            output.append(f"\n## {current_chapter}\n")
        elif elem.name == 'div' and 'border-top' in elem.get('style', ''):
            divs = elem.find_all('div')
            if len(divs) >= 2:
                timestamp = divs[0].get_text(strip=True)
                quote = divs[1].get_text(strip=True)
                # 清理连续空格，保证格式整洁
                quote = re.sub(r'\s+', ' ', quote)
                timestamp = re.sub(r'\s+', ' ', timestamp)
                output.append(f"> {quote}\n\n{timestamp}\n")
        elif elem.name == 'div' and elem.find('span') and elem.find('span').get_text(strip=True).startswith('注 |'):
            note_full = elem.get_text(strip=True)
            # 修正注释部分：统一给"注 |"后面补空格
            note_full = re.sub(r"注 \|(?=\S)", "注 | ", note_full)
            note_match = re.match(r"注 \| (#[^\s]+) (.+)", note_full)
            if note_match:
                tag = note_match.group(1)
                note_text = note_match.group(2)
                output.append(f"{tag} {note_text}\n\n---\n")
            else:
                output.append(f"{note_full}\n\n---\n")

    title_tag = soup.find('title')
    if title_tag and title_tag.get_text(strip=True):
        title_text = title_tag.get_text(strip=True)
    else:
        title_text = "Untitled"

    final_output = f"# {title_text}\n" + "\n".join(output)

    output_path = os.path.splitext(html_path)[0] + '.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

    return output_path

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])

    if not file_path:
        messagebox.showinfo("取消", "没有选择任何文件。程序结束。")
        return

    try:
        output_file = convert_html_to_md(file_path)
        messagebox.showinfo("完成", f"转换完成！\n生成文件：\n{output_file}")
    except Exception as e:
        messagebox.showerror("错误", f"转换过程中发生错误：{str(e)}")

# 创建图形界面
root = tk.Tk()
root.title("HTML to Markdown Converter for Boox Notes")

select_button = tk.Button(root, text="Select HTML File", command=select_file)
select_button.pack(padx=20, pady=20)

root.mainloop()