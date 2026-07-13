import re
import os

target_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"
html_files = [
    "obra.html",
    "obra-zombi-manifiesto.html",
    "obra-sueno.html",
    "obra-robinson-crusoe.html",
    "obra-odd-man-out.html",
    "obra-historia-de-un-jabali.html",
    "obra-hamlet.html",
    "obra-carrusel.html",
    "obra-a-fuego.html"
]

# We match:
# <h3>Sueño</h3> followed by anything until <div class="dates">
# and then match everything until the final closing </div> of the dates container.
# Since the dates container contains three inner <div>...</div> items,
# it ends with a closing </div> followed by the container's closing </div>.
pattern = re.compile(
    r'(<h3>Sueño</h3>[\s\S]*?<div class="dates">)([\s\S]*?)(</div>\s*</div>)',
    re.IGNORECASE
)

def replace_dates(match):
    header = match.group(1)
    dates_content = match.group(2)
    footer = match.group(3)
    # Replace all remaining 8:30 PM with 7:00 PM
    updated_dates = dates_content.replace('8:30 PM', '7:00 PM')
    return header + updated_dates + footer

for filename in html_files:
    filepath = os.path.join(target_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = pattern.search(content)
    if match:
        old_dates = match.group(2)
        new_dates = old_dates.replace('8:30 PM', '7:00 PM')
        if old_dates != new_dates:
            new_content = pattern.sub(replace_dates, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated {filename} dates block.")
        else:
            print(f"No replacement needed in {filename} (dates are already updated or don't match 8:30 PM)")
    else:
        print(f"Pattern not found in {filename}")
