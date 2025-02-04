import pathlib
import zipfile



def file_compressor(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, "compressed_file.zip")
    with zipfile.ZipFile(dest_dir, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


