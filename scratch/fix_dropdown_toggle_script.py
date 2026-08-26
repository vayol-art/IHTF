import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

robust_js = """<script>
  function toggleLangDropdown(e) {
    if (e && typeof e.stopPropagation === 'function') {
      e.stopPropagation();
    }
    const btn = (e && e.currentTarget) ? e.currentTarget : document.querySelector(".lang-btn");
    const selector = btn ? btn.closest(".lang-selector") : document.querySelector(".lang-selector");
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
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace function toggleLangDropdown block with robust_js
    content = re.sub(r'<script>\s*function toggleLangDropdown[\s\S]*?</script>', robust_js, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"Updated script in {filepath}")

print(f"Updated {count} HTML files with robust toggleLangDropdown.")
