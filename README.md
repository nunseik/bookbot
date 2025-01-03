# Project: Text Analysis Tool

## Overview
This project is a simple Python program that reads a text file, analyzes its content, and generates a report. The report includes the total word count and the frequency of each alphabetic character in the text.

## Features
- Reads a text file specified in the `book_path` variable.
- Counts the total number of words in the document.
- Counts the frequency of each alphabetic character.
- Sorts the characters by frequency in descending order.

## Requirements
- Python 3.x

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/nunseik/bookbot
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

## Usage
### Adjusting the `book_path`
Before running the program, ensure the `book_path` variable in the code points to the text file you want to analyze. By default, it is set to:
```python
book_path = "books/frankenstein.txt"
```
Replace `books/frankenstein.txt` with the path to your desired text file. Book not provided in this repo.

### Running the Program
Execute the script using Python:
```bash
python3 main.py
```

### Example Output
When analyzing a text file, the program outputs a report similar to this:
```
--- Begin report of books/frankenstein.txt ---
5000 words found in the document

The 'e' character was found 1023 times
The 't' character was found 920 times
...
--- End report ---
```

## Note on File Structure
- The program expects the text files to be in the `books/` directory by default. Ensure this directory exists and contains the text file you wish to analyze.

## .gitignore
The `books/` directory is included in the `.gitignore` file to prevent text files from being added to the repository. Ensure you add your text files locally without committing them to the repository.

Example `.gitignore` file content:
```
books/
```

## Limitations
- The `book_path` variable is hardcoded, so it must be adjusted manually for each text file.
- Only alphabetic characters are considered in the frequency count.

## License
This project is open-source. Feel free to modify and distribute it.