import glob
import re

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)

ctct_footer_code = """        <!-- Begin Constant Contact Active Forms -->
        <script> var _ctct_m = "6b84846d-b4c9-4b02-867d-09c8a7ac5d40"; </script>
        <script id="signupScript" src="https://static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
        <!-- End Constant Contact Active Forms -->
        <!-- Begin Constant Contact Inline Form Code -->
        <div class="ctct-inline-form" data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"></div>
        <!-- End Constant Contact Inline Form Code -->"""

count = 0
for filepath in html_files:
    # Skip contactanos pages for newsletter embed if user requested contactanos to be separate
    if 'contactanos' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target insertion point inside .newsletter container right after </style> or before </div> </section>
    pattern = r'(</style>[\s\n]*)(\s*</div>\s*</section>)'
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\1' + ctct_footer_code + r'\n\2', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Embedded newsletter form in: {filepath}")
    else:
        # Fallback target if <style> tag isn't inside .newsletter
        alt_pattern = r'(<section class="newsletter"[\s\S]*?<div class="section-inner[^>]*>[\s\S]*?<p>[\s\S]*?</p>\s*)(\s*</div>\s*</section>)'
        if re.search(alt_pattern, content):
            new_content = re.sub(alt_pattern, r'\1\n' + ctct_footer_code + r'\n\2', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Embedded newsletter form (alt pattern) in: {filepath}")

print(f"\nTotal files updated with footer newsletter embed: {count}")
