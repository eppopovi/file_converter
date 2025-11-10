from merge_pdfs_script import merge_pdfs

from pdf_to_heic_script import convert_pdf_to_heic
from pdf_to_jpg_script import convert_pdf_to_jpg
from pdf_to_png_script import convert_pdf_to_png

from jpg_to_heic_script import convert_jpg_to_heic
from jpg_to_pdf_script import convert_jpg_to_pdf
from jpg_to_png_script import convert_jpg_to_png

from png_to_heic_script import convert_png_to_heic
from png_to_jpg_script import convert_png_to_jpg
from png_to_pdf_script import convert_png_to_pdf

from heic_to_jpg_script import convert_heic_to_jpg
from heic_to_pdf_script import convert_heic_to_pdf
from heic_to_png_script import convert_heic_to_png

from jpg_or_png_to_pdf_script import convert_jpg_or_png_to_pdf

from youtube_to_mp3_script import convert_youtube_to_mp3 

from sort_by_type_and_date_script import sort_files_by_type_and_date

from hevc_to_mov_script import convert_hevc_to_mov
from hevc_to_mp4_script import convert_hevc_to_mp4 

from mov_to_hevc import convert_mov_to_hevc
from mov_to_mp4 import convert_mov_to_mp4

from mp4_to_hevc_script import convert_mp4_to_hevc
from mp4_to_mov_script import convert_mp4_to_mov

if __name__ == "__main__":
    print("What would you like to do today? Please refer to documentation for details on what the tool offers.")
    
    print("'merge pdfs': Merge all PDFs in a folder to one PDF")

    print("'pdf to heic': Convert all PDFs in a folder to HEICs")
    print("'pdf to jpg': Convert all PDFs in a folder to JPGs")
    print("'pdf to png': Convert all PDFs in a folder to PNGs")
    
    print("'jpg to heic': Convert all JPGs in a folder to HEICs")
    print("'jpg to pdf': Convert all JPGs in a folder to PDFs")
    print("'jpg to png': Convert all JPGs in a folder to PNGs")
    
    print("'png to heic': Convert all PNGs in a folder to HEICs")
    print("'png to jpg': Convert all PNGs in a folder to JPGs")
    print("'png to pdf': Convert all PNGs in a folder to PDFs")

    print("'heic to jpg': Convert all HEICs in a folder to JPGs")
    print("'heic to pdf': Convert all HEICs in a folder to PDFs")
    print("'heic to png': Convert all HEICs in a folder to PNG")

    print("'jpg or png to pdf': Convert all PNGs or JPGs in a folder to PDFs")
    
    print("'youtube to mp3': Convert all youtube links provided to mp3s in a specified folder")

    print("'sort files': Sort files by type and date")
    
    print("'hevc to mov': Convert all HEVCs to MOVs")
    print("'hevc to mp4': Convert all HEVCs to MP4s")
        
    print("'mov to hevc': Convert all MOVs to HEVCs")
    print("'mov to mp4': Convert all MOVs to MP4s")

    print("'mp4 to hevc': Convert all MP4s to HEVCs")
    print("'mp4 to mov': Convert all MP4s to MOVs")
    
    choice = input("\nEnter your choice as outlined in the documentaton: ").strip()

    if choice == "merge pdfs":
        directory = input("Enter the directory path containing the PDFs: ").strip()
        merge_pdfs(directory)
# ----------------------------------------------------------------------------------
    elif choice == "pdf to heic":
        input_path = input("Enter the path to your PDF files: ").strip()
        convert_pdf_to_heic(input_path)

    elif choice == "pdf to jpg":
        input_path = input("Enter the path to your PDF files: ").strip()
        convert_pdf_to_jpg(input_path)

    elif choice == "pdf to png":
        input_path = input("Enter the path to your PDF files: ").strip()
        convert_pdf_to_png(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "jpg to heic":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_jpg_to_heic(input_path)

    elif choice == "jpg to pdf":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_jpg_to_pdf(input_path)

    elif choice == "jpg to png":
        input_path = input("Enter the path to your JPG files: ").strip()
        convert_jpg_to_png(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "png to heic":
        input_path = input("Enter the path to your PNG files: ").strip()
        convert_png_to_heic(input_path)

    elif choice == "png to jpg":
        input_path = input("Enter the path to your PNG files: ").strip()
        convert_png_to_jpg(input_path)

    elif choice == "png to pdf":
        input_path = input("Enter the path to your PNG files: ").strip()
        convert_png_to_pdf(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "heic to jpg":
        input_path = input("Enter the path to your HEIC files: ").strip()
        convert_heic_to_jpg(input_path)

    elif choice == "heic to pdf":
        input_path = input("Enter the path to your HEIC files: ").strip()
        convert_heic_to_pdf(input_path)

    elif choice == "heic to png":
        input_path = input("Enter the path to your HEIC files: ").strip()
        convert_heic_to_png(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "convert jpg or png to pdf" or choice == "convert png or jpg to pdf":
        input_path = input("Enter the path to your PNG and JPG files: ").strip()
        convert_heic_to_png(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "convert jpg or png to pdf and merge pdfs" or choice == "convert png or jpg to pdf and merge pdfs":
        while True:
            input_path = input("Enter the path to your image file (or 'done' to stop): ").strip()
            if input_path.lower() == "done":
                break
            convert_jpg_or_png_to_pdf(input_path)
        combine = input("Would you like to merge all PDFs in a folder now? (yes/no): ").strip().lower()
        if combine == "yes":
            directory = input("Enter the directory path containing the PDFs: ").strip()
            merge_pdfs(directory)
# ----------------------------------------------------------------------------------
    elif choice == "youtube to mp3":
        print("\n🎧 YouTube → MP3 Converter")
        output_folder = input("Output folder (if you leave this blank it will save to your ffpmeg bin directory): ").strip() or "."
        urls = []

        while True:
            link = input("Enter YouTube link (or 'done'): ").strip()
            if link.lower() == "done":
                break
            if link:
                urls.append(link)

        if not urls:
            print("No links entered. Returning to main menu...")
        else:
            print(f"\nStarting {len(urls)} download(s)...\n")
            convert_youtube_to_mp3(urls, output_folder)
# ----------------------------------------------------------------------------------
    elif choice == "sort files":
        input_path = input("Enter the path to your files to sort by type and date: ").strip()
        sort_files_by_type_and_date(input_path)
# ----------------------------------------------------------------------------------
    elif choice == "hevc to mov":
        input_path = input("Enter the path to your HEVC files: ").strip()
        convert_hevc_to_mov(input_path)

    elif choice == "hevc to mp4":
        input_path = input("Enter the path to your HEVC files: ").strip()
        convert_hevc_to_mp4(input_path)        
# ----------------------------------------------------------------------------------
    elif choice == "mov to hevc":
        input_path = input("Enter the path to your MOV files: ").strip()
        convert_mov_to_hevc(input_path)

    elif choice == "mov to mp4":
        input_path = input("Enter the path to your MOV files: ").strip()
        convert_mov_to_mp4(input_path)       
# ----------------------------------------------------------------------------------
    elif choice == "mp4 to hevc":
        input_path = input("Enter the path to your MP4 files: ").strip()
        convert_mp4_to_hevc(input_path)

    elif choice == "mp4 to mov":
        input_path = input("Enter the path to your MP4 files: ").strip()
        convert_mp4_to_mov(input_path)    
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
    else:
        print("Invalid entry. Please try again")
