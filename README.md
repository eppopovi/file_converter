# File_Converter
Aimed to convert any file to any other file. 
I don't like how I need to go online to convert files from one format to another. 
No one ever knows if those websites are keeping or using your sensitive files. 

# Current File Conversions Supported
1. Merge pdf
2. pdf to heic
3. pdf to jpg
4. pdf to png
5. png to heic
6. png to jpg
7. png to pdf
8. png to heic
9. png to jpg
10. png to pdf
11. heic to png
12. heic to pdf
13. heic to png
14. jpg or png to pdf
15. youtube to mp3

**All names above should be straight forward. These are all case sensitive inputs into the main.py script**


# FULL SETUP (DEPENDENCIES)


| Package               | Purpose                                               |
| --------------------- | ----------------------------------------------------- |
| **pillow**            | Core image manipulation (JPG, PNG, PDF export)        |
| **pillow-heif**       | Adds HEIC/HEIF image format support                   |
| **pdf2image**         | Converts PDF pages to images                          |
| **PyPDF2**            | Merges, splits, or manipulates PDFs                   |
| **yt-dlp**            | Downloads YouTube videos and audio                    |
| **ffmpeg-downloader** | Automatically installs and manages `ffmpeg`           |
| **moviepy**           | Used for video/audio conversions (MP4 → MP3, etc.)    |
| **poppler**           | Backend for reading PDF pages (required by pdf2image) |

# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # (Windows)
or
source venv/bin/activate     # (macOS/Linux)

# 2. Install all dependencies
pip install -U pillow pillow-heif pdf2image PyPDF2 yt-dlp ffmpeg-downloader moviepy

# 3. Install ffmpeg (for YouTube → MP3 and video/audio conversions)
ffdl install
Verify ffmpeg installed correctly
ffmpeg -version

# 4. (Windows only) Install Poppler for PDF → image conversions
Download from: https://github.com/oschwartz10612/poppler-windows/releases
Extract the ZIP (e.g., to C:\Program Files\poppler)
Add "C:\Program Files\poppler\bin" to your PATH
OR on macOS:
brew install poppler
OR on Linux:
sudo apt install poppler-utils

# 5. Verify Python packages
python -m PIL
python -c "from pillow_heif import register_heif_opener; register_heif_opener(); print('HEIC support OK')"
python -c "import yt_dlp; print('yt-dlp OK')"
python -c "import pdf2image; print('pdf2image OK')"
python -c "import moviepy; print('moviepy OK')"

# 6. (Optional) Freeze all dependencies into a requirements file
pip freeze > requirements.txt
