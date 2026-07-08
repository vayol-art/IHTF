import re
import os
from PIL import Image

html_path = r'c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\index.html'
base_dir = r'c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF'

if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    tracks = re.findall(r'<div class="carousel-track">(.*?)</div>', html, re.DOTALL)
    print("Carousel Images Analysis:")
    
    # We will map index to the play names in index.html to make it readable
    # Let's search for the titles (<h3>...</h3>) preceding each carousel
    plays = re.findall(r'<h3>(.*?)</h3>', html)
    
    for idx, track in enumerate(tracks):
        play_title = plays[idx] if idx < len(plays) else f"Play {idx + 1}"
        imgs = re.findall(r'<img\s+src="([^"]+)"', track)
        print(f"\nObra: {play_title} (Carousel {idx + 1})")
        for img_rel in imgs:
            img_abs = os.path.join(base_dir, img_rel.replace('%20', ' '))
            if os.path.exists(img_abs):
                try:
                    with Image.open(img_abs) as img:
                        w, h = img.size
                        ratio = w / h
                        is_vertical = h > w
                        status = "VERTICAL (Alta probabilidad de corte de cabezas)" if is_vertical else "Horizontal"
                        print(f"  - {os.path.basename(img_rel)}: {w}x{h} (Ratio: {ratio:.2f}) -> {status}")
                except Exception as e:
                    print(f"  - {os.path.basename(img_rel)}: Error loading image: {e}")
            else:
                print(f"  - {os.path.basename(img_rel)}: FILE NOT FOUND at {img_abs}")
else:
    print("index.html not found!")
