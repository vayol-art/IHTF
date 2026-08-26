import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

js_toggle_function = """
<script>
  function toggleLangDropdown(e) {
    if (e) e.stopPropagation();
    const selector = document.querySelector(".lang-selector");
    const btn = document.querySelector(".lang-btn");
    if (selector) {
      const isOpen = selector.classList.toggle("open");
      if (btn) btn.setAttribute("aria-expanded", isOpen);
    }
  }
</script>
"""

count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    # Ensure lang-btn has onclick
    if '<button class="lang-btn"' in content and 'onclick="toggleLangDropdown(event)"' not in content:
        content = content.replace('<button class="lang-btn"', '<button class="lang-btn" onclick="toggleLangDropdown(event)"')
        modified = True
        
    if 'function toggleLangDropdown' not in content and '</head>' in content:
        content = content.replace('</head>', f'{js_toggle_function}\n</head>')
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"Updated language toggle in {filepath}")

print(f"Total HTML files updated with robust toggle: {count}")
