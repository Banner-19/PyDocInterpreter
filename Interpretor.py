import argparse
from pydocinterpreter import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the file')
    parser.add_argument('--file_type', type=str, required=True, choices=['pdf', 'xlsx', 'csv', 'docx'], help='Type of the file')
    parser.add_argument('--user_prompt', type=str, required=True, help='User prompt for processing the file')
    args = parser.parse_args()

    output = main(args.file_path, args.file_type, args.user_prompt)
    print(output)
