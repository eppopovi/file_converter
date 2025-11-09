from merge_pdfs_script import merge_pdfs

# from pdf_to_heic_script import convert_pdf_to_heic
# from pdf_to_jpg_script import convert_pdf_to_jpg
# from pdf_to_png_script import convert pdf_to_png

# from jpg_to_heic_script import convert_jpg_to_heic
from jpg_to_pdf_script import convert_jpg_to_pdf
# from jpg_to_png_script import convert_jpg_to_png

# from png_to_heic_script import convert_png_to_heic
# from png_to_jpg_script import convert_png_to_jpg
from png_to_pdf_script import convert_png_to_pdf


from jpg_or_png_to_pdf_script import convert_jpg_or_png_to_pdf

from heic_to_jpg_script import convert_heic_to_jpg
# from heic_to_pdf_script import convert_heic_to_pdf
from heic_to_png_script import convert_heic_to_png

if __name__ == "__main__":
    print("What would you like to do today? Please refer to documentation for details on what the tool offers.")
    
    # print("'merge pdfs': Merge all PDFs in a folder to one PDF")

    # print("'pdf to heic': Convert all PDFs in a folder to HEICs")
    # print("'pdf to jpg': Convert all PDFs in a folder to JPGs")
    # print("'pdf to png': Convert all PDFs in a folder to PNGs")
    
    # print("'jpg to heic': Convert all JPGs in a folder to HEICs")
    # print("'jpg to pdf': Convert all JPGs in a folder to PDFs")
    # print("'jpg to png': Convert all JPGs in a folder to PNGs")
    
    # print("'png to heic': Convert all PNG in a folder to HEICs")
    # print("'png to jpg': Convert all PNG in a folder to JPGs")
    # print("'png to pdf': Convert all PNG in a folder to PDFs")
    
    # print("'jpg or png to pdf': Convert all PNGs or JPGs in a folder to PDFs")

    # print("'heic to jpg': Convert all HEIC in a folder to JPGs")
    # print("'heic to pdf': Convert all HEIC in a folder to PDFs")
    # print("'heic to png': Convert all HEIC in a folder to PNG")


    # print("'datetime from jpg': Assign date and time to each JPG")
    # print("'datetime from png': Assign date and time to each PNG")
    
    
    choice = input("\nEnter your choice as outlined in the documentaton: ").strip()

    if choice == "merge pdfs":
        directory = input("Enter the directory path containing the PDFs: ").strip()
        merge_pdfs(directory)

    # elif choice == "pdf to heic":
    #     input_path = input("Enter the path to your PDF files: ").strip()
    #     convert_png_to_heic(input_path)

    # elif choice == "pdf to jpg":
    #     input_path = input("Enter the path to your PDF files: ").strip()
    #     convert_pdf_to_jpg(input_path)

    # elif choice == "pdf to png":
    #     input_path = input("Enter the path to your PDF files: ").strip()
    #     convert_pdf_to_png(input_path)
    
    # elif choice == "jpg to heic":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_jpg_to_heic(input_path)

    elif choice == "jpg to pdf":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_jpg_to_pdf(input_path)

    # elif choice == "jpg to png":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_jpg_to_png(input_path)

    # elif choice == "png to heic":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_png_to_heic(input_path)

    # elif choice == "png to jpg":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_png_to_jpg(input_path)

    elif choice == "png to pdf":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_png_to_pdf(input_path)

    # elif choice == "png to heic":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_png_to_heic(input_path)

    elif choice == "jpg or png to pdf":
        input_path = input("Enter the path to your PNG and JPG files: ").strip()
        convert_jpg_or_png_to_pdf(input_path)

    elif choice == "heic to jpg":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_heic_to_jpg(input_path)

    # elif choice == "heic to pdf":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     convert_heic_to_pdf(input_path)

    elif choice == "heic to png":
        input_path = input("Enter the path to your PNG and JPG files: ").strip()
        convert_heic_to_png(input_path)

    # elif choice == "datetime from jpg":
    #     input_path = input("Enter the path to your JPG files: ").strip()
    #     datetime(input_path)

    # elif choice == "datetime from png":
    #     input_path = input("Enter the path to your PNG and JPG files: ").strip()
    #     datetime(input_path)

    elif choice == "merge jpg or png and merge pdfs":
        while True:
            input_path = input("Enter the path to your image file (or 'done' to stop): ").strip()
            if input_path.lower() == "done":
                break
            convert_jpg_or_png_to_pdf(input_path)
        combine = input("Would you like to merge all PDFs in a folder now? (yes/no): ").strip().lower()
        if combine == "yes":
            directory = input("Enter the directory path containing the PDFs: ").strip()
            merge_pdfs(directory)

    else:
        print("Invalid entry. Please try again")
