import os
import glob

def update_files():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    es_files = glob.glob(os.path.join(base_dir, 'es', '**', '*.html'), recursive=True)
    en_files = glob.glob(os.path.join(base_dir, 'en', '**', '*.html'), recursive=True)
    
    updated_count = 0
    
    for file_path in es_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_es_root = '<a href="nosotros/#personal" class="submenu-item">Personal</a>'
        new_es_root = '<a href="nosotros/#personal" class="submenu-item">Personal</a>\n          <a href="nosotros/#cartelista" class="submenu-item">Cartelista</a>'
        
        old_es_sub = '<a href="../nosotros/#personal" class="submenu-item">Personal</a>'
        new_es_sub = '<a href="../nosotros/#personal" class="submenu-item">Personal</a>\n          <a href="../nosotros/#cartelista" class="submenu-item">Cartelista</a>'
        
        if old_es_root in content and 'Cartelista' not in content:
            content = content.replace(old_es_root, new_es_root)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated ES root match: {file_path}")
        elif old_es_sub in content and 'Cartelista' not in content:
            content = content.replace(old_es_sub, new_es_sub)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated ES sub match: {file_path}")

    for file_path in en_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_en_root = '<a href="nosotros/#personal" class="submenu-item">Staff</a>'
        new_en_root = '<a href="nosotros/#personal" class="submenu-item">Staff</a>\n          <a href="nosotros/#cartelista" class="submenu-item">Poster Artist</a>'
        
        old_en_sub = '<a href="../nosotros/#personal" class="submenu-item">Staff</a>'
        new_en_sub = '<a href="../nosotros/#personal" class="submenu-item">Staff</a>\n          <a href="../nosotros/#cartelista" class="submenu-item">Poster Artist</a>'
        
        if old_en_root in content and 'Poster Artist' not in content:
            content = content.replace(old_en_root, new_en_root)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated EN root match: {file_path}")
        elif old_en_sub in content and 'Poster Artist' not in content:
            content = content.replace(old_en_sub, new_en_sub)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated EN sub match: {file_path}")

    print(f"Total files updated: {updated_count}")

if __name__ == '__main__':
    update_files()
