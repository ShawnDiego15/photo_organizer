# pip install Pillow

import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

SOURCE_FOLDER = 'unorganized_media'
DEST_FOLDER = 'organized_media'

def get_exif_date(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        if not exif_data:
            return None

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'DateTimeOriginal':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Could not read EXIF for {filepath}: {e}")
    return None

def get_file_mod_date(filepath):
    return datetime.fromtimestamp(os.path.getmtime(filepath))

def organize_photos():
    if not os.path.exists(DEST_FOLDER):
        os.makedirs(DEST_FOLDER)

    for root, _, files in os.walk(SOURCE_FOLDER):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                full_path = os.path.join(root, filename)

                # Try EXIF first, fall back to mod date
                date_taken = get_exif_date(full_path) or get_file_mod_date(full_path)
                folder_name = date_taken.strftime('%Y-%m-%d')
                # dest_path = os.path.join(DEST_FOLDER, "baseball_game", folder_name)
                dest_path = os.path.join(DEST_FOLDER, folder_name)

                os.makedirs(dest_path, exist_ok=True)
                shutil.move(full_path, os.path.join(dest_path, filename))
                print(f"Moved {filename} to {dest_path}")

organize_photos()
