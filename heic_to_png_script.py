"""
📸 HEIC → PNG Batch Converter
─────────────────────────────
Converts all .HEIC images in a directory to .PNG format.

🔧 REQUIREMENTS (run these first):

pip install pillow pillow-heif

─────────────────────────────
💡 USAGE:
python heic_to_png_script.py
"""

import os
from pillow_heif import register_heif_opener
from PIL import Image

# Register HEIF/HEIC support for Pillow
register_heif_opener()

def convert_heic_to_png(directory):
    """Convert all HEIC files in a folder to PNG."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    heic_files = [f for f in os.listdir(directory) if f.lower().endswith(".heic")]
    if not heic_files:
        print("No HEIC files found.")
        return

    output_dir = os.path.join(directory, "converted_png")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(heic_files)} HEIC file(s). Converting...\n")

    for file in heic_files:
        heic_path = os.path.join(directory, file)
        png_name = os.path.splitext(file)[0] + ".png"
        png_path = os.path.join(output_dir, png_name)

        try:
            with Image.open(heic_path) as img:
                img.save(png_path, "PNG")
            print(f"✅ Converted: {file} → {png_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! PNGs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing HEIC files: ").strip()
    convert_heic_to_png(directory)
