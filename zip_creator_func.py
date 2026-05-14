import pathlib
import zipfile

def make_archive(filepaths, folderpath):
    folder = pathlib.Path(folderpath, "compressed_files.zip")
    with zipfile.ZipFile(folder, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)