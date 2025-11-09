"""
📄 PDF → PNG Batch Converter
─────────────────────────────
Converts every page of every PDF in a directory into PNG images.

🔧 REQUIREMENTS:
pip install pdf2image pillow
"""

import os
from pdf2image import convert_from_path

def convert_pdf_to_png(directory):
    """Convert all PDF pages in a folder to PNG images."""
    if not os.path.isdir(directory):
        print(f"❌ Invalid directory: {directory}")
        return

    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found.")
        return

    output_dir = os.path.join(directory, "converted_to_png")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(pdf_files)} PDF file(s). Converting...\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        base_name = os.path.splitext(pdf_file)[0]

        try:
            pages = convert_from_path(pdf_path)
            for i, page in enumerate(pages, start=1):
                png_name = f"{base_name}_page_{i}.png"
                png_path = os.path.join(output_dir, png_name)
                page.convert("RGB").save(png_path, "PNG")
                print(f"✅ {pdf_file} → {png_name}")
        except Exception as e:
            print(f"⚠️ Error converting {pdf_file}: {e}")

    print(f"\n🎉 Conversion complete! PNG files saved in: {output_dir}")

if __name__ == "__main__":
    directory = input("Enter the directory path containing PDF files: ").strip()
    convert_pdf_to_png(directory)
