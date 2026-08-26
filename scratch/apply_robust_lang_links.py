import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

switch_lang_js = """<script>
  function toggleLangDropdown(e) {
    if (e) {
      e.stopPropagation();
    }
    const selector = document.querySelector(".lang-selector");
    const btn = document.querySelector(".lang-btn");
    if (selector) {
      const isOpen = selector.classList.toggle("open");
      if (btn) btn.setAttribute("aria-expanded", isOpen);
    }
  }

  function switchLang(lang, targetUrl) {
    localStorage.setItem("preferred_lang", lang);
    if (targetUrl && targetUrl !== "#") {
      let finalUrl = targetUrl;
      if (window.location.search && targetUrl.includes("/obra/")) {
        finalUrl += window.location.search;
      }
      window.location.href = finalUrl;
    }
  }

  document.addEventListener("click", function (event) {
    const selector = document.querySelector(".lang-selector");
    const btn = document.querySelector(".lang-btn");
    if (selector && !selector.contains(event.target)) {
      selector.classList.remove("open");
      if (btn) btn.setAttribute("aria-expanded", "false");
    }
  });
</script>"""

count = 0
for filepath in html_files:
    # Normalize path separators
    norm_path = filepath.replace("\\", "/")
    parts = norm_path.split("/")
    
    current_lang = parts[0] # 'es' or 'en'
    other_lang = 'en' if current_lang == 'es' else 'es'
    
    # Reconstruct equivalent path in other language
    other_parts = [other_lang] + parts[1:]
    other_filepath = "/".join(other_parts)
    
    # Calculate relative path from norm_path directory to other_filepath directory
    dir_parts = parts[:-1] # directory of current file
    other_dir_parts = other_parts[:-1] # directory of target file
    
    # Steps to go up from dir_parts to root
    depth = len(dir_parts)
    up_steps = "../" * depth
    target_rel_dir = up_steps + "/".join(other_dir_parts) + "/"
    target_rel_dir = re.sub(r'/+', '/', target_rel_dir) # clean up slashes
    if not target_rel_dir.startswith("../"):
        target_rel_dir = "./" + target_rel_dir
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Build new dropdown HTML
    if current_lang == 'es':
        es_html = f'<a href="#" class="lang-opt active" onclick="switchLang(\'es\'); return false;">Español</a>'
        en_html = f'<a href="{target_rel_dir}" class="lang-opt" onclick="switchLang(\'en\', \'{target_rel_dir}\')">English</a>'
    else:
        en_html = f'<a href="#" class="lang-opt active" onclick="switchLang(\'en\'); return false;">English</a>'
        es_html = f'<a href="{target_rel_dir}" class="lang-opt" onclick="switchLang(\'es\', \'{target_rel_dir}\')">Español</a>'
        
    new_dropdown = f'<div class="lang-dropdown">\n          {en_html}\n          {es_html}\n        </div>' if current_lang == 'en' else f'<div class="lang-dropdown">\n          {es_html}\n          {en_html}\n        </div>'
    
    # Replace existing lang-dropdown in content
    content = re.sub(r'<div class="lang-dropdown">[\s\S]*?</div>', new_dropdown, content)
    
    # Ensure switch_lang_js is in head
    if 'function switchLang' not in content:
        content = re.sub(r'function toggleLangDropdown[\s\S]*?</script>', '', content) # remove old toggle function if exists
        content = content.replace('</head>', f'{switch_lang_js}\n</head>')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"Updated {filepath} -> target {other_lang}: {target_rel_dir}")

print(f"Total files updated with native <a> dropdown links: {count}")
