"""
🖼️ JPG → PDF Batch Converter
─────────────────────────────
Converts all .JPG and .JPEG images in a directory to .PDF format.

🔧 REQUIREMENTS (run these first):
pip install pillow

─────────────────────────────
💡 USAGE:
python jpg_to_pdf_script.py
"""

import os
from PIL import Image
import warnings

# Ignore AVIF-related warnings
warnings.filterwarnings("ignore", message="image file could not be identified because AVIF support not installed")

def convert_jpg_to_pdf(directory):
    """Convert all JPG/JPEG files in a folder to PDF."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    jpg_files = [f for f in os.listdir(directory) if f.lower().endswith((".jpg", ".jpeg"))]
    if not jpg_files:
        print("No JPG or JPEG files found.")
        return

    output_dir = os.path.join(directory, "converted_to_pdf")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(jpg_files)} JPG/JPEG file(s). Converting...\n")

    for file in jpg_files:
        jpg_path = os.path.join(directory, file)
        pdf_name = os.path.splitext(file)[0] + ".pdf"
        pdf_path = os.path.join(output_dir, pdf_name)

        try:
            with Image.open(jpg_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(pdf_path, "PDF", resolution=100.0)
            print(f"✅ Converted: {file} → {pdf_name}")
        except Exception as e:
            print(f"⚠️ Error converting {file}: {e}")

    print(f"\n🎉 Conversion complete! PDFs saved in: {output_dir}")
    
