import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We look for <article class="play-card ...">...</article> blocks.
pattern = re.compile(r'<article\s+class="play-card\s+([^"]+)"[^>]*>(.*?)</article>', re.DOTALL)
matches = list(pattern.finditer(content))

print(f"Found {len(matches)} play cards.")

def extract_dates(card_body):
    start_tag = re.search(r'<div\s+class="dates"([^>]*)>', card_body)
    if not start_tag:
        return "", ""
    start_idx = start_tag.end()
    
    end_idx = card_body.find('<div class="image-carousel"')
    if end_idx == -1:
        end_idx = card_body.find('<div class="image-carousel')
        
    if end_idx == -1:
        # Fallback
        return "", ""
        
    # Extract the block between start of dates inner and image-carousel
    dates_block = card_body[start_idx:end_idx].strip()
    
    # Strip the trailing closing div of the dates wrapper
    if dates_block.endswith("</div>"):
        dates_block = dates_block[:-6].strip()
        
    style_attr = start_tag.group(1).strip()
    dates_style = f" {style_attr}" if style_attr else ""
    return dates_block, dates_style

new_content = content
for match in matches:
    full_match = match.group(0)
    color_class = match.group(1).strip() # e.g. "purple", "teal special"
    card_body = match.group(2)
    
    # 1. Extract country
    country_match = re.search(r'<div\s+class="country">([^<]+)</div>', card_body)
    country = country_match.group(1).strip() if country_match else ""
    
    # Check if there is kids day class (kids-day)
    kids_match = re.search(r'<div\s+class="kids-day">([^<]+)</div>', card_body)
    kids_text = kids_match.group(1).strip() if kids_match else ""
    
    # 2. Extract title
    title_match = re.search(r'<h3>(.*?)</h3>', card_body, re.DOTALL)
    title = title_match.group(1).strip() if title_match else ""
    
    # 3. Extract ticket link
    ticket_match = re.search(r'<a\s+class="ticket"\s+href="([^"]+)"[^>]*>(.*?)</a>', card_body)
    if ticket_match:
        ticket_href = ticket_match.group(1).strip()
        ticket_text = ticket_match.group(2).strip()
    else:
        # Fallback for Robinson Crusoe
        ticket_href = "obra-robinson-crusoe.html"
        ticket_text = "Reservar"
    
    # Extract logos
    logos_wrapper_match = re.search(r'<div\s+class="logos-wrapper">(.*?)</div>', card_body, re.DOTALL)
    if logos_wrapper_match:
        logos_html = logos_wrapper_match.group(1).strip()
    else:
        # Check if there is class wide-logo
        wide_logo_match = re.search(r'<img\s+class="wide-logo"[^>]*src="([^"]+)"[^>]*>', card_body)
        if wide_logo_match:
            logos_html = f'<img src="{wide_logo_match.group(1)}" alt="Logo teatro" />'
        else:
            logos_html = ""
            
    # 4. Extract dates using the robust function
    dates_html, dates_style = extract_dates(card_body)
    
    # 5. Extract carousel
    carousel_match = re.search(r'<div\s+class="image-carousel"[^>]*>(.*?)</div>\s*</div>', card_body, re.DOTALL)
    if not carousel_match:
        carousel_match = re.search(r'<div\s+class="image-carousel"[^>]*>(.*?)</div>', card_body, re.DOTALL)
    carousel_html = carousel_match.group(0).strip() if carousel_match else ""
    
    # Now generate the new card wrapper
    top_badges = f'<span class="country-badge">{country}</span>'
    if kids_text:
        top_badges += f'\n          <span class="kids-badge">{kids_text}</span>'
        
    new_card_html = f"""          <div class="play-card-wrapper {color_class}">
            <article class="play-card">
              {carousel_html}
              <div class="card-content">
                <div class="card-top">
                  {top_badges}
                </div>
                <div class="card-bottom">
                  <div class="card-meta">
                    <h3>{title}</h3>
                    <div class="theatre-logos">
                      {logos_html}
                    </div>
                  </div>
                  <a class="ticket-btn" href="{ticket_href}">{ticket_text}</a>
                </div>
              </div>
            </article>
            <div class="dates"{dates_style}>
              {dates_html}
            </div>
          </div>"""
          
    new_content = new_content.replace(full_match, new_card_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Finished rewriting index.html!")
