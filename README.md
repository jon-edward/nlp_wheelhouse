# nlp_wheelhouse
This is a collection of useful NLP tools as Python wheels built for a Windows isolated environment.

## Installation
To install the libraries included, download the `nlp_wheelhouse-win_amd64.zip` from the 
[Releases](https://github.com/jon-edward/nlp_wheelhouse/releases) section, extract it into a directory 
named `wheelhouse`, then run `python -m pip install --no-index --find-links=wheelhouse -r wheelhouse\requirements.txt`.

## Adding a library
New libraries can be added to `nlp_requirements.txt` and will be picked up on the next release.
