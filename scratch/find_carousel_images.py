import re
import os

html_path = r'c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\index.html'

if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to find all image elements inside carousel-track
    # Let's search for <div class="carousel-track"> ... </div> and extract all <img> inside them
    tracks = re.findall(r'<div class="carousel-track">(.*?)</div>', html, re.DOTALL)
    print(f"Found {len(tracks)} carousel tracks:")
    for idx, track in enumerate(tracks):
        # find play name in parent card if possible
        # let's extract all <img> tags inside this track
        imgs = re.findall(r'<img\s+src="([^"]+)"', track)
        print(f"Carousel {idx + 1}:")
        for img in imgs:
            print(f"  - {img}")
else:
    print("index.html not found!")
