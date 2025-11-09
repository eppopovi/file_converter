import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    pdf_files = [f for f in os.listdir(directory_path) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    pdf_files.sort()
    merger = PdfMerger()

    print("Merging the following PDF files:")
    for pdf in pdf_files:
        pdf_path = os.path.join(directory_path, pdf)
        print(f"  - {pdf}")
        merger.append(pdf_path)

    output_path = os.path.join(directory_path, "merged_output.pdf")
    merger.write(output_path)
    merger.close()
    print(f"\n✅ PDFs merged successfully into: {output_path}")
