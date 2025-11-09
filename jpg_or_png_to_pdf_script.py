import os
from PIL import Image
import warnings

# Ignore AVIF warnings
warnings.filterwarnings("ignore", message="image file could not be identified because AVIF support not installed")


def convert_jpg_or_png_to_pdf(input_path, output_path=None):
    # --- Clean up path if pasted with quotes (Windows Copy as Path) ---
    if (input_path.startswith('"') and input_path.endswith('"')) or \
       (input_path.startswith("'") and input_path.endswith("'")):
        input_path = input_path[1:-1]

    # --- Validate input ---
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    ext = os.path.splitext(input_path)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png'):
        raise ValueError("Input file must be a .jpg, .jpeg, or .png image")

    # --- Default output path ---
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    # --- Convert image to PDF ---
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(output_path, "PDF", resolution=100.0)

    print(f"\n✅ PDF created successfully:\n{output_path}\n")
