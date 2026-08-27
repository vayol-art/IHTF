import os
import glob

css_files = glob.glob("*.css")

target_block = """.ctct-inline-form div[class*="ctct-form"],
.ctct-embed-signup div[class*="ctct-form"] {
  display: flex !important;"""

replacement_block = """.ctct-inline-form div[class*="ctct-form"]:not([style*="display: none"]):not([hidden]),
.ctct-embed-signup div[class*="ctct-form"]:not([style*="display: none"]):not([hidden]) {
  display: flex !important;"""

guard_rule = """

.ctct-inline-form [style*="display: none"],
.ctct-embed-signup [style*="display: none"],
.ctct-inline-form [hidden],
.ctct-embed-signup [hidden] {
  display: none !important;
}"""

contact_target = """.contact-form-wrap .ctct-form-defaults,
.contact-form-wrap .ctct-form-wrapper,
.contact-form-wrap div[class*="ctct-form"] {"""

contact_replacement = """.contact-form-wrap .ctct-form-defaults:not([style*="display: none"]):not([hidden]),
.contact-form-wrap .ctct-form-wrapper:not([style*="display: none"]):not([hidden]),
.contact-form-wrap div[class*="ctct-form"]:not([style*="display: none"]):not([hidden]) {"""

contact_guard = """

.contact-form-wrap [style*="display: none"],
.contact-form-wrap [hidden] {
  display: none !important;
}"""

modified_count = 0

for filepath in css_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    if target_block in new_content:
        new_content = new_content.replace(target_block, replacement_block)
        # Add guard rule if not present
        if ".ctct-inline-form [style*=\"display: none\"]" not in new_content:
            # Insert guard after the closing brace of the flex block
            find_str = replacement_block
            idx = new_content.find(find_str)
            if idx != -1:
                end_brace = new_content.find("}", idx)
                if end_brace != -1:
                    new_content = new_content[:end_brace+1] + guard_rule + new_content[end_brace+1:]

    if contact_target in new_content:
        new_content = new_content.replace(contact_target, contact_replacement)
        if ".contact-form-wrap [style*=\"display: none\"]" not in new_content:
            idx = new_content.find(contact_replacement)
            if idx != -1:
                end_brace = new_content.find("}", idx)
                if end_brace != -1:
                    new_content = new_content[:end_brace+1] + contact_guard + new_content[end_brace+1:]

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1
        print(f"Updated: {filepath}")

print(f"Total CSS files updated: {modified_count}")
