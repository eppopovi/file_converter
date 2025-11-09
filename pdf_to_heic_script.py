"""
📄 PDF → HEIC Batch Converter
─────────────────────────────
Converts every page of every PDF in a directory into HEIC images.

🔧 REQUIREMENTS:
pip install pdf2image pillow pillow-heif
"""

import os
from pdf2image import convert_from_path
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_pdf_to_heic(directory):
    """Convert all PDF pages in a folder to HEIC images."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found.")
        return

    output_dir = os.path.join(directory, "converted_to_heic")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(pdf_files)} PDF file(s). Converting...\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        base_name = os.path.splitext(pdf_file)[0]

        try:
            pages = convert_from_path(pdf_path)
            for i, page in enumerate(pages, start=1):
                heic_name = f"{base_name}_page_{i}.heic"
                heic_path = os.path.join(output_dir, heic_name)
                page = page.convert("RGB")
                page.save(heic_path, format="HEIC", quality=95)
                print(f"✅ {pdf_file} → {heic_name}")
        except Exception as e:
            print(f"⚠️ Error converting {pdf_file}: {e}")

    print(f"\n🎉 Conversion complete! HEIC files saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing PDF files: ").strip()
    convert_pdf_to_heic(directory)
