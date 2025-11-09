import os

def rename_files_in_directory(directory_path, prefix="new_"):
    """
    Renames all files in a specified directory by adding a prefix.
    """
    try:
        for filename in os.listdir(directory_path):
            old_filepath = os.path.join(directory_path, filename)

            # Ensure it's a file, not a directory
            if os.path.isfile(old_filepath):
                new_filename = prefix + filename
                new_filepath = os.path.join(directory_path, new_filename)

                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'path/to/your/files' with the actual directory path
rename_files_in_directory(r"C:\Users\Heron\Desktop\TO CATEGORIZE AND ORGANIZE\Files w same name but different size", prefix="new_")