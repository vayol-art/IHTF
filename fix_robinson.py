import glob

# we want to modify the Robinson Crusoe card across all html files
for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()

    # check if file contains the robinson crusoe card
    if '<h3>Las asombrosas aventuras de Robinson Crusoe</h3>' in content:
        # We need to remove the ticket-btn from the card-bottom
        btn_str = '<a class="ticket-btn" href="obra-robinson-crusoe.html">Reservar</a>'
        new_content = content.replace(btn_str, '')

        # And insert it into the 20th block
        target_str = '<div style="display: flex; align-items: center; gap: 8px;">\n                  <img src="assets/c6c34a67f99807d7cc132ebfb6abf5827c23757a.png"'
        
        replacement = '<div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">\n                  <div style="display: flex; align-items: center; gap: 8px;">\n                    <img src="assets/c6c34a67f99807d7cc132ebfb6abf5827c23757a.png"'
        
        # We also need to add the button after the logos
        logos_end = 'style="height: 20px; width: auto;" />\n                </div>'
        logos_replacement = 'style="height: 20px; width: auto;" />\n                  </div>\n                  <a class="ticket-btn" href="obra-robinson-crusoe.html" style="font-size: 11px; padding: 4px 12px; margin: 0; min-height: 0; background: #fff; color: var(--teal);">Reservar</a>\n                </div>'

        if target_str in new_content and logos_end in new_content:
            new_content = new_content.replace(target_str, replacement)
            new_content = new_content.replace(logos_end, logos_replacement)
            
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            # Let's try a regex approach because spacing might be different
            import re
            
            # Find the orange block
            orange_pattern = r'(<div[^>]*background:\s*var\(--orange\)[^>]*>.*?)<div style="display: flex; align-items: center; gap: 8px;">\s*<img src="assets/c6c34a67f99807d7cc132ebfb6abf5827c23757a\.png".*?style="height: 20px; width: auto;" />\s*</div>(.*?)</div>'
            
            # Actually, simpler:
            # Let's just find the exact block and replace it using a more resilient way
            pass

