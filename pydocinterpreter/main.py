from file_readers import read_pdf, read_xlsx, read_csv, read_docx
from code_writer import generate_code
from code_executor import execute_code
import pandas as pd

# Integration with Vanilla LLM
def process_file(file_path, file_type, user_prompt):
    if file_type == 'pdf':
        content = read_pdf(file_path)
    elif file_type == 'xlsx':
        content = read_xlsx(file_path)
    elif file_type == 'csv':
        content = read_csv(file_path)
    elif file_type == 'docx':
        content = read_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

    prompt = f"{user_prompt}\n\nFile Content:\n{content}"
    code = generate_code(prompt)
    result = execute_code(code)
    return result

#----------------------------------------------------------------------------------------------------------------

# Format Output
def format_output(result):
    if isinstance(result, dict):
        return pd.DataFrame(result).to_string()
    elif isinstance(result, str):
        return result
    else:
        return str(result)

#----------------------------------------------------------------------------------------------------------------

def main(file_path, file_type, user_prompt):
    result = process_file(file_path, file_type, user_prompt)
    formatted_output = format_output(result)
    return formatted_output

# Example
# if __name__ == "__main__":
#     file_path = "example.pdf"
#     file_type = "pdf"
#     user_prompt = "Summarize the content of this PDF."
#     output = main(file_path, file_type, user_prompt)
#     print(output)
