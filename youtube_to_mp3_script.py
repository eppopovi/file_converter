
# cd C:\Users\Heron\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin
# Video for mp4 to mp3 conversion using glob and moviepy https://www.youtube.com/watch?v=FJWf1Qjp9WA

import os
import subprocess
import shutil

def ensure_ffmpeg_available():
    """Return path to ffmpeg binary installed by ffmpeg-downloader."""
    # Default installation folder used by ffmpeg-downloader
    home = os.path.expanduser("~")
    ffdl_dir = os.path.join(home, ".local", "ffmpeg-downloader", "bin")
    if not os.path.exists(ffdl_dir):
        # On Windows the folder is under AppData
        ffdl_dir = os.path.join(home, "AppData", "Local", "ffmpeg-downloader", "bin")
    ffmpeg_path = shutil.which("ffmpeg") or os.path.join(ffdl_dir, "ffmpeg.exe" if os.name == "nt" else "ffmpeg")
    if not os.path.exists(ffmpeg_path):
        raise FileNotFoundError(
            "ffmpeg not found. Run 'ffdl install' once, or install ffmpeg manually."
        )
    return ffmpeg_path

def download_youtube_as_mp3(urls, output_folder="."):
    """Download YouTube videos as MP3 using yt-dlp + ffmpeg."""
    os.makedirs(output_folder, exist_ok=True)
    ffmpeg_path = ensure_ffmpeg_available()

    for url in urls:
        print(f"\n🎬 Downloading: {url}")
        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "--audio-quality", "192K",
            "--ffmpeg-location", ffmpeg_path,
            "-o", os.path.join(output_folder, "%(title)s.%(ext)s"),
            url
        ]
        try:
            subprocess.run(cmd, check=True)
            print("✅ Done.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error downloading {url}: {e}")

if __name__ == "__main__":
    print("🎧 YouTube → MP3 Converter (yt-dlp + ffmpeg-downloader)\n")
    output_folder = input("Output folder (blank = current): ").strip() or "."

    urls = []
    while True:
        link = input("YouTube link (or 'done'): ").strip()
        if link.lower() == "done":
            break
        if link:
            urls.append(link)

    if not urls:
        print("No links entered.")
    else:
        print(f"\nStarting {len(urls)} download(s)...\n")
        download_youtube_as_mp3(urls, output_folder)
        print("\n✅ All downloads complete!")
