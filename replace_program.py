import re
import glob

# Read index.html
with open('index.html', 'r') as f:
    index_html = f.read()

# Extract the program-section from index.html
# We look for <section class="program-section" id="programa"> and its matching closing tag
start_tag = '<section class="program-section" id="programa">'
start_idx = index_html.find(start_tag)
if start_idx != -1:
    # Find the closing </section>
    # Since there are no nested <section> tags inside program-section in index.html,
    # we can just find the next </section> after the start_idx.
    end_idx = index_html.find('</section>', start_idx) + len('</section>')
    
    new_program_section = index_html[start_idx:end_idx]
    
    # Now replace in all obra-*.html
    for filepath in glob.glob('obra-*.html'):
        with open(filepath, 'r') as f:
            content = f.read()
            
        ob_start = content.find(start_tag)
        if ob_start != -1:
            ob_end = content.find('</section>', ob_start) + len('</section>')
            new_content = content[:ob_start] + new_program_section + content[ob_end:]
            
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Replaced in {filepath}")
        else:
            print(f"Could not find program-section in {filepath}")
else:
    print("Could not find program-section in index.html")
