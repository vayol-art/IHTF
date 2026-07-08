from PIL import Image
import os

img_path = r'c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\assets\afiche_1.jpg'
output_path = r'c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\assets\afiche_1_horizontal.jpg'

if os.path.exists(img_path):
    print("Image found!")
    with Image.open(img_path) as img:
        w, h = img.size
        print(f"Original size: {w}x{h}")
        
        # We want a 16:9 horizontal crop from the center
        # Since it is vertical (w < h), the maximum width we can use is w.
        # Target height is w * 9 / 16.
        target_h = int(w * 9 / 16)
        
        # Crop from the center of the height
        top = (h - target_h) // 2
        bottom = top + target_h
        left = 0
        right = w
        
        print(f"Cropping box: left={left}, top={top}, right={right}, bottom={bottom}")
        cropped = img.crop((left, top, right, bottom))
        
        # Resize to a reasonable web size (e.g. 1920x1080) to save space and load faster
        if w > 1920:
            cropped = cropped.resize((1920, 1080), Image.Resampling.LANCZOS)
            print("Resized to 1920x1080")
            
        cropped.save(output_path, 'JPEG', quality=85)
        print(f"Saved to {output_path}")
else:
    print("Image not found!")
