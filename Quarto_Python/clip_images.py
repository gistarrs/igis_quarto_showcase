from PIL import Image, ImageOps, ImageDraw
import os

input_folder = "image_assets/staff_raw"
output_folder = "image_assets/staff_circles"
os.makedirs(output_folder, exist_ok=True)

final_size = 512  # pixels

def crop_to_circle(in_path, out_path):
    img = Image.open(in_path).convert("RGBA")

    # Make image square
    img_square = ImageOps.fit(img, (final_size, final_size), method=Image.LANCZOS)

    # Create circular mask
    mask = Image.new("L", (final_size, final_size))
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, final_size, final_size), fill=255)

    # Apply mask
    img_circle = img_square.copy()
    img_circle.putalpha(mask)

    img_circle.save(out_path, format="PNG")
    print(f"Saved: {out_path}")

for f in os.listdir(input_folder):
    if f.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, f)
        output_path = os.path.join(output_folder, f.rsplit(".", 1)[0] + "_circle.png")
        crop_to_circle(input_path, output_path)
