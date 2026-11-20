"""Example script: tidy a folder of exports by date."""
from pathlib import Path
import shutil, datetime

def tidy(folder: str) -> None:
    for f in Path(folder).iterdir():
        if f.is_file():
            day = datetime.date.fromtimestamp(f.stat().st_mtime).isoformat()
            dest = Path(folder) / day
            dest.mkdir(exist_ok=True)
            shutil.move(str(f), dest / f.name)

if __name__ == "__main__":
    tidy("exports")
