import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

def fix_css_files():
    css_files = ["style.css", "agenda.css", "obra.css"]
    css_rule = """
/* Background fix to prevent white space during carousel transitions */
.play-card-wrapper,
.play-card,
.image-carousel,
.carousel-track,
.carousel-track img {
  background-color: #141414 !important;
}
"""
    for rel_css in css_files:
        abs_css = os.path.join(BASE_DIR, rel_css)
        if os.path.exists(abs_css):
            with open(abs_css, "r", encoding="utf-8") as f:
                content = f.read()

            if ".play-card-wrapper," not in content or "background-color: #141414 !important;" not in content:
                content += "\n" + css_rule
                with open(abs_css, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated CSS background fix in {rel_css}")

def fix_html_files():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, BASE_DIR)

                with open(abs_path, "r", encoding="utf-8") as f:
                    content = f.read()

                modified = False

                # 1. Remove loading="lazy" from carousel-track img
                # Match carousel-track block and replace loading="lazy" inside it with loading="eager"
                def replace_lazy_in_track(match):
                    track_content = match.group(0)
                    return track_content.replace('loading="lazy"', 'loading="eager"')

                new_content = re.sub(r'<div class="carousel-track">.*?</div>', replace_lazy_in_track, content, flags=re.DOTALL)
                if new_content != content:
                    content = new_content
                    modified = True

                # 2. Add image preloader in carousel JS logic if carousel JS exists
                if 'document.querySelectorAll(".carousel-track")' in content or 'document.querySelectorAll(\'.carousel-track\')' in content:
                    preload_js = """
      // Eagerly preload all carousel track images to prevent blank white space
      document.querySelectorAll(".carousel-track img").forEach(img => {
        const src = img.getAttribute("src");
        if (src) {
          const p = new Image();
          p.src = src;
        }
      });
"""
                    if "Eagerly preload all carousel track images" not in content:
                        content = content.replace('const carousels = document.querySelectorAll(".carousel-track");', preload_js + '\n      const carousels = document.querySelectorAll(".carousel-track");')
                        modified = True

                if modified:
                    with open(abs_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated carousel loading fix in {rel_path}")

def main():
    fix_css_files()
    fix_html_files()
    print("Carousel white space fix complete!")

if __name__ == "__main__":
    main()
