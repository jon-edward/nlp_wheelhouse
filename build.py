from pathlib import Path
import shutil
import subprocess
import sys

import requests


_current_directory = Path(__file__).parent

PLATFORM = "win_amd64"

WHEELHOUSE =  _current_directory.joinpath(f"nlp_wheelhouse{'' if not PLATFORM else '-' + PLATFORM}")

SETUP_SCRIPT = _current_directory.joinpath("setup.py")
REQUIREMENTS = _current_directory.joinpath("requirements.txt")

EXTRA_REQUIRES = [
    "en_core_web_sm"
]

EXTRA_WHEELS = [
    "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl"
]


def main():
    WHEELHOUSE.mkdir(exist_ok=True)

    platform_ident = ()

    if PLATFORM:
        platform_ident = "--platform", PLATFORM
    
    subprocess.check_call([
        sys.executable, "-m", "pip", "download", ".", 
        *platform_ident, "-d", str(WHEELHOUSE), "--only-binary=:all:"
    ])

    for url in EXTRA_WHEELS:
        filename = url.split("/")[-1]
        WHEELHOUSE.joinpath(filename).write_bytes(requests.get(url).content)
    
    WHEELHOUSE.joinpath("setup.py").write_text(SETUP_SCRIPT.read_text())

    with REQUIREMENTS.open() as f:
        requirements = [x.strip() for x in f.readlines() + EXTRA_REQUIRES if x.strip()]
        WHEELHOUSE.joinpath("requirements.txt").write_text("\n".join(requirements))

    shutil.make_archive(WHEELHOUSE.name, "zip", root_dir=WHEELHOUSE)


if __name__ == "__main__":
    main()
