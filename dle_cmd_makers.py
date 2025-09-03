import json
import os
import sys

def compare_json_and_generate_commands(input_file, exist_file, output_file, command='dle', format_str='{cmd} {id}'):
    """
    比较输入JSON文件和已存在JSON文件，为新条目生成下载命令
    
    Args:
        input_file (str): 输入JSON文件路径
        exist_file (str): 已存在JSON文件路径
        output_file (str): 输出TXT文件路径
        command (str): 用于下载的命令
        format_str (str): 下载命令的格式
        
    Returns:
        dict: 操作统计信息
    """
    # 检查文件是否存在
    for file_path in [input_file, exist_file]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件 '{file_path}' 不存在。")

    # 加载JSON文件
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"'{input_file}' 不是有效的JSON文件。")

    try:
        with open(exist_file, 'r', encoding='utf-8') as f:
            exist_data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"'{exist_file}' 不是有效的JSON文件。")

    # 转换存在的数据为set，方便快速查找
    exist_set = set(exist_data)

    # 找出新条目
    new_entries = [entry for entry in input_data if entry not in exist_set]

    # 生成下载命令
    commands = [format_str.format(cmd=command, id=entry) for entry in new_entries]

    # 将命令写入输出文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(commands))
    except Exception as e:
        raise IOError(f"写入 '{output_file}' 时出错: {e}")

    # 返回统计信息
    stats = {
        "new_entries": len(new_entries),
        "input_entries": len(input_data),
        "existing_entries": len(exist_data),
        "new_entries_list": new_entries
    }
    
    return stats

def main():
    import argparse
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='为新条目生成下载命令')
    parser.add_argument('--input', '-i', required=True, help='输入JSON文件路径')
    parser.add_argument('--exist', '-e', required=True, help='已存在JSON文件路径')
    parser.add_argument('--output', '-o', required=True, help='输出TXT文件路径')
    parser.add_argument('--command', '-c', default='dle', help='用于下载的命令 (默认: dle)')
    parser.add_argument('--format', '-f', default='{cmd} {id}', help='下载命令的格式 (默认: "{cmd} {id}")')
    args = parser.parse_args()

    try:
        stats = compare_json_and_generate_commands(
            args.input,
            args.exist,
            args.output,
            args.command,
            args.format
        )
        
        print(f"已生成 {stats['new_entries']} 条下载命令到 {args.output}")
        print(f"新条目: {stats['new_entries']}, 输入条目总数: {stats['input_entries']}, 已存在条目: {stats['existing_entries']}")
        if stats['new_entries'] > 0:
            print(f"新条目列表: {stats['new_entries_list'][:5]}{'...' if len(stats['new_entries_list']) > 5 else ''}")
    
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
