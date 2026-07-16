import re

with open('style.css', 'r') as f:
    style_content = f.read()

with open('obra.css', 'r') as f:
    obra_content = f.read()

# Find the start of the program-section in style.css
# We look for .program-section
start_idx = style_content.find('.program-section {')

# Find the end of it (before Newsletter Section)
end_idx = style_content.find('/* Newsletter Section */')

program_css = style_content[start_idx:end_idx]

# Replace in obra.css
ob_start = obra_content.find('/* ==========================================================================')
# Let's find the specific block:
ob_start = obra_content.find('/* ==========================================================================\n   Program Section Styles (from style.css)\n   ========================================================================== */')
if ob_start != -1:
    ob_end = obra_content.find('/* ==========================================================================', ob_start + 10)
    # If not found another section, maybe till the end of that part.
    if ob_end == -1:
        ob_end = obra_content.find('.newsletter {', ob_start) # wait, we shouldn't delete newsletter.
        # let's just find where .new-play-card-section starts, which is what we appended
        ob_end = obra_content.find('/* --- NEW PLAY CARD LAYOUT --- */')

    if ob_end != -1:
        new_obra_content = obra_content[:ob_start] + "/* --- PROGRAM SECTION --- */\n" + program_css + "\n" + obra_content[ob_end:]
        with open('obra.css', 'w') as f:
            f.write(new_obra_content)
        print("CSS replaced.")
    else:
        print("Could not find end of program section in obra.css")
else:
    print("Could not find start of program section in obra.css")
