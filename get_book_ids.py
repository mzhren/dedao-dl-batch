import json
import argparse
import os
import re

def extract_book_ids(input_file):
    """
    从输入文件中提取书籍ID
    """
    book_ids = set()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line in lines:
            # 检查是否是表格行（以"|"开头）
            if line.startswith('│'):
                parts = line.split('│')
                if len(parts) > 3:
                    # 尝试从第三列提取ID
                    id_part = parts[2].strip()
                    # 使用正则表达式提取数字ID
                    id_match = re.search(r'\d+', id_part)
                    if id_match:
                        book_id = id_match.group()
                        book_ids.add(book_id)
    except Exception as e:
        print(f"处理文件时出错: {e}")
    
    return book_ids

def save_to_json(book_ids, output_file):
    """
    将书籍ID保存到JSON文件
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(list(book_ids), file, ensure_ascii=False, indent=4)
        print(f"成功保存{len(book_ids)}个书籍ID到 {output_file}")
    except Exception as e:
        print(f"保存JSON文件时出错: {e}")

def main():
    parser = argparse.ArgumentParser(description="提取书籍ID并保存为JSON")
    parser.add_argument('-i', '--input', type=str, required=True, help='输入文件路径')
    parser.add_argument('-o', '--output', type=str, default='202507_02.json', help='输出JSON文件路径')
    args = parser.parse_args()
    
    book_ids = extract_book_ids(args.input)
    if book_ids:
        save_to_json(book_ids, args.output)
        print(f"共找到{len(book_ids)}个书籍ID")
    else:
        print("未找到任何书籍ID")

if __name__ == "__main__":
    main()
