import glob
import re

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)
count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove active forms block with comments
    content = re.sub(r'<!-- Begin Constant Contact Active Forms -->[\s\S]*?<!-- End Constant Contact Active Forms -->\s*', '', content)
    
    # Remove inline form block with comments
    content = re.sub(r'<!-- Begin Constant Contact Inline Form Code -->[\s\S]*?<!-- End Constant Contact Inline Form Code -->\s*', '', content)
    
    # Remove any standalone ctct-inline-form divs
    content = re.sub(r'<div class="ctct-inline-form"[\s\S]*?>\s*</div>\s*', '', content)
    
    # Remove any standalone signupScript tags
    content = re.sub(r'<script id="signupScript"[\s\S]*?></script>\s*', '', content)
    
    # Remove any standalone _ctct_m scripts
    content = re.sub(r'<script>\s*var _ctct_m = [\s\S]*?</script>\s*', '', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Removed Constant Contact code from: {filepath}")

print(f"\nTotal files cleaned of Constant Contact code: {count}")
