import argparse
import os

def get_already_downloaded_books(directory, output_file):
    if not os.path.exists(output_file):
        print(f"File {output_file} does not exist. Creating a new one.")
        open(output_file, 'w').close()

    books = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.epub') or file.endswith('.pdf'):
                books.append(file)

    with open(output_file, 'w') as file:
        for book in books:
            file.write(f"{book}\n")

    return books

def main():
    parser = argparse.ArgumentParser(description='Get already downloaded book list.')
    parser.add_argument('-d', '--directory', required=True, help='Directory to search for books')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    args = parser.parse_args()

    books = get_already_downloaded_books(args.directory, args.output)
    if books:
        print("Already downloaded books:")
        for book in books:
            print(book)
    else:
        print("No books found or output file is empty.")

if __name__ == '__main__':
    main()
