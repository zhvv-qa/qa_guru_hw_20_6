import os
import shutil
import zipfile
import pytest

from script_os1 import TMP_DIR, ZIP_DIR, ARCHIVE_DIR

@pytest.fixture(scope="session", autouse=True)
def create_archive():
    if not os.path.exists(ARCHIVE_DIR):  # проверка существует ли папка
        os.mkdir(ARCHIVE_DIR)  # создание папки если её нет
        with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создание архива
            for file in os.listdir(TMP_DIR): zf.write(os.path.join(TMP_DIR, file), file) # добавление файлов в архив
    yield
    shutil.rmtree(ARCHIVE_DIR)
