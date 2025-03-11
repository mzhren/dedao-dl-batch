import argparse
import os

def get_already_downloaded_books(directory, output_file, append=False):
    if not os.path.exists(output_file):
        print(f"File {output_file} does not exist. Creating a new one.")
        open(output_file, 'w', encoding='utf-8').close()
        append = False  # 如果文件不存在，忽略append参数

    books = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.epub') or file.endswith('.pdf'):
                books.append(file)

    # 根据append参数决定是追加还是覆盖
    mode = 'a' if append else 'w'
    with open(output_file, mode, encoding='utf-8') as file:
        for book in books:
            file.write(f"{book}\n")

    return books

def main():
    parser = argparse.ArgumentParser(description='Get already downloaded book list.')
    parser.add_argument('-d', '--directory', required=True, help='Directory to search for books')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    parser.add_argument('-a', '--append', action='store_true', help='Append to output file if it exists')
    args = parser.parse_args()

    books = get_already_downloaded_books(args.directory, args.output, args.append)
    if books:
        print("Already downloaded books:")
        for book in books:
            print(book)
    else:
        print("No books found or output file is empty.")

if __name__ == '__main__':
    main()
