# File_Converter
Aimed to convert any file to any other file. 
I don't like how I need to go online to convert files from one format to another. 
No one ever knows if those websites are keeping or using your sensitive files. 

File conversions include
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
Dependencies so that code could run smooth:

🧩 Environment Setup — All Converter Scripts
✅ 1️⃣ Create & Activate a Virtual Environment
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

✅ 2️⃣ Install All Required Dependencies
pip install -U pillow pillow-heif pdf2image PyPDF2 yt-dlp ffmpeg-downloader moviepy

✅ 3️⃣ Install ffmpeg (for audio/video conversions)
# Download and register ffmpeg automatically
ffdl install
💡 This only needs to be done once.
ffmpeg will be stored in:
Windows: C:\Users\<USERNAME>\AppData\Local\ffmpeg-downloader\bin
Mac/Linux: ~/.local/ffmpeg-downloader/bin
Verify installation:
ffmpeg -version

✅ 4️⃣ Install Poppler (for PDF → Image conversions)
🪟 Windows

Download from: https://github.com/oschwartz10612/poppler-windows/releases

Extract the ZIP (e.g., to C:\Program Files\poppler)

Add the bin folder to your system PATH (e.g. C:\Program Files\poppler\bin)
🍎 macOS
brew install poppler
🐧 Linux
sudo apt install poppler-utils

✅ 5️⃣ Verify Everything Is Installed
python -m PIL
python -c "from pillow_heif import register_heif_opener; register_heif_opener(); print('✅ HEIC support OK')"
python -c "import yt_dlp; print('✅ yt-dlp OK')"
python -c "import pdf2image; print('✅ pdf2image OK')"
python -c "import moviepy; print('✅ moviepy OK')"
ffmpeg -version

✅ 6️⃣ Optional: Generate a requirements.txt
pip freeze > requirements.txt


Then others can simply do:

pip install -r requirements.txt

🧰 Summary of Dependencies
Package	Purpose
pillow	Core image manipulation (JPG, PNG, PDF export)
pillow-heif	Adds HEIC/HEIF image format support
pdf2image	Converts PDF pages to images
PyPDF2	Merges, splits, or manipulates PDFs
yt-dlp	Downloads YouTube videos and audio
ffmpeg-downloader	Automatically installs and manages ffmpeg
moviepy	Used for video/audio conversions (MP4 → MP3, etc.)
poppler	Backend for reading PDF pages (required by pdf2image)

✅ After completing these steps, every script in your repository will work out of the box.
