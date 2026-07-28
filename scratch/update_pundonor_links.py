import os
import glob

arsht_url = "https://www.arshtcenter.org/tickets/2025-2026/international-hispanic-theatre-festival-of-miami/pundonor/"

html_files = glob.glob("*.html") + glob.glob("en/*.html")

updated_files = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # Spanish replacement
    old_es = '<a class="ticket-btn" href="obra-pundonor.html" onclick="event.stopPropagation();">Entradas</a>'
    new_es = f'<a class="ticket-btn" href="{arsht_url}" target="_blank" onclick="event.stopPropagation();">Entradas</a>'
    
    # English replacement
    old_en = '<a class="ticket-btn" href="obra-pundonor.html" onclick="event.stopPropagation();">Tickets</a>'
    new_en = f'<a class="ticket-btn" href="{arsht_url}" target="_blank" onclick="event.stopPropagation();">Tickets</a>'

    new_content = new_content.replace(old_es, new_es)
    new_content = new_content.replace(old_en, new_en)
    
    # If in obra-pundonor.html, also check buyBtn.href
    if "obra-pundonor.html" in filepath:
        old_buy = 'buyBtn.href = "https://www.squadup.com/events/40-festival-internacional-de-teatro-hispano-de-miami-1?legacy=0";'
        new_buy = f'buyBtn.href = play.ticketUrl || "{arsht_url}";'
        new_content = new_content.replace(old_buy, new_buy)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(filepath)

print(f"Updated {len(updated_files)} files: {updated_files}")
