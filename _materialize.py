from pathlib import Path
import base64, zipfile, shutil

payload = Path('.course.zip.b64')
archive = Path('.course.zip')
archive.write_bytes(base64.b64decode(payload.read_text()))
with zipfile.ZipFile(archive) as z:
    z.extractall('.course-unpack')
source = Path('.course-unpack/zen-course')
for item in source.iterdir():
    target = Path(item.name)
    if item.is_dir():
        if target.exists(): shutil.rmtree(target)
        shutil.copytree(item, target)
    else:
        shutil.copy2(item, target)
for path in [payload, archive, Path('.course-unpack'), Path('_materialize.py')]:
    if path.is_dir(): shutil.rmtree(path)
    elif path.exists(): path.unlink()
