import os
import glob
import re

# Constant Contact replacement HTML for the newsletter section
new_newsletter_content = """        <style>
          .newsletter {
            padding: 40px 24px 20px !important;
          }

          .newsletter .section-inner {
            padding: 25px 30px 20px !important;
          }

          .newsletter h2 {
            margin-bottom: 6px !important;
          }

          .newsletter p {
            margin: 6px auto 16px !important;
          }
        </style>

        <!-- Begin Constant Contact Active Forms -->
        <script> var _ctct_m = "6b84846d-b4c9-4b02-867d-09c8a7ac5d40"; </script>
        <script id="signupScript" src="https://static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
        <!-- End Constant Contact Active Forms -->
        <!-- Begin Constant Contact Inline Form Code -->
        <div class="ctct-inline-form" data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"></div>
        <!-- End Constant Contact Inline Form Code -->"""

# Regex pattern to match the contents inside <div class="section-inner narrow"> of <section class="newsletter"...>
# specifically from <style> to <script src="https://link.msgsndr.com/js/form_embed.js"></script>
pattern = re.compile(
    r'(<section\s+class="newsletter"[^>]*>\s*<div\s+class="section-inner\s+narrow">\s*<h2>.*?</h2>\s*<p>.*?</p>)\s*<style>.*?</script>',
    re.DOTALL
)

html_files = glob.glob('**/*.html', recursive=True)
updated_count = 0
not_matched = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="newsletter"' in content or 'class="newsletter"' in content:
        if pattern.search(content):
            new_content = pattern.sub(r'\1\n' + new_newsletter_content, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f"Updated: {filepath}")
        else:
            not_matched.append(filepath)

print(f"\nTotal files updated: {updated_count}")
if not_matched:
    print(f"Files with newsletter section that did not match pattern: {not_matched}")
