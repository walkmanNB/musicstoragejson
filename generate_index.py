import os
import json
from mutagen import File

MUSIC_DIR = "music"  # 假设你的音乐放在这个文件夹
library = []

for root, dirs, files in os.walk(MUSIC_DIR):
    for file in files:
        if file.lower().endswith(('.mp3', '.flac', '.m4a', '.wav')):
            file_path = os.path.join(root, file)
            audio = File(file_path, easy=True)

            # 提取 Tag
            title = audio.get('title', [file])[0]
            artist = audio.get('artist', ['Unknown Artist'])[0]
            album = audio.get('album', ['Unknown Album'])[0]

            # 构造 GitHub Raw 访问链接
            raw_url = f"https://raw.githubusercontent.com/你的用户名/你的仓库名/main/{file_path}"

            library.append({
                "title": title,
                "artist": artist,
                "album": album,
                "url": raw_url
            })

with open('library.json', 'w', encoding='utf-8') as f:
    json.dump(library, f, ensure_ascii=False, indent=4)
