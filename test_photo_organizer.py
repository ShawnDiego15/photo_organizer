import unittest
import os

from photo_organizer import is_valid_media_file, should_skip_folder

class TestPhotoOrganizer(unittest.TestCase):

    def test_is_valid_media_file(self):
        # Valid extensions (case insensitive)
        self.assertTrue(is_valid_media_file("photo.jpg"))
        self.assertTrue(is_valid_media_file("image.JPEG"))
        self.assertTrue(is_valid_media_file("snapshot.png"))
        self.assertTrue(is_valid_media_file("raw.NEF"))

        # Invalid extensions
        self.assertFalse(is_valid_media_file("document.pdf"))
        self.assertFalse(is_valid_media_file("video.mp4"))
        self.assertFalse(is_valid_media_file("archive.zip"))
        self.assertFalse(is_valid_media_file("image.jpgg"))  # typo

        # Files without extension
        self.assertFalse(is_valid_media_file("no_extension"))

    def test_should_skip_folder(self):
        source = os.path.abspath("unorganized_media")
        dest = os.path.abspath("organized_media")

        # Case: organizing in place (source == dest)
        self.assertFalse(should_skip_folder(source, source, source))
        self.assertFalse(should_skip_folder(os.path.join(source, "subfolder"), source, source))

        # Case: different source and dest, folder inside dest (should skip)
        folder_in_dest = os.path.join(dest, "some_folder")
        self.assertTrue(should_skip_folder(folder_in_dest, source, dest))

        # Folder is source itself (should NOT skip)
        self.assertFalse(should_skip_folder(source, source, dest))

        # Folder outside dest (should NOT skip)
        unrelated_folder = os.path.abspath("some_other_folder")
        self.assertFalse(should_skip_folder(unrelated_folder, source, dest))

if __name__ == "__main__":
    unittest.main()
