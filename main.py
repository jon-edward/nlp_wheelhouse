from argparse import ArgumentParser
from pathlib import Path
import shutil
import subprocess
import sys


def build(platform: str, wheelhouse: Path, requirements: Path):
    wheelhouse.mkdir(exist_ok=True)

    platform_subcommand = ()

    if platform:
        platform_subcommand = "--platform", platform

    subprocess.check_call([
        sys.executable, "-m", "pip", "download", "-r", str(requirements), 
        *platform_subcommand, "-d", str(wheelhouse), "--only-binary=:all:"
    ])

    wheelhouse.joinpath("requirements.txt").write_text(requirements.read_text())


def test_installation(wheelhouse: Path):
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--no-index", 
        f"--find-links={wheelhouse}", "-r", str(wheelhouse.joinpath("requirements.txt"))
    ])


def zip_directory(dir_path: Path):
    shutil.make_archive(dir_path.name, "zip", dir_path)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="NlpWheelhouse",
        description="Build requirements to a zipped wheelhouse directory ."
    )
    
    parser.add_argument(
        "--platform", 
        type=str, 
        default="",
        help="Platform string to query PyPI for. If not included, use the system platform."
    )
    
    parser.add_argument(
        "--wheelhouse",
        type=Path,
        default=Path(__file__).parent.joinpath("wheelhouse") ,
        help="Output directory for wheelhouse."
    )

    parser.add_argument(
        "--requirements",
        type=Path,
        default=Path(__file__).parent.joinpath("nlp_requirements.txt"),
        help="Requirements file to build from. Copied to wheelhouse directory as 'requirements.txt'."
    )

    parser.add_argument(
        "--no-test",
        action="store_true",
        help="Do not run installation test."
    )

    parser.add_argument(
        "--no-zip",
        action="store_true",
        help="Do not zip wheelhouse directory."
    )

    args = parser.parse_args()

    _platform = args.platform
    _wheelhouse = args.wheelhouse
    _requirements = args.requirements

    _test = not args.no_test
    _zip = not args.no_zip

    build(_platform, _wheelhouse, _requirements)
    
    if _test:
        test_installation(_wheelhouse)

    if _zip:
        zip_directory(_wheelhouse)


