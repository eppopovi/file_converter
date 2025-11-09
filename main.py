from merge_pdfs_in_directory_script import merge_pdfs_in_directory
from jpg_or_png_to_pdf_script import image_to_pdf

if __name__ == "__main__":
    print("What would you like to do today?")
    print("1️ Merge all PDFs in a folder directory")
    print("2 Convert an image (JPG/PNG) to PDF")
    print("3️ Both (convert images first (JPG/PNG), then merge PDFs in the folder)")
    print("4 Convert an image (HEIC) to JPG")
    
    choice = input("\nEnter your choice (1/2/3...): ").strip()

    if choice == "1":
        directory = input("Enter the directory path containing the PDFs: ").strip()
        merge_pdfs_in_directory(directory)

    elif choice == "2":
        input_path = input("Enter the path to your image file: ").strip()
        image_to_pdf(input_path)

    elif choice == "3":
        while True:
            input_path = input("Enter the path to your image file (or 'done' to stop): ").strip()
            if input_path.lower() == "done":
                break
            image_to_pdf(input_path)
        combine = input("Would you like to merge all PDFs in a folder now? (yes/no): ").strip().lower()
        if combine == "yes":
            directory = input("Enter the directory path containing the PDFs: ").strip()
            merge_pdfs_in_directory(directory)
