import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

clean_js_block = """<script>
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
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove all previous occurrences of toggleLangDropdown / switchLang script blocks
    content = re.sub(r'<script>\s*function toggleLangDropdown[\s\S]*?</script>', '', content)
    content = re.sub(r'<script>\s*\n\s*<script>', '<script>', content) # fix any orphaned <script><script>
    content = re.sub(r'<script>\s*</script>', '', content) # remove empty scripts
    
    # Insert clean JS block right before </head>
    content = content.replace('</head>', f'{clean_js_block}\n</head>')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"Cleaned script tags in {filepath}")

print(f"Total files cleaned: {count}")
