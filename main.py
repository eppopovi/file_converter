from merge_pdfs_script import merge_pdfs
from jpg_to_pdf_script import convert_jpg_to_pdf
from png_to_pdf_script import convert_png_to_pdf
from jpg_or_png_to_pdf_script import image_to_pdf
from heic_to_jpg_script import convert_heic_to_jpg
from heic_to_png_script import convert_heic_to_png

if __name__ == "__main__":
    print("What would you like to do today? Please refer to documentation for details on what the tool offers.")
    print("'pdf merge': Merge all PDFs in a folder to one PDF")
    print("'pdf to jpg': Convert all PDFs in a folder to JPGs")
    print("'pdf to png': Convert all PDFs in a folder to PNGs")
    print("'jpg to pdf': Convert all JPGs in a folder to PDFs")
    print("'jpg to png': Convert all JPGs in a folder to PNGs")
    print("'jpg to heic': Convert all JPGs in a folder to HEICs")
    print("'png to pdf': Convert all PNG in a folder to PDFs")
    print("'png to jpg': Convert all PNG in a folder to JPGs")
    print("'png to heic': Convert all PNG in a folder to HEICs")
    print("'heic to jpg': Convert all HEIC in a folder to JPGs")
    print("'heic to png': Convert all HEIC in a folder to PNG")
    print("'heic to pdf': Convert all HEIC in a folder to PDFs")
    print("'datetime from jpg': Assign date and time to each JPG")
    print("'datetime from png': Assign date and time to each PNG")
    
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

    else:
        print("Invalid entry. Please try again")
