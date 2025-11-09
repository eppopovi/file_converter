"""
🖼️ PNG → JPG Batch Converter
─────────────────────────────
Converts all .PNG images in a directory to .JPG format.

🔧 REQUIREMENTS (run these first):
pip install pillow

─────────────────────────────
💡 USAGE:
python png_to_jpg.py
"""

import os
from PIL import Image

def convert_png_to_jpg(directory):
    """Convert all PNG files in a folder to JPG."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    png_files = [f for f in os.listdir(directory) if f.lower().endswith(".png")]
    if not png_files:
        print("No PNG files found.")
        return

    output_dir = os.path.join(directory, "converted_to_jpg")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(png_files)} PNG file(s). Converting...\n")

    for file in png_files:
        png_path = os.path.join(directory, file)
        jpg_name = os.path.splitext(file)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_name)

        try:
            with Image.open(png_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(jpg_path, "JPEG", quality=95)
            print(f"✅ Converted: {file} → {jpg_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! JPGs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing PNG files: ").strip()
    convert_png_to_jpg(directory)
