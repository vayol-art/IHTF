import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_code_1 = '''      const sentences = play.description.split(". ");
      let currentParagraph = "";
      sentences.forEach((sentence, index) => {
        if (sentence.trim()) {
          currentParagraph += sentence.trim() + ". ";
          if ((index + 1) % 2 === 0 || index === sentences.length - 1) {
            const p = document.createElement("p");
            p.textContent = currentParagraph;
            descContainer.appendChild(p);
            currentParagraph = "";
          }
        }
      });'''

    new_code_1 = '''      const sentences = play.description.split(". ");
      let currentParagraph = "";
      sentences.forEach((sentence, index) => {
        if (sentence.trim()) {
          const cleanSentence = sentence.trim().replace(/\\.+$/, "");
          currentParagraph += cleanSentence + ". ";
          if ((index + 1) % 2 === 0 || index === sentences.length - 1) {
            const p = document.createElement("p");
            p.textContent = currentParagraph.trim();
            descContainer.appendChild(p);
            currentParagraph = "";
          }
        }
      });'''

    old_code_2 = '''      const descText = play.description_en || play.description;
      const sentences = descText.split(". ");
      let currentParagraph = "";
      sentences.forEach((sentence, index) => {
        if (sentence.trim()) {
          currentParagraph += sentence.trim() + ". ";
          if ((index + 1) % 2 === 0 || index === sentences.length - 1) {
            const p = document.createElement("p");
            p.textContent = currentParagraph;
            descContainer.appendChild(p);
            currentParagraph = "";
          }
        }
      });'''

    new_code_2 = '''      const descText = play.description_en || play.description;
      const sentences = descText.split(". ");
      let currentParagraph = "";
      sentences.forEach((sentence, index) => {
        if (sentence.trim()) {
          const cleanSentence = sentence.trim().replace(/\\.+$/, "");
          currentParagraph += cleanSentence + ". ";
          if ((index + 1) % 2 === 0 || index === sentences.length - 1) {
            const p = document.createElement("p");
            p.textContent = currentParagraph.trim();
            descContainer.appendChild(p);
            currentParagraph = "";
          }
        }
      });'''

    modified = False
    if old_code_1 in content:
        content = content.replace(old_code_1, new_code_1)
        modified = True
    if old_code_2 in content:
        content = content.replace(old_code_2, new_code_2)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

files = glob.glob("obra*.html") + glob.glob("en/obra*.html") + glob.glob("obra.html") + glob.glob("en/obra.html")
for file in files:
    fix_file(file)
