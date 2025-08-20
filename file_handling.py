"""
File Handling Assignment
Student: [Your Name]
Date: [Submission Date]
Description: Advanced file handling with error handling and multiple modification options
"""

import os

def file_handling_assignment():
    """
    Comprehensive file handling program with error handling and multiple modification options
    """
    print("📁 Advanced File Handling Program")
    print("=" * 50)
    
    while True:
        try:
            # Get filename from user
            filename = input("\nEnter filename to read (or 'quit' to exit): ").strip()
            
            if filename.lower() == 'quit':
                print("👋 Thank you for using the program!")
                break
            
            # Check if file exists
            if not os.path.exists(filename):
                print(f"❌ Error: File '{filename}' does not exist.")
                continue
                
            # Check if it's a directory
            if os.path.isdir(filename):
                print(f"❌ Error: '{filename}' is a directory, not a file.")
                continue
            
            # Read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print(f"✅ Successfully read '{filename}'")
            print(f"📄 Content length: {len(content)} characters")
            
            # Modification options
            print("\n🛠️ Choose modification type:")
            print("1. Convert to UPPERCASE")
            print("2. Convert to lowercase")
            print("3. Capitalize First Letters")
            print("4. Reverse Content")
            print("5. Double Content")
            
            choice = input("Enter your choice (1-5): ")
            
            # Apply modification
            if choice == '1':
                modified_content = content.upper()
                mod_type = "uppercase"
            elif choice == '2':
                modified_content = content.lower()
                mod_type = "lowercase"
            elif choice == '3':
                modified_content = content.title()
                mod_type = "title_case"
            elif choice == '4':
                modified_content = content[::-1]
                mod_type = "reversed"
            elif choice == '5':
                modified_content = content + "\n" + content
                mod_type = "doubled"
            else:
                print("⚠️ Invalid choice. Using UPPERCASE as default.")
                modified_content = content.upper()
                mod_type = "uppercase"
            
            # Create output filename
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_modified_{mod_type}{ext}"
            
            # Write to new file
            with open(new_filename, 'w', encoding='utf-8') as new_file:
                new_file.write(modified_content)
            
            print(f"✅ Success! Modified file saved as: {new_filename}")
            print(f"📄 Modified content length: {len(modified_content)} characters")
            
            # Preview
            print("\n👀 Preview of modified content:")
            print("=" * 40)
            preview = modified_content[:100] + "..." if len(modified_content) > 100 else modified_content
            print(preview)
            print("=" * 40)
            
            # Continue?
            continue_choice = input("\nProcess another file? (y/n): ")
            if continue_choice.lower() != 'y':
                print("👋 Thank you for using the program!")
                break
                
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' was not found.")
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{filename}'.")
        except IsADirectoryError:
            print(f"❌ Error: '{filename}' is a directory.")
        except UnicodeDecodeError:
            print(f"❌ Error: Cannot read '{filename}' - it may be a binary file.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_handling_assignment()
