"""
🖼️ PNG → HEIC Batch Converter
─────────────────────────────
Converts all .PNG images in a directory to .HEIC format.

🔧 REQUIREMENTS (run these first):
pip install pillow pillow-heif

─────────────────────────────
💡 USAGE:
python png_to_heic.py
"""

import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF/HEIC support for Pillow
register_heif_opener()

def convert_png_to_heic(directory):
    """Convert all PNG files in a folder to HEIC."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    png_files = [f for f in os.listdir(directory) if f.lower().endswith(".png")]
    if not png_files:
        print("No PNG files found.")
        return

    output_dir = os.path.join(directory, "converted_to_heic")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(png_files)} PNG file(s). Converting...\n")

    for file in png_files:
        png_path = os.path.join(directory, file)
        heic_name = os.path.splitext(file)[0] + ".heic"
        heic_path = os.path.join(output_dir, heic_name)

        try:
            with Image.open(png_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(heic_path, "HEIC", quality=90)
            print(f"✅ Converted: {file} → {heic_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! HEICs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing PNG files: ").strip()
    convert_png_to_heic(directory)
