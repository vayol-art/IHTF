import glob

en_play_files = glob.glob('en/obra-*/index.html')
count = 0

old_str = 'document.getElementById("play-author").textContent = play.author;'
new_str = 'document.getElementById("play-author").textContent = play.author_en || play.author;'

for filepath in en_play_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated author script in: {filepath}")

print(f"\nTotal English play pages updated: {count}")
