"""
🎞️ HEVC (H.265) → MOV BATCH CONVERTER

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
python hevc_to_mov_converter.py

- Enter the folder containing your HEVC video files (.mp4, .mkv, etc.).
- Converted MOV files will be saved into: 'converted_to_mov'
"""

import os
import subprocess

ffmpeg_directory_run = r"C:\Users\Heron\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin"  
os.chdir(ffmpeg_directory_run)

def convert_hevc_to_mov(input_path, output_path):
    """Convert an HEVC-encoded video to MOV using FFmpeg."""
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "prores_ks",   # Apple ProRes codec for MOV
        "-profile:v", "3",     # ProRes 422 (good balance of quality/size)
        "-c:a", "pcm_s16le",   # Uncompressed audio
        output_path,
        "-y"
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✅ Converted: {os.path.basename(input_path)} → {os.path.basename(output_path)}")
    except subprocess.CalledProcessError:
        print(f"❌ Error converting: {input_path}")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install via 'pip install ffmpeg-downloader' and run 'ffdl install'.")


def batch_convert_hevc_to_mov(input_folder):
    """Convert all HEVC (H.265) videos in a directory to MOV."""
    input_folder = input_folder.strip('"').strip("'")

    if not os.path.isdir(input_folder):
        print(f"❌ Invalid directory: {input_folder}")
        return

    output_folder = os.path.join(input_folder, "converted_to_mov")
    os.makedirs(output_folder, exist_ok=True)

    hevc_files = [
        f for f in os.listdir(input_folder)
        if f.lower().endswith((".mp4", ".mkv", ".hevc"))
    ]
    if not hevc_files:
        print("⚠️ No HEVC files found.")
        return

    print(f"\n🎬 Starting conversion of {len(hevc_files)} HEVC file(s)...\n")

    for filename in hevc_files:
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + ".mov")
        convert_hevc_to_mov(input_path, output_path)

    print(f"\n✅ All conversions complete! Files saved in: {output_folder}")


if __name__ == "__main__":
    print("🎞️ HEVC → MOV Converter\n")
    folder = input("Enter the path to your folder containing HEVC videos: ").strip()
    batch_convert_hevc_to_mov(folder)
