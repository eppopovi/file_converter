"""
🎞️ HEVC → MP4 BATCH CONVERTER (No tqdm or shutil)

──────────────────────────────────────────────
📦 PREREQUISITES
──────────────────────────────────────────────
• FFmpeg must be installed and available in your system PATH.

To install easily:
    pip install ffmpeg-downloader
    ffdl install

──────────────────────────────────────────────
💡 USAGE
──────────────────────────────────────────────
python hevc_to_mp4_converter_simple.py

- Enter the folder containing your .hevc files.
- Converted MP4 files will be saved into a new folder: 'converted_to_mp4'
"""

import os
import subprocess

ffmpeg_directory_run = r"C:\Users\Heron\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin"  
os.chdir(ffmpeg_directory_run)

def convert_hevc_to_mp4(input_path, output_path):
    """Convert a single HEVC file to MP4 using ffmpeg."""
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx264",  # H.264 for MP4
        "-preset", "medium",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "128k",
        output_path,
        "-y"
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✅ Converted: {os.path.basename(input_path)} → {os.path.basename(output_path)}")
    except subprocess.CalledProcessError:
        print(f"❌ Error converting: {input_path}")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Install via 'pip install ffmpeg-downloader' and run 'ffdl install'.")


def batch_convert_hevc_to_mp4(input_folder):
    """Convert all .hevc files in a folder to MP4."""
    input_folder = input_folder.strip('"').strip("'")

    if not os.path.isdir(input_folder):
        print(f"❌ Not a valid directory: {input_folder}")
        return

    output_folder = os.path.join(input_folder, "converted_to_mp4")
    os.makedirs(output_folder, exist_ok=True)

    hevc_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".hevc")]
    if not hevc_files:
        print("⚠️ No HEVC files found in the directory.")
        return

    print(f"\n🎬 Starting conversion of {len(hevc_files)} HEVC file(s)...\n")

    for filename in hevc_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp4")
        convert_hevc_to_mp4(input_path, output_path)

    print(f"\n✅ All conversions complete! Files saved in: {output_folder}")


if __name__ == "__main__":
    print("🎞️ HEVC → MP4 Converter\n")
    folder = input("Enter the path to your folder containing HEVC files: ").strip()
    batch_convert_hevc_to_mp4(folder)
