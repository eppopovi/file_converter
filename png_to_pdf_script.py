"""
🖼️ PNG → PDF Batch Converter
─────────────────────────────
Converts all .PNG images in a directory to .PDF format.

🔧 REQUIREMENTS (run these first):
pip install pillow

─────────────────────────────
💡 USAGE:
python png_to_pdf_script.py
"""

import os
from PIL import Image
import warnings

# Ignore AVIF-related warnings
warnings.filterwarnings("ignore", message="image file could not be identified because AVIF support not installed")

def convert_png_to_pdf(directory):
    """Convert all PNG files in a folder to PDF."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    png_files = [f for f in os.listdir(directory) if f.lower().endswith(".png")]
    if not png_files:
        print("No PNG files found.")
        return

    output_dir = os.path.join(directory, "converted_to_pdf")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(png_files)} PNG file(s). Converting...\n")

    for file in png_files:
        png_path = os.path.join(directory, file)
        pdf_name = os.path.splitext(file)[0] + ".pdf"
        pdf_path = os.path.join(output_dir, pdf_name)

        try:
            with Image.open(png_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(pdf_path, "PDF", resolution=100.0)
            print(f"✅ Converted: {file} → {pdf_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! PDFs saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing PNG files: ").strip()
    convert_png_to_pdf(directory)
