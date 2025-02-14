import argparse
import os

def get_already_downloaded_books(directory):
    filelist_path = os.path.join(directory, 'filelist.txt')
    if not os.path.exists(filelist_path):
        print(f"File {filelist_path} does not exist. Creating a new one.")
        open(filelist_path, 'w').close()

    books = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.epub') or file.endswith('.pdf'):
                books.append(file)

    with open(filelist_path, 'w') as file:
        for book in books:
            file.write(f"{book}\n")

    return books

def main():
    parser = argparse.ArgumentParser(description='Get already downloaded book list.')
    parser.add_argument('-d', '--directory', required=True, help='Directory containing filelist.txt')
    args = parser.parse_args()

    books = get_already_downloaded_books(args.directory)
    if books:
        print("Already downloaded books:")
        for book in books:
            print(book)
    else:
        print("No books found or filelist.txt is empty.")

if __name__ == '__main__':
    main()
