import os
import glob

base_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

target_str = 'const carousels = document.querySelectorAll(".carousel-track");'

replacement_str = """// Detect image orientation and add appropriate class
      document.querySelectorAll(".carousel-track img").forEach(img => {
        const checkOrientation = () => {
          if (img.naturalHeight > img.naturalWidth) {
            img.classList.add("is-portrait");
            img.classList.remove("is-landscape");
          } else {
            img.classList.add("is-landscape");
            img.classList.remove("is-portrait");
          }
        };
        if (img.complete) {
          checkOrientation();
        } else {
          img.addEventListener("load", checkOrientation);
        }
      });

      const carousels = document.querySelectorAll(".carousel-track");"""

print(f"Searching in {len(html_files)} HTML files...")

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if target_str in content:
        print(f"Modifying {os.path.basename(file_path)}...")
        new_content = content.replace(target_str, replacement_str)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"Skipping {os.path.basename(file_path)} (target string not found)")

print("Done!")
