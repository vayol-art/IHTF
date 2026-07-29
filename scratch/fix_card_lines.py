import os

BASE_DIR = "/Users/vanessa/Documents/IHTF"

CSS_RULE = """
/* Explicit white lines for program cards (outer border, date dividers, and top border) */
.play-card-wrapper {
  border: 1px solid #ffffff !important;
}

.dates {
  background: #ffffff !important;
  border-top: 1px solid #ffffff !important;
}
"""

def main():
    css_files = ["style.css", "agenda.css", "obra.css"]
    for rel_css in css_files:
        abs_css = os.path.join(BASE_DIR, rel_css)
        if os.path.exists(abs_css):
            with open(abs_css, "r", encoding="utf-8") as f:
                content = f.read()

            if "border: 1px solid #ffffff !important;" not in content:
                content += "\n" + CSS_RULE
                with open(abs_css, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated card white lines in {rel_css}")

if __name__ == "__main__":
    main()
