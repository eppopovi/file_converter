"""
🎞️ MOV → HEVC (H.265) BATCH CONVERTER

──────────────────────────────────────────────
📦 PREREQUISITES
──────────────────────────────────────────────
• FFmpeg must be installed and available in your PATH.

Easiest setup:
    pip install ffmpeg-downloader
    ffdl install

──────────────────────────────────────────────
💡 USAGE
──────────────────────────────────────────────
python mov_to_hevc_converter.py

- Enter the folder containing your .mov files.
- Converted HEVC (H.265) videos will be saved into: 'converted_to_hevc'
"""

import os
import subprocess

ffmpeg_directory_run = r"C:\Users\Heron\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin"  
os.chdir(ffmpeg_directory_run)

def convert_mov_to_hevc(input_path, output_path):
    """Convert a MOV file to HEVC (H.265) using FFmpeg."""
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx265",  # Use HEVC codec
        "-preset", "medium",  # Encoding speed/efficiency tradeoff
        "-crf", "28",  # Quality (lower = better quality, 18–28 typical)
        "-c:a", "aac",  # Audio codec
        "-b:a", "128k",
        output_path,
        "-y"  # Overwrite output if exists
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✅ Converted: {os.path.basename(input_path)} → {os.path.basename(output_path)}")
    except subprocess.CalledProcessError:
        print(f"❌ Error converting: {input_path}")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install via 'pip install ffmpeg-downloader' and run 'ffdl install'.")


def batch_convert_mov_to_hevc(input_folder):
    """Convert all MOV files in a directory to HEVC format."""
    input_folder = input_folder.strip('"').strip("'")

    if not os.path.isdir(input_folder):
        print(f"❌ Invalid directory: {input_folder}")
        return

    output_folder = os.path.join(input_folder, "converted_to_hevc")
    os.makedirs(output_folder, exist_ok=True)

    mov_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".mov")]
    if not mov_files:
        print("⚠️ No MOV files found.")
        return

    print(f"\n🎬 Starting conversion of {len(mov_files)} MOV file(s)...\n")

    for filename in mov_files:
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + "_hevc.mp4")
        convert_mov_to_hevc(input_path, output_path)

    print(f"\n✅ All conversions complete! Files saved in: {output_folder}")


if __name__ == "__main__":
    print("🎞️ MOV → HEVC Converter\n")
    folder = input("Enter the path to your folder containing MOV files: ").strip()
    batch_convert_mov_to_hevc(folder)
