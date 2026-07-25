import glob

files = glob.glob('en/**/*.html', recursive=True) + glob.glob('en/*.html')
count = 0
for f in set(files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if '41st FESTIVAL REGISTRATIONS' in content:
        content = content.replace('41st FESTIVAL REGISTRATIONS', '41st IHTF INSCRIPTIONS')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1
        print(f"Updated {f}")
print(f"Total files updated: {count}")
