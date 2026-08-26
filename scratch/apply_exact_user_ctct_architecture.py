import glob
import re

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)

activator_code = """  <!-- Begin Constant Contact Active Forms -->
  <script> var _ctct_m = "a79e89c0998befa80793c5464469c842"; </script>
  <script id="signupScript" src="//static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
  <!-- End Constant Contact Active Forms -->"""

newsletter_inline_code = """        <!-- Begin Constant Contact Inline Form Code -->
        <div class="ctct-inline-form" data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"></div>
        <!-- End Constant Contact Inline Form Code -->"""

contact_inline_code = """          <!-- Begin Constant Contact Inline Form Code -->
          <div class="ctct-inline-form" data-form-id="b0e7dcb5-c478-4f0f-bd92-01a4e41cd519"></div>
          <!-- End Constant Contact Inline Form Code -->"""

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Clean existing Constant Contact blocks
    content = re.sub(r'<!-- Begin Constant Contact Active Forms -->[\s\S]*?<!-- End Constant Contact Active Forms -->\s*', '', content)
    content = re.sub(r'<!-- Begin Constant Contact Inline Form Code -->[\s\S]*?<!-- End Constant Contact Inline Form Code -->\s*', '', content)
    content = re.sub(r'<div class="ctct-inline-form"[\s\S]*?>\s*</div>\s*', '', content)
    content = re.sub(r'<script id="signupScript"[\s\S]*?></script>\s*', '', content)
    content = re.sub(r'<script>\s*var _ctct_m = [\s\S]*?</script>\s*', '', content)
    
    # 2. Insert Activator code in <head> right after <head>
    content = re.sub(r'(<head[^>]*>\s*)', r'\1' + activator_code + '\n', content, count=1)
    
    # 3. Insert Inline Form Code in appropriate location
    if 'contactanos' in filepath:
        content = re.sub(r'(<div class="contact-form-wrap">\s*)', r'\1' + contact_inline_code + '\n', content, count=1)
    else:
        pattern = r'(</style>[\s\n]*)(\s*</div>\s*</section>)'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1' + newsletter_inline_code + r'\n\2', content, count=1)
        else:
            alt_pattern = r'(<section class="newsletter"[\s\S]*?<div class="section-inner[^>]*>[\s\S]*?<p>[\s\S]*?</p>\s*)(\s*</div>\s*</section>)'
            content = re.sub(alt_pattern, r'\1\n' + newsletter_inline_code + r'\n\2', content, count=1)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Applied CTCT architecture in: {filepath}")

print(f"\nTotal files updated: {count}")
