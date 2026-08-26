import glob
import re

user_ctct_code = """<!-- Begin Constant Contact Active Forms -->
<script> var _ctct_m = "a79e89c0998befa80793c5464469c842"; </script>
<script id="signupScript" src="//static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
<!-- End Constant Contact Active Forms -->"""

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)
updated_count = 0

pattern = r'<!-- Begin Constant Contact Active Forms -->[\s\S]*?<!-- End Constant Contact Active Forms -->'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, user_ctct_code, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated CTCT script in: {filepath}")

print(f"\nTotal files updated with user's Constant Contact code: {updated_count}")
