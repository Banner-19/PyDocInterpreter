# PyDocInterpreter
PyDocInterpreter is a sophisticated code interpreter designed to seamlessly convert various document formats into executable Python code using the power of AI.By leveraging state-of-the-art technologies, PyDocInterpreter offers robust functionality to handle PDF, XLSX, CSV, and DOCX files, enabling users to extract and process content efficiently.

## Installation
__1. Clone the repository:__
```bash
git clone https://github.com/Banner-19/pydocinterpreter.git
cd pydocinterpreter
```
__2. Create a virtual environment:__
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
__3. Install dependencies:__
```bash
pip install -r requirements.txt
```
__4. Set up OpenAI API key:__

* Obtain your API key from OpenAI.
* Set the API key as an environment variable:
```bash
export OPENAI_API_KEY='your_api_key_here'
```

## Usage
__1. Run the main script:__
```bash
python main.py --file_path path_to_your_file --file_type file_type --user_prompt "your prompt"
```

## Project Structure
```bash
pydocinterpreter/
│
├── file_readers/
│   ├── __init__.py
│   ├── pdf_reader.py
│   ├── xlsx_reader.py
│   ├── csv_reader.py
│   ├── docx_reader.py
│
├── code_writer/
│   ├── __init__.py
│   ├── code_generator.py
│
├── code_executor/
│   ├── __init__.py
│   ├── code_executor.py
│
├── main.py
└──  requirements.txt
```

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
