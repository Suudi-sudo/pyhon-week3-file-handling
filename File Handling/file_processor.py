import os
from pathlib import Path

def read_and_modify_file():
    """
    Main function that handles file reading, modification, and writing
    with comprehensive error handling.
    """
    print("File Read & Write Challenge")
    print("=" * 40)
    
    while True:
        try:
            # Get filename from user
            filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
            
            if filename.lower() == 'quit':
                print("Goodbye!")
                break
            
            if not filename:
                print("Please enter a valid filename.")
                continue
            
            # Attempt to read the file
            print(f"\nAttempting to read '{filename}'...")
            
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print(f"Successfully read {len(content)} characters from '{filename}'")
            
            # Display original content (first 200 chars if long)
            if len(content) > 200:
                print(f"\nOriginal content (first 200 chars):\n{content[:200]}...")
            else:
                print(f"\nOriginal content:\n{content}")
            
            # Modify the content
            modified_content = modify_content(content, filename)
            
            # Generate output filename
            base_name = Path(filename).stem
            extension = Path(filename).suffix
            output_filename = f"{base_name}_modified{extension}"
            
            # Write modified content to new file
            write_modified_file(output_filename, modified_content)
            
            # Ask if user wants to process another file
            continue_choice = input("\nProcess another file? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("Thanks for using the File Processor!")
                break
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please check the filename and try again.")
            
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{filename}'. Make sure you have read permissions.")
            
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{filename}' as text. This might be a binary file. Try a text file.")
            
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please specify a file.")
            
        except OSError as e:
            print(f"OS Error: {e}. There was a system-level error accessing the file.")
            
        except Exception as e:
            print(f"Unexpected error: {e}. An unexpected error occurred. Please try again.")

def modify_content(content, filename):
    """
    Modify the file content in various ways.
    """
    print("\nModifying content...")
    
    # Get file extension to determine modification strategy
    extension = Path(filename).suffix.lower()
    
    modifications = []
    
    # Add header with file info
    header = f"=== MODIFIED VERSION OF {filename.upper()} ===\n"
    header += f"Original length: {len(content)} characters\n"
    header += f"Lines: {len(content.splitlines())}\n"
    header += f"Words: {len(content.split())}\n"
    header += "=" * 50 + "\n\n"
    
    modified_content = header + content
    modifications.append("Added file statistics header")
    
    # Text-specific modifications
    if extension in ['.txt', '.md', '.py', '.js', '.html', '.css']:
        # Add line numbers
        lines = content.splitlines()
        numbered_lines = [f"{i+1:3d}: {line}" for i, line in enumerate(lines)]
        numbered_content = "\n".join(numbered_lines)
        
        modified_content = header + "=== CONTENT WITH LINE NUMBERS ===\n\n" + numbered_content
        modifications.append("Added line numbers")
        
        # Add word count for each line
        modified_content += "\n\n=== LINE STATISTICS ===\n"
        for i, line in enumerate(lines):
            word_count = len(line.split())
            char_count = len(line)
            modified_content += f"Line {i+1}: {word_count} words, {char_count} characters\n"
        modifications.append("Added line statistics")
    
    # Add footer
    footer = f"\n\n=== END OF MODIFIED FILE ===\n"
    footer += f"Modifications applied: {', '.join(modifications)}\n"
    footer += f"Processing completed successfully!"
    
    modified_content += footer
    
    print(f"Applied {len(modifications)} modifications:")
    for mod in modifications:
        print(f"   • {mod}")
    
    return modified_content

def write_modified_file(output_filename, content):
    """
    Write the modified content to a new file with error handling.
    """
    try:
        print(f"\nWriting modified content to '{output_filename}'...")
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        file_size = os.path.getsize(output_filename)
        print(f"Successfully wrote {len(content)} characters ({file_size} bytes) to '{output_filename}'")
        
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{output_filename}'. Make sure you have write permissions.")
        
    except OSError as e:
        print(f"OS Error while writing file: {e}. There was a system-level error writing the file.")
        
    except Exception as e:
        print(f"Unexpected error while writing file: {e}")

def create_sample_file():
    """
    Create a sample file for testing if none exists.
    """
    sample_filename = "sample.txt"
    sample_content = """Welcome to the File Processing Challenge!

This is a sample text file that you can use to test the file processor.

Here are some interesting facts:
- Python is great for file handling
- Error handling makes programs robust
- Files can contain various types of data

You can create your own files to test with different content types:
- Text files (.txt)
- Python files (.py)
- Markdown files (.md)
- And many more!

Happy coding!
"""
    
    try:
        if not os.path.exists(sample_filename):
            with open(sample_filename, 'w', encoding='utf-8') as file:
                file.write(sample_content)
            print(f"Created sample file '{sample_filename}' for testing!")
        return sample_filename
    except Exception as e:
        print(f"Could not create sample file: {e}")
        return None

if __name__ == "__main__":
    print("Error Handling Lab - File Operations")
    print("This program demonstrates robust file handling with comprehensive error management.")
    
    # Create a sample file for testing
    sample_file = create_sample_file()
    if sample_file:
        print(f"Tip: Try using '{sample_file}' as your first test file!")
    
    # Run the main program
    read_and_modify_file()
