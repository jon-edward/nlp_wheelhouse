from pathlib import Path
from setuptools import setup


with Path(__file__).parent.joinpath("requirements.txt").open() as f:
    requirements = f.readlines()

setup(
    name="nlp_wheelhouse",
    url="https://github.com/jon-edward/nlp_wheelhouse",
    license="License :: OSI Approved :: MIT License",
    version = '0.0.8',
    install_requires=requirements,
    python_requires=">=3.10.0",
    description="This is a wrapper library for packaging various NLP tools.",
)
