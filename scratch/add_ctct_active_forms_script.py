import glob
import re

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)

combined_ctct_code = """        <!-- Begin Constant Contact Active Forms -->
        <script> var _ctct_m = "a79e89c0998befa80793c5464469c842"; </script>
        <script id="signupScript" src="//static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
        <!-- End Constant Contact Active Forms -->
        <!-- Begin Constant Contact Inline Form Code -->
        <div class="ctct-inline-form" data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"></div>
        <!-- End Constant Contact Inline Form Code -->"""

count = 0
for filepath in html_files:
    if 'contactanos' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing ctct-inline-form or ctct blocks with combined_ctct_code
    pattern = r'<!-- Begin Constant Contact Active Forms -->[\s\S]*?<!-- End Constant Contact Inline Form Code -->'
    if re.search(pattern, content):
        new_content = re.sub(pattern, combined_ctct_code, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated active forms + inline form in: {filepath}")
    else:
        pattern2 = r'<!-- Begin Constant Contact Inline Form Code -->[\s\S]*?<!-- End Constant Contact Inline Form Code -->'
        if re.search(pattern2, content):
            new_content = re.sub(pattern2, combined_ctct_code, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Replaced inline form with active forms + inline form in: {filepath}")

print(f"\nTotal files updated: {count}")
