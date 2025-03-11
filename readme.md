# 得到电子书批量下载工具

本项项目是基于[yann0917/dedao-dl: 得到 APP 课程下载工具，可在终端查看文章内容，可生成 PDF，音频文件，markdown 文稿，可下载电子书。](https://github.com/yann0917/dedao-dl)的脚本。通过dedao-dl工具获取得到电子书的 ID，然后通过该脚本生成下载命令。

## 简介

`dedao-dl-utils` 是一组用于管理和下载电子书的实用工具。包括以下脚本：

- `main.py`: 从输入文件中提取 ID 并生成下载命令，同时检查 `exist.txt` 文件中列出的电子书是否已经存在。
- `get_downloaded_filelist.py`: 递归遍历指定目录下的所有目录和文件，把 `.epub` 和 `.pdf` 文件名称列举到 `exist.txt` 中。

## 安装

确保你已经安装了 Python 3.6 或更高版本。

## 使用方法

### get_downloaded_filelist.py

该脚本递归遍历指定目录下的所有目录和文件，把 `.epub` 和 `.pdf` 文件名称列举到 `filelist.txt` 中。如果 `filelist.txt` 文件不存在，则创建它。

```sh
python get_downloaded_filelist.py -d /path/to/your/directory -o filelist.txt -a
```

参数说明：
- `-d` 或 `--directory`: 指定包含 `filelist.txt` 的目录。
- `-o` 或 `--output`: （可选）输出文件路径。默认为 `filelist.txt`。
- `-a` 或 `--append`: （可选）追加模式。如果提供此参数，则追加到 `filelist.txt` 文件中。

### main.py

该脚本从输入文件中提取 ID 并生成下载命令，同时检查 `exist.txt` 文件中列出的电子书是否已经存在。

```sh
python main.py -i input_file -o output_file -t 3 -e exist.txt
```

参数说明：
- `-i` 或 `--input`: 输入文件路径。
- `-o` 或 `--output`: 输出文件路径。
- `-t` 或 `--type`: 格式类型，1 表示 html，2 表示 pdf，3 表示 epub，4 表示同时下载 pdf 和 epub。
- `-e` 或 `--exist`: （可选）存在文件路径。如果没有提供，则 `existing_books` 是一个空的集合。

## 贡献

欢迎提交问题和贡献代码！

## 许可证

本项目采用 MIT 许可证。