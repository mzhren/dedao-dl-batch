import argparse
import os
import json

def load_existing_books_json(exist_file):
    if not exist_file or not os.path.exists(exist_file):
        return set()
    
    existing_books = set()
    with open(exist_file, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {exist_file}. Returning empty set.")
            return existing_books
        for item in data:
            existing_books.add(item)
    return existing_books

def extract_ids_and_generate_commands(input_file, output_file, format_type, exist_file=None):
    existing_books = load_existing_books_json(exist_file)

    input_books = set()
    
    with open(input_file, 'r', encoding='utf-8') as file:
       try: 
           data = json.load(file)
       except json.JSONDecodeError:
              print(f"Error decoding JSON from {input_file}. Returning empty set.")
              return
       for item in data:
           input_books.add(item)

    input_books_not_in_existing = input_books - existing_books

    commands = []
    for id in input_books_not_in_existing:
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
