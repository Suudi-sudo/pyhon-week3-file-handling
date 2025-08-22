# File Read & Write Challenge 

A comprehensive Python program demonstrating robust file handling, error management, and multi-format file processing capabilities. This project showcases best practices for reading, writing, and analyzing various file types with graceful error handling.

##  Project Overview

This repository contains two complementary Python programs designed to teach and demonstrate professional file handling techniques:

1. **Basic File Processor** (`file_processor.py`) - Interactive file reading/writing with comprehensive error handling
2. **Advanced File Handler** (`file_handler.py`) - Multi-format file processor with intelligent analysis capabilities

## Features

### Basic File Processor
- **Interactive file processing** with user-friendly prompts
- **Content modification** with line numbering and statistics
- **Comprehensive error handling** for all common file operations
- **Sample file generation** for immediate testing
- **Detailed feedback** and helpful error messages

### Advanced File Handler
- **Multi-format support**: Text, JSON, CSV, Python, and Markdown files
- **Intelligent file analysis** based on file type and content
- **Enhanced output generation** with metadata and processing reports
- **Object-oriented design** for extensibility and maintainability
- **Processing history tracking** with summary reports

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses only standard library)

### Installation
1. Clone this repository or download the files
2. Ensure Python is installed on your system
3. Navigate to the project directory

### Quick Start
\`\`\`bash
# Run the basic file processor
python Fie Handling/file_processor.py

# Run the advanced file handler
python Fie Handling/file_handler.py
\`\`\`

##  Usage Examples

### Basic File Processor
\`\`\`bash
$ python File Handling/file_processor.py
 Error Handling Lab - File Operations
 Created sample file 'sample.txt' for testing!
 Tip: Try using 'sample.txt' as your first test file!

 File Read & Write Challenge


Enter the filename to read (or 'quit' to exit): sample.txt
 Attempting to read 'sample.txt'...
 Successfully read 234 characters from 'sample.txt'
\`\`\`

### Advanced File Handler
\`\`\`bash
$ python File Handling/file_handler.py
 Advanced File Processor
Supported file types: .txt, .json, .csv, .py, .md

 Enter filename to process: data.json
 Processing JSON file: data.json
Created: data_enhanced.json
 Processing completed successfully!
\`\`\`

##  Error Handling

Both programs implement comprehensive error handling for:

| Error Type | Description | Handling Strategy |
|------------|-------------|-------------------|
| `FileNotFoundError` | File doesn't exist | User-friendly message with suggestions |
| `PermissionError` | Insufficient permissions | Clear explanation and troubleshooting tips |
| `UnicodeDecodeError` | Binary or encoding issues | Detection and appropriate handling |
| `IsADirectoryError` | Directory instead of file | Clear distinction and guidance |
| `JSONDecodeError` | Malformed JSON files | Specific JSON error reporting |
| `csv.Error` | CSV parsing issues | CSV-specific error handling |

##  File Type Support

### Supported Formats

| Format | Extension | Analysis Features |
|--------|-----------|-------------------|
| **Text** | `.txt` | Line/word/character counts, longest line analysis |
| **JSON** | `.json` | Structure analysis, nested object exploration |
| **CSV** | `.csv` | Column/row statistics, data validation |
| **Python** | `.py` | Code metrics, function/class counting, documentation |
| **Markdown** | `.md` | Header extraction, link/image counting, TOC generation |

### Output Files

Each processed file generates enhanced versions:
- `filename_modified.ext` - Basic processor output
- `filename_analyzed.ext` - Text analysis reports
- `filename_enhanced.ext` - Advanced processor output
- `filename_documented.py` - Python files with added documentation

##  Code Structure

### Basic File Processor (`file_processor.py`)
\`\`\`python
def read_and_modify_file()     # Main interactive loop
def modify_content()           # Content transformation logic
def write_modified_file()      # Safe file writing with error handling
def create_sample_file()       # Test file generation
\`\`\`

### Advanced File Handler (`file_handler.py`)
\`\`\`python
class FileProcessor:
    def process_file()         # Main processing orchestrator
    def process_text_file()    # Text-specific processing
    def process_json_file()    # JSON analysis and enhancement
    def process_csv_file()     # CSV statistics and validation
    def process_python_file()  # Python code analysis
    def process_markdown_file() # Markdown enhancement
\`\`\`

##  Learning Outcomes

By exploring this project, you'll master:

- **File I/O Operations**: Reading and writing files safely
- **Error Handling**: Implementing robust exception management
- **Data Analysis**: Extracting meaningful insights from file content
- **Code Organization**: Structuring programs for maintainability
- **User Experience**: Creating intuitive command-line interfaces
- **File Format Processing**: Handling multiple data formats appropriately

## Testing

### Manual Testing
1. Run either program
2. Test with various file types and scenarios:
   - Existing files
   - Non-existent files
   - Binary files
   - Files without permissions
   - Empty files
   - Large files

### Sample Test Cases
\`\`\`bash
# Test error handling
Enter filename: nonexistent.txt     # FileNotFoundError
Enter filename: /root/protected.txt  # PermissionError
Enter filename: image.jpg            # UnicodeDecodeError

# Test file types
Enter filename: data.json            # JSON processing
Enter filename: spreadsheet.csv      # CSV analysis
Enter filename: script.py            # Python code analysis
\`\`\`



##  Support

If you encounter issues or have questions:
1. Check the error messages for troubleshooting tips
2. Ensure file permissions are correct
3. Verify Python version compatibility
4. Review the code comments for implementation details

---

