import os.path


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "resources")
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "resources2")
ZIP_DIR = os.path.join(ARCHIVE_DIR, "test_archive.zip")
