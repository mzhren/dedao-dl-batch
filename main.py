import argparse
import os

def load_existing_books(exist_file):
    if not exist_file or not os.path.exists(exist_file):
        return set()
    
    existing_books = set()
    with open(exist_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split('_')
            if len(parts) > 1:
                id = parts[0]
                ext = parts[-1].split('.')[-1].strip()
                existing_books.add((id, ext))
    return existing_books

def extract_ids_and_generate_commands(input_file, output_file, format_type, exist_file=None):
    existing_books = load_existing_books(exist_file)
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    ids = []
    for line in lines:
        if line.startswith('|'):
            parts = line.split('|')
            if len(parts) > 2 and parts[2].strip().isdigit():
                ids.append(parts[2].strip())

    commands = []
    for id in ids:
        if format_type == 4:
            if not (id, 'pdf') in existing_books or not (id, 'epub') in existing_books:
                if (id, 'pdf') not in existing_books:
                    commands.append(f"dedao-dl dle {id} -t 2")
                if (id, 'epub') not in existing_books:
                    commands.append(f"dedao-dl dle {id} -t 3")
        else:
            ext = {1: 'html', 2: 'pdf', 3: 'epub'}.get(format_type, 'epub')
            if (id, ext) not in existing_books:
                commands.append(f"dedao-dl dle {id} -t {format_type}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(commands))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract IDs and generate commands.")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path')
    parser.add_argument('-t', '--type', type=int, default=3, choices=[1, 2, 3, 4], help='Format type: 1 for html, 2 for pdf, 3 for epub, 4 for both pdf and epub')
    parser.add_argument('-e', '--exist', type=str, help='Exist file path')
    args = parser.parse_args()

    extract_ids_and_generate_commands(args.input, args.output, args.type, args.exist)
