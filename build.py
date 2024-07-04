from pathlib import Path
import shutil
import subprocess
import sys
from typing import Iterable

import requests


def build(platform: str, wheelhouse_path: Path, setup_script_path: Path, requirements_path: Path, extra_wheel_urls: Iterable[str]):
    wheelhouse_path.mkdir(exist_ok=True)

    platform_ident = ()

    if platform:
        platform_ident = "--platform", platform
    
    subprocess.check_call([
        sys.executable, "-m", "pip", "download", ".", 
        *platform_ident, "-d", str(wheelhouse_path), "--only-binary=:all:"
    ])

    with requirements_path.open() as f:
        requirements = [x.strip() for x in f.readlines() if x.strip()]

    for url in extra_wheel_urls:
        filename = url.split("/")[-1]
        
        distribution, *_ = filename.split("-")
        requirements.append(distribution)

        wheelhouse_path.joinpath(filename).write_bytes(requests.get(url).content)
    
    wheelhouse_path.joinpath("setup.py").write_text(setup_script_path.read_text())
    wheelhouse_path.joinpath("requirements.txt").write_text("\n".join(requirements))

    shutil.make_archive(wheelhouse_path.name, "zip", root_dir=wheelhouse_path)


if __name__ == "__main__":
    import argparse

    _current_directory = Path(__file__).parent

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "platform",
        type=str,
        nargs="?",
        default="",
        help="Which platform tag to query PyPI for"
    )

    parser.add_argument(
        "--wheelhouse-path",
        "-w",
        type=Path,
        default=_current_directory.joinpath("nlp_wheelhouse"),
        help="Where to download the wheelhouse directory."
    )

    parser.add_argument(
        "--setup-script-path",
        "-s",
        type=Path,
        default=_current_directory.joinpath("setup.py"),
        help="Where to copy the setup script from."
    )

    parser.add_argument(
        "--requirements-path",
        "-r",
        type=Path,
        default=_current_directory.joinpath("requirements.txt"),
        help="Where to copy requirements from."
    )

    parser.add_argument(
        "--extra_wheel_urls",
        "-e",
        type=str,
        nargs="*",
        help="Adds wheel file urls to final build and their distribution identifier to requirements."
    )

    args = parser.parse_args()

    _platform = args.platform
    _wheelhouse_path = args.wheelhouse_path
    _setup_script_path = args.setup_script_path
    _requirements_path = args.requirements_path
    _extra_wheel_urls = args.extra_wheel_urls

    build(
        platform=_platform,
        wheelhouse_path=_wheelhouse_path,
        setup_script_path=_setup_script_path,
        requirements_path=_requirements_path,
        extra_wheel_urls=_extra_wheel_urls
    )
