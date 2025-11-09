"""
🎞️ MP4 → HEVC BATCH CONVERTER (No tqdm or shutil)

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
python mp4_to_hevc_converter_simple.py

- Enter the folder containing your .mp4 files.
- Converted HEVC files will be saved into a new folder: 'converted_to_hevc'
"""

import os
import subprocess

ffmpeg_directory_run = r"C:\Users\Heron\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin"  
os.chdir(ffmpeg_directory_run)

def convert_mp4_to_hevc(input_path, output_path):
    """Convert a single MP4 file to HEVC (H.265) format."""
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx265",  # H.265 for HEVC
        "-preset", "medium",
        "-crf", "28",       # Higher = smaller file, lower = higher quality
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


def batch_convert_mp4_to_hevc(input_folder):
    """Convert all .mp4 files in a folder to HEVC format."""
    input_folder = input_folder.strip('"').strip("'")

    if not os.path.isdir(input_folder):
        print(f"❌ Not a valid directory: {input_folder}")
        return

    output_folder = os.path.join(input_folder, "converted_to_hevc")
    os.makedirs(output_folder, exist_ok=True)

    mp4_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".mp4")]
    if not mp4_files:
        print("⚠️ No MP4 files found in the directory.")
        return

    print(f"\n🎬 Starting conversion of {len(mp4_files)} MP4 file(s)...\n")

    for filename in mp4_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".hevc")
        convert_mp4_to_hevc(input_path, output_path)

    print(f"\n✅ All conversions complete! Files saved in: {output_folder}")


if __name__ == "__main__":
    print("🎞️ MP4 → HEVC Converter\n")
    folder = input("Enter the path to your folder containing MP4 files: ").strip()
    batch_convert_mp4_to_hevc(folder)
