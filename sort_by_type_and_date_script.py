"""
🗂️ MULTI-FILE COPY SORTER BY DATE MODIFIED

──────────────────────────────────────────────
📦 PREREQUISITES
──────────────────────────────────────────────
pip install pillow pillow-heif

──────────────────────────────────────────────
💡 USAGE
──────────────────────────────────────────────
python multi_file_copy_sort_by_date.py

- Enter the folder containing your files.
- The script will scan for JPG, PNG, HEIC, and PDF files.
- Files are copied into type-specific folders under 'sorted_files_output',
  with subfolders for the date modified in format YYYY-MM-DD.
- Original files are preserved in their original location.
"""

import os
import shutil
from datetime import datetime

# Supported file types and their output folder names
FILE_TYPES = {
    ".jpg": "jpg_sorted",
    ".jpeg": "jpg_sorted",
    ".png": "png_sorted",
    ".heic": "heic_sorted",
    ".pdf": "pdf_sorted"
}

def sort_files_by_type_and_date(input_folder):
    """Copy JPG, PNG, HEIC, and PDF files by type and date modified into a dedicated output folder."""

    input_folder = input_folder.strip('"').strip("'")
    if not os.path.isdir(input_folder):
        raise NotADirectoryError(f"❌ Not a valid directory: {input_folder}")

    # Dedicated root output folder
    root_output = os.path.join(input_folder, "sorted_files_output")
    os.makedirs(root_output, exist_ok=True)

    # Scan for supported files
    files_found = [f for f in os.listdir(input_folder)
                   if os.path.isfile(os.path.join(input_folder, f)) and
                   os.path.splitext(f)[1].lower() in FILE_TYPES]

    if not files_found:
        print("⚠️ No supported files found in the directory.")
        return

    for file in files_found:
        file_path = os.path.join(input_folder, file)
        ext = os.path.splitext(file)[1].lower()
        type_folder = os.path.join(root_output, FILE_TYPES[ext])
        os.makedirs(type_folder, exist_ok=True)

        # Get modification date
        timestamp = os.path.getmtime(file_path)
        date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        # Create subfolder for the date
        date_folder = os.path.join(type_folder, date_str)
        os.makedirs(date_folder, exist_ok=True)

        # Copy file
        destination = os.path.join(date_folder, file)
        shutil.copy2(file_path, destination)  # copy2 preserves metadata
        print(f"📦 Copied: {file} → {FILE_TYPES[ext]}/{date_str}/")

    print(f"\n✅ All files copied successfully into '{root_output}'")

if __name__ == "__main__":
    print("🗂️ Multi-File Copy Sorter by Date Modified\n")
    input_folder = input("Enter the path to your folder containing files: ").strip()
    sort_files_by_type_and_date(input_folder)
