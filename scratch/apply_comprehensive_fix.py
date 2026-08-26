import os
import glob
import re

css_snippet = """
/* =====================================================
   GLOBAL FIX: Language Dropdown & Constant Contact Newsletter
   ===================================================== */
.site-header {
  z-index: 9999 !important;
}

.lang-selector {
  position: relative !important;
  z-index: 10000 !important;
}

.lang-dropdown {
  z-index: 10001 !important;
}

.lang-selector.open .lang-dropdown {
  display: flex !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateX(-50%) translateY(0) !important;
}

/* Constant Contact Newsletter Embed Layout Fix */
.ctct-inline-form,
.ctct-embed-signup {
  width: 100% !important;
  max-width: 650px !important;
  margin: 0 auto !important;
}

.ctct-inline-form form,
.ctct-embed-signup form {
  width: 100% !important;
  display: block !important;
}

.ctct-inline-form div[class*="ctct-form"],
.ctct-embed-signup div[class*="ctct-form"] {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  width: 100% !important;
  box-sizing: border-box !important;
  gap: 10px !important;
}

.ctct-inline-form label,
.ctct-inline-form input,
.ctct-inline-form p,
.ctct-inline-form button,
.ctct-embed-signup label,
.ctct-embed-signup input,
.ctct-embed-signup p,
.ctct-embed-signup button {
  position: static !important;
  float: none !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  text-align: center !important;
}

.ctct-inline-form input[type="email"],
.ctct-embed-signup input[type="email"] {
  max-width: 480px !important;
  margin: 0 auto !important;
  padding: 12px 16px !important;
  border-radius: 8px !important;
}

.ctct-inline-form button[type="submit"],
.ctct-embed-signup button[type="submit"],
.ctct-button {
  width: auto !important;
  min-width: 180px !important;
  max-width: 280px !important;
  margin: 14px auto 0 !important;
  padding: 12px 28px !important;
  border-radius: 999px !important;
  background-color: #1a789e !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  cursor: pointer !important;
}
"""

css_files = glob.glob("*.css")
for css_file in css_files:
    with open(css_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Avoid duplicate appending
    if "GLOBAL FIX: Language Dropdown & Constant Contact Newsletter" not in content:
        content += "\n" + css_snippet
        with open(css_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Appended fixes to {css_file}")

print("CSS files update complete.")
