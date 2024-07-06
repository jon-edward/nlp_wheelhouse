import glob
import logging
from pathlib import Path
import shutil
import subprocess
import sys


def create_wheelhouse(platform: str, wheelhouse_path: Path, requirements_path: Path):
    wheelhouse_path.mkdir(parents=True, exist_ok=True)

    platform_subcommand = ()

    if platform:
        platform_subcommand = "--platform", platform

    py_args = [
        sys.executable, "-m", "pip", "download", *platform_subcommand, 
        "-d", str(wheelhouse_path), "--only-binary=:all:", 
        "-r", str(requirements_path), "--no-cache-dir"
    ]

    logging.info("Running command: %s", " ".join(py_args))
    
    subprocess.check_call(py_args)

    shutil.make_archive(wheelhouse_path.name, "zip", wheelhouse_path)


def install(wheelhouse_path: Path, requirements_path: Path):
    py_args = [
        sys.executable, "-m", "pip", "install", f"--find-links={str(wheelhouse_path)}", 
        "--no-index", "-r", str(requirements_path)
    ]

    logging.info("Running command: %s", " ".join(py_args))

    subprocess.check_call(py_args)


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
        "--install",
        action="store_true",
        default=False,
        help="It provided, installs all wheelhouses after creation. Should only be used for testing."
    )

    args = parser.parse_args()

    _platform = args.platform

    for file_name in glob.glob(str(_current_directory.joinpath("wheel_requirements", "*_requirements.txt"))):
        _requirements_path = Path(file_name)
        wheelhouse_identifier, *_ = _requirements_path.name.split("_")

        _wheelhouse_path = _current_directory.joinpath(f"{wheelhouse_identifier}_wheels")
        wheelhouse_path_out = _wheelhouse_path.joinpath(_wheelhouse_path.name)

        create_wheelhouse(_platform, wheelhouse_path_out, _requirements_path)

        shutil.make_archive(_wheelhouse_path.name, "zip", _wheelhouse_path)

        if args.install:
            install(wheelhouse_path_out, _requirements_path)
