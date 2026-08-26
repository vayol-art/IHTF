import glob

files = glob.glob("**/*.html", recursive=True)
issues = []
for f in files:
    content = open(f, encoding="utf-8").read()
    if '//";' in content or '//"' in content:
        issues.append(f)

print("Files with double slash issues:", issues)
