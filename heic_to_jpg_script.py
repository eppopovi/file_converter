"""
📸 HEIC → JPG Batch Converter
─────────────────────────────
Converts all .HEIC images in a directory to .JPG format.

🔧 REQUIREMENTS (run these first):

pip install pillow pillow-heif

─────────────────────────────
💡 USAGE:
python heic_to_jpg.py
"""

import os
from pillow_heif import register_heif_opener
from PIL import Image

# Register HEIF/HEIC support for Pillow
register_heif_opener()

def heic_to_jpg(directory):
    """Convert all HEIC files in a folder to JPG."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    heic_files = [f for f in os.listdir(directory) if f.lower().endswith(".heic")]
    if not heic_files:
        print("No HEIC files found.")
        return

    output_dir = os.path.join(directory, "converted_jpg")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(heic_files)} HEIC file(s). Converting...\n")

    for file in heic_files:
        heic_path = os.path.join(directory, file)
        jpg_name = os.path.splitext(file)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_name)

        try:
            with Image.open(heic_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(jpg_path, "JPEG", quality=95)
            print(f"✅ Converted: {file} → {jpg_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! JPGs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing HEIC files: ").strip()
    heic_to_jpg(directory)
