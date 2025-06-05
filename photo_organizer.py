# pip install Pillow
# pip install exifread

import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import exifread

SOURCE_FOLDER = 'unorganized_media'
# Potential for working within each drive: /media/shawn/MyDrive
#   E:/MyPhotos
#   Change depending on file structure.
DEST_FOLDER = SOURCE_FOLDER # Set to SOURCE_FOLDER to organize in place

def get_exif_date(filepath):
    """Reads EXIF data from JPEG/PNG images."""
    try:
        with Image.open(filepath) as image:
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


def get_exif_date_raw(filepath):
    """Reads EXIF date from NEF (RAW) files."""
    try:
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal', details=False)
            date_tag = tags.get('EXIF DateTimeOriginal')
            if date_tag:
                return datetime.strptime(str(date_tag), '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Could not read EXIF (exifread) for {filepath}: {e}")
    return None

def get_file_mod_date(filepath):
    """If other attempts fail, pull the files last modified date."""
    return datetime.fromtimestamp(os.path.getmtime(filepath))

def get_photo_date(filepath):
    """Returns date from EXIF or file modification time, based on file type."""
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext in ('.jpg', '.jpeg', '.png'):
        return get_exif_date(filepath) or get_file_mod_date(filepath)
    elif ext == '.nef':
        return get_exif_date_raw(filepath) or get_file_mod_date(filepath)
    else:
        return get_file_mod_date(filepath)

def move_photo_to_folder(filepath, dest_folder):
    """Creates folder if needed and moves file to it."""
    os.makedirs(dest_folder, exist_ok=True)
    filename = os.path.basename(filepath)
    try:
        shutil.move(filepath, os.path.join(dest_folder, filename))
        print(f"Moved {filename} to {dest_folder}")
    except Exception as e:
        print(f"Error moving {filename}: {e}")

def is_valid_media_file(filename):
    """Check if filename has a supported media extension."""
    valid_exts = {'.jpg', '.jpeg', '.png', '.nef'}
    ext = os.path.splitext(filename)[1].lower()
    return ext in valid_exts

def should_skip_folder(abs_root, abs_source, abs_dest):
    """
    Returns True if folder should be skipped to avoid reprocessing files 
    inside the destination folder (unless organizing in place).
    """
    if abs_dest == abs_source:
        return False
    return abs_root.startswith(abs_dest) and abs_root != abs_source

def organize_photos():
    """Organizes all supported media files based on metadata or modified time."""
    os.makedirs(DEST_FOLDER, exist_ok=True)
    abs_source = os.path.abspath(SOURCE_FOLDER)
    abs_dest = os.path.abspath(DEST_FOLDER)
    base_folder = abs_dest if abs_dest != abs_source else abs_source

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        abs_root = os.path.abspath(root)

        if should_skip_folder(abs_root, abs_source, abs_dest):
            continue

        for filename in files:
            if not is_valid_media_file(filename):
                continue
            
            full_path = os.path.join(root, filename)
            date_taken = get_photo_date(full_path)

            # Change folder name as needed based on organization needs.
            folder_name = date_taken.strftime('%Y-%m-%d')
            # folder_name = "baseball_game"

            #   If the need for a topic - date structure is needed the following can be used:
            dest_path = os.path.join(DEST_FOLDER, "baseball_game", folder_name)
            # dest_path = os.path.join(base_folder, folder_name)

            move_photo_to_folder(full_path, dest_path)

if __name__ == "__main__":
    organize_photos()
