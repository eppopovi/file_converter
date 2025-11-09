"""
🖼️ JPG → PNG Batch Converter
─────────────────────────────
Converts all .JPG and .JPEG images in a directory to .PNG format.

🔧 REQUIREMENTS (run these first):
pip install pillow

─────────────────────────────
💡 USAGE:
python jpg_to_png.py
"""

import os
from PIL import Image

def convert_jpg_to_png(directory):
    """Convert all JPG/JPEG files in a folder to PNG."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    jpg_files = [f for f in os.listdir(directory) if f.lower().endswith((".jpg", ".jpeg"))]
    if not jpg_files:
        print("No JPG or JPEG files found.")
        return

    output_dir = os.path.join(directory, "converted_to_png")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(jpg_files)} JPG/JPEG file(s). Converting...\n")

    for file in jpg_files:
        jpg_path = os.path.join(directory, file)
        png_name = os.path.splitext(file)[0] + ".png"
        png_path = os.path.join(output_dir, png_name)

        try:
            with Image.open(jpg_path) as img:
                img.save(png_path, "PNG")
            print(f"✅ Converted: {file} → {png_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! PNGs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing JPG files: ").strip()
    convert_jpg_to_png(directory)
