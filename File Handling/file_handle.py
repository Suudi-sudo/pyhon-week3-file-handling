import json
import csv
import os
from datetime import datetime
from pathlib import Path

class FileProcessor:
    """
    Advanced file processor with support for multiple file types
    and comprehensive error handling.
    """
    
    def __init__(self):
        self.supported_extensions = {
            '.txt': self.process_text_file,
            '.json': self.process_json_file,
            '.csv': self.process_csv_file,
            '.py': self.process_python_file,
            '.md': self.process_markdown_file
        }
        self.processed_files = []
    
    def process_file(self, filename):
        """
        Process a file based on its extension with appropriate error handling.
        """
        try:
            file_path = Path(filename)
            
            # Validate file exists
            if not file_path.exists():
                raise FileNotFoundError(f"File '{filename}' does not exist")
            
            # Validate it's a file, not a directory
            if not file_path.is_file():
                raise IsADirectoryError(f"'{filename}' is not a file")
            
            # Get file extension
            extension = file_path.suffix.lower()
            
            # Check if we support this file type
            if extension not in self.supported_extensions:
                print(f"  Warning: '{extension}' files are not specifically supported.")
                print("   Treating as generic text file...")
                extension = '.txt'
            
            # Process the file
            processor = self.supported_extensions[extension]
            result = processor(filename)
            
            # Track processed file
            self.processed_files.append({
                'filename': filename,
                'extension': extension,
                'processed_at': datetime.now().isoformat(),
                'success': True
            })
            
            return result
            
        except FileNotFoundError as e:
            print(f" File Not Found: {e}")
            return None
            
        except PermissionError as e:
            print(f" Permission Denied: {e}")
            print(" Check file permissions and try again.")
            return None
            
        except UnicodeDecodeError as e:
            print(f" Encoding Error: Cannot read file as text")
            print(" This might be a binary file or use a different encoding.")
            return None
            
        except json.JSONDecodeError as e:
            print(f" JSON Error: Invalid JSON format - {e}")
            return None
            
        except csv.Error as e:
            print(f" CSV Error: {e}")
            return None
            
        except Exception as e:
            print(f" Unexpected Error: {e}")
            return None
    
    def process_text_file(self, filename):
        """Process plain text files."""
        print(f" Processing text file: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Analyze text
        lines = content.splitlines()
        words = content.split()
        
        analysis = {
            'type': 'text',
            'lines': len(lines),
            'words': len(words),
            'characters': len(content),
            'longest_line': max(len(line) for line in lines) if lines else 0,
            'average_words_per_line': len(words) / len(lines) if lines else 0
        }
        
        # Create modified version
        modified_content = self.create_text_analysis_report(filename, content, analysis)
        output_file = self.write_output_file(filename, modified_content, '_analyzed')
        
        return {'analysis': analysis, 'output_file': output_file}
    
    def process_json_file(self, filename):
        """Process JSON files."""
        print(f"🔧 Processing JSON file: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Analyze JSON structure
        analysis = self.analyze_json_structure(data)
        
        # Create enhanced JSON with metadata
        enhanced_data = {
            '_metadata': {
                'original_file': filename,
                'processed_at': datetime.now().isoformat(),
                'analysis': analysis
            },
            'data': data
        }
        
        output_file = self.write_json_file(filename, enhanced_data, '_enhanced')
        
        return {'analysis': analysis, 'output_file': output_file}
    
    def process_csv_file(self, filename):
        """Process CSV files."""
        print(f" Processing CSV file: {filename}")
        
        rows = []
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            rows = list(csv_reader)
        
        if not headers:
            raise csv.Error("CSV file appears to be empty or malformed")
        
        # Analyze CSV
        analysis = {
            'type': 'csv',
            'columns': len(headers),
            'rows': len(rows),
            'headers': headers,
            'total_cells': len(headers) * len(rows)
        }
        
        # Create enhanced CSV with statistics
        output_file = self.create_enhanced_csv(filename, headers, rows, analysis)
        
        return {'analysis': analysis, 'output_file': output_file}
    
    def process_python_file(self, filename):
        """Process Python files."""
        print(f" Processing Python file: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Basic Python code analysis
        lines = content.splitlines()
        analysis = {
            'type': 'python',
            'total_lines': len(lines),
            'code_lines': len([line for line in lines if line.strip() and not line.strip().startswith('#')]),
            'comment_lines': len([line for line in lines if line.strip().startswith('#')]),
            'blank_lines': len([line for line in lines if not line.strip()]),
            'imports': len([line for line in lines if line.strip().startswith(('import ', 'from '))]),
            'functions': content.count('def '),
            'classes': content.count('class ')
        }
        
        # Create documented version
        documented_content = self.create_python_documentation(filename, content, analysis)
        output_file = self.write_output_file(filename, documented_content, '_documented')
        
        return {'analysis': analysis, 'output_file': output_file}
    
    def process_markdown_file(self, filename):
        """Process Markdown files."""
        print(f" Processing Markdown file: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.splitlines()
        analysis = {
            'type': 'markdown',
            'total_lines': len(lines),
            'headers': len([line for line in lines if line.strip().startswith('#')]),
            'links': content.count('['),
            'images': content.count('!['),
            'code_blocks': content.count('```'),
            'bold_text': content.count('**'),
            'italic_text': content.count('*') - content.count('**') * 2
        }
        
        # Create enhanced markdown with table of contents
        enhanced_content = self.create_enhanced_markdown(filename, content, analysis)
        output_file = self.write_output_file(filename, enhanced_content, '_enhanced')
        
        return {'analysis': analysis, 'output_file': output_file}
    
    def analyze_json_structure(self, data, path="root"):
        """Recursively analyze JSON structure."""
        if isinstance(data, dict):
            return {
                'type': 'object',
                'keys': len(data),
                'key_names': list(data.keys()),
                'nested_structure': {k: self.analyze_json_structure(v, f"{path}.{k}") 
                                   for k, v in data.items()}
            }
        elif isinstance(data, list):
            return {
                'type': 'array',
                'length': len(data),
                'item_types': list(set(type(item).__name__ for item in data))
            }
        else:
            return {
                'type': type(data).__name__,
                'value': str(data)[:50] + ('...' if len(str(data)) > 50 else '')
            }
    
    def create_text_analysis_report(self, filename, content, analysis):
        """Create a detailed analysis report for text files."""
        report = f"""# TEXT FILE ANALYSIS REPORT
## File: {filename}
## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### Statistics:
- Total Lines: {analysis['lines']}
- Total Words: {analysis['words']}
- Total Characters: {analysis['characters']}
- Longest Line: {analysis['longest_line']} characters
- Average Words per Line: {analysis['average_words_per_line']:.2f}

### Original Content:
{'-' * 50}
{content}
{'-' * 50}

### Line-by-Line Analysis:
"""
        
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            word_count = len(line.split())
            char_count = len(line)
            report += f"Line {i:3d}: {word_count:3d} words, {char_count:3d} chars | {line}\n"
        
        return report
    
    def write_output_file(self, original_filename, content, suffix):
        """Write content to output file with error handling."""
        try:
            path = Path(original_filename)
            output_filename = f"{path.stem}{suffix}{path.suffix}"
            
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f" Created: {output_filename}")
            return output_filename
            
        except Exception as e:
            print(f" Error writing output file: {e}")
            return None
    
    def write_json_file(self, original_filename, data, suffix):
        """Write JSON data to file."""
        try:
            path = Path(original_filename)
            output_filename = f"{path.stem}{suffix}.json"
            
            with open(output_filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            print(f" Created: {output_filename}")
            return output_filename
            
        except Exception as e:
            print(f" Error writing JSON file: {e}")
            return None
    
    def create_enhanced_csv(self, filename, headers, rows, analysis):
        """Create enhanced CSV with statistics."""
        try:
            path = Path(filename)
            output_filename = f"{path.stem}_enhanced.csv"
            
            with open(output_filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write metadata
                writer.writerow(['# Enhanced CSV File'])
                writer.writerow([f'# Original: {filename}'])
                writer.writerow([f'# Processed: {datetime.now().isoformat()}'])
                writer.writerow([f'# Columns: {analysis["columns"]}'])
                writer.writerow([f'# Rows: {analysis["rows"]}'])
                writer.writerow([''])
                
                # Write original data
                writer.writerow(headers)
                writer.writerows(rows)
                
                # Write statistics
                writer.writerow([''])
                writer.writerow(['# Column Statistics'])
                for i, header in enumerate(headers):
                    column_data = [row[i] if i < len(row) else '' for row in rows]
                    non_empty = len([cell for cell in column_data if cell.strip()])
                    writer.writerow([f'Column: {header}', f'Non-empty cells: {non_empty}'])
            
            print(f" Created: {output_filename}")
            return output_filename
            
        except Exception as e:
            print(f" Error creating enhanced CSV: {e}")
            return None
    
    def create_python_documentation(self, filename, content, analysis):
        """Create documented Python file."""
        doc_header = f'''"""
PYTHON FILE ANALYSIS AND DOCUMENTATION
======================================
Original File: {filename}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Code Statistics:
- Total Lines: {analysis['total_lines']}
- Code Lines: {analysis['code_lines']}
- Comment Lines: {analysis['comment_lines']}
- Blank Lines: {analysis['blank_lines']}
- Import Statements: {analysis['imports']}
- Functions: {analysis['functions']}
- Classes: {analysis['classes']}

Code Quality Metrics:
- Comment Ratio: {(analysis['comment_lines'] / analysis['total_lines'] * 100):.1f}%
- Code Density: {(analysis['code_lines'] / analysis['total_lines'] * 100):.1f}%
"""

'''
        
        return doc_header + content
    
    def create_enhanced_markdown(self, filename, content, analysis):
        """Create enhanced Markdown with table of contents."""
        # Extract headers for TOC
        lines = content.splitlines()
        headers = []
        for line in lines:
            if line.strip().startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                title = line.strip('#').strip()
                headers.append((level, title))
        
        # Create table of contents
        toc = "# Table of Contents\n\n"
        for level, title in headers:
            indent = "  " * (level - 1)
            toc += f"{indent}- {title}\n"
        
        enhanced_content = f"""# Enhanced Markdown Document

**Original File:** {filename}  
**Enhanced:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Document Statistics
- Total Lines: {analysis['total_lines']}
- Headers: {analysis['headers']}
- Links: {analysis['links']}
- Images: {analysis['images']}
- Code Blocks: {analysis['code_blocks']}
- Bold Text Instances: {analysis['bold_text']}
- Italic Text Instances: {analysis['italic_text']}

{toc}

---

# Original Content

{content}
"""
        
        return enhanced_content
    
    def generate_summary_report(self):
        """Generate a summary report of all processed files."""
        if not self.processed_files:
            print(" No files have been processed yet.")
            return
        
        report_filename = f"processing_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(report_filename, 'w', encoding='utf-8') as file:
                file.write("FILE PROCESSING SUMMARY REPORT\n")
                file.write("=" * 50 + "\n")
                file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total Files Processed: {len(self.processed_files)}\n\n")
                
                for i, file_info in enumerate(self.processed_files, 1):
                    file.write(f"{i}. {file_info['filename']}\n")
                    file.write(f"   Type: {file_info['extension']}\n")
                    file.write(f"   Processed: {file_info['processed_at']}\n")
                    file.write(f"   Status: {' Success' if file_info['success'] else ' Failed'}\n\n")
            
            print(f" Summary report saved to: {report_filename}")
            
        except Exception as e:
            print(f" Error generating summary report: {e}")

def main():
    """Main function to run the advanced file processor."""
    processor = FileProcessor()
    
    print("🚀 Advanced File Processor")
    print("=" * 50)
    print("Supported file types: .txt, .json, .csv, .py, .md")
    print("Type 'quit' to exit, 'summary' for processing report")
    
    while True:
        try:
            filename = input("\n Enter filename to process: ").strip()
            
            if filename.lower() == 'quit':
                processor.generate_summary_report()
                print(" Goodbye!")
                break
            
            if filename.lower() == 'summary':
                processor.generate_summary_report()
                continue
            
            if not filename:
                print(" Please enter a valid filename.")
                continue
            
            result = processor.process_file(filename)
            
            if result:
                print(f" Processing completed successfully!")
                print(f" Analysis: {result['analysis']}")
                if result.get('output_file'):
                    print(f" Output saved to: {result['output_file']}")
            
        except KeyboardInterrupt:
            print("\n\n  Process interrupted by user.")
            processor.generate_summary_report()
            break
        except Exception as e:
            print(f" Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()
